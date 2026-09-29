export const RISK = Object.freeze({
  R0: "R0",
  R1: "R1",
  R2: "R2",
  R3: "R3",
  R4: "R4",
});

const VALID_REVIEW = new Set(["PASS", "PASS_WITH_NOTES", "REWORK", "BLOCKED"]);
const VALID_ARBITER = new Set(["UPHOLD_REVIEW", "OVERTURN_REVIEW", "RETEST_REQUIRED", "BLOCKED"]);
const VALID_GATE = new Set(["RELEASE_APPROVED", "RELEASE_DENIED", "RELEASE_BLOCKED"]);

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

export function createSupervisionRun({ taskId, riskClass, workerId, acceptanceCriteria = [] }) {
  assert(taskId, "taskId is required");
  assert(Object.values(RISK).includes(riskClass), "invalid riskClass");
  assert(workerId, "workerId is required");

  return {
    taskId,
    riskClass,
    workerId,
    acceptanceCriteria: [...acceptanceCriteria],
    materialVersion: 0,
    materialChanges: [],
    review: null,
    supervisor: null,
    arbiter: null,
    metaAudit: null,
    releaseGate: null,
    findings: [],
  };
}

export function recordMaterialChange(run, { actorId, evidenceRefs = [], summary = "" }) {
  assert(actorId, "actorId is required");
  run.materialVersion += 1;
  run.materialChanges.push({
    version: run.materialVersion,
    actorId,
    evidenceRefs: [...evidenceRefs],
    summary,
  });
  return run;
}

export function recordReview(run, { reviewerId, verdict, evidenceRefs = [], findings = [] }) {
  assert(reviewerId, "reviewerId is required");
  assert(reviewerId !== run.workerId, "material creator cannot be sole final reviewer");
  assert(VALID_REVIEW.has(verdict), "invalid reviewer verdict");
  if (verdict === "PASS" || verdict === "PASS_WITH_NOTES") {
    assert(evidenceRefs.length > 0, "PASS requires current evidence");
  }
  run.review = {
    reviewerId,
    verdict,
    evidenceRefs: [...evidenceRefs],
    reviewedVersion: run.materialVersion,
  };
  run.findings = [...findings];
  return run;
}

export function recordSupervisor(run, { supervisorId, verdict, evidenceRefs = [] }) {
  assert(supervisorId, "supervisorId is required");
  assert(supervisorId !== run.workerId, "worker cannot supervise its own material work");
  if (run.review) assert(supervisorId !== run.review.reviewerId, "domain supervisor must be distinct from independent reviewer");
  assert(["PASS", "REWORK", "BLOCKED"].includes(verdict), "invalid supervisor verdict");
  if (verdict === "PASS") assert(evidenceRefs.length > 0, "supervisor PASS requires evidence");
  run.supervisor = {
    supervisorId,
    verdict,
    evidenceRefs: [...evidenceRefs],
    supervisedVersion: run.materialVersion,
  };
  return run;
}

export function recordArbitration(run, { arbiterId, verdict, evidenceRefs = [] }) {
  assert(arbiterId, "arbiterId is required");
  assert(VALID_ARBITER.has(verdict), "invalid arbiter verdict");
  assert(evidenceRefs.length > 0 || verdict === "BLOCKED", "arbiter decision requires evidence unless blocked");
  run.arbiter = {
    arbiterId,
    verdict,
    evidenceRefs: [...evidenceRefs],
    arbitratedVersion: run.materialVersion,
  };
  return run;
}

