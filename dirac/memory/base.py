from __future__ import annotations

from abc import ABC, abstractmethod

from dirac.types import MemoryPatch, MemoryQuery, MemoryRecord, MemoryWrite


class BaseMemory(ABC):
    @abstractmethod
    async def search(self, query: MemoryQuery) -> list[MemoryRecord]:
        raise NotImplementedError

    @abstractmethod
    async def add(self, record: MemoryWrite) -> MemoryRecord:
        raise NotImplementedError

    @abstractmethod
    async def update(self, memory_id: str, patch: MemoryPatch) -> MemoryRecord:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, memory_id: str) -> None:
        raise NotImplementedError


BaseVirtualMemory = BaseMemory
