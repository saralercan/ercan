-- 2026-10-11: Separate user-controlled pause from first-touch release readiness.
-- A marketing-channel review is not a global agent failure and should not be
-- reported as an owner-requested BLOCKED state.
-- This migration DOES NOT authorize Gmail sending, create new leads, reset the
-- dedupe ledger, or change the first-touch RPC's fail-closed OPEN requirement.

CREATE OR REPLACE FUNCTION public.vinterro_outreach_control_status()
RETURNS jsonb
LANGUAGE sql
STABLE
SECURITY INVOKER
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
    WHEN s.health->>'outreach_first_touch_release_gate' = 'OPEN'
      THEN 'RELEASED_REQUIRES_PER_MESSAGE_QA'
    ELSE 'REVIEW_REQUIRED'
  END,
  'first_touch_release_open',
  (coalesce(s.health->>'outreach_first_touch_release_gate','REVIEW_REQUIRED') = 'OPEN'),
  'remaining_review_items',
  coalesce(s.health->'outreach_first_touch_remaining_blockers','[]'::jsonb),
  'outreach_executor',
  coalesce(s.health->>'agent_executor_state','NOT_VERIFIED'),
  'sender_domain_authentication',
  coalesce(s.health->>'mail_domain_authentication_gate','NOT_VERIFIED'),
  'manual_operator_command_required', true,
  'status_is_not_send_authorization', true,
  'status_semantics_version',
  '2026-10-11'
)
FROM public.vinterro_sales_super_agent_state AS s
WHERE s.id = 'primary';
$function$;

-- IMPORTANT: An agent must not clear a real owner pause merely by
-- reclassifying the unrelated first-touch verification status.
-- The migration changes only the first-touch review label. It does NOT
-- change outreach_owner_paused, agent_executor_state, or sender DNS status.
-- The send RPC still explicitly requires OPEN, independently of this label.
UPDATE public.vinterro_sales_super_agent_state
SET
  health = coalesce(health,'{}'::jsonb)
    || jsonb_build_object(
      'outreach_first_touch_review_status','REVIEW_REQUIRED',
      'outreach_status_semantics_version','2026-10-11',
      'outreach_first_touch_release_gate','REVIEW_REQUIRED'
    ),
  updated_at = now()
WHERE id = 'primary'
  AND health->>'outreach_first_touch_release_gate' = 'BLOCKED';

-- Confirmed sent, bounced, opted-out, and duplicate account claims are untouched.
-- Before production first-touch the existing function must still see gate=OPEN,
-- plus independent account-level dedupe, template and provider-channel clearance.
