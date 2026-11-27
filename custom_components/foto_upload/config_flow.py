from __future__ import annotations

from urllib.parse import urlsplit

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_ACCESS_TOKEN, CONF_URL
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers import selector

from .api import AuthenticationError, FotoUploadApi
from .const import DOMAIN


class FotoUploadConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 2

    @staticmethod
    def _token_field():
        return selector.TextSelector(
            selector.TextSelectorConfig(type=selector.TextSelectorType.PASSWORD)
        )

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input:
            url = user_input[CONF_URL].strip().rstrip("/")
            parsed = urlsplit(url)
            if (
                parsed.scheme not in {"http", "https"}
                or not parsed.hostname
                or parsed.username
                or parsed.password
                or parsed.path not in {"", "/"}
                or parsed.query
                or parsed.fragment
            ):
                errors["base"] = "invalid_url"
            else:
                try:
                    token = user_input[CONF_ACCESS_TOKEN]
                    data = await FotoUploadApi(async_get_clientsession(self.hass), url, token).status()
                except AuthenticationError:
                    errors["base"] = "invalid_auth"
                except ConnectionError:
                    errors["base"] = "cannot_connect"
                else:
                    await self.async_set_unique_id(url.lower())
                    self._abort_if_unique_id_configured()
                    return self.async_create_entry(
                        title=f"Foto-Upload {data.get('version', '')}".strip(),
                        data={CONF_URL: url, CONF_ACCESS_TOKEN: token},
                    )
        schema = vol.Schema({
            vol.Required(CONF_URL, default=(user_input or {}).get(CONF_URL, "http://homeassistant.local:8080")): str,
            vol.Required(CONF_ACCESS_TOKEN): self._token_field(),
        })
        return self.async_show_form(step_id="user", data_schema=schema, errors=errors)

    async def async_step_reauth(self, entry_data):
        self._reauth_entry = self.hass.config_entries.async_get_entry(self.context["entry_id"])
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(self, user_input=None):
        errors = {}
        if user_input:
            token = user_input[CONF_ACCESS_TOKEN]
            try:
                await FotoUploadApi(
                    async_get_clientsession(self.hass),
                    self._reauth_entry.data[CONF_URL],
                    token,
                ).status()
            except AuthenticationError:
                errors["base"] = "invalid_auth"
            except ConnectionError:
                errors["base"] = "cannot_connect"
            else:
                self.hass.config_entries.async_update_entry(
                    self._reauth_entry,
                    data={**self._reauth_entry.data, CONF_ACCESS_TOKEN: token},
                )
                await self.hass.config_entries.async_reload(self._reauth_entry.entry_id)
                return self.async_abort(reason="reauth_successful")
        return self.async_show_form(
            step_id="reauth_confirm",
            data_schema=vol.Schema({vol.Required(CONF_ACCESS_TOKEN): self._token_field()}),
            errors=errors,
        )
