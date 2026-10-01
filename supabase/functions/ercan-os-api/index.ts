import { createClient } from 'npm:@supabase/supabase-js@2.112.2'

const OWNER_EMAIL_HASHES = new Set([
  '560c6c2879a2084c35e78377bb800a09e30a9dcc9fc60cf6083a317e59a5454c',
  '35d039ff6d0697e6667a66c13c8d03e55dc5a8e27f85180fb88e2b05352a97a4',
])
async function isAuthorizedOwner(user: any) {
  const email = String(user?.email || '').trim().toLowerCase()
  if (!email) return false
  const bytes = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(email))
  const hash = Array.from(new Uint8Array(bytes)).map((b) => b.toString(16).padStart(2, '0')).join('')
  return OWNER_EMAIL_HASHES.has(hash)
}

const cors = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Content-Type': 'application/json',
}
const SUPABASE_URL = Deno.env.get('SUPABASE_URL') ?? ''
const ANON_KEY = Deno.env.get('SUPABASE_ANON_KEY') ?? ''
const SERVICE_KEY = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
const json = (data: unknown, status = 200) => new Response(JSON.stringify(data), { status, headers: cors })
const now = () => new Date().toISOString()
const slugify = (value: string) => value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || crypto.randomUUID().slice(0, 8)

const MASTER_TRIGGER = /(ajanları çalıştır|ajanlari calistir|tüm ajanları çalıştır|tum ajanlari calistir|bütün ajanları çalıştır|butun ajanlari calistir|run agents|run the agents|run all agents)/i

type RoutingRule = { rx: RegExp; agents: string[]; weight?: number }
const ROUTING_RULES: RoutingRule[] = [
  { rx: /\b(finans|finance|fp&a|bütçe|budget|cash flow|nakit ak|marj|margin|unit economics|değerleme|valuation|forecast|tahmin|p&l|gelir tablosu|bilanço)\b/i, agents: ['Finance Expert Agent','Analytics & Attribution Agent','Research Agent'], weight: 10 },
  { rx: /\b(e-?commerce|ecommerce|e-ticaret|eticaret|marketplace|pazar yeri|merchant center|checkout|cart|sepet|catalog|katalog|merchandising|stok|inventory|shipping|kargo|returns?|iade)\b/i, agents: ['E-commerce Expert Agent','Conversion & CRO Agent','Analytics & Attribution Agent','SEO Meta & Schema Agent'], weight: 10 },
  { rx: /\b(shopify|liquid|collection|koleksiyon|product|ürün|pdp|plp)\b/i, agents: ['Shopify Agent','Shopify Theme Developer','E-commerce Expert Agent'], weight: 9 },
  { rx: /\b(wordpress|woocommerce|wp|plugin|tema|theme)\b/i, agents: ['WordPress Agent','WordPress Plugin Developer','E-commerce Expert Agent'], weight: 9 },
  { rx: /\b(seo|geo|schema|canonical|search console|index|sitemap|hreflang|merchant feed)\b/i, agents: ['SEO/GEO Agent','SEO Meta & Schema Agent','Web SEO/GEO Intelligence Agent'], weight: 9 },
  { rx: /\b(research|araştır|benchmark|rakip|competitor|trend|kaynak|source)\b/i, agents: ['Research Agent','GitHub Web Intelligence Agent','Competitive & Trend Intelligence Agent'], weight: 8 },
  { rx: /\b(deploy|deployment|vercel|server|devops|ci|github|release|rollback)\b/i, agents: ['DevOps Agent','Deploy Guardian','CI Failure Investigator Agent'], weight: 9 },
  { rx: /\b(görsel|graphic|tasarım|design|image|instagram|carousel|brand|marka|ui|ux|figma|motion)\b/i, agents: ['Graphic Agent','Creative Director','UI/UX Director','Brand Systems Agent','Creative QA & Brand Consistency Agent'], weight: 8 },
  { rx: /\b(içerik|content|caption|metin|copy|blog|editorial|newsletter|email copy)\b/i, agents: ['Content Agent','Content & SEO Editor','Content Distribution Agent'], weight: 8 },
  { rx: /\b(kod|code|api|bug|hata|frontend|backend|javascript|typescript|react|next\.js|supabase|firebase)\b/i, agents: ['Developer Agent','Debugger','Next.js + Supabase Engineer','Language Freshness Agent'], weight: 9 },
  { rx: /\b(qa|test|verify|doğrula|kontrol|e2e|browser|responsive|accessibility|performance)\b/i, agents: ['QA Agent','QA Auditor','Browser QA','Accessibility Agent','Performance Agent','Responsive QA Agent'], weight: 8 },
  { rx: /\b(social|sosyal medya|instagram|facebook|pinterest|reels|story|caption)\b/i, agents: ['Social Media Director','Social Media Intelligence Agent','Social Creative Agent'], weight: 8 },
  { rx: /\b(ad|ads|reklam|meta ads|google ads|paid media|campaign|kampanya)\b/i, agents: ['Paid Media Intelligence Agent','Campaign Creative Intelligence Agent','Analytics & Attribution Agent','Marketing Compliance Agent'], weight: 9 },
  { rx: /\b(agent|ajan|mcp|tool|runtime|sandbox|permission|policy|supply chain)\b/i, agents: ['Agent Lifecycle Agent','Capability Risk Agent','MCP Risk Scanner Agent','Runtime Guard Agent','Supply Chain Guard Agent'], weight: 8 },
  { rx: /\b(security|güvenlik|auth|authorization|rls|secret|credential|ssrf|injection)\b/i, agents: ['Security Auditor','Security & License Agent','Runtime Guard Agent','Policy Engine Agent'], weight: 10 },
  { rx: /\b(ayvalık|cunda|keşif|mekan|venue|event|etkinlik|poi|türkiye geneli)\b/i, agents: ['Vinterro Keşif Agent','Source Verification Agent','Place Intelligence Agent','Keşif QA Agent'], weight: 9 },
]

