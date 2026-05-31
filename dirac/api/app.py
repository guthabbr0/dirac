from __future__ import annotations

from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title="Dirac API")

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"ok": "true"}

    @app.get("/api/runtime")
    async def runtime() -> dict[str, str]:
        return {"status": "skeleton"}

    return app
