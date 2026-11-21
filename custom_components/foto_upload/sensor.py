from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    entities = [TotalFiles(coordinator, entry.entry_id), Version(coordinator, entry.entry_id)]
    entities.extend(AlbumFiles(coordinator, entry.entry_id, slug) for slug in coordinator.data.get("files", {}))
    async_add_entities(entities)


class Base(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator, entry_id, key):
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry_id}_{key}"
        self._attr_device_info = {"identifiers": {(DOMAIN, entry_id)}, "name": "Foto-Upload", "manufacturer": "ThomS263"}


class TotalFiles(Base):
    _attr_name = "Dateien gesamt"
    _attr_icon = "mdi:image-multiple"

    def __init__(self, coordinator, entry_id): super().__init__(coordinator, entry_id, "files_total")
    @property
    def native_value(self): return sum(self.coordinator.data.get("files", {}).values())


class Version(Base):
    _attr_name = "Version"
    _attr_icon = "mdi:information-outline"

    def __init__(self, coordinator, entry_id): super().__init__(coordinator, entry_id, "version")
    @property
    def native_value(self): return self.coordinator.data.get("version", "unbekannt")


class AlbumFiles(Base):
    _attr_icon = "mdi:image-album"

    def __init__(self, coordinator, entry_id, slug):
        super().__init__(coordinator, entry_id, f"album_{slug}")
        self.slug = slug
        self._attr_name = f"Album {slug}"

    @property
    def native_value(self): return self.coordinator.data.get("files", {}).get(self.slug, 0)