export function recordMetaAudit(run, { auditorId, verdict, evidenceRefs = [] }) {
  assert(auditorId, "auditorId is required");
  assert(auditorId !== run.workerId, "worker cannot meta-audit its own run");
  if (run.review) assert(auditorId !== run.review.reviewerId, "meta auditor must be distinct from reviewer");
  if (run.supervisor) assert(auditorId !== run.supervisor.supervisorId, "meta auditor must be distinct from domain supervisor");
  assert(["PASS", "REVIEW_REQUIRED", "BLOCKED"].includes(verdict), "invalid meta-audit verdict");
  if (verdict === "PASS") assert(evidenceRefs.length > 0, "meta-audit PASS requires evidence");
  run.metaAudit = {
    auditorId,
    verdict,
    evidenceRefs: [...evidenceRefs],
    auditedVersion: run.materialVersion,
  };
  return run;
}

export function recordReleaseGate(run, { gatekeeperId, verdict, evidenceRefs = [] }) {
  assert(gatekeeperId, "gatekeeperId is required");
  assert(gatekeeperId !== run.workerId, "worker cannot approve its own release");
  if (run.review) assert(gatekeeperId !== run.review.reviewerId, "release gate must be distinct from reviewer");
  if (run.supervisor) assert(gatekeeperId !== run.supervisor.supervisorId, "release gate must be distinct from domain supervisor");
  assert(VALID_GATE.has(verdict), "invalid release-gate verdict");
  if (verdict === "RELEASE_APPROVED") assert(evidenceRefs.length > 0, "release approval requires evidence");
  run.releaseGate = {
    gatekeeperId,
    verdict,
    evidenceRefs: [...evidenceRefs],
    gatedVersion: run.materialVersion,
  };
  return run;
}

function current(record, run) {
  if (!record) return false;
  const version = record.reviewedVersion ?? record.supervisedVersion ?? record.arbitratedVersion ?? record.auditedVersion ?? record.gatedVersion;
  return version === run.materialVersion;
}

export function evaluateCompletion(run) {
  const risk = Number(run.riskClass.slice(1));

  if (risk === 0) {
    return { state: "VERIFIED", reason: "R0 fast-path; no independent gate required by core policy" };
  }

  if (!current(run.review, run)) return { state: "NOT_VERIFIED", reason: "missing or stale independent review" };
  const reviewPassed = ["PASS", "PASS_WITH_NOTES"].includes(run.review.verdict);
  const arbiterOverturnedCurrentReview =
    current(run.arbiter, run) && run.arbiter.verdict === "OVERTURN_REVIEW";
  if (!reviewPassed && !arbiterOverturnedCurrentReview) {
    if (current(run.arbiter, run) && run.arbiter.verdict === "BLOCKED") {
      return { state: "BLOCKED", reason: "arbiter blocked disputed review" };
    }
    return { state: run.review.verdict === "BLOCKED" ? "BLOCKED" : "NOT_VERIFIED", reason: "independent review did not pass" };
  }

  if (risk >= 2) {
    if (!current(run.supervisor, run)) return { state: "NOT_VERIFIED", reason: "missing or stale domain supervisor PASS" };
    if (run.supervisor.verdict !== "PASS") {
      return { state: run.supervisor.verdict === "BLOCKED" ? "BLOCKED" : "NOT_VERIFIED", reason: "domain supervisor did not pass" };
    }
  }

  if (risk >= 4) {
    if (!current(run.metaAudit, run)) return { state: "NOT_VERIFIED", reason: "missing or stale meta-audit PASS" };
    if (run.metaAudit.verdict !== "PASS") {
      return { state: run.metaAudit.verdict === "BLOCKED" ? "BLOCKED" : "NOT_VERIFIED", reason: "meta-audit did not pass" };
    }
  }

  if (risk >= 3) {
    if (!current(run.releaseGate, run)) return { state: "NOT_VERIFIED", reason: "missing or stale release gate" };
    if (run.releaseGate.verdict !== "RELEASE_APPROVED") {
      return { state: run.releaseGate.verdict === "RELEASE_BLOCKED" ? "BLOCKED" : "NOT_VERIFIED", reason: "release gate did not approve" };
    }
  }

  return { state: "VERIFIED", reason: "all required current supervision gates passed" };
}
