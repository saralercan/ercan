-- Vinterro One: consolidate five paid-media/marketing researchers into ONE
-- user-facing canonical agent "Reklam Ajansı" without destroying history.
-- Exact organization and UUID guards prevent cross-project modifications.
-- Existing specialist source rows, learning provenance and run history remain.
-- No execution, external ads API access, campaign mutation, billable call or Gmail send.
begin;
do $safe_merge$
declare
  v_org uuid := '1805532c-8bbe-4280-8164-dac244ed46b4';
  v_lead uuid := 'b2acac02-29d7-418c-9f04-24552e947776';
  v_old text[] := array[
    'Paid Media Intelligence Agent','Campaign Creative Intelligence Agent',
    'Growth & Brand Orchestrator','Marketing Compliance Agent',
    'Marketing Source Discovery Agent'
  ];
  v_total int;
  v_distinct int;
  v_external_runs int;
begin
  select count(*),count(distinct name) into v_total,v_distinct
    from public.ercan_os_agents
    where organization_id=v_org and name=any(v_old) and status='active';
  if v_total<>5 or v_distinct<>5 then
    raise exception 'MERGE_REFUSED: expected five unique active specialists, found % / %',v_total,v_distinct;
  end if;
  if not exists (
    select 1 from public.ercan_os_agents
    where id=v_lead and organization_id=v_org and name='Paid Media Intelligence Agent'
  ) then raise exception 'MERGE_REFUSED: canonical target does not match'; end if;
  if exists (
    select 1 from public.ercan_os_agents
    where organization_id=v_org and name='Reklam Ajansı'
  ) then raise exception 'MERGE_REFUSED: canonical name already exists'; end if;
  if exists (
    select 1 from public.ercan_os_agents
    where organization_id=v_org and name=any(v_old) and project_id is not null
  ) then raise exception 'MERGE_REFUSED: unexpectedly project-scoped specialist'; end if;
  -- Historical agent references make deleting/rewriting specialist identity unsafe.
  -- Abort if a specialist already produced jobs, reviews, or test results.
  select count(*) into v_external_runs from (
    select r.id::text from public.ercan_os_runs r join public.ercan_os_agents a on a.id=r.agent_id
      where a.organization_id=v_org and a.name=any(v_old)
    union all select r.id::text from public.ercan_os_eval_runs r
      join public.ercan_os_agents a on a.id=r.agent_id
      where a.organization_id=v_org and a.name=any(v_old)
    union all select r.id::text from public.vinterro_one_supervision_runs r
      join public.ercan_os_agents a on a.id=r.producer_agent_id
      where a.organization_id=v_org and a.name=any(v_old)
    union all select r.id::text from public.vinterro_one_supervision_reviews r
      join public.ercan_os_agents a on a.id=r.reviewer_agent_id
      where a.organization_id=v_org and a.name=any(v_old)
  ) historical;
  if v_external_runs>0 then
    raise exception 'MERGE_REFUSED: existing executable history requires manual reroute (%)',v_external_runs;
  end if;
end;
$safe_merge$;

-- Reuse the existing paid-media UUID so callers holding its identifier can
-- still resolve the canonical agency (a newly generated ID would break callers).
update public.ercan_os_agents a
set name='Reklam Ajansı',
    version='2.0.0',
    role='web_research',
    tools='["web","github_research","knowledge","qa","graphic","content","seo"]'::jsonb,
    permissions='["read","research","workspace.write"]'::jsonb,
    handoffs='["QA Agent","Analytics & Attribution Agent","Brand Systems Agent","Social Creative Agent","Conversion & CRO Agent","SEO Meta & Schema Agent","Security & License Agent","Human Approval Agent","Research Agent","Creative QA & Brand Consistency Agent","Local SEO & Merchant Agent","Social Media Intelligence Agent"]'::jsonb,
    max_steps=16,
    max_retries=2,
    max_cost_usd=2.00,
    instructions=$agency_rules$