function normalizeRouteText(value: string) {
  return String(value || '')
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/ı/g, 'i')
    .replace(/ğ/g, 'g')
    .replace(/ş/g, 's')
    .replace(/ç/g, 'c')
    .replace(/ö/g, 'o')
    .replace(/ü/g, 'u')
    .replace(/&/g, ' and ')
    .replace(/[^a-z0-9]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim()
}

const ROUTE_STOPWORDS = new Set([
  'agent','ajani','ajan','uzman','bas','lead','expert','project','proje','vinterro','one',
  'the','and','for','with','run','all','tum','butun','calistir','task','gorev','current','active'
])

function routeTokens(value: string) {
  return normalizeRouteText(value)
    .split(' ')
    .filter((token) => token.length >= 3 && !ROUTE_STOPWORDS.has(token))
}

function resolveProject(task: string, projects: any[], explicitProjectId?: string | null) {
  const activeProjects = (projects || []).filter((p: any) => p.status === 'active')
  if (explicitProjectId) {
    const exact = activeProjects.find((p: any) => p.id === explicitProjectId)
    if (exact) return exact
  }

  const text = normalizeRouteText(task)
  let best: any = null
  let bestScore = 0
  for (const project of activeProjects) {
    const name = normalizeRouteText(project.name)
    const slug = normalizeRouteText(project.slug)
    const aliases = new Set<string>([name, slug])
    if (name.includes('drag and drop')) aliases.add('dragdrop')
    if (name === 'forme') aliases.add('forme')
    if (name.includes('cicek sahaf')) aliases.add('cicek sahaf')
    if (name.includes('dukkan ayvalik')) aliases.add('dukkan ayvalik')
    if (name.includes('go ayvalik')) aliases.add('go ayvalik')
    if (name.includes('ayvalik vibes')) aliases.add('ayvalik vibes')
    if (name.includes('ayvalik reklam')) aliases.add('ayvalik reklam')
    if (name.includes('vinterro kesif')) aliases.add('vinterro kesif')
    if (name.includes('vinterro digital')) aliases.add('vinterro digital')
    if (name.includes('vinterro studio')) aliases.add('vinterro studio')
    if (name.includes('vinterro social')) aliases.add('vinterro social os')

    let score = 0
    for (const alias of aliases) {
      if (!alias) continue
      if (text.includes(alias)) score = Math.max(score, 50 + alias.length)
    }
    const tokens = routeTokens(name)
    const overlap = tokens.filter((token) => text.includes(token)).length
    if (tokens.length >= 2 && overlap >= 2) score = Math.max(score, 20 + overlap * 5)
    if (score > bestScore) {
      best = project
      bestScore = score
    }
  }
  return best
}

function projectAgentTaskScore(task: string, agent: any) {
  const taskText = normalizeRouteText(task)
  const tokens = [...new Set([...routeTokens(agent.name), ...routeTokens(agent.role)])]
  let score = 0
  for (const token of tokens) {
    if (taskText.includes(token)) score += token.length >= 7 ? 4 : 2
  }
  return score
}

function selectAgentPod(
  task: string,
  agents: any[],
  requestedAction = 'research',
  projects: any[] = [],
  explicitProjectId?: string | null,
) {
  const activeAgents = agents.filter((a: any) => a.status === 'active')
  const byName = new Map(activeAgents.map((a: any) => [a.name, a]))
  const scores = new Map<string, number>()
  const add = (name: string, score: number) => {
    if (!byName.has(name)) return
    scores.set(name, Math.max(scores.get(name) || 0, score))
  }

  const masterMode = MASTER_TRIGGER.test(task)
  const project = resolveProject(task, projects, explicitProjectId)
  const projectAgents = project
    ? activeAgents.filter((a: any) => a.project_id === project.id)
    : []
  const projectLead =
    projectAgents.find((a: any) => a.role === 'project_lead_expert') ||
    projectAgents.find((a: any) => /lead/i.test(String(a.role || ''))) ||
    projectAgents.find((a: any) => /bas uzman|baş uzman/i.test(String(a.name || ''))) ||
    projectAgents.find((a: any) => /vinterro_kesif_lead/i.test(String(a.role || ''))) ||
    null

  if (masterMode) add('Orchestrator', 100)
  if (projectLead) add(projectLead.name, 120)

  for (const rule of ROUTING_RULES) {
    if (!rule.rx.test(task)) continue
    const base = rule.weight || 5
    rule.agents.forEach((name, i) => add(name, Math.max(1, base - i)))
  }

  if (project) {
    for (const agent of projectAgents) {
      if (projectLead && agent.id === projectLead.id) continue
      const lexical = projectAgentTaskScore(task, agent)
      if (lexical > 0) add(agent.name, 30 + lexical)
    }
  }

  const riskText = requestedAction + ' ' + task
  if (/production\.|deploy|publish|send|email|delete|billing|payment|odeme|ödeme|price|fiyat|inventory|stok/i.test(riskText)) {
    add('Policy Engine Agent', 18)
    add('Human Approval Agent', 17)
  }
  if (/security|guvenlik|güvenlik|auth|authorization|rls|secret|credential|oauth|dependency|ci\/cd|infrastructure|deploy/i.test(riskText)) {
    add('Vinterro One Security Director', 22)
    add('Security Auditor', 21)
  }

  const materialTask = /code|kod|site|web|shopify|wordpress|design|tasarim|tasarım|seo|mail|email|deploy|publish|campaign|kampanya|security|guvenlik|güvenlik|api|database|supabase|performance|accessibility|odeme|ödeme|checkout|cart|sepet/i.test(riskText)
  if (materialTask) add('QA Agent', 16)

  if (!scores.size) {
    if (projectLead) add(projectLead.name, 120)
    else add(masterMode ? 'Orchestrator' : 'Research Agent', 5)
  }

  const ranked = [...scores.entries()]
    .sort((a,b) => b[1] - a[1])
    .map(([name,score]) => ({ ...(byName.get(name) || {}), routing_score: score }))

  const primary = projectLead
    ? ({ ...projectLead, routing_score: Math.max(scores.get(projectLead.name) || 0, 120) })
    : masterMode
      ? ({ ...(byName.get('Orchestrator') || ranked[0] || activeAgents[0] || {}), routing_score: scores.get('Orchestrator') || ranked[0]?.routing_score || 0 })
      : (ranked[0] || byName.get('Orchestrator') || activeAgents[0] || null)

  const selected: any[] = []
  const seen = new Set<string>()
  if (primary?.name) {
    selected.push(primary)
    seen.add(primary.name)
  }
  for (const agent of ranked) {
    if (!seen.has(agent.name)) {
      selected.push(agent)
      seen.add(agent.name)
    }
  }

  if (materialTask && !seen.has('QA Agent') && byName.has('QA Agent')) {
    selected.push({ ...(byName.get('QA Agent') || {}), routing_score: 16 })
    seen.add('QA Agent')
  }

  const standby = activeAgents.filter((a: any) => !seen.has(a.name))
  const routingReason = [
    project ? `project=${project.name}` : 'project=unresolved',
    masterMode ? 'master-trigger-complete-relevant-pod' : 'task-relevance',
    `active=${selected.length}`,
    'no-fixed-agent-cap',
  ].join('; ')

  return {
    primary,
    active: selected,
    standby,
    master_mode: masterMode,
    routing_reason: routingReason,
    project,
  }
}

