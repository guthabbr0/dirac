from __future__ import annotations

from .openai_compatible import OpenAICompatibleProviderClient


class OpenRouterProviderClient(OpenAICompatibleProviderClient):
    """OpenRouter over the same BaseProviderClient contract."""

    def __init__(
        self,
        *,
        base_url: str = "https://openrouter.ai/api/v1",
        api_key: str = "",
        timeout_s: float = 120.0,
        name: str = "openrouter",
    ) -> None:
        super().__init__(
            base_url=base_url,
            api_key=api_key,
            timeout_s=timeout_s,
            name=name,
            default_headers={
                "HTTP-Referer": "http://127.0.0.1:8765",
                "X-Title": "Dirac",
            },
        )
