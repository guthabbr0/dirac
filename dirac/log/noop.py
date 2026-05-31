from __future__ import annotations

from dirac.types import LogEvent

from .base import BaseLog


class NoopLog(BaseLog):
    async def event(self, event: LogEvent) -> None:
        _ = event
