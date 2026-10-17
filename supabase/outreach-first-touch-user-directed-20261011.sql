-- Forward compatibility: supersedes archived release-gate SQL from Oct 9.
-- Applied in Supabase on 2026-10-11; old files remain historic evidence.
-- Does not start Vinterro One, enable Gmail sending or waive transport QA.

CREATE OR REPLACE FUNCTION vinterro_internal.serverless_dedupe_audit()
 RETURNS jsonb
 LANGUAGE plpgsql
 SET search_path TO 'pg_catalog'
AS $function$
DECLARE
  v_day date := pg_catalog.timezone('UTC', pg_catalog.now())::date;
  v_owner_paused text;
  v_auth text;
  v_executor text;
  v_send_ready integer := 0;
  v_claims bigint := 0;
  v_flagged bigint := 0;
  v_stale bigint := 0;
  v_ambiguous bigint := 0;
  v_shared_email_groups bigint := 0;
  v_history_rows bigint := 0;
  v_history_distinct bigint := 0;
  v_history_repeat_groups bigint := 0;
  v_history_max timestamptz;
  v_status text;
  v_metrics jsonb;
BEGIN
  IF NOT pg_catalog.pg_try_advisory_xact_lock(
    pg_catalog.hashtext('vinterro_dedupe_audit_v1')
  ) THEN
    RETURN pg_catalog.jsonb_build_object('ok', false, 'reason', 'overlap_skipped');
  END IF;

  -- Idempotent per UTC day: do not rewrite existing evidence when cron retries.
  IF EXISTS (
    SELECT 1 FROM vinterro_internal.serverless_dedupe_audits
    WHERE audit_day = v_day
  ) THEN
    RETURN pg_catalog.jsonb_build_object(
      'ok', true, 'reason', 'already_audited', 'audit_day', v_day
    );
  END IF;

  SELECT
    health->>'outreach_owner_paused',
    health->>'mail_domain_authentication_gate',
    health->>'agent_executor_state'
  INTO v_owner_paused, v_auth, v_executor
  FROM public.vinterro_sales_super_agent_state
  WHERE id = 'primary';

  IF NOT FOUND THEN
    -- Do not silently declare a pass when the central safety state is missing.
    v_owner_paused := 'MISSING';
  END IF;

  SELECT pg_catalog.count(*)::integer INTO v_send_ready
  FROM public.vinterro_sales_super_agent_tasks
  WHERE kind = 'gmail_send_ready' AND status IN ('pending', 'in_progress');

  SELECT
    pg_catalog.count(*),
    pg_catalog.count(*) FILTER (WHERE duplicate_detected IS TRUE),
    pg_catalog.count(*) FILTER (
      WHERE send_outcome IN ('attempting', 'ambiguous_needs_gmail_reconcile')
        AND coalesce(last_send_attempt_at,updated_at)
          < pg_catalog.now() - interval '15 minutes'
    ),
    pg_catalog.count(*) FILTER (
      WHERE send_outcome = 'ambiguous_needs_gmail_reconcile'
    )
  INTO v_claims, v_flagged, v_stale, v_ambiguous
  FROM public.vinterro_outreach_account_claims;

  -- Multiple distinct *account records* claiming the same normalized
  -- address. Deduplicate repeated emails within each individual claim first.
  SELECT pg_catalog.count(*) INTO v_shared_email_groups
  FROM (
    SELECT e.email
    FROM (
      SELECT DISTINCT a.id, pg_catalog.lower(pg_catalog.btrim(addr.email)) AS email
      FROM public.vinterro_outreach_account_claims a
      CROSS JOIN LATERAL pg_catalog.unnest(
        coalesce(a.emails,'{}'::text[])
        || ARRAY[coalesce(a.primary_email,'')]
      ) AS addr(email)
      WHERE nullif(pg_catalog.btrim(addr.email),'') IS NOT NULL
    ) e
    GROUP BY e.email HAVING pg_catalog.count(DISTINCT e.id) > 1
  ) shared;

  SELECT
    pg_catalog.count(*),
    pg_catalog.count(DISTINCT pg_catalog.lower(pg_catalog.btrim(recipient_email))),
    pg_catalog.max(sent_at)
  INTO v_history_rows,v_history_distinct,v_history_max
  FROM vinterro_internal.outreach_gmail_sent_evidence;

  SELECT pg_catalog.count(*) INTO v_history_repeat_groups
  FROM (
    SELECT pg_catalog.lower(pg_catalog.btrim(recipient_email)) AS recipient
    FROM vinterro_internal.outreach_gmail_sent_evidence
    WHERE nullif(pg_catalog.btrim(recipient_email),'') IS NOT NULL
    GROUP BY pg_catalog.lower(pg_catalog.btrim(recipient_email))
    HAVING pg_catalog.count(*) > 1
  ) repeated;

  v_status := CASE
    WHEN v_send_ready > 0 THEN 'outbound_queue_requires_review'
    WHEN v_owner_paused IS DISTINCT FROM 'true' THEN 'owner_active_require_per_message_qa'
    WHEN v_stale > 0 OR v_shared_email_groups > 0 OR v_ambiguous > 0
      OR v_flagged > 0
      THEN 'review_required'
    ELSE 'paused_safe'
  END;

  v_metrics := pg_catalog.jsonb_build_object(
    'mode','read_only_reconciliation_audit',
    'outreach_owner_paused',v_owner_paused,
    'mail_domain_auth_gate',v_auth,
    'model_executor_state',v_executor,
    'gmail_send_ready_count',v_send_ready,
    'total_account_claims',v_claims,
    'historically_flagged_account_claims',v_flagged,
    'stale_or_unresolved_attempts',v_stale,
    'ambiguous_attempts',v_ambiguous,
    'shared_email_claim_groups',v_shared_email_groups,
    'archived_gmail_sent_rows',v_history_rows,
    'archived_gmail_distinct_recipients',v_history_distinct,
    'archived_gmail_repeated_recipient_groups',v_history_repeat_groups,
    'latest_archived_gmail_sent_at',v_history_max,
    'repeat_is_not_proof_of_duplicate_cold_send',true,
    'requires_independent_gmail_alias_review',v_status <> 'paused_safe',
    'emails_sent',0,
    'model_calls',0,
    'external_api_calls',0,
    'ai_execution_verified',false
  );

  INSERT INTO vinterro_internal.serverless_dedupe_audits (
    audit_day,status,metrics,checked_at
  ) VALUES (v_day,v_status,v_metrics,pg_catalog.now());

  RETURN pg_catalog.jsonb_build_object(
    'ok',true,'status',v_status,'audit_day',v_day
  );
