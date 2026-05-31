# AGENTS.md

This file is the working contract for coding agents in Dirac.

Dirac is being rebuilt as a modular Python 3.14+ runtime. The old implementation is a behavior reference only. Do not imitate its shape, revive deleted docs, or move complexity into another large file.

## Mission

Make the smallest coherent modular change that preserves current behavior and improves separation. Every change must leave the code easier for the next agent to reason about.

## First move for any task

1. Identify the owning module.
2. Identify the public contract that should change.
3. Add or update tests around that contract.
4. Implement through injected dependencies and typed values.
5. Run focused tests, then the full test suite when practical.
6. Update README or the relevant module notes only when the public contract changes.

Do not begin by reading every file. Do not build a new global map in your context. Work from the owner module outward.

## Dependency rule

Use the Law of Demeter.

A module may call methods on its own dependencies. It may not reach through returned objects to control another module's internals. Passing raw mutable state across boundaries is a bug unless that state is an explicit domain value.

Good:

```python
await memory.search(MemoryQuery(text=query, scope=scope))
await provider.chat(request)
await log.event(event)
```

Bad:

```python
memory.store.conn.execute(...)
provider.session.headers["Authorization"] = secret
runtime.state.tasks[task_id]["next"] = value
```

## Module ownership

- `runtime` owns lifecycle, TaskGroup creation, shutdown, and composition.
- `config` owns files, environment values, secrets, and typed settings.
- `log` owns structured events, redaction, console controls, and sinks.
- `provider` owns provider routing, request translation, HTTP calls, response parsing, usage, and fake clients.
- `permission` owns authorization, scope decisions, blocked users, and capability checks.
- `discord` owns Discord-specific adapters, message delivery, identity collection, and Discord event DTOs.
- `command` owns deterministic command parsing and command execution.
- `context` owns model-facing context assembly and filters.
- `memory` owns durable memory and recent visible event access through one public contract.
- `tool` owns tool definitions, scoped tool visibility, tool execution, and tool result normalization.
- `task` owns periodic task definitions, due-task selection, attempts, and result delivery.
- `consolidation` owns quiet-phase memory assimilation and consolidation audits.
- `doctor` owns maintenance, repair, validation, and recovery ports.
- `api` owns authenticated HTTP routes and DTOs.
- `web` owns frontend code and calls only the HTTP API.

If a change seems to need many owners, create or adjust a small contract first.

## Invariants to preserve

- Unauthorized commands never reach a provider.
- Authorized commands are handled by code and excluded from reusable model context.
- Blocked users are excluded from model-facing context.
- Scope and capability resolution remain explicit and inspectable.
- Discord tool filtering stays strict: only enabled tools for the current scope may run.
- Secrets are never logged, returned, sent to providers as model context, or written into task output.
- Exact `dirac` fenced runtime blocks are removed from model-facing history and consolidation slices.
- Runtime timestamps are UTC internally. UI display can localize time.
- Background work is owned by an `asyncio.TaskGroup` from runtime composition.
- Provider calls go through `BaseProviderClient` implementations.
- Memory calls go through the memory contract.
- Tool argument errors stay self-explaining so the model can recover on the next turn.
- Runtime-authored warnings are distinguishable from model-authored text.

## Provider work

Do not build provider HTTP requests outside the provider module.

A provider implementation must own:

- URL construction
- headers
- auth handling
- request body translation
- tool payload translation
- supported and ignored parameters
- response parsing
- usage extraction
- error normalization
- redacted tracing

Use `httpx` by default. Do not add provider SDKs to core paths. If a dependency is justified, it must be fully encapsulated behind `BaseProviderClient` and covered by fake-client tests.

## Memory work

Do not expose storage details through memory APIs, task code, context code, command handlers, or WebUI routes.

The public memory operations are:

- `search`
- `add`
- `update`
- `delete`

Memory records must carry enough provenance for humans and consolidation to understand where they came from. The model should receive helpful usage and validation errors, not raw exceptions.

## Consolidation work

Quiet-phase consolidation is not a normal periodic task.

It reads recent visible events and the previous consolidation audit, then uses memory tools to preserve useful facts, merge duplicates, supersede stale records, and remove clear bloat. It must never invent a successful result when the runtime cut it short.

Do not put fixed tool-round counts or fixed model-loop budgets in documentation. Budgets belong in runtime config and tests.

## Task work

The periodic task loop is intentionally simple.

On a loose local tick, find enabled periodic tasks whose next run is due, choose one due task randomly, advance its next due time before execution, then launch one attempt through the runtime TaskGroup. Task intervals are minute-granularity. Failed attempts are recorded and may run again on their next due time.

Do not replace this with a heavyweight scheduler unless the product contract changes.

## Permission and command work

The command path is before the model path.

When adding or changing commands:

1. Parse deterministically.
2. Authorize before doing work.
3. Execute in code.
4. Log the accepted or rejected attempt.
5. Return deterministic output.
6. Keep command text out of reusable model context.

Emergency runtime controls remain the most protected command family.

## Context work

The context module may assemble from public service methods only. It must not know provider internals or memory storage internals.

Context can include trusted runtime notes, scoped instructions, Discord identity grounding, durable memory, visible recent conversation, task state summaries, and capability notes. Keep runtime-generated command blocks out of model-facing history.

## API and WebUI work

The WebUI imports no Python modules and reads no local runtime files. It calls the authenticated HTTP API.

API routes call services. They do not implement provider translation, memory storage, task selection, permission rules, or logging sinks inline.

External assistant clients also use the API. Do not introduce or search for named assistant implementations in this repository.

## Doctor work

Doctor may be closer to the plumbing than the API, but it must still use explicit repair ports. It must redact secrets, back up before destructive repair, and print exact changes. Do not give ordinary API clients doctor-level access.

## Logging work

Emit structured events. Do not print directly from domain modules except at process bootstrap before the logger exists.

Preserve console controls for verbosity and filtering. A no-op logger must be valid for tests and quiet runs.

## Config work

Config exposes typed settings, not arbitrary shared dictionaries. Static values stay in files or environment variables. Runtime modules do not mutate config behind each other's backs.

Secrets must be represented as secret values or redacted summaries. Never pass a full secret into logs, API DTOs, task output, memory, or model context.

## Testing expectations

Prefer tests around public contracts:

- permission decisions
- scope and tool visibility
- provider request translation using fake transports
- memory search/add/update/delete through fake or temporary stores
- context filtering
- task due selection and next-run advancement
- consolidation audit behavior
- API route auth and DTO shape

No live provider calls in tests. No Discord network calls in tests.

## Forbidden patterns

- New god files.
- Compatibility facades that import everything.
- Direct provider HTTP calls outside provider clients.
- Direct memory storage access outside the memory implementation.
- UI routes that duplicate domain logic.
- Global mutable singletons as hidden dependencies.
- Root docs that describe storage internals.
- Reusable transcripts containing rendered tool-turn banners.
- Fixed loop or tool budgets in docs.
- Adding behavior by pasting another block into the old large file.

## Done means

- The owning module contract is clear.
- Existing product invariants still hold.
- Tests cover the behavior you touched.
- Secrets remain redacted.
- Background work is TaskGroup-owned.
- The next agent can continue without rereading the whole repository.
