-- Vinterro Digital MailAgent security hardening.
-- No Gmail sends, no claim/CRM row changes, no release-gate state change.
-- Preserve the owner-facing read-only client experience; reserve writes and
-- atomically claimed first-touch send functions for backend service_role.
--
-- Rationale: prior permissive MFA-only ALL policies allowed any signed-in
-- user without an enrolled MFA factor to pass the policy and alter safety
-- state. RLS policies are OR-combined by default, so owner SELECT alone was
-- not sufficient to protect the state table.

begin;

-- RLS enabled already, enforce again for defense in depth.
alter table public.vinterro_outreach_account_claims enable row level security;
alter table public.vinterro_sales_super_agent_state enable row level security;

-- Remove permissive MFA-only ALL policies on these two high-risk objects.
drop policy if exists vinterro_one_mfa_guard
  on public.vinterro_outreach_account_claims;
drop policy if exists vinterro_one_mfa_guard
  on public.vinterro_sales_super_agent_state;

-- Only a signed-in, AAL2, explicitly authorized Vinterro Digital owner can
-- read the underlying first-touch claims. The private.ercan_os_has_access()
-- function already enforces the owner's membership and approved identity.
drop policy if exists vinterro_outreach_claims_owner_select
  on public.vinterro_outreach_account_claims;
create policy vinterro_outreach_claims_owner_select
on public.vinterro_outreach_account_claims
for select to authenticated using (
  exists (
    select 1
    from public.ercan_os_memberships m
    join public.ercan_os_projects p
      on p.organization_id = m.organization_id
    where m.user_id = (select auth.uid())
      and m.role = 'owner'
      and p.name = 'Vinterro Digital'
      and private.ercan_os_has_access(m.organization_id)
  )
);

-- Existing "ERCAN OS owner can read sales super agent state" remains in place.
-- No direct web/SDK client may overwrite the current BLOCKED safety gate.
revoke all on table public.vinterro_outreach_account_claims
  from public, anon, authenticated;
revoke all on table public.vinterro_sales_super_agent_state
  from public, anon, authenticated;
grant select on table public.vinterro_outreach_account_claims
  to authenticated;
grant select on table public.vinterro_sales_super_agent_state
  to authenticated;

-- Backend-only atomic claim/send state transitions.
-- Revoking from PUBLIC matters: inherited default EXECUTE grants survive
-- a revoke from anon/authenticated alone.
revoke execute on function public.vinterro_prepare_first_touch(
  text,text,text,text,text,text[],text[],text
) from public, anon, authenticated;
revoke execute on function public.vinterro_finalize_first_touch_sent(
  text,uuid,text,text,timestamptz
) from public, anon, authenticated;
revoke execute on function public.vinterro_mark_first_touch_ambiguous(
  text,uuid,text
) from public, anon, authenticated;
revoke execute on function public.vinterro_release_first_touch_after_no_send(
  text,uuid,text
) from public, anon, authenticated;

grant execute on function public.vinterro_prepare_first_touch(
  text,text,text,text,text,text[],text[],text
) to service_role;
grant execute on function public.vinterro_finalize_first_touch_sent(
  text,uuid,text,text,timestamptz
) to service_role;
grant execute on function public.vinterro_mark_first_touch_ambiguous(
  text,uuid,text
) to service_role;
grant execute on function public.vinterro_release_first_touch_after_no_send(
  text,uuid,text
) to service_role;

commit;
