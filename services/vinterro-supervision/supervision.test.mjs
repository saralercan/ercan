import test from "node:test";
import assert from "node:assert/strict";
import {
  RISK,
  createSupervisionRun,
  recordMaterialChange,
  recordReview,
  recordSupervisor,
  recordMetaAudit,
  recordReleaseGate,
  recordArbitration,
  evaluateCompletion,
} from "./supervision.mjs";

test("material worker cannot self-certify", () => {
  const run = createSupervisionRun({ taskId: "t1", riskClass: RISK.R1, workerId: "worker" });
  recordMaterialChange(run, { actorId: "worker", evidenceRefs: ["diff:1"] });
  assert.throws(() => recordReview(run, { reviewerId: "worker", verdict: "PASS", evidenceRefs: ["test:1"] }));
});

test("PASS requires evidence", () => {
  const run = createSupervisionRun({ taskId: "t2", riskClass: RISK.R1, workerId: "worker" });
  assert.throws(() => recordReview(run, { reviewerId: "qa", verdict: "PASS", evidenceRefs: [] }));
});

test("material change invalidates stale PASS", () => {
  const run = createSupervisionRun({ taskId: "t3", riskClass: RISK.R1, workerId: "worker" });
  recordMaterialChange(run, { actorId: "worker", evidenceRefs: ["diff:1"] });
  recordReview(run, { reviewerId: "qa", verdict: "PASS", evidenceRefs: ["test:1"] });
  assert.equal(evaluateCompletion(run).state, "VERIFIED");
  recordMaterialChange(run, { actorId: "worker", evidenceRefs: ["diff:2"] });
  assert.equal(evaluateCompletion(run).state, "NOT_VERIFIED");
});

test("R3 requires reviewer, supervisor and release gate", () => {
  const run = createSupervisionRun({ taskId: "t4", riskClass: RISK.R3, workerId: "worker" });
  recordMaterialChange(run, { actorId: "worker", evidenceRefs: ["deploy-diff"] });
  recordReview(run, { reviewerId: "qa", verdict: "PASS", evidenceRefs: ["runtime-check"] });
  recordSupervisor(run, { supervisorId: "web-supervisor", verdict: "PASS", evidenceRefs: ["browser-check"] });
  assert.equal(evaluateCompletion(run).state, "NOT_VERIFIED");
  recordReleaseGate(run, { gatekeeperId: "release-gate", verdict: "RELEASE_APPROVED", evidenceRefs: ["post-deploy-health"] });
  assert.equal(evaluateCompletion(run).state, "VERIFIED");
});

test("R4 additionally requires meta-audit", () => {
  const run = createSupervisionRun({ taskId: "t5", riskClass: RISK.R4, workerId: "runtime-worker" });
  recordMaterialChange(run, { actorId: "runtime-worker", evidenceRefs: ["policy-diff"] });
  recordReview(run, { reviewerId: "independent-qa", verdict: "PASS", evidenceRefs: ["regression-suite"] });
  recordSupervisor(run, { supervisorId: "runtime-supervisor", verdict: "PASS", evidenceRefs: ["routing-audit"] });
  recordReleaseGate(run, { gatekeeperId: "release-gate", verdict: "RELEASE_APPROVED", evidenceRefs: ["release-check"] });
  assert.equal(evaluateCompletion(run).state, "NOT_VERIFIED");
  recordMetaAudit(run, { auditorId: "meta-auditor", verdict: "PASS", evidenceRefs: ["false-pass-audit"] });
  assert.equal(evaluateCompletion(run).state, "VERIFIED");
});

test("R2 requires distinct reviewer and domain supervisor", () => {
  const run = createSupervisionRun({ taskId: "t6", riskClass: RISK.R2, workerId: "worker" });
  recordMaterialChange(run, { actorId: "worker", evidenceRefs: ["diff"] });
  recordReview(run, { reviewerId: "qa", verdict: "PASS", evidenceRefs: ["test"] });
  assert.throws(() => recordSupervisor(run, { supervisorId: "qa", verdict: "PASS", evidenceRefs: ["runtime"] }));
});

test("current arbiter can overturn a disputed review with evidence", () => {
  const run = createSupervisionRun({ taskId: "t7", riskClass: RISK.R1, workerId: "worker" });
  recordMaterialChange(run, { actorId: "worker", evidenceRefs: ["diff"] });
  recordReview(run, { reviewerId: "qa", verdict: "REWORK", evidenceRefs: ["review-evidence"] });
  assert.equal(evaluateCompletion(run).state, "NOT_VERIFIED");
  recordArbitration(run, { arbiterId: "arbiter", verdict: "OVERTURN_REVIEW", evidenceRefs: ["decisive-test"] });
  assert.equal(evaluateCompletion(run).state, "VERIFIED");
});

test("release gate must be independent from worker reviewer and supervisor", () => {
  const run = createSupervisionRun({ taskId: "t8", riskClass: RISK.R3, workerId: "worker" });
  recordMaterialChange(run, { actorId: "worker", evidenceRefs: ["diff"] });
  recordReview(run, { reviewerId: "qa", verdict: "PASS", evidenceRefs: ["test"] });
  recordSupervisor(run, { supervisorId: "supervisor", verdict: "PASS", evidenceRefs: ["runtime"] });
  assert.throws(() => recordReleaseGate(run, { gatekeeperId: "worker", verdict: "RELEASE_APPROVED", evidenceRefs: ["gate"] }));
  assert.throws(() => recordReleaseGate(run, { gatekeeperId: "qa", verdict: "RELEASE_APPROVED", evidenceRefs: ["gate"] }));
  assert.throws(() => recordReleaseGate(run, { gatekeeperId: "supervisor", verdict: "RELEASE_APPROVED", evidenceRefs: ["gate"] }));
});
