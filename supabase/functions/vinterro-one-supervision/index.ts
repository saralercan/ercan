
import { createClient } from 'npm:@supabase/supabase-js@2.112.2'

const SUPABASE_URL = Deno.env.get('SUPABASE_URL') ?? ''
const ANON_KEY = Deno.env.get('SUPABASE_ANON_KEY') ?? ''
const SERVICE_KEY = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''

const OWNER_EMAIL_HASHES = new Set([
  '560c6c2879a2084c35e78377bb800a09e30a9dcc9fc60cf6083a317e59a5454c',
  '35d039ff6d0697e6667a66c13c8d03e55dc5a8e27f85180fb88e2b05352a97a4',
])

const cors = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Content-Type': 'application/json',
}

const J = (data: unknown, status = 200) => new Response(JSON.stringify(data), { status, headers: cors })
const now = () => new Date().toISOString()

async function owner(user: any) {
  const email = String(user?.email || '').trim().toLowerCase()
  if (!email) return false
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(email))
  const hash = Array.from(new Uint8Array(digest)).map((b) => b.toString(16).padStart(2, '0')).join('')
  return OWNER_EMAIL_HASHES.has(hash)
}

function classifyTask(task: string, requestedAction: string) {
  const s = `${requestedAction} ${task}`.toLowerCase()
  let taskClass = 'general'
  if (/security|güvenlik|auth|rls|secret|credential|injection|ssrf|permission/.test(s)) taskClass = 'security'
  else if (/deploy|release|production|ci\/cd|rollback|vercel|railway/.test(s)) taskClass = 'deployment_release'
  else if (/mail|email|outreach|gmail|reply|follow.?up|bounce|müşteri|teklif/.test(s)) taskClass = 'mail_outreach'
  else if (/shopify|woocommerce|checkout|cart|sepet|payment|ödeme|product|ürün|catalog|inventory|stok/.test(s)) taskClass = 'commerce'
  else if (/seo|geo|aeo|schema|canonical|index|sitemap|hreflang|search console/.test(s)) taskClass = 'seo_aeo_geo'
  else if (/ui|ux|frontend|responsive|browser|layout|tasarım|design|css|html|motion|glass/.test(s)) taskClass = 'web_ui'
  else if (/brand|marka|creative|grafik|graphic|logo|typography/.test(s)) taskClass = 'brand_creative'
  else if (/social|instagram|facebook|pinterest|reels|story/.test(s)) taskClass = 'social'
  else if (/agent|ajan|mcp|runtime|orchestrat|handoff|supervisor|reviewer/.test(s)) taskClass = 'agent_runtime'
  else if (/finance|finans|budget|bütçe|cash flow|margin|marj|forecast|valuation/.test(s)) taskClass = 'finance_operations'
  else if (/research|araştır|benchmark|source|kaynak|competitor|rakip/.test(s)) taskClass = 'research_upstream'

  let riskTier = 'R1'
  if (/delete|drop|truncate|destroy|credential|secret rotation|billing|payment execution|destructive|irreversible|mass migration/.test(s)) riskTier = 'R4'
  else if (/production\.deploy|production\.write|deploy|publish|send|outreach|checkout|payment|auth|rls|database write|migration|dns|customer reply/.test(s)) riskTier = 'R3'
  else if (/fix|implement|feature|code|automation|seo|ui|ux|customer deliverable|dashboard|integration/.test(s)) riskTier = 'R2'
  else if (/typo|docs only|read only|lookup|araştırma only/.test(s)) riskTier = 'R0'

  return { taskClass, riskTier }
}

const REVIEWERS: Record<string, string[]> = {
  security: ['Vinterro One Security Director','Security Auditor','Runtime Guard Agent','Capability Risk Agent','QA Auditor'],
  deployment_release: ['Deploy Guardian','CI Failure Investigator Agent','QA Auditor','Runtime Guard Agent'],
  mail_outreach: ['QA Auditor','Marketing Compliance Agent','Source Verification Agent','Vinterro Digital Baş Uzman Ajanı'],
  commerce: ['QA Auditor','Browser QA','E-commerce Expert Agent','Policy Engine Agent'],
  seo_aeo_geo: ['QA Auditor','Source Verification Agent','SEO Meta & Schema Agent','Web SEO/GEO Intelligence Agent'],
  web_ui: ['Browser QA','Responsive QA Agent','Accessibility Agent','Performance Agent','QA Auditor'],
  brand_creative: ['Creative QA & Brand Consistency Agent','UI/UX Director','QA Auditor','Brand Systems Agent'],
  social: ['Marketing Compliance Agent','Social Media Intelligence Agent','QA Auditor','Source Verification Agent'],
  agent_runtime: ['Agent Health Agent','Runtime Guard Agent','Handoff Guard Agent','QA Auditor','Capability Risk Agent'],
  finance_operations: ['QA Auditor','Source Verification Agent','Finance Expert Agent'],
  research_upstream: ['Source Verification Agent','QA Auditor','GitHub Web Intelligence Agent','Research Agent'],
  general: ['QA Auditor','Source Verification Agent','Agent Health Agent','Policy Engine Agent'],
}