REKLAM AJANSI — Vinterro One's single user-facing global paid-media and marketing agency.
Former specialist competencies are INTERNAL CAPABILITY LANES of this ONE agent, not independent agents:
(1) Media Strategy & Buying Research — Google/Meta/Microsoft/Pinterest/TikTok, marketplaces, Search/Shopping, keyword intent, structure and budgets;
(2) Campaign Creative Studio — genuine product creative, premium art direction, native-language campaign copy, A/B testing;
(3) Growth & Brand Strategy — product/landing continuity, marketing plans, conversion and cross-channel reporting;
(4) Ads Compliance & Privacy — accurate advertising claims, consent, applicable platform rules, GDPR/KVKK and country eligibility;
(5) Worldwide Ads Research & Education — curated sources, academic evidence, maintained GitHub projects, international native markets.
Read docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md and docs/academy/VINTERRO_GLOBAL_PAID_MEDIA_ACADEMY_TR.md and the canonical ercan_os_agent_sources source register; verify mutable platform rules against CURRENT primary documentation in the task's language. Source and exam entries are curricula, NOT proven model training, exam passes or advertising platform certifications. Distinguish observed purchases, platform-attributed conversions and scientifically incremental sales. Mark assumptions and source limitations.
Before material deliverables ask independent QA Agent / Creative QA & Brand Consistency Agent or appropriate compliance reviewers; DO NOT self-certify, especially not for legal, privacy, budget, conversions, or real ad lift.
Default is RESEARCH + DRAFTS ONLY. NEVER launch, unpause, pause, publish, update live budget/bidding/audience/payment, apply() recommendations, perform paid model/tool operations without authorized runtime, or access client campaign accounts without explicit scope and approval. No cold Gmail outreach; global first-touch gate remains BLOCKED. No unsupported performance metrics, fake credentials or certifications. Legacy aliases from former agents must resolve to this single agency.
$agency_rules$,
    expertise_profile=coalesce(a.expertise_profile,'{}'::jsonb)||
      jsonb_build_object(
        'agency_consolidation',
        jsonb_build_object(
          'canonical_name','Reklam Ajansı',
          'schema_version','2026-10-09/v1',
          'merged_at',now(),
          'source_agents',jsonb_build_array(
            'Paid Media Intelligence Agent','Campaign Creative Intelligence Agent',
            'Growth & Brand Orchestrator','Marketing Compliance Agent',
            'Marketing Source Discovery Agent'
          ),
          'original_paid_media_instructions',a.instructions,
          'internal_lanes',jsonb_build_array(
            'Media Strategy & Buying','Campaign Creative Studio','Growth & Brand Strategy',
            'Advertising Compliance & Privacy','Worldwide Ads Research'
          ),
          'actual_live_exam_passes',0,
          'model_training_status','CURATED_NOT_MODEL_EXECUTED',
          'independent_reviewer_required',true,
          'media_account_write_authority',false
        )
      )
where a.id='b2acac02-29d7-418c-9f04-24552e947776'::uuid
  and a.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid
  and a.name='Paid Media Intelligence Agent'
  and a.status='active';

-- Consolidate DISTINCT external sources into the existing lead identity.
-- Keep every donor source row intact as an audit/provenance record.
with scope as (
 select a.id,a.name from public.ercan_os_agents a
 where a.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid
   and (a.name='Reklam Ajansı' or a.name in (
     'Campaign Creative Intelligence Agent','Growth & Brand Orchestrator',
     'Marketing Compliance Agent','Marketing Source Discovery Agent'
   ))
), chosen as (
 select distinct on (s.source_uri)
   s.*,a.name donor_name
 from public.ercan_os_agent_sources s
 join scope a on a.id=s.agent_id
 where s.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid
 order by s.source_uri,
   case when s.agent_id='b2acac02-29d7-418c-9f04-24552e947776'::uuid then 0 else 1 end,
   s.authority_tier asc, s.last_verified_at desc nulls last
), provenance as (
 select s.source_uri,jsonb_agg(distinct a.name) as origin_agents
 from public.ercan_os_agent_sources s join scope a on a.id=s.agent_id
 where s.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid
 group by s.source_uri
)
insert into public.ercan_os_agent_sources (
 organization_id,agent_id,agent_name,topic,source_name,source_uri,source_kind,
 authority_tier,freshness_days,enabled,last_verified_at,last_content_hash,metadata
)
select s.organization_id,'b2acac02-29d7-418c-9f04-24552e947776'::uuid,'Reklam Ajansı',
 s.topic,s.source_name,s.source_uri,s.source_kind,s.authority_tier,
 s.freshness_days,s.enabled,s.last_verified_at,s.last_content_hash,
 coalesce(s.metadata,'{}'::jsonb)||jsonb_build_object(
  'canonical_agent','Reklam Ajansı',
  'merged_source_agents',p.origin_agents,
  'source_merge_mode','lossless_donor_preservation'
 )
