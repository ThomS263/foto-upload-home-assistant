from __future__ import annotations

from typing import Any

from aiohttp import ClientError, ClientSession


class FotoUploadApi:
    def __init__(self, session: ClientSession, url: str, token: str) -> None:
        self.session = session
        self.url = url.rstrip("/")
        self.token = token

    async def status(self) -> dict[str, Any]:
        try:
            async with self.session.get(
                f"{self.url}/health",
                headers={"Authorization": f"Bearer {self.token}"},
                timeout=10,
            ) as response:
                if response.status == 401:
                    raise AuthenticationError("Status-Token wurde abgelehnt")
                response.raise_for_status()
                data = await response.json()
        except (ClientError, TimeoutError, ValueError) as error:
            raise ConnectionError("Foto-Upload ist nicht erreichbar") from error
        if data.get("ok") is not True or not isinstance(data.get("files", {}), dict):
            raise ConnectionError("Ungültige Antwort des Foto-Upload-Servers")
        return data


class AuthenticationError(ConnectionError):
    """Raised when the read-only server token is rejected."""