function requiredReviewerCount(risk: string) {
  if (risk === 'R0') return 0
  if (risk === 'R1') return 1
  if (risk === 'R2') return 2
  if (risk === 'R3') return 2
  return 3
}

function evidenceRequirements(taskClass: string, riskTier: string) {
  const base = ['latest-state evidence', 'acceptance criteria mapping']
  const map: Record<string,string[]> = {
    web_ui: ['browser/runtime check', 'representative responsive viewport evidence'],
    commerce: ['real commerce flow evidence', 'read-after-action state'],
    mail_outreach: ['Gmail SENT/thread evidence', 'dedupe/compliance evidence'],
    security: ['deterministic security/policy check', 'no weakened guardrail evidence'],
    deployment_release: ['live target/version health', 'rollback or recovery evidence'],
    seo_aeo_geo: ['generated HTML/indexability evidence', 'source-of-truth configuration'],
    agent_runtime: ['trace/tool evidence', 'handoff/permission evidence'],
    finance_operations: ['calculation/source evidence', 'assumption separation'],
    research_upstream: ['primary-source provenance', 'freshness evidence'],
  }
  const out = [...base, ...(map[taskClass] || ['task-relevant outcome evidence'])]
  if (riskTier === 'R3' || riskTier === 'R4') out.push('independent final-gate evidence')
  return out
}

async function selectPlan(admin: any, orgId: string, run: any, activeProducerNames: string[] = []) {
  const { taskClass, riskTier } = classifyTask(String(run.task || ''), String(run.output?.requested_action || run.requested_action || 'research'))
  const { data: agents, error } = await admin.from('ercan_os_agents').select('id,name,role,status,instructions').eq('organization_id', orgId).eq('status', 'active')
  if (error) throw error
  const byName = new Map((agents || []).map((a:any) => [a.name, a]))
  const excluded = new Set([run.agent_id ? (agents || []).find((a:any)=>a.id===run.agent_id)?.name : null, ...activeProducerNames].filter(Boolean))
  const preferred = REVIEWERS[taskClass] || REVIEWERS.general
  const count = requiredReviewerCount(riskTier)
  const reviewers:any[] = []
  for (const name of preferred) {
    const a = byName.get(name)
    if (a && !excluded.has(name) && reviewers.length < count) reviewers.push(a)
  }
  if (reviewers.length < count) {
    for (const a of agents || []) {
      if (reviewers.length >= count) break
      if (excluded.has(a.name) || reviewers.some((r:any)=>r.id===a.id)) continue
      if (/qa|audit|guard|verification|approval|risk|review/i.test(`${a.name} ${a.role}`)) reviewers.push(a)
    }
  }
  const supervisors = reviewers.slice()
  const meta = byName.get('Agent Health Agent')
  if (riskTier === 'R3' || riskTier === 'R4') {
    const qa = byName.get('QA Auditor')
    if (qa && !excluded.has(qa.name) && !supervisors.some((x:any)=>x.id===qa.id)) supervisors.push(qa)
  }
  if (meta && !excluded.has(meta.name) && !supervisors.some((x:any)=>x.id===meta.id)) supervisors.push(meta)
  return {
    taskClass, riskTier, reviewers, supervisors,
    evidenceRequirements: evidenceRequirements(taskClass, riskTier),
  }
}

