from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_URL
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import FotoUploadApi
from .const import DOMAIN


class FotoUploadConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input:
            url = user_input[CONF_URL].strip().rstrip("/")
            try:
                data = await FotoUploadApi(async_get_clientsession(self.hass), url).status()
            except ConnectionError:
                errors["base"] = "cannot_connect"
            else:
                await self.async_set_unique_id(url.lower())
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title=f"Foto-Upload {data.get('version', '')}".strip(), data={CONF_URL: url})
        schema = vol.Schema({vol.Required(CONF_URL, default=(user_input or {}).get(CONF_URL, "http://homeassistant.local:8080")): str})
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)
