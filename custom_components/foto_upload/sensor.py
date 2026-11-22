from __future__ import annotations

from datetime import datetime, timezone

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        TotalFiles(coordinator, entry), Version(coordinator, entry), StorageFree(coordinator, entry),
        ActiveAlbums(coordinator, entry), ArchivedAlbums(coordinator, entry),
        LastUpload(coordinator, entry), LastBackup(coordinator, entry), ExpiredShares(coordinator, entry),
    ])
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


class StorageFree(Base):
    _attr_name = "Speicher frei"
    _attr_icon = "mdi:harddisk"
    _attr_native_unit_of_measurement = "GiB"

    def __init__(self, coordinator, entry): super().__init__(coordinator, entry, "storage_free")
    @property
    def native_value(self): return round(self.coordinator.data.get("storage", {}).get("free", 0) / 1024**3, 1)
    @property
    def extra_state_attributes(self):
        return {"total_gib": round(self.coordinator.data.get("storage", {}).get("total", 0) / 1024**3, 1)}


class ActiveAlbums(Base):
    _attr_name = "Aktive Alben"
    _attr_icon = "mdi:image-album"

    def __init__(self, coordinator, entry): super().__init__(coordinator, entry, "albums_active")
    @property
    def native_value(self): return self.coordinator.data.get("albums", {}).get("active", 0)


class ArchivedAlbums(Base):
    _attr_name = "Archivierte Alben"
    _attr_icon = "mdi:archive"

    def __init__(self, coordinator, entry): super().__init__(coordinator, entry, "albums_archived")
    @property
    def native_value(self): return self.coordinator.data.get("albums", {}).get("archived", 0)


class LastUpload(Base):
    _attr_name = "Letzter Upload"
    _attr_icon = "mdi:clock-outline"
    _attr_device_class = SensorDeviceClass.TIMESTAMP

    def __init__(self, coordinator, entry): super().__init__(coordinator, entry, "last_upload")
    @property
    def native_value(self):
        value = self.coordinator.data.get("last_upload", 0)
        return datetime.fromtimestamp(value, timezone.utc) if value else None


class LastBackup(Base):
    _attr_name = "Letzte Sicherung"
    _attr_icon = "mdi:backup-restore"
    _attr_device_class = SensorDeviceClass.TIMESTAMP

    def __init__(self, coordinator, entry): super().__init__(coordinator, entry, "last_backup")
    @property
    def native_value(self):
        value = self.coordinator.data.get("backup", {}).get("success", 0)
        return datetime.fromtimestamp(value, timezone.utc) if value else None
    @property
    def extra_state_attributes(self): return self.coordinator.data.get("backup", {})


class ExpiredShares(Base):
    _attr_name = "Abgelaufene Gästelinks"
    _attr_icon = "mdi:link-off"

    def __init__(self, coordinator, entry): super().__init__(coordinator, entry, "expired_shares")
    @property
    def native_value(self): return self.coordinator.data.get("expired_shares", 0)
