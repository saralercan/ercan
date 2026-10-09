-- Correct Vinterro One execution observability. Routing/blocked runs do
-- not represent provider usage. Do not mark agent health from queued jobs.
-- Cost USD remains 0 because provider billing/pricing is UNVERIFIED; metadata
-- explicitly records that pricing is unknown rather than a true zero charge.
-- No Gmail calls, model invocation, or automated run transitions.

CREATE OR REPLACE FUNCTION private.ercan_os_capture_run_observability()
 RETURNS trigger
 LANGUAGE plpgsql
 SECURITY DEFINER
 SET search_path TO 'pg_catalog', 'public'
AS $function$
declare
  u jsonb;
  v_input bigint := 0;
  v_output bigint := 0;
  v_cached bigint := 0;
begin
  if new.status in ('success','error','blocked') and (old.status is distinct from new.status or old.completed_at is distinct from new.completed_at) then
    -- Only record token usage when a producer reported an identified model
    -- and positive well-formed token counts. A routing-only/blocked run is
    -- never an external provider invocation or an incurred model charge.
    u := coalesce(new.output->'usage','{}'::jsonb);
    if new.status in ('success','error')
       and nullif(btrim(coalesce(new.output->>'provider','')),'') is not null
       and lower(new.output->>'provider') <> 'unknown'
       and nullif(btrim(coalesce(new.output->>'model','')),'') is not null
       and lower(new.output->>'model') <> 'unknown'
       and jsonb_typeof(u) = 'object' then
      v_input := case when coalesce(u->>'input_tokens','') ~ '^[0-9]{1,18}$'
                      then (u->>'input_tokens')::bigint else 0 end;
      v_output := case when coalesce(u->>'output_tokens','') ~ '^[0-9]{1,18}$'
                       then (u->>'output_tokens')::bigint else 0 end;
      v_cached := case when coalesce(u->>'cached_tokens','') ~ '^[0-9]{1,18}$'
                       then (u->>'cached_tokens')::bigint else 0 end;
      if v_input > 0 or v_output > 0 or v_cached > 0 then
        insert into public.ercan_os_usage_costs(
          organization_id, run_id, provider, model, input_tokens, output_tokens,
          cached_tokens, cost_usd, metadata
        ) values (
          new.organization_id, new.id, new.output->>'provider',
          new.output->>'model', v_input, v_output, v_cached, 0,
          jsonb_build_object(
            'pricing_status','unpriced',
            'cost_not_verified',true,
            'source','run_output_provider_usage',
            'run_status',new.status
          )
        ) on conflict (run_id) where run_id is not null do update set
          provider=excluded.provider, model=excluded.model,
          input_tokens=excluded.input_tokens,
          output_tokens=excluded.output_tokens,
          cached_tokens=excluded.cached_tokens,
          metadata=excluded.metadata;
      end if;
    end if;

    if new.status='error' then
      insert into public.ercan_os_incidents(organization_id,run_id,severity,incident_type,title,details,status)
      values(new.organization_id,new.id,'medium','agent_run_error','Agent run failed',jsonb_build_object('task',new.task,'output',new.output),'open');
    end if;

  end if;
  return new;
end;
$function$