async function getOrPlan(admin: any, orgId: string, runId: string, body: any = {}) {
  let { data: supervision } = await admin.from('vinterro_one_supervision_runs').select('*').eq('organization_id',orgId).eq('run_id',runId).maybeSingle()
  if (supervision) return supervision
  const { data: run, error } = await admin.from('ercan_os_runs').select('*').eq('organization_id',orgId).eq('id',runId).single()
  if (error) throw error
  const activeNames = Array.isArray(run.output?.routing?.active_agents) ? run.output.routing.active_agents : []
  const plan = await selectPlan(admin, orgId, run, activeNames)
  const { data, error: insertError } = await admin.from('vinterro_one_supervision_runs').insert({
    organization_id: orgId,
    run_id: run.id,
    project_id: run.project_id,
    producer_agent_id: run.agent_id,
    producer_agent_name: activeNames[0] || null,
    task_class: plan.taskClass,
    requested_action: String(run.output?.requested_action || body.requested_action || 'research'),
    risk_tier: plan.riskTier,
    state: run.status === 'running' ? 'EXECUTING' : 'PLANNED',
    reviewer_agent_ids: plan.reviewers.map((a:any)=>a.id),
    reviewer_agent_names: plan.reviewers.map((a:any)=>a.name),
    supervisor_agent_ids: plan.supervisors.map((a:any)=>a.id),
    supervisor_agent_names: plan.supervisors.map((a:any)=>a.name),
    acceptance_criteria: body.acceptance_criteria || [],
    do_not_touch: body.do_not_touch || [],
    evidence_requirements: plan.evidenceRequirements,
  }).select().single()
  if (insertError) throw insertError
  await admin.from('vinterro_one_supervision_events').insert({
    organization_id: orgId, supervision_id: data.id, run_id: run.id, event_type: 'supervision_planned',
    detail: { risk_tier: plan.riskTier, task_class: plan.taskClass, reviewers: plan.reviewers.map((a:any)=>a.name), evidence_requirements: plan.evidenceRequirements }
  })
  return data
}

function extractResponseText(data:any) {
  if (typeof data?.output_text === 'string') return data.output_text
  if (typeof data?.response?.output_text === 'string') return data.response.output_text
  const root = data?.response || data
  for (const item of root?.output || []) {
    for (const c of item?.content || []) if (typeof c?.text === 'string') return c.text
  }
  return ''
}

