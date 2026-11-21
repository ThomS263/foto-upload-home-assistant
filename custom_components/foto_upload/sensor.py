from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([TotalFiles(coordinator, entry), Version(coordinator, entry)])
    known = set()

    def add_albums():
        missing = set(coordinator.data.get("files", {})) - known
        if missing:
            async_add_entities([AlbumFiles(coordinator, entry, slug) for slug in sorted(missing)])
            known.update(missing)

    add_albums()
    entry.async_on_unload(coordinator.async_add_listener(add_albums))


class Base(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator, entry, key):
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_{key}"
        self._attr_device_info = {"identifiers": {(DOMAIN, entry.entry_id)}, "name": "Foto-Upload", "manufacturer": "ThomS263", "configuration_url": entry.data["url"]}


class TotalFiles(Base):
    _attr_name = "Dateien gesamt"
    _attr_icon = "mdi:image-multiple"

    def __init__(self, coordinator, entry): super().__init__(coordinator, entry, "files_total")
    @property
    def native_value(self): return sum(self.coordinator.data.get("files", {}).values())
    @property
    def extra_state_attributes(self): return {"albums": self.coordinator.data.get("files", {})}


class Version(Base):
    _attr_name = "Version"
    _attr_icon = "mdi:information-outline"

    def __init__(self, coordinator, entry): super().__init__(coordinator, entry, "version")
    @property
    def native_value(self): return self.coordinator.data.get("version", "unbekannt")


class AlbumFiles(Base):
    _attr_icon = "mdi:image-album"

    def __init__(self, coordinator, entry, slug):
        super().__init__(coordinator, entry, f"album_{slug}")
        self.slug = slug
        self._attr_name = f"Album {slug}"

    @property
    def native_value(self): return self.coordinator.data.get("files", {}).get(self.slug, 0)
