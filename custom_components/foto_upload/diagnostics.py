from __future__ import annotations

from .const import DOMAIN


async def async_get_config_entry_diagnostics(hass, entry):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    return {
        "server": entry.data.get("url"),
        "available": coordinator.last_update_success,
        "status": coordinator.data,
    }