function parseReview(text:string) {
  const cleaned = text.trim().replace(/^\`\`\`(?:json)?/i,'').replace(/\`\`\`$/,'').trim()
  try { return JSON.parse(cleaned) } catch {}
  const a = cleaned.indexOf('{'), b = cleaned.lastIndexOf('}')
  if (a >= 0 && b > a) try { return JSON.parse(cleaned.slice(a,b+1)) } catch {}
  return {
    verdict:'PARTIAL', severity:'MAJOR',
    claim_reviewed:'Reviewer output could not be parsed',
    expected_state:'Structured evidence-backed review',
    observed_state:cleaned.slice(0,2000),
    evidence_refs:[],
    violated_rule_or_acceptance_criterion:'review output contract',
    root_cause_hypothesis:'unstructured reviewer output',
    required_fix:'repeat review with structured JSON',
    retest_plan:'rerun independent review',
    freshness_requirement:'fresh review required'
  }
}

async function callReviewer(authHeader:string, reviewer:any, run:any, supervision:any, evidence:any[]) {
  const prompt = [
    'You are an independent Vinterro One verification agent.',
    'You did not implement the work. Do not rubber-stamp. Grade real evidence, not the producer\'s confidence.',
    'Deterministic environment/account/tool facts outrank semantic opinion.',
    'If evidence is insufficient to prove the requested outcome, do NOT return PASS.',
    'Return ONLY valid JSON with keys: verdict, severity, claim_reviewed, expected_state, observed_state, evidence_refs, violated_rule_or_acceptance_criterion, root_cause_hypothesis, required_fix, retest_plan, freshness_requirement.',
    'Allowed verdict: PASS, CORRECTION_REQUIRED, DISPUTED, BLOCKED, PARTIAL.',
    'Allowed severity: INFO, MINOR, MAJOR, BLOCKER, CRITICAL.',
    '',
    `Reviewer: ${reviewer.name} / ${reviewer.role}`,
    `Reviewer mandate: ${String(reviewer.instructions || '')}`,
    `Risk tier: ${supervision.risk_tier}`,
    `Task class: ${supervision.task_class}`,
    `Task: ${run.task}`,
    `Acceptance criteria: ${JSON.stringify(supervision.acceptance_criteria || [])}`,
    `Do-not-touch: ${JSON.stringify(supervision.do_not_touch || [])}`,
    `Evidence requirements: ${JSON.stringify(supervision.evidence_requirements || [])}`,
    `Producer output/claim: ${JSON.stringify(run.output || {})}`,
    `Independent evidence: ${JSON.stringify(evidence || [])}`,
    'PASS is allowed only if the supplied evidence proves the latest requested outcome and no MAJOR/BLOCKER/CRITICAL issue remains.'
  ].join('\n')
  const response = await fetch(`${SUPABASE_URL}/functions/v1/ercan-openai-runtime`, {
    method:'POST',
    headers:{ Authorization:authHeader, apikey:ANON_KEY, 'Content-Type':'application/json' },
    body:JSON.stringify({ action:'responses', body:{ model:'gpt-5.6-sol', input:prompt } }),
    signal:AbortSignal.timeout(55000)
  })
  const data = await response.json().catch(()=>({}))
  if (!response.ok || !data?.ok) {
    return {
      verdict:'PARTIAL', severity:'MAJOR', claim_reviewed:'Automated independent review',
      expected_state:'Independent reviewer completed', observed_state:`Reviewer runtime unavailable: ${data?.error || response.status}`,
      evidence_refs:[], violated_rule_or_acceptance_criterion:'independent review required',
      root_cause_hypothesis:'reviewer runtime unavailable', required_fix:'restore reviewer runtime or perform independent review through another qualified runtime',
      retest_plan:'repeat review after reviewer runtime is available', freshness_requirement:'fresh review required',
      runtime_error:data?.error || `HTTP ${response.status}`
    }
  }
  return parseReview(extractResponseText(data))
}

async function updateReliability(admin:any, orgId:string, agentId:string|null, taskClass:string, delta:Record<string,number>) {
  if (!agentId) return
  const { data: current } = await admin.from('vinterro_one_agent_reliability').select('*')
    .eq('organization_id',orgId).eq('agent_id',agentId).eq('task_class',taskClass).maybeSingle()
  const row:any = current || { organization_id:orgId, agent_id:agentId, task_class:taskClass }
  const numeric = [
    'producer_reviewed_count','producer_first_pass_count','producer_correction_count','producer_blocker_count',
    'producer_regression_count','unsupported_completion_claims','reviewer_review_count','reviewer_false_pass_count',
    'reviewer_false_block_count','reviewer_arbitration_overturn_count','reviewer_seeded_failure_detect_count',
    'freshness_violation_count'
  ]
  for (const k of numeric) row[k] = Number(row[k] || 0) + Number(delta[k] || 0)
  row.updated_at = now()
  row.last_reviewed_at = now()
  await admin.from('vinterro_one_agent_reliability').upsert(row,{onConflict:'organization_id,agent_id,task_class'})
}

async function finalize(admin:any, orgId:string, supervision:any) {
  const { data: reviews } = await admin.from('vinterro_one_supervision_reviews').select('*')
    .eq('organization_id',orgId).eq('supervision_id',supervision.id).order('created_at',{ascending:false})
  const latestByReviewer = new Map<string,any>()
  for (const r of reviews || []) if (!latestByReviewer.has(r.reviewer_agent_name)) latestByReviewer.set(r.reviewer_agent_name,r)
  const latest = [...latestByReviewer.values()]
  const required = requiredReviewerCount(supervision.risk_tier)
  let state = 'NOT_VERIFIED'
  let reason = `Need ${required} independent review(s); have ${latest.length}`
  if (latest.some((r:any)=>r.verdict==='BLOCKED' || r.severity==='CRITICAL')) { state='BLOCKED'; reason='Blocking or critical finding remains' }
  else if (latest.some((r:any)=>r.verdict==='CORRECTION_REQUIRED')) { state='CORRECTION_REQUIRED'; reason='Correction required before fresh review' }
  else if (latest.some((r:any)=>r.verdict==='DISPUTED')) { state='DISPUTED'; reason='Reviewer disagreement requires arbitration' }
  else if (latest.length >= required && required > 0 && latest.slice(0,required).every((r:any)=>r.verdict==='PASS')) { state='VERIFIED'; reason='Independent review gate passed' }
  else if (required===0) { state='NOT_VERIFIED'; reason='R0 cannot bypass independent review' }
  else if (latest.some((r:any)=>r.verdict==='PARTIAL')) { state='PARTIAL'; reason='Evidence/review is incomplete' }

  // A provider result, even from an authorized owner, is not verified
  // execution unless a registered live worker recorded an immutable receipt.
  if (supervision.run_id) {
    const { data: hasReceipt, error: receiptError } = await admin.rpc(
      'vinterro_has_agent_execution_receipt', { p_run_id: supervision.run_id }
    )
    if (receiptError || hasReceipt !== true) {
      state='NOT_VERIFIED'
      reason='Registered worker/provider execution receipt is missing'
    } else if (state==='VERIFIED' && !latest.some((r:any)=>
      r.verdict==='PASS' && r.reviewer_agent_id!==supervision.producer_agent_id
    )) {
      state='NOT_VERIFIED'
      reason='Independent PASS reviewer is required'
    }
  }

  await admin.from('vinterro_one_supervision_runs').update({
    state, final_gate_state: state, final_gate_reason: reason, updated_at:now()
  }).eq('id',supervision.id).eq('organization_id',orgId)

  if (supervision.run_id && state!=='NOT_VERIFIED') {
    const runStatus = state==='VERIFIED' ? 'success' : state==='BLOCKED' ? 'blocked' : state==='CORRECTION_REQUIRED' ? 'running' : 'under_review'
    await admin.from('ercan_os_runs').update({
      status:runStatus,
      completed_at:state==='VERIFIED'||state==='BLOCKED' ? now() : null
    }).eq('id',supervision.run_id).eq('organization_id',orgId)
  }
  await admin.from('vinterro_one_supervision_events').insert({
    organization_id:orgId, supervision_id:supervision.id, run_id:supervision.run_id,
    event_type:'final_gate_evaluated', detail:{state,reason,review_count:latest.length,required}
  })
  return { state, reason, reviews: latest }
}

Deno.serve(async (req:Request) => {
  if (req.method==='OPTIONS') return new Response('ok',{headers:cors})
  if (req.method!=='POST') return J({error:'POST only'},405)
  try {
    const authHeader=req.headers.get('authorization')||''
    const userClient=createClient(SUPABASE_URL,ANON_KEY,{global:{headers:{Authorization:authHeader}}})
    const admin=createClient(SUPABASE_URL,SERVICE_KEY,{auth:{persistSession:false,autoRefreshToken:false}})
    const {data:{user},error:userError}=await userClient.auth.getUser()
    if (userError||!user) return J({error:'Unauthorized'},401)
    if (!(await owner(user))) return J({error:'Forbidden'},403)
    const {data:membership,error:membershipError}=await userClient.from('ercan_os_memberships').select('organization_id').limit(1).maybeSingle()
    if (membershipError) throw membershipError
    if (!membership?.organization_id) return J({error:'Vinterro One organization not found'},404)
    const orgId=membership.organization_id
    const body=await req.json().catch(()=>({}))
    const action=String(body.action||'status')

    if (action==='status') {
      const [{count:agents},{count:profiles},{data:open}] = await Promise.all([
        admin.from('ercan_os_agents').select('*',{count:'exact',head:true}).eq('organization_id',orgId).eq('status','active'),
        admin.from('ercan_os_agent_expertise_profiles').select('*',{count:'exact',head:true}).eq('organization_id',orgId),
        admin.from('vinterro_one_supervision_runs').select('id,state,risk_tier,task_class,created_at').eq('organization_id',orgId)
          .not('state','in','("VERIFIED","BLOCKED")').order('created_at',{ascending:false}).limit(20)
      ])
      return J({ok:true,system:'Vinterro One',active_agents:agents||0,expertise_profiles:profiles||0,expertise_gap:Math.max(0,Number(agents||0)-Number(profiles||0)),open_supervision:open||[]})
    }

    if (action==='plan_run') {
      const runId=String(body.run_id||'')
      if (!runId) return J({error:'run_id required'},400)
      const supervision=await getOrPlan(admin,orgId,runId,body)
      return J({ok:true,supervision})
    }

    if (action==='claim_run') {
      const runId=String(body.run_id||'')
      const supervision=await getOrPlan(admin,orgId,runId,body)
      const {data:run,error}=await admin.from('ercan_os_runs').select('*').eq('organization_id',orgId).eq('id',runId).single()
      if (error) throw error
      await admin.from('vinterro_one_supervision_runs').update({
        state:'CLAIMED', producer_claim:body.claim||run.output||{}, updated_at:now()
      }).eq('id',supervision.id)
      await admin.from('vinterro_one_supervision_events').insert({
        organization_id:orgId,supervision_id:supervision.id,run_id:runId,event_type:'producer_claimed',
        actor_agent_id:run.agent_id,detail:{claim:body.claim||run.output||{}}
      })
      return J({ok:true,state:'CLAIMED',supervision_id:supervision.id})
    }

    if (action==='review_run') {
      const runId=String(body.run_id||'')
      if (!runId) return J({error:'run_id required'},400)
      const { data: hasReceipt, error: receiptError } = await admin.rpc(
        'vinterro_has_agent_execution_receipt', { p_run_id: runId }
      )
      if (receiptError || hasReceipt !== true) {
        return J({
          ok:false, code:'agent_execution_receipt_required',
          error:'No registered worker/model evidence; independent model review not started'
        },409)
      }
      let supervision=await getOrPlan(admin,orgId,runId,body)
      const {data:run,error}=await admin.from('ercan_os_runs').select('*').eq('organization_id',orgId).eq('id',runId).single()
      if (error) throw error
      await admin.from('vinterro_one_supervision_runs').update({state:'UNDER_REVIEW',producer_claim:run.output||{},updated_at:now()}).eq('id',supervision.id)
      const {data:reviewers}=await admin.from('ercan_os_agents').select('id,name,role,instructions')
        .in('id',supervision.reviewer_agent_ids||[])
      const {data:toolCalls}=await admin.from('ercan_os_tool_calls').select('id,tool_name,status,latency_ms,created_at,output')
        .eq('organization_id',orgId).eq('run_id',runId).order('created_at',{ascending:false}).limit(30)
      const evidence=[
        ...(Array.isArray(body.evidence)?body.evidence:[]),
        ...(toolCalls||[]).map((t:any)=>({type:'tool_call',id:t.id,tool:t.tool_name,status:t.status,created_at:t.created_at,output:t.output}))
      ]
      const results=await Promise.all((reviewers||[]).map(async(reviewer:any)=>{
        const raw=await callReviewer(authHeader,reviewer,run,supervision,evidence)
        const verdict=['PASS','CORRECTION_REQUIRED','DISPUTED','BLOCKED','PARTIAL'].includes(raw.verdict)?raw.verdict:'PARTIAL'
        const severity=['INFO','MINOR','MAJOR','BLOCKER','CRITICAL'].includes(raw.severity)?raw.severity:'MAJOR'
        const {data:review,error:reviewError}=await admin.from('vinterro_one_supervision_reviews').insert({
          organization_id:orgId,supervision_id:supervision.id,run_id:runId,reviewer_agent_id:reviewer.id,
          reviewer_agent_name:reviewer.name,reviewer_kind:'independent_reviewer',verdict,severity,
          claim_reviewed:raw.claim_reviewed||null,expected_state:raw.expected_state||null,observed_state:raw.observed_state||null,
          evidence_refs:Array.isArray(raw.evidence_refs)?raw.evidence_refs:[],violated_rule_or_acceptance_criterion:raw.violated_rule_or_acceptance_criterion||null,
          root_cause_hypothesis:raw.root_cause_hypothesis||null,required_fix:raw.required_fix||null,
          do_not_touch:supervision.do_not_touch||[],retest_plan:raw.retest_plan||null,freshness_requirement:raw.freshness_requirement||null,raw_review:raw
        }).select().single()
        if (reviewError) throw reviewError
        await updateReliability(admin,orgId,reviewer.id,supervision.task_class,{reviewer_review_count:1})
        return review
      }))
      await updateReliability(admin,orgId,supervision.producer_agent_id,supervision.task_class,{
        producer_reviewed_count:1,
        producer_first_pass_count:results.length>0&&results.every((r:any)=>r.verdict==='PASS')?1:0,
        producer_correction_count:results.some((r:any)=>r.verdict==='CORRECTION_REQUIRED')?1:0,
        producer_blocker_count:results.some((r:any)=>r.verdict==='BLOCKED'||r.severity==='CRITICAL')?1:0
      })
      supervision=(await admin.from('vinterro_one_supervision_runs').select('*').eq('id',supervision.id).single()).data
      const gate=await finalize(admin,orgId,supervision)
      return J({ok:true,supervision_id:supervision.id,reviews:results,final_gate:gate})
    }

    if (action==='submit_review') {
      const supervisionId=String(body.supervision_id||'')
      const {data:supervision,error:sErr}=await admin.from('vinterro_one_supervision_runs').select('*').eq('organization_id',orgId).eq('id',supervisionId).single()
      if (sErr) throw sErr
      const reviewerId=String(body.reviewer_agent_id||'')
      if (!reviewerId || !(supervision.reviewer_agent_ids||[]).includes(reviewerId)) return J({error:'Reviewer is not assigned to this supervision'},403)
      if (reviewerId===supervision.producer_agent_id) return J({error:'Producer cannot verify own material work'},409)
      const {data:agent}=await admin.from('ercan_os_agents').select('name').eq('id',reviewerId).single()
      const verdict=['PASS','CORRECTION_REQUIRED','DISPUTED','BLOCKED','PARTIAL'].includes(body.verdict)?body.verdict:'PARTIAL'
      const severity=['INFO','MINOR','MAJOR','BLOCKER','CRITICAL'].includes(body.severity)?body.severity:'MAJOR'
      const {data:review,error:rErr}=await admin.from('vinterro_one_supervision_reviews').insert({
        organization_id:orgId,supervision_id:supervision.id,run_id:supervision.run_id,reviewer_agent_id:reviewerId,
        reviewer_agent_name:agent?.name||'Unknown Reviewer',reviewer_kind:body.reviewer_kind||'independent_reviewer',verdict,severity,
        claim_reviewed:body.claim_reviewed||null,expected_state:body.expected_state||null,observed_state:body.observed_state||null,
        evidence_refs:Array.isArray(body.evidence_refs)?body.evidence_refs:[],violated_rule_or_acceptance_criterion:body.violated_rule_or_acceptance_criterion||null,
        root_cause_hypothesis:body.root_cause_hypothesis||null,required_fix:body.required_fix||null,
        do_not_touch:supervision.do_not_touch||[],retest_plan:body.retest_plan||null,freshness_requirement:body.freshness_requirement||null,
        raw_review:body.raw_review||{}
      }).select().single()
      if (rErr) throw rErr
      const gate=await finalize(admin,orgId,supervision)
      return J({ok:true,review,final_gate:gate})
    }

    if (action==='mark_retesting') {
      const supervisionId=String(body.supervision_id||'')
      const {data:supervision,error}=await admin.from('vinterro_one_supervision_runs').select('*').eq('organization_id',orgId).eq('id',supervisionId).single()
      if (error) throw error
      const retry=Number(supervision.retry_count||0)+1
      await admin.from('vinterro_one_supervision_runs').update({state:'RETESTING',retry_count:retry,final_gate_state:null,final_gate_reason:null,updated_at:now()}).eq('id',supervisionId)
      await admin.from('vinterro_one_supervision_events').insert({
        organization_id:orgId,supervision_id:supervisionId,run_id:supervision.run_id,event_type:retry>=2?'recovery_escalated':'retesting',
        detail:{retry_count:retry,root_cause_reset_required:retry>=2,alternate_owner_required:retry>=2}
      })
      return J({ok:true,state:'RETESTING',retry_count:retry,recovery_escalated:retry>=2})
    }

    if (action==='get_supervision') {
      const supervisionId=String(body.supervision_id||'')
      const runId=String(body.run_id||'')
      let q=admin.from('vinterro_one_supervision_runs').select('*').eq('organization_id',orgId)
      q=supervisionId?q.eq('id',supervisionId):q.eq('run_id',runId)
      const {data:supervision,error}=await q.single()
      if (error) throw error
      const [{data:reviews},{data:events}]=await Promise.all([
        admin.from('vinterro_one_supervision_reviews').select('*').eq('supervision_id',supervision.id).order('created_at'),
        admin.from('vinterro_one_supervision_events').select('*').eq('supervision_id',supervision.id).order('created_at')
      ])
      return J({ok:true,supervision,reviews:reviews||[],events:events||[]})
    }

    if (action==='reliability') {
      const {data,error}=await admin.from('vinterro_one_agent_reliability').select('*,ercan_os_agents(name,role)')
        .eq('organization_id',orgId).order('updated_at',{ascending:false})
      if (error) throw error
      return J({ok:true,reliability:data||[]})
    }

    return J({error:`Unknown action: ${action}`},400)
  } catch (e) {
    console.error('Vinterro One supervision error',e)
    return J({error:e instanceof Error?e.message:String(e)},500)
  }
})
