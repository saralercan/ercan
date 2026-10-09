-- Vinterro One: no completed autonomous task without a server-recorded,
-- registered-worker execution receipt and independent supervision.
-- NO Gmail action; NO model call; NO credential creation; NO existing run writes.
-- First-touch release remains BLOCKED.

begin;

create table if not exists vinterro_internal.agent_execution_receipts (
  run_id uuid primary key references public.ercan_os_runs(id) on delete restrict,
  worker_id text not null check (length(btrim(worker_id)) between 3 and 128),
  provider text not null check (length(btrim(provider)) between 2 and 128),
  model text not null check (length(btrim(model)) between 2 and 256),
  provider_request_id text not null check (length(btrim(provider_request_id)) between 3 and 256),
  input_tokens bigint not null check (input_tokens >= 0),
  output_tokens bigint not null check (output_tokens >= 0),
  receipt_recorded_at timestamptz not null default now(),
  constraint provider_usage_must_be_positive check (input_tokens + output_tokens > 0)
);

alter table vinterro_internal.agent_execution_receipts enable row level security;
revoke all on table vinterro_internal.agent_execution_receipts from public, anon, authenticated;
grant select, insert on table vinterro_internal.agent_execution_receipts to service_role;
comment on table vinterro_internal.agent_execution_receipts is
  'Service-recorded provider execution evidence for registered active workers. No receipt implies no autonomous execution verification.';

-- Exactly one immutable receipt per run. No UPDATE / DELETE granted to service role.
create or replace function public.vinterro_has_agent_execution_receipt(p_run_id uuid)
returns boolean
language sql
stable
security invoker
set search_path to 'pg_catalog','public','vinterro_internal'
as $function$
  select exists (
    select 1 from vinterro_internal.agent_execution_receipts e
    join public.vinterro_sales_worker_credentials w
      on w.worker_id = e.worker_id
    where e.run_id = p_run_id
      and w.active is true
      and w.last_seen_at is not null
      and w.last_seen_at >= e.receipt_recorded_at - interval '15 minutes'
      and e.input_tokens + e.output_tokens > 0
      and length(btrim(e.provider_request_id)) > 2
  );
$function$;

revoke execute on function public.vinterro_has_agent_execution_receipt(uuid)
  from public, anon, authenticated;
grant execute on function public.vinterro_has_agent_execution_receipt(uuid)
  to service_role;

-- Even a directly writable authorized client cannot mark an unexecuted run
-- under review or successful via the public Data API.
create or replace function private.ercan_os_require_execution_receipt()
returns trigger
language plpgsql
security definer
set search_path to 'pg_catalog','public','vinterro_internal'
as $function$
begin
  if new.status in ('under_review','success')
     and not public.vinterro_has_agent_execution_receipt(new.id) then
    raise exception using
      errcode = '23514',
      message = 'agent_execution_receipt_required';
  end if;

  if new.status = 'success'
     and not exists (
       select 1 from public.vinterro_one_supervision_runs s
       join public.vinterro_one_supervision_reviews r
         on r.supervision_id=s.id
       where s.run_id=new.id
         and s.organization_id=new.organization_id
         and s.final_gate_state='VERIFIED'
         and r.verdict='PASS'
         and r.reviewer_agent_id is distinct from s.producer_agent_id
     ) then
    raise exception using
      errcode = '23514',
      message = 'independent_supervision_required';
  end if;
  return new;
end;
$function$;

revoke execute on function private.ercan_os_require_execution_receipt()
  from public, anon, authenticated;

drop trigger if exists ercan_os_runs_execution_receipt_gate on public.ercan_os_runs;
create trigger ercan_os_runs_execution_receipt_gate
before insert or update of status on public.ercan_os_runs
for each row execute function private.ercan_os_require_execution_receipt();

commit;