from chosen s join provenance p on p.source_uri=s.source_uri
on conflict (organization_id,agent_id,source_uri) do update set
 agent_name='Reklam Ajansı',
 metadata=coalesce(public.ercan_os_agent_sources.metadata,'{}'::jsonb)||
   jsonb_build_object('canonical_agent','Reklam Ajansı','merged_source_agents',excluded.metadata->'merged_source_agents',
   'source_merge_mode','lossless_donor_preservation'),
 authority_tier=least(public.ercan_os_agent_sources.authority_tier,excluded.authority_tier),
 enabled=public.ercan_os_agent_sources.enabled or excluded.enabled,
 updated_at=now();

-- Re-map only the lead's display name. Historic donors stay untouched.
update public.ercan_os_agent_learning_events
set agent_name='Reklam Ajansı'
where agent_id='b2acac02-29d7-418c-9f04-24552e947776'::uuid
and organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid;
update public.ercan_os_agent_sources
set agent_name='Reklam Ajansı'
where agent_id='b2acac02-29d7-418c-9f04-24552e947776'::uuid
and organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid;

-- Import distinct research notes as pending independent verification.
-- The old agents' already-assigned status is retained on THEIR rows only;
-- copying 'verified' into a new identity is not proof of agent training.
with old_agents as (
 select id,name from public.ercan_os_agents
 where organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid
 and name in ('Campaign Creative Intelligence Agent','Growth & Brand Orchestrator',
              'Marketing Compliance Agent','Marketing Source Discovery Agent')
), unique_notes as (
 select distinct on (e.topic,e.title,coalesce(e.source_uri,''))
 e.*,a.name donor_name
 from public.ercan_os_agent_learning_events e
 join old_agents a on a.id=e.agent_id
 order by e.topic,e.title,coalesce(e.source_uri,''),e.learned_at desc
)
insert into public.ercan_os_agent_learning_events
(organization_id,agent_id,agent_name,source_id,source_uri,topic,title,
 summary,evidence,confidence,status,learned_at,expires_at,content_hash)
select e.organization_id,'b2acac02-29d7-418c-9f04-24552e947776'::uuid,'Reklam Ajansı',
 s.id,e.source_uri,e.topic,e.title,e.summary,
 coalesce(e.evidence,'{}'::jsonb)||jsonb_build_object(
 'original_specialist',e.donor_name,'original_specialist_learning_status',e.status,
 'copy_learning_status','PENDING_INDEPENDENT_REVALIDATION'
 ),
 e.confidence,'pending_qa',e.learned_at,e.expires_at,e.content_hash
from unique_notes e
left join public.ercan_os_agent_sources s
 on s.agent_id='b2acac02-29d7-418c-9f04-24552e947776'::uuid
 and s.source_uri=e.source_uri
where not exists (
 select 1 from public.ercan_os_agent_learning_events current
 where current.agent_id='b2acac02-29d7-418c-9f04-24552e947776'::uuid
 and current.topic=e.topic and current.title=e.title
 and coalesce(current.source_uri,'')=coalesce(e.source_uri,'')
);

-- Retain per-specialty curricula and QA rules INSIDE one live profile.
with original as (
 select a.id,a.name,p.curriculum,p.research_policy,p.source_hierarchy
 from public.ercan_os_agents a
 join public.ercan_os_agent_expertise_profiles p on p.agent_id=a.id
 where a.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid
 and (a.name='Reklam Ajansı' or a.name in (
 'Campaign Creative Intelligence Agent','Growth & Brand Orchestrator',
 'Marketing Compliance Agent','Marketing Source Discovery Agent'))
)
update public.ercan_os_agent_expertise_profiles p
set agent_name='Reklam Ajansı',
 curriculum=coalesce(p.curriculum,'{}'::jsonb)||
  jsonb_build_object(
   'reklam_ajansi_consolidated',jsonb_build_object(
      'version','2026-10-09/v1',
      'internal_specialist_curricula',(select jsonb_object_agg(name,curriculum) from original),
      'standalone_agent_count',1,
      'agency_exam_passes',0,
      'training_status','PENDING_REAL_EXECUTOR_AND_INDEPENDENT_QA',
      'academy_base','docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md',
      'academy_global','docs/academy/VINTERRO_GLOBAL_PAID_MEDIA_ACADEMY_TR.md'
   )
  ),
 research_policy=coalesce(p.research_policy,'{}'::jsonb)||
  jsonb_build_object('reklam_ajansi_single_owner',true,
                     'original_agent_curriculum_preserved',true,
                     'explicit_approval_for_media_mutation',true,
                     'independent_qa_required',true,
                     'no_self_certification',true),
 updated_at=now()
