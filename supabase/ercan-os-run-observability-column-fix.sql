-- Restore Vinterro One run-state observability writes.
-- The ercan_os_agents table has no updated_at column; updating it aborts
-- every run status transition to success/error/blocked.
-- Preserve all other trigger semantics, grants, definer and tracing.

CREATE OR REPLACE FUNCTION private.ercan_os_capture_run_observability()
 RETURNS trigger
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'public'
AS $function$
declare
  u jsonb;
  recent_total integer;
  recent_success integer;
begin
  if new.status in ('success','error','blocked') and (old.status is distinct from new.status or old.completed_at is distinct from new.completed_at) then
    u := coalesce(new.output->'usage','{}'::jsonb);
    insert into public.ercan_os_usage_costs(
      organization_id, run_id, provider, model, input_tokens, output_tokens, cached_tokens, cost_usd, metadata
    ) values (
      new.organization_id, new.id, coalesce(new.output->>'provider','unknown'), coalesce(new.output->>'model','unknown'),
      coalesce(nullif(u->>'input_tokens','')::bigint,0), coalesce(nullif(u->>'output_tokens','')::bigint,0),
      coalesce(nullif(u->>'cached_tokens','')::bigint,0), 0,
      jsonb_build_object('pricing_status','not_configured','captured_from_run',true)
    ) on conflict (run_id) where run_id is not null do update set
      provider=excluded.provider, model=excluded.model, input_tokens=excluded.input_tokens,
      output_tokens=excluded.output_tokens, cached_tokens=excluded.cached_tokens, metadata=excluded.metadata;

    if new.status='error' then
      insert into public.ercan_os_incidents(organization_id,run_id,severity,incident_type,title,details,status)
      values(new.organization_id,new.id,'medium','agent_run_error','Agent run failed',jsonb_build_object('task',new.task,'output',new.output),'open');
    end if;

    if new.agent_id is not null then
      select count(*), count(*) filter (where status='success') into recent_total,recent_success
      from (select status from public.ercan_os_runs where agent_id=new.agent_id order by created_at desc limit 20) r;
      update public.ercan_os_agents set health = case when recent_total=0 then 100 else greatest(0,least(100,round(recent_success::numeric/recent_total*100))) end
      where id=new.agent_id;
    end if;
  end if;
  return new;
end;
$function$
