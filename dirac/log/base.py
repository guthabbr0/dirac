from __future__ import annotations

from abc import ABC, abstractmethod

from dirac.types import LogEvent


class BaseLog(ABC):
    @abstractmethod
    async def event(self, event: LogEvent) -> None:
        raise NotImplementedError