where p.agent_id='b2acac02-29d7-418c-9f04-24552e947776'::uuid
and p.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid;

-- Archive four replaced agent identities only after their sources and
-- curricula were copied. Keep every ID, original row and foreign key.
update public.ercan_os_agents a set
 status='inactive',
 expertise_profile=coalesce(a.expertise_profile,'{}'::jsonb)||
  jsonb_build_object('consolidated_into','Reklam Ajansı',
                     'consolidated_into_agent_id','b2acac02-29d7-418c-9f04-24552e947776',
                     'archived_reason','unified_ads_agency_user_request',
                     'archived_on',now())
where a.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid
and a.name in ('Campaign Creative Intelligence Agent','Growth & Brand Orchestrator',
               'Marketing Compliance Agent','Marketing Source Discovery Agent')
and a.status='active';

update public.ercan_os_agent_expertise_profiles p set
 status='inactive',updated_at=now()
where p.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid
and p.agent_id in (
 select id from public.ercan_os_agents a where a.organization_id=p.organization_id
 and a.status='inactive' and a.name in (
  'Campaign Creative Intelligence Agent','Growth & Brand Orchestrator',
  'Marketing Compliance Agent','Marketing Source Discovery Agent')
);

-- Replace old specialist names in all LIVE handoff arrays, deduplicating
-- repeated aliases and never creating a handoff to oneself.
with new_handoffs as (
 select a.id,
   (select coalesce(jsonb_agg(d.routed order by d.first_order),'[]'::jsonb)
    from (
      select normalized.routed,min(normalized.ord) first_order
      from (
        select case when e.value in (
           'Paid Media Intelligence Agent','Campaign Creative Intelligence Agent',
           'Growth & Brand Orchestrator','Marketing Compliance Agent',
           'Marketing Source Discovery Agent'
         ) then 'Reklam Ajansı' else e.value end routed,
         e.ord
        from jsonb_array_elements_text(a.handoffs)
             with ordinality e(value,ord)
      ) normalized
      where normalized.routed <> a.name
      group by normalized.routed
    ) d
   ) rerouted
 from public.ercan_os_agents a
 where a.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid and a.status='active'
)
update public.ercan_os_agents a
set handoffs=h.rerouted
from new_handoffs h where a.id=h.id and a.handoffs is distinct from h.rerouted;

-- Assert desired single active identity and complete unique source coverage.
do $verify$
declare active_count int; archived_count int; distinct_sources int; merged_sources int; stale_routes int;
begin
 select count(*) filter (where status='active'),count(*) filter (where status='inactive')
 into active_count,archived_count from public.ercan_os_agents a
 where a.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid
 and a.name in (
 'Reklam Ajansı','Campaign Creative Intelligence Agent',
 'Growth & Brand Orchestrator','Marketing Compliance Agent',
 'Marketing Source Discovery Agent');
 select count(distinct source_uri) into distinct_sources
 from public.ercan_os_agent_sources s where s.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid
 and s.agent_id in (
  'b2acac02-29d7-418c-9f04-24552e947776'::uuid,
  'c807acb9-b9df-4fba-8d47-15226fbcc37f'::uuid,
  '8347c02b-57c0-4c4d-892e-134fc02e76fd'::uuid,
  '16e6cdd4-5420-45cb-8198-154986b9a1b3'::uuid,
  '686273c3-3392-4bc3-9b6a-c71f4cd09325'::uuid
 );
 select count(*) into merged_sources from public.ercan_os_agent_sources s
 where s.agent_id='b2acac02-29d7-418c-9f04-24552e947776'::uuid;
 select count(*) into stale_routes from public.ercan_os_agents a
 where a.organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid and a.status='active'
 and exists (
 select 1 from jsonb_array_elements_text(a.handoffs) h(name)
 where h.name in ('Paid Media Intelligence Agent','Campaign Creative Intelligence Agent',
 'Growth & Brand Orchestrator','Marketing Compliance Agent','Marketing Source Discovery Agent')
 );
 if active_count<>1 or archived_count<>4 or merged_sources<>distinct_sources or stale_routes<>0 then
   raise exception 'SINGLE_AGENT_VERIFY_FAILED: active %, archived %, sources %/% routes %',
     active_count,archived_count,merged_sources,distinct_sources,stale_routes;
 end if;
end;
$verify$;
commit;
