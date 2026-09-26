import http from "node:http";
import { pathToFileURL } from "node:url";

const PORT = Number(process.env.PORT || 3000);
const SUPABASE_URL = String(process.env.SUPABASE_URL || "").replace(/\/$/, "");
const WORKER_TOKEN = String(process.env.VINTERRO_SALES_WORKER_TOKEN || "");
const WORKER_ID = String(process.env.VINTERRO_SALES_WORKER_ID || "railway-sales-control");
const TICK_INTERVAL_MS = Number(process.env.VINTERRO_SALES_TICK_INTERVAL_MS || 15000);
const REQUEST_TIMEOUT_MS = Number(process.env.VINTERRO_SALES_REQUEST_TIMEOUT_MS || 10000);

export function configOk() {
  return Boolean(
    SUPABASE_URL &&
    WORKER_TOKEN &&
    /^[a-z0-9][a-z0-9._-]{2,80}$/.test(WORKER_ID) &&
    Number.isFinite(TICK_INTERVAL_MS) &&
    TICK_INTERVAL_MS >= 5000
  );
}

export async function runTick(fetchImpl = fetch) {
  if (!configOk()) {
    throw new Error("worker_misconfigured");
  }

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);

  try {
    const response = await fetchImpl(
      `${SUPABASE_URL}/functions/v1/vinterro-sales-worker-tick`,
      {
        method: "POST",
        headers: {
          "content-type": "application/json",
          "x-vinterro-worker-token": WORKER_TOKEN
        },
        body: JSON.stringify({ worker_id: WORKER_ID }),
        signal: controller.signal
      }
    );

    const body = await response.json().catch(() => ({}));
    if (!response.ok || body?.ok !== true) {
      const code = String(body?.error || `http_${response.status}`);
      throw new Error(`worker_tick_failed:${code}`);
    }

    return body;
  } finally {
    clearTimeout(timeout);
  }
}

let lastTickAt = null;
let lastSuccessAt = null;
let lastError = null;
let inFlight = false;

async function tickSafely() {
  if (inFlight) return;
  inFlight = true;
  lastTickAt = new Date().toISOString();

  try {
    await runTick();
    lastSuccessAt = new Date().toISOString();
    lastError = null;
  } catch (error) {
    lastError = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify({
      level: "error",
      event: "worker_tick_failed",
      worker_id: WORKER_ID,
      error: lastError,
      at: new Date().toISOString()
    }));
  } finally {
    inFlight = false;
  }
}

export function createHealthServer() {
  return http.createServer((req, res) => {
    if (req.method === "GET" && req.url === "/health") {
      const healthy = configOk() && Boolean(lastSuccessAt);
      res.writeHead(healthy ? 200 : 503, {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "no-store",
        "x-content-type-options": "nosniff"
      });
      res.end(JSON.stringify({
        ok: healthy,
        worker_id: WORKER_ID,
        configured: configOk(),
        in_flight: inFlight,
        last_tick_at: lastTickAt,
        last_success_at: lastSuccessAt,
        last_error: lastError
      }));
      return;
    }

    res.writeHead(404, {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store"
    });
    res.end(JSON.stringify({ error: "not_found" }));
  });
}

export function startWorker() {
  const server = createHealthServer();
  server.listen(PORT, "0.0.0.0", () => {
    console.log(JSON.stringify({
      level: "info",
      event: "worker_started",
      worker_id: WORKER_ID,
      port: PORT,
      tick_interval_ms: TICK_INTERVAL_MS
    }));
  });

  if (configOk()) {
    void tickSafely();
    setInterval(() => void tickSafely(), TICK_INTERVAL_MS).unref();
  } else {
    console.error(JSON.stringify({
      level: "error",
      event: "worker_misconfigured",
      worker_id: WORKER_ID
    }));
  }

  return server;
}

const isMain =
  process.argv[1] &&
  import.meta.url === pathToFileURL(process.argv[1]).href;

if (isMain) {
  startWorker();
}