END;
$function$;

CREATE OR REPLACE FUNCTION vinterro_internal.serverless_qa_tick()
 RETURNS jsonb
 LANGUAGE plpgsql
 SET search_path TO 'pg_catalog'
AS $function$
DECLARE
  v_id uuid;
  v_owner_paused text;
  v_sender_auth text;
  v_agent_executor text;
  v_send_ready integer;
  v_state_found boolean;
  v_ok boolean;
  v_evidence jsonb;
BEGIN
  IF NOT pg_catalog.pg_try_advisory_xact_lock(
    pg_catalog.hashtext('vinterro_serverless_qa_tick_v1')
  ) THEN
    RETURN pg_catalog.jsonb_build_object('ok', false, 'reason', 'overlap_skipped');
  END IF;

  -- One canary per UTC hour. No accumulating 15-second event log or model charges.
  INSERT INTO vinterro_internal.serverless_qa_runs (run_key)
  VALUES ('qa-gates-' || pg_catalog.to_char(
    pg_catalog.timezone('UTC', pg_catalog.now()), 'YYYYMMDDHH24'
  ))
  ON CONFLICT (run_key) DO NOTHING;

  SELECT id INTO v_id
  FROM vinterro_internal.serverless_qa_runs
  WHERE status = 'pending'
  ORDER BY created_at, id
  FOR UPDATE SKIP LOCKED
  LIMIT 1;

  IF v_id IS NULL THEN
    RETURN pg_catalog.jsonb_build_object('ok', true, 'reason', 'no_qa_job');
  END IF;

  SELECT
    health->>'outreach_owner_paused',
    health->>'mail_domain_authentication_gate',
    health->>'agent_executor_state'
  INTO v_owner_paused, v_sender_auth, v_agent_executor
  FROM public.vinterro_sales_super_agent_state
  WHERE id = 'primary';

  v_state_found := FOUND;

  SELECT count(*)::integer
  INTO v_send_ready
  FROM public.vinterro_sales_super_agent_tasks
  WHERE kind = 'gmail_send_ready' AND status IN ('pending', 'in_progress');

  -- PASS means only that the no-send security canary ran and gates were
  -- independently observed. It is NEVER proof of an LLM worker/model receipt.
  v_ok := v_state_found
    AND v_owner_paused = 'true'
    AND v_sender_auth = 'PASS'
    AND v_send_ready = 0;

  v_evidence := pg_catalog.jsonb_build_object(
    'mode', 'deterministic_qa_only',
    'outreach_owner_paused', v_owner_paused,
    'mail_domain_authentication_gate', v_sender_auth,
    'agent_executor_state', v_agent_executor,
    'gmail_send_ready_count', v_send_ready,
    'external_api_calls', 0,
    'emails_sent', 0,
    'model_calls', 0,
    'model_execution_verified', false,
    'gate_readiness_passed', v_ok,
    'checked_at', pg_catalog.now()
  );

  UPDATE vinterro_internal.serverless_qa_runs
  SET status = CASE WHEN v_ok THEN 'pass' ELSE 'fail' END,
      evidence = v_evidence,
      completed_at = pg_catalog.now()
  WHERE id = v_id;

  RETURN pg_catalog.jsonb_build_object(
    'ok', v_ok,
    'run_id', v_id,
    'status', CASE WHEN v_ok THEN 'pass' ELSE 'fail' END,
    'mode', 'deterministic_qa_only'
  );
