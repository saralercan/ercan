import { DatabaseSync } from "node:sqlite";
import { isAbsolute } from "node:path";

// Isolated single-host ledger. Use a private directory on a local disk.
// Never use this as a distributed ledger or refund ambiguous executions.
export function createAggregateReservation(path, totalTokens) {
  if (typeof path !== "string" || !isAbsolute(path) ||
      !Number.isSafeInteger(totalTokens) || totalTokens <= 0) throw Error("invalid_ledger_config");
  const db = new DatabaseSync(path);
  try {
    db.exec("PRAGMA busy_timeout=5000; PRAGMA synchronous=FULL; CREATE TABLE IF NOT EXISTS budget (id INTEGER PRIMARY KEY CHECK(id=1), cap INTEGER NOT NULL, spent INTEGER NOT NULL CHECK(spent>=0 AND spent<=cap)); CREATE TABLE IF NOT EXISTS reservations (run_id TEXT PRIMARY KEY, tokens INTEGER NOT NULL CHECK(tokens>0));");
    db.prepare("INSERT OR IGNORE INTO budget VALUES(1,?,0)").run(totalTokens);
    if (db.prepare("SELECT cap FROM budget WHERE id=1").get().cap !== totalTokens) throw Error("budget_config_mismatch");
  } catch (error) { db.close(); throw error; }
  const reserve = async grant => {
    const {runId,workerId,maxInputTokens,maxOutputTokens} = grant ?? {};
    const tokens = maxInputTokens + maxOutputTokens;
    if (typeof runId !== "string" || !/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(runId) ||
        typeof workerId !== "string" || !/^[a-z0-9_.-]{3,128}$/i.test(workerId) ||
        !Number.isSafeInteger(maxInputTokens) || maxInputTokens<=0 ||
        !Number.isSafeInteger(maxOutputTokens) || maxOutputTokens<=0 ||
        !Number.isSafeInteger(tokens)) throw Error("invalid_reservation");
    db.exec("BEGIN IMMEDIATE");
    try {
      if (db.prepare("SELECT 1 FROM reservations WHERE run_id=?").get(runId.toLowerCase()) ||
          db.prepare("UPDATE budget SET spent=spent+? WHERE id=1 AND ?<=cap-spent").run(tokens,tokens).changes !== 1) {
        db.exec("ROLLBACK"); return {approved:false};
      }
      db.prepare("INSERT INTO reservations VALUES(?,?)").run(runId.toLowerCase(),tokens);
      db.exec("COMMIT");
      return {runId,workerId,maxInputTokens,maxOutputTokens,approved:true};
    } catch (error) { try { db.exec("ROLLBACK"); } catch {} throw error; }
  };
  return {reserve, close:()=>db.close()};
}
