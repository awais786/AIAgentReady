# ADR-0001: Python as the implementation stack

**Status:** Accepted
**Date:** 2026-07-09

## Context

AIAgentReady needs an implementation language for the analyzer, generators, grounding and
validation components, and (in Phase 3) the git-intelligence MCP server. The first pilot
target (edx-platform) and the surrounding ecosystem shape the choice.

## Decision

Implement everything in Python (≥3.11), as a single package `aiagentready` under `src/`
layout, with `mcp-git-intelligence` as a separate Python package later.

## Rationale

- The MCP / LLM tooling ecosystem the kit builds on (MCP SDKs, LLM client libraries,
  structural-indexing tools) is strongest in Python.
- The Phase 1 pilot repo, edx-platform, is Python/Django — one language for both the kit
  and its first target keeps the pilot tight.
- Team familiarity: Python is the team's primary language.

## Consequences

- `pyproject.toml` (hatchling) is the single source of packaging metadata; pytest + ruff
  for tests and lint.
- Alternatives (TypeScript/Node for MCP-server affinity, Go for distribution) were
  considered and rejected: neither outweighs ecosystem + pilot alignment.

## Note: pending product rename

`aiagentready.dev` is held by an unrelated website-readiness tool. The product/package name
may change before public launch; the name currently only lives in `pyproject.toml` and the
package directory, so a rename is mechanical. Revisit before publicizing.