END;
$function$;

CREATE OR REPLACE FUNCTION public.vinterro_outreach_control_status()
 RETURNS jsonb
 LANGUAGE sql
 STABLE
 SET search_path TO 'public', 'pg_temp'
AS $function$
SELECT jsonb_build_object(
  'general_operations',
  CASE
    WHEN lower(coalesce(s.health->>'outreach_owner_paused','false')) = 'true'
      THEN 'PAUSED_BY_OWNER'
    ELSE 'ACTIVE'
  END,
  'owner_paused',
  (lower(coalesce(s.health->>'outreach_owner_paused','false')) = 'true'),
  'first_touch',
  CASE
    WHEN lower(coalesce(s.health->>'outreach_owner_paused','false')) = 'true'
      THEN 'PAUSED_BY_OWNER'
    WHEN s.health->>'outreach_first_touch_review_status' = 'CLEARED'
      AND s.health->>'outreach_platform_channel_safety_verified' = 'true'
      AND s.health->>'mail_domain_authentication_gate' = 'PASS'
      THEN 'READY_REQUIRES_PER_MESSAGE_QA'
    ELSE 'REVIEW_REQUIRED'
  END,
  'first_touch_ready',
  (s.health->>'outreach_first_touch_review_status' = 'CLEARED'
    AND s.health->>'outreach_platform_channel_safety_verified' = 'true'
    AND s.health->>'mail_domain_authentication_gate' = 'PASS'),
  'remaining_review_items',
  coalesce(s.health->'outreach_first_touch_remaining_blockers','[]'::jsonb),
  'outreach_executor',
  coalesce(s.health->>'agent_executor_state','NOT_VERIFIED'),
  'status_semantics_version',
  '2026-10-11-owner-directed'
)
FROM public.vinterro_sales_super_agent_state AS s
WHERE s.id = 'primary';
$function$;

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
  v_review_domains text[];
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

  -- Legacy campaign-wide release flag retired; independent checks retained.
  IF coalesce((SELECT health->>'outreach_first_touch_review_status' FROM public.vinterro_sales_super_agent_state WHERE id='primary'),'REVIEW_REQUIRED') <> 'CLEARED' THEN
    RETURN jsonb_build_object('allowed',false,'reason','independent_identity_review_pending');
  END IF;
  IF coalesce((SELECT health->>'outreach_platform_channel_safety_verified' FROM public.vinterro_sales_super_agent_state WHERE id='primary'),'false') <> 'true' THEN
    RETURN jsonb_build_object('allowed',false,'reason','provider_channel_safety_unverified');
  END IF;

  -- Independently verify sender authentication:
  -- Gmail returned 550 5.7.27 SPF authentication failure on 2026-10-10.
  -- Opening the campaign release gate cannot override broken sender DNS.
  if coalesce((
    select health->>'mail_domain_authentication_gate'
    from public.vinterro_sales_super_agent_state where id='primary'
  ),'NOT_VERIFIED') <> 'PASS' then
    return jsonb_build_object(
      'allowed',false,
      'reason','sender_email_authentication_gate_blocked',
      'next_action','verify_spf_dkim_dmarc_with_independent_dns_and_delivery_test'
    );
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

  -- Review the entire candidate identity: canonical web domain plus all
  -- normalized supplied mailboxes, not only the primary address.
  -- Shared providers / booking portals must not be treated as one business.
  v_review_domains := array(
    select distinct d.domain_name
    from (
      select v_domain as domain_name
      union all
      select nullif(split_part(addr,'@',2),'') as domain_name
      from unnest(v_emails) as addr
    ) d
    where d.domain_name is not null
      and d.domain_name not in (
       'gmail.com','googlemail.com','hotmail.com','outlook.com',
       'live.com','icloud.com','me.com','yahoo.com','yahoo.com.tr',
       'aol.com','proton.me','protonmail.com','mail.ru',
       'yandex.ru','yandex.com','gmx.com','msn.com',
       'qq.com','163.com','126.com','booking.com',
       'expedia.com','airbnb.com','tripadvisor.com'
      )
  );
  if exists (
    select 1
    from unnest(v_review_domains) as candidate_domain
    join vinterro_internal.outreach_gmail_sent_evidence e
      on split_part(e.recipient_email,'@',2)=candidate_domain
  ) then
    return jsonb_build_object(
      'allowed',false,
      'reason','historical_corporate_domain_manual_review_required',
      'review_domains',v_review_domains
    );
  end if;


  -- Additional fail-closed brand/alias collision check.
  -- Historical SENT evidence can be stored under an email-only identity
  -- while an incoming first touch uses a brand and another email.
  -- Such collisions require human identity review, not a repeat send.
  if exists (
    select 1
    from public.vinterro_outreach_account_claims c
    where coalesce(c.send_outcome,'') <> 'reconciled_no_send'
      and exists (
        select 1
        from unnest(
          coalesce(c.aliases,'{}'::text[]) ||
          array[coalesce(c.normalized_business_name,'')]
        ) as existing_brand(name)
        join unnest(
          coalesce(p_aliases,'{}'::text[]) ||
          array[coalesce(p_business_name,'')]
        ) as incoming_brand(name)
          on lower(regexp_replace(btrim(existing_brand.name),'[[:space:]]+',' ','g')) =
             lower(regexp_replace(btrim(incoming_brand.name),'[[:space:]]+',' ','g'))
        where length(btrim(existing_brand.name)) >= 4
          and length(btrim(incoming_brand.name)) >= 4
          and position('@' in existing_brand.name) = 0
          and position('@' in incoming_brand.name) = 0
      )
  ) then
    return jsonb_build_object(
      'allowed',false,
      'reason','historical_brand_alias_manual_review_required',
      'next_action','resolve_same_business_and_location_before_first_touch',
      'release_gate_override_allowed',false
    );
  end if;


  -- Secondary Gmail SENT evidence guard. Some earlier campaigns wrote to
  -- Gmail without a corresponding CRM claim or with a different mailbox.
  -- Match the brand label from the authoritative sent subject conservatively:
  -- a match blocks and requires a manual identity review; it never grants send.
  if exists (
    select 1 from vinterro_internal.outreach_gmail_sent_evidence e
    join unnest(
       coalesce(p_aliases,'{}'::text[]) ||
       array[coalesce(p_business_name,'')]
    ) as candidate(name)
      on lower(regexp_replace(btrim(candidate.name),'[[:space:]]+',' ','g')) =
         lower(regexp_replace(btrim(split_part(e.subject,' — ',1)),'[[:space:]]+',' ','g'))
    where position(' — ' in coalesce(e.subject,''))>0
      and length(btrim(candidate.name))>=4
      and position('@' in candidate.name)=0
      and length(btrim(split_part(e.subject,' — ',1)))>=4
  ) then
    return jsonb_build_object(
      'allowed',false,
      'reason','historical_gmail_brand_subject_manual_review_required',
      'next_action','check_prior_contact_brand_and_aliases',
      'release_gate_override_allowed',false
    );
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
$function$;

UPDATE public.vinterro_sales_super_agent_state
SET health=(health-'outreach_first_touch_release_gate') || jsonb_build_object(
  'outreach_send_control_model','USER_DIRECTED_PER_MESSAGE_QA',
  'outreach_platform_channel_safety_verified',coalesce((health->>'outreach_platform_channel_safety_verified')::boolean,false)),
  updated_at=now()
WHERE id='primary';
