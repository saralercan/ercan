# Ercan OS Inspect Benchmark Runtime

This directory is an **optional isolated benchmark environment**, not a production dependency.

## Why Inspect

Inspect provides a common evaluation runtime for datasets, agents/tools, scorers and logs. Ercan OS may use it to orchestrate compatible benchmark runs, but canonical benchmark scoring/version rules always win.

## Current pins

See `../manifest.json`. Pins are reviewed on 2026-08-31 and must be re-checked before paid/comparative runs.

## Installation boundary

Do not install this environment globally. Create an isolated Python environment and resolve a lockfile for the target runner. Verify package provenance/hashes before installation. No API keys or production credentials belong in this directory.

## Running

A behavioral run requires a configured model adapter/provider secret and a task-specific run manifest. If the required credential/runtime is unavailable, leave the benchmark `NOT_RUN`.

For OpenAI Agents SDK-based agents, disable sensitive trace payload capture when fixtures may contain private or sensitive data. Record the Ercan OS policy commit and harness identifier in the run ledger.

## Output

Store only sanitized reproducibility metadata in Git. Raw logs that contain model prompts, tool payloads, credentials, private user data or licensed benchmark data must remain in the approved artifact store and be referenced by hash/ID rather than committed.