async function currentOrg(userClient: any) {
  const { data, error } = await userClient.from('ercan_os_memberships').select('organization_id, role').limit(1)
  if (error) throw error
  if (!data?.length) throw new Error('No organization membership')
  return data[0]
}

async function seedNativeConnectors(admin: any, orgId: string, userId: string) {
  const rows = [
    { name: 'Supabase Control Plane', provider: 'supabase', kind: 'native', status: 'connected', config: { project_ref: 'mjigewyqwnkknjbqxjuk' }, capabilities: ['database.read','database.write','edge.invoke','auth.read'] },
    { name: 'Vercel AI Gateway', provider: 'vercel', kind: 'native', status: 'connected', config: { auth: 'oidc', model: 'openai/gpt-5.6-sol' }, capabilities: ['ai.generate','ai.tool_call'] },
  ]
  for (const row of rows) {
    const { data } = await admin.from('ercan_os_connectors').select('id').eq('organization_id', orgId).eq('name', row.name).maybeSingle()
    if (!data) await admin.from('ercan_os_connectors').insert({ organization_id: orgId, created_by: userId, ...row })
  }
}

async function bootstrap(admin: any, userId: string) {
  const { data: existing, error: membershipError } = await admin.from('ercan_os_memberships').select('organization_id, role').eq('user_id', userId).limit(1)
  if (membershipError) throw membershipError
  if (existing?.length) {
    await seedNativeConnectors(admin, existing[0].organization_id, userId)
    return existing[0].organization_id
  }
  const orgSlug = `ercan-os-${userId.slice(0, 8)}`
  const { data: org, error: orgError } = await admin.from('ercan_os_organizations').insert({ name: 'ERCAN OS', slug: orgSlug }).select('id').single()
  if (orgError) throw orgError
  const { error: memberInsertError } = await admin.from('ercan_os_memberships').insert({ organization_id: org.id, user_id: userId, role: 'owner' })
  if (memberInsertError) throw memberInsertError
  const projectNames = ['Vinterro Digital', 'Drag&Drop', 'Ayvalık Vibes', 'Go Ayvalık', 'Ayvalık Reklam']
  const { error: projectError } = await admin.from('ercan_os_projects').insert(projectNames.map((name) => ({ organization_id: org.id, name, slug: slugify(name), status: 'active', health: 100 })))
  if (projectError) throw projectError
  const agents = [
    ['Orchestrator','orchestrator','Route tasks to the smallest necessary specialist set and enforce policy gates.'],
    ['Research Agent','research','Perform source-backed research and competitive analysis.'],
    ['SEO/GEO Agent','seo','Audit technical SEO, GEO, schema, indexation and search visibility.'],
    ['Developer Agent','developer','Implement and debug application code and APIs.'],
    ['QA Agent','qa','Verify outputs, regressions, policies and deployment health.'],
    ['Content Agent','content','Create and refine brand-aligned content.'],
    ['Graphic Agent','graphic','Prepare visual briefs, social layouts and design QA.'],
    ['WordPress Agent','wordpress','Operate WordPress workflows under policy controls.'],
    ['Shopify Agent','shopify','Operate Shopify catalog and theme workflows under policy controls.'],
    ['DevOps Agent','devops','Handle deployments, CI/CD, monitoring and infrastructure checks.'],
  ].map(([name, role, instructions]) => ({ organization_id: org.id, name, role, instructions, status: 'active', version: '0.6.0', health: 100 }))
  const { error: agentError } = await admin.from('ercan_os_agents').insert(agents)
  if (agentError) throw agentError
  const policies = [['read','allow'],['research','allow'],['production.write','approval_required'],['production.deploy','approval_required'],['delete','deny'],['billing.change','approval_required']]
    .map(([action, decision]) => ({ organization_id: org.id, action, decision, enabled: true }))
  const { error: policyError } = await admin.from('ercan_os_policies').insert(policies)
  if (policyError) throw policyError
  await seedNativeConnectors(admin, org.id, userId)
  return org.id
}

async function policyDecision(userClient: any, orgId: string, requestedAction: string) {
  const { data: policy } = await userClient.from('ercan_os_policies').select('*').eq('organization_id', orgId).eq('action', requestedAction).eq('enabled', true).maybeSingle()
  return policy?.decision ?? (requestedAction.startsWith('production.') ? 'approval_required' : 'allow')
}

function basicAuth(value: string) { return 'Basic ' + btoa(value) }
async function readSecret(admin: any, credential: any) {
  if (!credential?.secret_id) return null
  const { data, error } = await admin.rpc('ercan_os_vault_get_secret', { p_secret_id: credential.secret_id })
  if (error) throw error
  return data as string | null
}

