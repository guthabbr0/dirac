from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class ConsolidationAudit:
    ok: bool
    result: str
    memory_writes: int = 0
    warnings: tuple[str, ...] = ()
    detail: dict[str, Any] = field(default_factory=dict)
