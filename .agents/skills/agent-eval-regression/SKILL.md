---
name: agent-eval-regression
description: Turn agent failures/corrections/new capabilities into repeatable eval and regression cases. Use after repeated user corrections, tool/routing failures, new agent skills, provider adapters or material agent behavior changes.
---

# Agent Eval & Regression

Load `AGENT_ENGINEERING.md` and the relevant domain/project standard.

## Procedure
1. Capture the failure or target behavior as an observable outcome, not a vague prompt preference.
2. Classify cause: context, routing, tool, permission, skill, prompt/spec, architecture, security guardrail, test oracle, memory or provider behavior.
3. Build a minimal representative case with inputs, expected behavior, forbidden behavior and objective evidence where possible.
4. Add positive and negative activation cases for JIT skills/routing changes.
5. For stochastic tasks, use multiple trials or tolerant grading rather than brittle single-output string matching.
6. Separate capability benchmark from regression suite: benchmark asks how good; regression asks whether a previously fixed failure returned.
7. Grade real environment/tool outcome where mutations occur, not the assistant's statement that it succeeded.
8. If provider-native evals exist (for example Google Agents CLI), use them as additional evidence; they do not replace Ercan OS regression cases.
9. Validate the evaluator itself for underspecification, false positives and loopholes.
10. Record the fix at the narrowest durable layer: prompt, skill, tool contract, routing, test, guardrail or architecture.

## Recommended case fields
- case_id
- project/domain
- source correction/failure
- input/context fixture
- expected outcome
- forbidden outcome
- grader/oracle
- trials/tolerance
- evidence source
- linked skill/standard/change
- status/date

## Completion
A correction is durable only when the behavior change and representative regression case both pass, or when a concrete reason is recorded for why deterministic regression coverage is impractical.