from homeassistant.components.binary_sensor import BinarySensorEntity, BinarySensorDeviceClass
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([Online(hass.data[DOMAIN][entry.entry_id], entry.entry_id)])


class Online(CoordinatorEntity, BinarySensorEntity):
    _attr_name = "Server"
    _attr_has_entity_name = True
    _attr_device_class = BinarySensorDeviceClass.CONNECTIVITY

    def __init__(self, coordinator, entry_id):
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry_id}_online"
        self._attr_device_info = {"identifiers": {(DOMAIN, entry_id)}, "name": "Foto-Upload", "manufacturer": "ThomS263"}

    @property
    def is_on(self): return self.coordinator.last_update_success
