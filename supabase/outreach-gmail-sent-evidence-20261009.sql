-- Gmail-verified SENT evidence quarantine. Separate from CRM identity claims.
-- Does not send any email, mark delivery, or infer account identity.
-- The live outreach release gate remains BLOCKED until historical reconciliation QA.

create table if not exists vinterro_internal.outreach_gmail_sent_evidence (
    gmail_message_id text primary key,
    gmail_thread_id text,
    recipient_email text not null,
    subject text not null,
    sent_at timestamptz not null,
    source text not null default 'gmail_sent_verified',
    recorded_at timestamptz not null default now(),
    constraint normalized_recipient_email check (
       recipient_email=lower(btrim(recipient_email))
       and recipient_email ~ '^[^[:space:]@]+@[^[:space:]@]+[.][^[:space:]@]+$'
    ),
    constraint nonempty_gmail_id check (length(btrim(gmail_message_id))>0)
);
create index if not exists outreach_gmail_sent_evidence_recipient_idx
  on vinterro_internal.outreach_gmail_sent_evidence(recipient_email,sent_at desc);
alter table vinterro_internal.outreach_gmail_sent_evidence enable row level security;
revoke all on vinterro_internal.outreach_gmail_sent_evidence from public, anon, authenticated;
grant select on vinterro_internal.outreach_gmail_sent_evidence to service_role;
comment on table vinterro_internal.outreach_gmail_sent_evidence is
  'Immutable historical Gmail SENT facts used to suppress repeat first touch. Not evidence of delivery.';

-- Preserve the existing live fail-closed status gate and transaction serialization.
CREATE OR REPLACE FUNCTION public.vinterro_prepare_first_touch(p_account_key text, p_business_name text, p_location text DEFAULT ''::text, p_canonical_domain text DEFAULT NULL::text, p_primary_email text DEFAULT NULL::text, p_aliases text[] DEFAULT '{}'::text[], p_emails text[] DEFAULT '{}'::text[], p_source text DEFAULT 'vinterro_one'::text)
 RETURNS jsonb
 LANGUAGE plpgsql
 SET search_path TO 'public'
AS $function$
declare
  v_key text := lower(btrim(coalesce(p_account_key,'')));
  v_name text := lower(btrim(coalesce(p_business_name,'')));
  v_location text := lower(btrim(coalesce(p_location,'')));
  v_domain text := nullif(lower(btrim(regexp_replace(coalesce(p_canonical_domain,''),'^https?://(www\.)?|/.*$','','gi'))),'');
  v_email text := nullif(lower(btrim(coalesce(p_primary_email,''))),'');
  v_emails text[] := array(
    select distinct lower(btrim(x))
    from unnest(coalesce(p_emails,'{}'::text[]) || case when p_primary_email is null then '{}'::text[] else array[p_primary_email] end) x
    where btrim(x) <> ''
  );
  v_existing public.vinterro_outreach_account_claims%rowtype;
  v_token uuid := gen_random_uuid();
begin
  if v_key = '' or v_name = '' then
    return jsonb_build_object('allowed',false,'reason','invalid_identity');
  end if;

  -- Fail closed at canonical send boundary. A flag cannot itself block
  -- direct Gmail access; every conforming first-touch path must call this.
  if coalesce((
      select health->>'outreach_first_touch_release_gate'
      from public.vinterro_sales_super_agent_state
      where id = 'primary'
    ), 'BLOCKED') <> 'OPEN' then
    return jsonb_build_object('allowed',false,'reason','first_touch_release_gate_blocked');
  end if;

  -- Serialize prepare across distinct keys/alias sets so two parallel
  -- requests cannot both see a missing claim before inserting.
  -- Low-volume first touch (<=180/day); transaction lock auto-releases.
  perform pg_catalog.pg_advisory_xact_lock(pg_catalog.hashtext('vinterro_outreach_first_touch_prepare_v1'));

  -- Gmail SENT evidence is independent of the legacy CRM ledger.
  -- Suppress exact recipient addresses without inventing a business identity.
  if exists (
    select 1 from vinterro_internal.outreach_gmail_sent_evidence e
    where e.recipient_email = v_email
       or e.recipient_email = any(v_emails)
  ) then
    return jsonb_build_object('allowed',false,'reason','historical_gmail_sent_suppressed');
  end if;

  select *
  into v_existing
  from public.vinterro_outreach_account_claims c
  where c.account_key = v_key
     or (lower(c.normalized_business_name)=v_name and lower(c.normalized_location)=v_location)
     or (v_domain is not null and c.canonical_domain is not null and lower(c.canonical_domain)=v_domain)
     or (v_email is not null and c.primary_email is not null and lower(c.primary_email)=v_email)
     or (cardinality(v_emails)>0 and c.emails && v_emails)
  order by c.created_at asc
  limit 1;

  if found then
    if v_existing.first_touch_gmail_message_id is null
       and v_existing.send_outcome='reconciled_no_send' then
      update public.vinterro_outreach_account_claims
      set account_key=v_key,
          normalized_business_name=v_name,
          normalized_location=v_location,
          canonical_domain=coalesce(v_domain,canonical_domain),
          primary_email=coalesce(v_email,primary_email),
          aliases=(select array(select distinct e from unnest(aliases || coalesce(p_aliases,'{}'::text[])) e where btrim(e)<>'')),
          emails=(select array(select distinct lower(btrim(e)) from unnest(emails || v_emails) e where btrim(e)<>'')),
          source=coalesce(nullif(p_source,''),source),
          claim_status='claimed',
          send_outcome='attempting',
          send_attempt_token=v_token,
          send_attempt_count=send_attempt_count+1,
          last_send_attempt_at=now(),
          updated_at=now(),
          metadata=metadata || jsonb_build_object('retry_after_reconcile_at',now())
      where id=v_existing.id;

      return jsonb_build_object(
        'allowed',true,
        'reason','retry_after_reconciled_no_send',
        'account_key',v_key,
        'send_attempt_token',v_token,
        'send_outcome','attempting'
      );
    end if;

    return jsonb_build_object(
      'allowed',false,
      'reason','account_already_claimed_or_contacted',
      'account_key',v_existing.account_key,
      'claim_status',v_existing.claim_status,
      'send_outcome',v_existing.send_outcome,
      'gmail_message_id',v_existing.first_touch_gmail_message_id,
      'duplicate_detected',v_existing.duplicate_detected
    );
  end if;

  begin
    insert into public.vinterro_outreach_account_claims(
      account_key,normalized_business_name,normalized_location,canonical_domain,
      primary_email,aliases,emails,source,claim_status,send_outcome,
      send_attempt_token,send_attempt_count,last_send_attempt_at,metadata
    ) values (
      v_key,v_name,v_location,v_domain,v_email,
      coalesce(p_aliases,'{}'::text[]),v_emails,coalesce(nullif(p_source,''),'vinterro_one'),
      'claimed','attempting',v_token,1,now(),
      jsonb_build_object('hard_gate_version','2.1','prepared_at',now())
    );
  exception when unique_violation then
    return jsonb_build_object('allowed',false,'reason','atomic_conflict','account_key',v_key);
  end;

  return jsonb_build_object(
    'allowed',true,
    'reason','new_atomic_claim',
    'account_key',v_key,
    'send_attempt_token',v_token,
    'send_outcome','attempting'
  );
end;
$function$

