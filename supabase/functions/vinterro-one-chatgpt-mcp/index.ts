import { pipeline } from 'npm:@supabase/middleware@0.5.0'
import { withOAuthProtectedResource, withSupabase } from 'npm:@supabase/server@1.6.0'
import { createMcpHandler, McpServer } from 'npm:@modelcontextprotocol/server@2.2.0'
import * as z from 'npm:zod@4.6.5'

const SUPABASE_URL = Deno.env.get('SUPABASE_URL') ?? ''
const ANON_KEY = Deno.env.get('SUPABASE_ANON_KEY') ?? ''

type SupabaseClientLike = any

function textResult(data: unknown) {
  return {
    content: [{ type: 'text' as const, text: JSON.stringify(data) }],
    structuredContent: data && typeof data === 'object' ? data as Record<string, unknown> : { value: data },
  }
}

function errorResult(message: string, details?: unknown) {
  return {
    content: [{ type: 'text' as const, text: message }],
    structuredContent: { ok: false, error: message, details: details ?? null },
    isError: true,
  }
}

async function callControlPlane(authHeader: string, body: Record<string, unknown>) {
  const response = await fetch(`${SUPABASE_URL}/functions/v1/ercan-os-api`, {
    method: 'POST',
    headers: {
      Authorization: authHeader,
      apikey: ANON_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
    signal: AbortSignal.timeout(30000),
  })
  const data = await response.json().catch(() => ({}))
  if (!response.ok) {
    throw new Error(String(data?.error || `Vinterro One control plane HTTP ${response.status}`))
  }
  return data
}

function createServer(supabase: SupabaseClientLike, authHeader: string) {
  const server = new McpServer(
    { name: 'vinterro-one', version: '1.0.0' },
    {
      instructions: [
        'Vinterro One is the canonical multi-agent control plane.',
        'For a task, call vinterro_route_task first unless the route is already current in this turn.',
        'Treat returned ACTIVE agents as bounded specialist responsibilities, not fictional persistent processes.',
        'When master_mode=true, execute the complete materially relevant pod; never reduce it to a minimum-team shortcut and never fan out to unrelated agents.',
        'For material work, preserve producer -> independent reviewer -> correction/retest -> release-gate semantics.',
        'Never claim an external send, publish, deploy, payment, auth/security mutation or other provider action occurred without direct provider evidence.',
      ].join(' '),
    },
  )

  server.registerTool(
    'vinterro_status',
    {
      title: 'Vinterro One status',
      description: 'Read current Vinterro One project and active-agent counts for the connected account.',
      inputSchema: z.object({}),
      annotations: { readOnlyHint: true, destructiveHint: false },
    },
    async () => {
      const [{ count: activeAgents, error: agentError }, { data: projects, error: projectError }] = await Promise.all([
        supabase.from('ercan_os_agents').select('id', { count: 'exact', head: true }).eq('status', 'active'),
        supabase.from('ercan_os_projects').select('id,name,slug,status,health').eq('status', 'active').order('created_at'),
      ])
      if (agentError) return errorResult('Could not read Vinterro One agents', agentError)
      if (projectError) return errorResult('Could not read Vinterro One projects', projectError)
      return textResult({
        ok: true,
        system: 'Vinterro One',
        active_agents: activeAgents ?? 0,
        active_projects: projects ?? [],
      })
    },
  )

  server.registerTool(
    'vinterro_route_task',
    {
      title: 'Route task through Vinterro One',
      description: 'Resolve the current project, project lead, complete materially relevant ACTIVE specialist pod, standby count, expertise freshness, and routing reason for a task. Call this before substantial project work or whenever the user asks to run agents/all agents.',
      inputSchema: z.object({
        task: z.string().min(1),
        requested_action: z.string().default('research'),
        project_id: z.string().uuid().optional(),
      }),
      annotations: { readOnlyHint: true, destructiveHint: false },
    },
    async ({ task, requested_action, project_id }) => {
      try {
        const data = await callControlPlane(authHeader, {
          action: 'resolve_specialists',
          task,
          requested_action,
          project_id: project_id ?? null,
        })
        return textResult(data)
      } catch (error) {
        return errorResult(error instanceof Error ? error.message : String(error))
      }
    },
  )

  server.registerTool(
    'vinterro_get_agent',
    {
      title: 'Get Vinterro One agent',
      description: 'Read one Vinterro One agent mandate, permissions, handoffs, tools, version, health and expertise freshness by exact agent name.',
      inputSchema: z.object({ name: z.string().min(1) }),
      annotations: { readOnlyHint: true, destructiveHint: false },
    },
    async ({ name }) => {
      const { data: agent, error } = await supabase
        .from('ercan_os_agents')
        .select('id,project_id,name,role,status,version,health,instructions,tools,permissions,handoffs,max_steps,max_retries,max_cost_usd,expertise_state,expertise_verified_at')
        .eq('name', name)
        .eq('status', 'active')
        .maybeSingle()
      if (error) return errorResult('Could not read Vinterro One agent', error)
      if (!agent) return errorResult(`Active Vinterro One agent not found: ${name}`)

      const { data: health } = await supabase
        .from('ercan_os_agent_expertise_health')
        .select('expertise_state,refresh_hours,last_source_verification_at,verified_learning_count,last_learning_at,source_count,authority_source_count')
        .eq('agent_id', agent.id)
        .maybeSingle()

      return textResult({
        ok: true,
        agent,
        expertise_health: health ?? null,
        research_required: (health?.expertise_state || agent.expertise_state || 'UNKNOWN') !== 'CURRENT',
      })
    },
  )

  server.registerTool(
    'vinterro_get_project',
    {
      title: 'Get Vinterro One project',
      description: 'Read an active Vinterro One project and its active project-scoped agents by project name or slug.',
      inputSchema: z.object({ project: z.string().min(1) }),
      annotations: { readOnlyHint: true, destructiveHint: false },
    },
    async ({ project }) => {
      const needle = project.trim()
      let { data: row, error } = await supabase
        .from('ercan_os_projects')
        .select('id,name,slug,status,health,created_at')
        .eq('status', 'active')
        .ilike('name', needle)
        .maybeSingle()
      if (!row && !error) {
        const result = await supabase
          .from('ercan_os_projects')
          .select('id,name,slug,status,health,created_at')
          .eq('status', 'active')
          .eq('slug', needle)
          .maybeSingle()
        row = result.data
        error = result.error
      }
      if (error) return errorResult('Could not read Vinterro One project', error)
      if (!row) return errorResult(`Active Vinterro One project not found: ${project}`)

      const { data: agents, error: agentError } = await supabase
        .from('ercan_os_agents')
        .select('id,name,role,status,version,health,tools,permissions,handoffs,expertise_state')
        .eq('project_id', row.id)
        .eq('status', 'active')
        .order('role')
      if (agentError) return errorResult('Could not read project agents', agentError)
      return textResult({ ok: true, project: row, agents: agents ?? [] })
    },
  )

  server.registerTool(
    'vinterro_get_supervision',
    {
      title: 'Get Vinterro One supervision state',
      description: 'Read supervision, independent review and release-gate state for an existing Vinterro One run.',
      inputSchema: z.object({ run_id: z.string().uuid() }),
      annotations: { readOnlyHint: true, destructiveHint: false },
    },
    async ({ run_id }) => {
      try {
        const response = await fetch(`${SUPABASE_URL}/functions/v1/vinterro-one-supervision`, {
          method: 'POST',
          headers: {
            Authorization: authHeader,
            apikey: ANON_KEY,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ action: 'get_supervision', run_id }),
          signal: AbortSignal.timeout(30000),
        })
        const data = await response.json().catch(() => ({}))
        if (!response.ok) {
          return errorResult(String(data?.error || `Vinterro One supervision HTTP ${response.status}`), data)
        }
        return textResult(data)
      } catch (error) {
        return errorResult(error instanceof Error ? error.message : String(error))
      }
    },
  )

  return server
}

const protectedHandler = pipeline(
  [
    withOAuthProtectedResource(),
    withSupabase({ auth: 'user' }),
  ],
  async (req, { supabase }) => {
    const authHeader = req.headers.get('authorization') || ''
    const handler = createMcpHandler(() => createServer(supabase, authHeader))
    return handler.fetch(req)
  },
)

Deno.serve((req: Request) => protectedHandler(req))