async function supervisionRequest(authHeader: string, payload: any) {
  const response = await fetch(`${SUPABASE_URL}/functions/v1/vinterro-one-supervision`, {
    method: 'POST',
    headers: {
      Authorization: authHeader,
      apikey: ANON_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
    signal: AbortSignal.timeout(60000),
  })
  const data = await response.json().catch(() => ({}))
  if (!response.ok || data?.ok === false) {
    throw new Error(`Vinterro One supervision failed: ${data?.error || 'HTTP ' + response.status}`)
  }
  return data
}

async function connectorRequest(admin: any, connector: any, secret: string | null, operation: string, args: any) {
  const started = Date.now()
  let url = connector.endpoint || ''
  let method = 'GET'
  let body: string | undefined
  const headers: Record<string,string> = { 'Accept': 'application/json', 'User-Agent': 'ERCAN-OS/0.6' }
  const provider = connector.provider
  if (provider === 'github') {
    headers['Authorization'] = `Bearer ${secret || ''}`
    headers['X-GitHub-Api-Version'] = '2022-11-28'
    if (operation === 'viewer') url = 'https://api.github.com/user'
    else if (operation === 'repos') url = `https://api.github.com/user/repos?per_page=${Math.min(Number(args?.limit || 20),100)}&sort=updated`
    else if (operation === 'repo') url = `https://api.github.com/repos/${encodeURIComponent(args?.owner || '')}/${encodeURIComponent(args?.repo || '')}`
    else throw new Error(`Unsupported GitHub operation: ${operation}`)
  } else if (provider === 'shopify') {
    if (!url) throw new Error('Shopify connector endpoint is required, e.g. https://shop.myshopify.com')
    url = url.replace(/\/$/, '')
    headers['X-Shopify-Access-Token'] = secret || ''
    if (operation === 'shop') url += '/admin/api/2026-07/shop.json'
    else if (operation === 'products') url += `/admin/api/2026-07/products.json?limit=${Math.min(Number(args?.limit || 20),250)}`
    else throw new Error(`Unsupported Shopify operation: ${operation}`)
  } else if (provider === 'wordpress') {
    if (!url) throw new Error('WordPress connector endpoint is required')
    url = url.replace(/\/$/, '')
    if (secret) headers['Authorization'] = basicAuth(secret)
    if (operation === 'me') url += '/wp-json/wp/v2/users/me?context=edit'
    else if (operation === 'posts') url += `/wp-json/wp/v2/posts?per_page=${Math.min(Number(args?.limit || 10),100)}`
    else if (operation === 'site') url += '/wp-json/'
    else throw new Error(`Unsupported WordPress operation: ${operation}`)
  } else if (connector.kind === 'mcp' || provider === 'mcp') {
    if (!url) throw new Error('MCP endpoint is required')
    method = 'POST'; headers['Content-Type'] = 'application/json'
    if (secret) headers['Authorization'] = `Bearer ${secret}`
    if (operation === 'tools/list') body = JSON.stringify({ jsonrpc: '2.0', id: crypto.randomUUID(), method: 'tools/list', params: {} })
    else if (operation === 'tools/call') body = JSON.stringify({ jsonrpc: '2.0', id: crypto.randomUUID(), method: 'tools/call', params: { name: args?.name, arguments: args?.arguments || {} } })
    else throw new Error(`Unsupported MCP operation: ${operation}`)
  } else {
    if (!url) throw new Error('Connector endpoint is required')
    if (secret) headers['Authorization'] = `Bearer ${secret}`
  }
  const response = await fetch(url, { method, headers, body, signal: AbortSignal.timeout(15000) })
  const text = await response.text()
  let data: any
  try { data = text ? JSON.parse(text) : {} } catch { data = { text: text.slice(0, 4000) } }
  return { ok: response.ok, status: response.status, data, latency_ms: Date.now() - started, url }
}

Deno.serve(async (req: Request) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: cors })
  if (req.method !== 'POST') return json({ error: 'POST only' }, 405)
  try {
    const authHeader = req.headers.get('Authorization') ?? ''
    const userClient = createClient(SUPABASE_URL, ANON_KEY, { global: { headers: { Authorization: authHeader } } })
    const admin = createClient(SUPABASE_URL, SERVICE_KEY, { auth: { persistSession: false, autoRefreshToken: false } })
    const { data: { user }, error: userError } = await userClient.auth.getUser()
    if (userError || !user) return json({ error: 'Unauthorized' }, 401)
    if (!(await isAuthorizedOwner(user))) return json({ error: 'Forbidden' }, 403)
    const body = await req.json().catch(() => ({}))
    const action = body.action ?? 'overview'
    if (action === 'bootstrap') {
      const organizationId = await bootstrap(admin, user.id)
      return json({ ok: true, organization_id: organizationId, user: { id: user.id, email: user.email } })
    }
    const membership = await currentOrg(userClient)
    const orgId = membership.organization_id
    if (action === 'overview') {
      const [{ data: organization }, { data: projects }, { data: agents }, { data: runs }, { data: approvals }, { data: policies }, { data: connectors }, { data: toolCalls }] = await Promise.all([
        userClient.from('ercan_os_organizations').select('*').eq('id', orgId).single(),
        userClient.from('ercan_os_projects').select('*').eq('organization_id', orgId).order('created_at'),
        userClient.from('ercan_os_agents').select('*').eq('organization_id', orgId).order('created_at'),
        userClient.from('ercan_os_runs').select('*').eq('organization_id', orgId).order('created_at', { ascending: false }).limit(50),
        userClient.from('ercan_os_approvals').select('*').eq('organization_id', orgId).eq('status', 'pending').order('created_at', { ascending: false }),
        userClient.from('ercan_os_policies').select('*').eq('organization_id', orgId).order('created_at'),
        userClient.from('ercan_os_connectors').select('id,organization_id,name,provider,kind,endpoint,credential_id,status,config,capabilities,last_checked_at,last_error,created_at').eq('organization_id', orgId).order('created_at'),
        userClient.from('ercan_os_tool_calls').select('*').eq('organization_id', orgId).order('created_at', { ascending: false }).limit(50),
      ])
      const activeAgents = (agents ?? []).filter((a: any) => a.status === 'active')
      const successRuns = (runs ?? []).filter((r: any) => r.status === 'success')
      const toolErrors = (toolCalls ?? []).filter((t: any) => t.status === 'error').length
      return json({ user: { id: user.id, email: user.email }, organization, organization_id: orgId, role: membership.role,
        metrics: { system_health: activeAgents.length ? Math.round(activeAgents.reduce((n: number, a: any) => n + Number(a.health ?? 0), 0) / activeAgents.length) : 0, active_agents: activeAgents.length, projects: (projects ?? []).length, recent_runs: (runs ?? []).length, success_rate: (runs ?? []).length ? Math.round(successRuns.length / (runs ?? []).length * 1000) / 10 : 100, pending_approvals: (approvals ?? []).length, tool_errors: toolErrors, connected_tools: (connectors ?? []).filter((c: any) => c.status === 'connected').length },
        projects: projects ?? [], agents: agents ?? [], runs: runs ?? [], approvals: approvals ?? [], policies: policies ?? [], connectors: connectors ?? [], tool_calls: toolCalls ?? [] })
    }
    if (action === 'agent_expertise') {
      const agentName = String(body.agent_name ?? '').trim()
      const agentId = String(body.agent_id ?? '').trim()
      let query = userClient.from('ercan_os_agents').select('*').eq('organization_id', orgId)
      if (agentId) query = query.eq('id', agentId)
      else if (agentName) query = query.eq('name', agentName)
      else return json({ error: 'agent_name or agent_id required' }, 400)
      const { data: agent, error: agentError } = await query.maybeSingle()
      if (agentError) throw agentError
      if (!agent) return json({ error: 'agent not found' }, 404)
      const [{ data: profile }, { data: sources }, { data: learning }, { data: health }] = await Promise.all([
        userClient.from('ercan_os_agent_expertise_profiles').select('*').eq('organization_id', orgId).eq('agent_id', agent.id).maybeSingle(),
        userClient.from('ercan_os_agent_sources').select('*').eq('organization_id', orgId).eq('agent_id', agent.id).eq('enabled', true).order('authority_tier').order('topic'),
        userClient.from('ercan_os_agent_learning_events').select('*').eq('organization_id', orgId).eq('agent_id', agent.id).order('learned_at', { ascending: false }).limit(25),
        userClient.from('ercan_os_agent_expertise_health').select('*').eq('organization_id', orgId).eq('agent_id', agent.id).maybeSingle(),
      ])
      return json({ ok: true, agent, profile, sources: sources ?? [], learning: learning ?? [], health })
    }
    if (action === 'expertise_due') {
      const limit = Math.max(1, Math.min(Number(body.limit ?? 20), 89))
      const { data, error } = await userClient.from('ercan_os_agent_expertise_health')
        .select('*')
        .eq('organization_id', orgId)
        .neq('expertise_state', 'CURRENT')
        .order('authority_source_count', { ascending: true })
        .order('source_count', { ascending: true })
        .limit(limit)
      if (error) throw error
      return json({ ok: true, due: data ?? [], count: (data ?? []).length })
    }
    if (action === 'record_agent_learning') {
      const agentName = String(body.agent_name ?? '').trim()
      const title = String(body.title ?? '').trim()
      const summary = String(body.summary ?? '').trim()
      const topic = String(body.topic ?? 'general').trim()
      const sourceUri = body.source_uri ? String(body.source_uri) : null
      if (!agentName || !title || !summary) return json({ error: 'agent_name, title, summary required' }, 400)
      const { data: agent, error: agentError } = await userClient.from('ercan_os_agents').select('id,name').eq('organization_id', orgId).eq('name', agentName).maybeSingle()
      if (agentError) throw agentError
      if (!agent) return json({ error: 'agent not found' }, 404)
      let sourceId = null
      if (sourceUri) {
        const { data: source } = await userClient.from('ercan_os_agent_sources').select('id').eq('organization_id', orgId).eq('agent_id', agent.id).eq('source_uri', sourceUri).maybeSingle()
        sourceId = source?.id || null
      }
      const confidence = Math.max(0, Math.min(Number(body.confidence ?? 0.8), 1))
      const status = body.status === 'candidate' ? 'candidate' : 'verified'
      const expiresDays = Math.max(1, Math.min(Number(body.expires_days ?? 30), 365))
      const { data: learning, error } = await userClient.from('ercan_os_agent_learning_events').insert({
        organization_id: orgId,
        agent_id: agent.id,
        agent_name: agent.name,
        source_id: sourceId,
        source_uri: sourceUri,
        topic,
        title,
        summary,
        evidence: body.evidence || {},
        confidence,
        expires_at: new Date(Date.now() + expiresDays * 86400000).toISOString(),
        content_hash: body.content_hash || null,
        status,
      }).select().single()
      if (error) throw error
      if (sourceId) {
        await userClient.from('ercan_os_agent_sources').update({ last_verified_at: now() }).eq('organization_id', orgId).eq('id', sourceId)
      }
      await userClient.from('ercan_os_agent_expertise_profiles').update({ last_reviewed_at: now(), updated_at: now() }).eq('organization_id', orgId).eq('agent_id', agent.id)
      return json({ ok: true, learning })
    }
    if (action === 'create_project') {
      const name = String(body.name ?? '').trim(); if (!name) return json({ error: 'name required' }, 400)
      const { data, error } = await userClient.from('ercan_os_projects').insert({ organization_id: orgId, name, slug: slugify(body.slug || name), status: 'active', health: 100 }).select().single(); if (error) throw error
      return json({ ok: true, project: data })
    }
    if (action === 'toggle_agent') {
      const id = String(body.agent_id ?? '')
      const { data: current, error: findError } = await userClient.from('ercan_os_agents').select('status').eq('id', id).eq('organization_id', orgId).single(); if (findError) throw findError
      const next = current.status === 'active' ? 'paused' : 'active'
      const { data, error } = await userClient.from('ercan_os_agents').update({ status: next }).eq('id', id).eq('organization_id', orgId).select().single(); if (error) throw error
      return json({ ok: true, agent: data })
    }
    if (action === 'resolve_specialists') {
      const task = String(body.task ?? '').trim(); if (!task) return json({ error: 'task required' }, 400)
      const requestedAction = String(body.requested_action ?? 'research')
      const [{ data: agents, error: agentsError }, { data: projects, error: projectsError }] = await Promise.all([
        userClient.from('ercan_os_agents').select('*').eq('organization_id', orgId),
        userClient.from('ercan_os_projects').select('*').eq('organization_id', orgId).eq('status', 'active'),
      ])
      if (agentsError) throw agentsError
      if (projectsError) throw projectsError
      const routing = selectAgentPod(task, agents ?? [], requestedAction, projects ?? [], body.project_id || null)
      const activeIds = routing.active.map((a: any) => a.id)
      const { data: expertiseHealth } = activeIds.length
        ? await userClient.from('ercan_os_agent_expertise_health').select('agent_id,agent_name,expertise_state,refresh_hours,last_source_verification_at,verified_learning_count,last_learning_at,source_count,authority_source_count').in('agent_id', activeIds)
        : { data: [] }
      const healthById = new Map((expertiseHealth || []).map((h: any) => [h.agent_id, h]))
      const enrich = (a: any) => {
        const h = healthById.get(a.id)
        return {
          id:a.id,name:a.name,role:a.role,instructions:a.instructions,score:a.routing_score || null,
          expertise_state:h?.expertise_state || 'UNKNOWN',
          research_required:(h?.expertise_state || 'UNKNOWN') !== 'CURRENT',
          refresh_hours:h?.refresh_hours || null,
          last_source_verification_at:h?.last_source_verification_at || null,
          last_learning_at:h?.last_learning_at || null,
          source_count:h?.source_count || 0,
          authority_source_count:h?.authority_source_count || 0,
        }
      }
      return json({
        ok: true,
        primary: routing.primary ? enrich(routing.primary) : null,
        active: routing.active.map(enrich),
        standby_count: routing.standby.length,
        master_mode: routing.master_mode,
        routing_reason: routing.routing_reason,
        project: routing.project ? { id: routing.project.id, name: routing.project.name, slug: routing.project.slug } : null,
        refresh_required: routing.active.some((a:any) => (healthById.get(a.id)?.expertise_state || 'UNKNOWN') !== 'CURRENT'),
      })
    }
    if (action === 'start_ai_run' || action === 'create_run') {
      const task = String(body.task ?? '').trim(); if (!task) return json({ error: 'task required' }, 400)
      const [{ data: agents, error: agentsError }, { data: projects, error: projectsError }] = await Promise.all([
        userClient.from('ercan_os_agents').select('*').eq('organization_id', orgId),
        userClient.from('ercan_os_projects').select('*').eq('organization_id', orgId).eq('status', 'active'),
      ])
      if (agentsError) throw agentsError
      if (projectsError) throw projectsError
      const requestedAction = String(body.requested_action ?? 'research')
      const routing = selectAgentPod(task, agents ?? [], requestedAction, projects ?? [], body.project_id || null)
      const agent = routing.primary; if (!agent) return json({ error: 'No active agent available' }, 409)
      const decision = await policyDecision(userClient, orgId, requestedAction)
      const status = decision === 'deny' ? 'blocked' : decision === 'approval_required' ? 'awaiting_approval' : (action === 'start_ai_run' ? 'running' : 'success')
      const started = Date.now()
      const activeNames = routing.active.map((a: any) => a.name)
      const activeIds = routing.active.map((a: any) => a.id)
      const [{ data: expertiseProfiles }, { data: expertiseSources }, { data: expertiseHealth }] = await Promise.all([
        userClient.from('ercan_os_agent_expertise_profiles')
          .select('agent_id,agent_name,research_mode,research_policy,source_hierarchy,curriculum,min_independent_sources,refresh_hours,last_reviewed_at')
          .in('agent_id', activeIds),
        userClient.from('ercan_os_agent_sources')
          .select('agent_id,agent_name,topic,source_name,source_uri,source_kind,authority_tier,freshness_days,last_verified_at,metadata')
          .in('agent_id', activeIds)
          .eq('enabled', true)
          .order('authority_tier', { ascending: true }),
        userClient.from('ercan_os_agent_expertise_health')
          .select('agent_id,agent_name,expertise_state,refresh_hours,last_source_verification_at,verified_learning_count,last_learning_at,source_count,authority_source_count')
          .in('agent_id', activeIds)
      ])
      const sourceByAgent = new Map<string, any[]>()
      for (const s of expertiseSources || []) {
        const list = sourceByAgent.get(s.agent_id) || []
        if (list.length < 12) list.push(s)
        sourceByAgent.set(s.agent_id, list)
      }
      const profileByAgent = new Map((expertiseProfiles || []).map((p: any) => [p.agent_id, p]))
      const healthByAgent = new Map((expertiseHealth || []).map((h: any) => [h.agent_id, h]))
      const expertiseContext = routing.active.map((a: any) => {
        const profile = profileByAgent.get(a.id)
        const health = healthByAgent.get(a.id)
        const sources = sourceByAgent.get(a.id) || []
        return {
          name: a.name,
          specialist_role: a.role,
          expertise_state: health?.expertise_state || 'UNKNOWN',
          research_required: (health?.expertise_state || 'UNKNOWN') !== 'CURRENT',
          last_learning_at: health?.last_learning_at || null,
          last_source_verification_at: health?.last_source_verification_at || null,
          verified_learning_count: health?.verified_learning_count || 0,
          min_sources: profile?.min_independent_sources || 3,
          refresh_hours: profile?.refresh_hours || 168,
          source_hierarchy: profile?.source_hierarchy || [],
          authority_sources: sources.map((s: any) => ({
            topic: s.topic,
            name: s.source_name,
            uri: s.source_uri,
            kind: s.source_kind,
            tier: s.authority_tier,
            freshness_days: s.freshness_days,
            last_verified_at: s.last_verified_at,
          })),
        }
      })
      const podInstructions = routing.active.map((a: any) =>
        `[${a.name} / ${a.role}] ${String(a.instructions || '')}`
      ).join('\n\n')
      const expertiseInstruction = [
        'ACTIVE POD EXPERTISE CONTEXT:',
        JSON.stringify(expertiseContext),
        '',
        'ACTIVE POD SPECIALIST MANDATES:',
        podInstructions,
        '',
        'Continuous expertise rule: inspect each ACTIVE specialist expertise_state. If research_required=true or expertise_state is not CURRENT, refresh that specialist from current authoritative sources BEFORE relying on its domain knowledge for material decisions. Discover broadly across the public web, GitHub, standards, changelogs and primary research; adopt narrowly after provenance, freshness, maintenance, security/license and contradiction checks. Community sources are discovery signals, not authority. If a fixed source is archived/deprecated, locate and prefer its current official successor. Record uncertainty; never pretend the entire internet was exhaustively covered. When reusable verified knowledge materially changes future behavior, record it through the governed learning path rather than silently growing prompts.'
      ].join('\n')
      const trace = [
        { at: now(), event: 'task_received' },
        { at: now(), event: 'agent_selected', agent: agent.name },
        { at: now(), event: 'specialist_pod_selected', active: activeNames, standby_count: routing.standby.length, master_mode: routing.master_mode },
        { at: now(), event: 'policy_decision', action: requestedAction, decision }
      ]
      const routingOutput = {
        primary: agent.name,
        active_agents: activeNames,
        standby_count: routing.standby.length,
        master_mode: routing.master_mode,
        routing_reason: routing.routing_reason,
        project: routing.project ? { id: routing.project.id, name: routing.project.name, slug: routing.project.slug } : null,
      }
      const selectedProjectId = routing.project?.id || body.project_id || null
      const { data: run, error: runError } = await userClient.from('ercan_os_runs').insert({ organization_id: orgId, project_id: selectedProjectId, agent_id: agent.id, task, status, requested_by: user.id, output: status === 'success' ? { message: `Control plane routed task to ${agent.name} with relevant specialist pod.`, runtime: 'supabase-edge-deterministic', requested_action: requestedAction, routing: routingOutput } : { decision, requested_action: requestedAction, routing: routingOutput }, trace, latency_ms: Date.now() - started, completed_at: status === 'success' || status === 'blocked' ? now() : null }).select().single(); if (runError) throw runError
      let supervision = null
      if (status !== 'blocked') {
        try {
          supervision = await supervisionRequest(authHeader, {
            action: 'plan_run',
            run_id: run.id,
            requested_action: requestedAction,
            acceptance_criteria: body.acceptance_criteria || [],
            do_not_touch: body.do_not_touch || [],
          })
        } catch (supervisionError) {
          await userClient.from('ercan_os_runs').update({
            status: 'blocked',
            completed_at: now(),
            output: { decision: 'supervision_unavailable', requested_action: requestedAction, routing: routingOutput, error: supervisionError instanceof Error ? supervisionError.message : String(supervisionError) }
          }).eq('id', run.id).eq('organization_id', orgId)
          return json({ ok: false, error: supervisionError instanceof Error ? supervisionError.message : String(supervisionError), code: 'supervision_required', run_id: run.id }, 503)
        }
      }
      let approval = null
      if (status === 'awaiting_approval') {
        const { data, error } = await userClient.from('ercan_os_approvals').insert({ organization_id: orgId, run_id: run.id, action: requestedAction, risk: requestedAction.includes('deploy') ? 'high' : 'medium', status: 'pending', requested_by: user.id, payload: { task, agent: agent.name, active_agents: activeNames } }).select().single(); if (error) throw error; approval = data
      }
      return json({
        ok: true,
        run,
        agent: {
          id: agent.id,
          name: agent.name,
          role: 'research',
          specialist_role: agent.role,
          instructions: [String(agent.instructions || ''), expertiseInstruction].join('\n\n')
        },
        pod: {
          active: routing.active.map((a: any) => ({ id:a.id,name:a.name,role:a.role,instructions:a.instructions })),
          standby_count: routing.standby.length,
          master_mode: routing.master_mode,
          routing_reason: routing.routing_reason,
        },
        decision,
        approval,
        supervision: supervision?.supervision || supervision || null
      })
    }
    if (action === 'complete_ai_run') {
      const id = String(body.run_id ?? '')
      const { data: current, error: findError } = await userClient.from('ercan_os_runs').select('*').eq('id', id).eq('organization_id', orgId).single(); if (findError) throw findError
      const trace = Array.isArray(current.trace) ? current.trace : []
      const modelSucceeded = body.status === 'success'
      trace.push({ at: now(), event: modelSucceeded ? 'producer_claimed_completion' : 'model_error', model: body.model || 'openai/gpt-5.6-sol' })
      const { data, error } = await userClient.from('ercan_os_runs').update({
        status: modelSucceeded ? 'under_review' : 'error',
        output: body.output || {},
        trace,
        latency_ms: Number(body.latency_ms || current.latency_ms || 0),
        completed_at: modelSucceeded ? null : now()
      }).eq('id', id).eq('organization_id', orgId).select().single(); if (error) throw error

      if (!modelSucceeded) return json({ ok: true, run: data, supervision: { state: 'NOT_VERIFIED', reason: 'producer/model execution failed' } })

      try {
        await supervisionRequest(authHeader, { action: 'claim_run', run_id: id, claim: body.output || {} })
        const review = await supervisionRequest(authHeader, {
          action: 'review_run',
          run_id: id,
          evidence: Array.isArray(body.evidence) ? body.evidence : [],
        })
        const { data: refreshed } = await userClient.from('ercan_os_runs').select('*').eq('id', id).eq('organization_id', orgId).single()
        return json({ ok: true, run: refreshed || data, supervision: review })
      } catch (supervisionError) {
        await userClient.from('ercan_os_runs').update({ status: 'under_review', completed_at: null }).eq('id', id).eq('organization_id', orgId)
        return json({
          ok: false,
          run: data,
          code: 'supervision_incomplete',
          error: supervisionError instanceof Error ? supervisionError.message : String(supervisionError),
          supervision: { state: 'NOT_VERIFIED', final_gate: 'NOT_VERIFIED' }
        }, 503)
      }
    }
    if (action === 'decide_approval') {
      const id = String(body.approval_id ?? ''); const decision = body.decision === 'approved' ? 'approved' : 'rejected'
      const { data: approval, error } = await userClient.from('ercan_os_approvals').update({ status: decision, decided_by: user.id, decided_at: now() }).eq('id', id).eq('organization_id', orgId).select().single(); if (error) throw error
      if (approval.run_id) await userClient.from('ercan_os_runs').update({ status: decision === 'approved' ? 'approved' : 'blocked', completed_at: decision === 'approved' ? null : now(), output: { approval: decision } }).eq('id', approval.run_id).eq('organization_id', orgId)
      return json({ ok: true, approval })
    }
    if (action === 'set_policy') {
      const { data, error } = await userClient.from('ercan_os_policies').update({ enabled: Boolean(body.enabled) }).eq('id', String(body.policy_id ?? '')).eq('organization_id', orgId).select().single(); if (error) throw error
      return json({ ok: true, policy: data })
    }
    if (action === 'list_connectors') {
      const { data, error } = await userClient.from('ercan_os_connectors').select('id,name,provider,kind,endpoint,status,config,capabilities,last_checked_at,last_error,credential_id').eq('organization_id', orgId).order('created_at'); if (error) throw error
      return json({ ok: true, connectors: data ?? [] })
    }
    if (action === 'create_credential') {
      const name = String(body.name ?? '').trim(); const provider = String(body.provider ?? '').trim(); const secret = String(body.secret ?? '')
      if (!name || !provider || !secret) return json({ error: 'name, provider and secret required' }, 400)
      const vaultName = `ercan-os/${orgId}/${provider}/${slugify(name)}/${crypto.randomUUID()}`
      const { data: secretId, error: vaultError } = await admin.rpc('ercan_os_vault_store_secret', { p_name: vaultName, p_secret: secret, p_description: `ERCAN OS ${provider} credential for ${name}` }); if (vaultError) throw vaultError
      const { data, error } = await admin.from('ercan_os_credentials').insert({ organization_id: orgId, name, provider, secret_id: secretId, metadata: body.metadata || {}, created_by: user.id }).select('id,name,provider,metadata,created_at').single(); if (error) { await admin.rpc('ercan_os_vault_delete_secret', { p_secret_id: secretId }); throw error }
      return json({ ok: true, credential: data })
    }
    if (action === 'list_credentials') {
      const { data, error } = await userClient.from('ercan_os_credentials').select('id,name,provider,metadata,created_at,updated_at').eq('organization_id', orgId).order('created_at'); if (error) throw error
      return json({ ok: true, credentials: data ?? [] })
    }
    if (action === 'create_connector') {
      const name = String(body.name ?? '').trim(); const provider = String(body.provider ?? '').trim(); const kind = String(body.kind ?? 'rest')
      if (!name || !provider) return json({ error: 'name and provider required' }, 400)
      if (body.credential_id) { const { data: cred } = await admin.from('ercan_os_credentials').select('id').eq('id', body.credential_id).eq('organization_id', orgId).maybeSingle(); if (!cred) return json({ error: 'credential not found' }, 404) }
      const { data, error } = await admin.from('ercan_os_connectors').insert({ organization_id: orgId, name, provider, kind, endpoint: body.endpoint || null, credential_id: body.credential_id || null, status: 'pending', config: body.config || {}, capabilities: body.capabilities || [], created_by: user.id }).select('id,name,provider,kind,endpoint,status,config,capabilities,credential_id').single(); if (error) throw error
      return json({ ok: true, connector: data })
    }
    if (action === 'test_connector' || action === 'invoke_connector') {
      const connectorId = String(body.connector_id ?? '')
      const { data: connector, error: conError } = await admin.from('ercan_os_connectors').select('*').eq('id', connectorId).eq('organization_id', orgId).single(); if (conError) throw conError
      let credential = null; if (connector.credential_id) { const { data } = await admin.from('ercan_os_credentials').select('*').eq('id', connector.credential_id).eq('organization_id', orgId).single(); credential = data }
      const secret = await readSecret(admin, credential)
      const requestedAction = String(body.requested_action ?? 'read')
      const decision = await policyDecision(userClient, orgId, requestedAction)
      if (decision === 'deny') return json({ error: `Policy denied ${requestedAction}`, decision }, 403)
      if (decision === 'approval_required') return json({ ok: false, decision, error: `Approval required for ${requestedAction}` }, 409)
      let operation = String(body.operation ?? '')
      if (action === 'test_connector') { if (connector.provider === 'github') operation = 'viewer'; else if (connector.provider === 'shopify') operation = 'shop'; else if (connector.provider === 'wordpress') operation = 'site'; else if (connector.kind === 'mcp') operation = 'tools/list' }
      const result = await connectorRequest(admin, connector, secret, operation, body.arguments || {})
      const status = result.ok ? 'success' : 'error'
      await admin.from('ercan_os_tool_calls').insert({ organization_id: orgId, run_id: body.run_id || null, connector_id: connector.id, tool_name: `${connector.provider}.${operation}`, input: body.arguments || {}, output: result.data || {}, status, latency_ms: result.latency_ms })
      await admin.from('ercan_os_connectors').update({ status: result.ok ? 'connected' : 'error', last_checked_at: now(), last_error: result.ok ? null : `HTTP ${result.status}` }).eq('id', connector.id).eq('organization_id', orgId)
      return json({ ok: result.ok, connector: { id: connector.id, name: connector.name, provider: connector.provider }, operation, status: result.status, latency_ms: result.latency_ms, data: result.data })
    }
    return json({ error: `Unknown action: ${action}` }, 400)
  } catch (error) {
    console.error(error)
    return json({ error: error instanceof Error ? error.message : String(error) }, 500)
  }
})