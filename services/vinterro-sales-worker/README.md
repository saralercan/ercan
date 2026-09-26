# Vinterro Sales Railway Worker

Persistent Railway control worker for Vinterro One · Sales · AutoGTM.

## Security contract

- Railway never receives a Supabase `service_role` key.
- The worker receives only a dedicated `VINTERRO_SALES_WORKER_TOKEN`.
- Supabase stores only the SHA-256 hash of that token.
- The public Edge Function performs constant-time token verification before invoking the privileged internal RPC.
- Reply-review work remains approval-gated and is never sent by this worker.
- Gmail delivery truth remains the Gmail SENT record.
- Social recovery never counts as successful email delivery.

## Runtime variables

- `SUPABASE_URL`
- `VINTERRO_SALES_WORKER_TOKEN`
- `VINTERRO_SALES_WORKER_ID` (default: `railway-sales-control`)
- `VINTERRO_SALES_TICK_INTERVAL_MS` (default: `15000`)
- `VINTERRO_SALES_REQUEST_TIMEOUT_MS` (default: `10000`)

Health endpoint: `GET /health`.
