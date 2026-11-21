from __future__ import annotations

from typing import Any

from aiohttp import ClientError, ClientSession


class FotoUploadApi:
    def __init__(self, session: ClientSession, url: str) -> None:
        self.session = session
        self.url = url.rstrip("/")

    async def status(self) -> dict[str, Any]:
        try:
            async with self.session.get(f"{self.url}/health", timeout=10) as response:
                response.raise_for_status()
                data = await response.json()
        except (ClientError, TimeoutError, ValueError) as error:
            raise ConnectionError("Foto-Upload ist nicht erreichbar") from error
        if data.get("ok") is not True or not isinstance(data.get("files", {}), dict):
            raise ConnectionError("Ungültige Antwort des Foto-Upload-Servers")
        return data
