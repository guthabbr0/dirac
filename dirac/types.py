from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal


ScopeName = Literal[
    "global",
    "guild",
    "channel",
    "dm",
    "group",
    "user",
    "task",
    "panel",
    "api",
    "discord",
]


@dataclass(frozen=True, slots=True)
class Scope:
    scope_type: str = "global"
    scope_id: str | None = None

    def label(self) -> str:
        return f"{self.scope_type}:{self.scope_id or '*'}"


@dataclass(frozen=True, slots=True)
class ProviderRequest:
    messages: list[dict[str, Any]]
    model: str
    scope: Scope = field(default_factory=Scope)
    tools: list[dict[str, Any]] | None = None
    params: dict[str, Any] = field(default_factory=dict)
    source: str = "unknown"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ProviderResponse:
    content: str
    raw: Any = None
    tool_calls: list[dict[str, Any]] = field(default_factory=list)
    usage: dict[str, Any] = field(default_factory=dict)
    provider_name: str = "unknown"
    model: str = "unknown"


@dataclass(frozen=True, slots=True)
class MemoryQuery:
    text: str | None = None
    discord_id: str | None = None
    scope: Scope | None = None
    limit: int = 10


@dataclass(frozen=True, slots=True)
class MemoryWrite:
    discord_id: str
    annotations: str
    tags: tuple[str, ...] = ()
    confidence: float = 0.7
    created_by: str = "system"


@dataclass(frozen=True, slots=True)
class MemoryPatch:
    annotations: str | None = None
    tags: tuple[str, ...] | None = None
    confidence: float | None = None
    updated_by: str = "system"


@dataclass(frozen=True, slots=True)
class MemoryRecord:
    memory_id: str
    discord_id: str
    annotations: str
    tags: tuple[str, ...] = ()
    confidence: float = 0.7
    created_by: str = "system"
    created_utc: str | None = None
    superseded_by: str | None = None


@dataclass(frozen=True, slots=True)
class ToolResult:
    name: str
    ok: bool
    payload: dict[str, Any] = field(default_factory=dict)
    needs_model_followup: bool = False


@dataclass(slots=True)
class TaskDefinition:
    task_id: str
    name: str
    prompt: str
    scope: Scope = field(default_factory=Scope)
    enabled: bool = True
    schedule_minutes: int | None = None
    next_run_utc: str | None = None
    run_count: int = 0
    max_runs: int | None = None
    runtime_kind: str = "default"


@dataclass(frozen=True, slots=True)
class LogEvent:
    level: str
    component: str
    message: str
    detail: dict[str, Any] = field(default_factory=dict)
    scope: Scope | None = None
    timestamp_utc: str | None = None
