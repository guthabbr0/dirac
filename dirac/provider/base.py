from __future__ import annotations

from abc import ABC, abstractmethod

from dirac.types import ProviderRequest, ProviderResponse


class ProviderError(RuntimeError):
    pass


class BaseProviderClient(ABC):
    name: str

    @abstractmethod
    async def chat(self, request: ProviderRequest) -> ProviderResponse:
        raise NotImplementedError
