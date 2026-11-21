from __future__ import annotations

from datetime import timedelta

from homeassistant.const import CONF_URL, Platform
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import FotoUploadApi
from .const import DOMAIN, SCAN_INTERVAL_SECONDS

PLATFORMS = [Platform.SENSOR, Platform.BINARY_SENSOR]


async def async_setup_entry(hass, entry):
    api = FotoUploadApi(async_get_clientsession(hass), entry.data[CONF_URL])

    async def update():
        try:
            return await api.status()
        except ConnectionError as error:
            raise UpdateFailed(str(error)) from error

    coordinator = DataUpdateCoordinator(
        hass, logger=__import__("logging").getLogger(__name__), name="Foto-Upload",
        update_method=update, update_interval=timedelta(seconds=SCAN_INTERVAL_SECONDS),
    )
    await coordinator.async_config_entry_first_refresh()
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator
    previous = sum(coordinator.data.get("files", {}).values())

    def detect_uploads():
        nonlocal previous
        current = sum(coordinator.data.get("files", {}).values())
        if current > previous:
            hass.bus.async_fire(
                "foto_upload_new_files",
                {"entry_id": entry.entry_id, "count": current - previous, "total": current},
            )
        previous = current

    entry.async_on_unload(coordinator.async_add_listener(detect_uploads))
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass, entry):
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unloaded
