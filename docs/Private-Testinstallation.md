# Private Testinstallation

## Integration manuell testen

1. Dieses private Repository auf einen Computer mit Git-Zugriff klonen.
2. Den Ordner `custom_components/foto_upload` nach `/config/custom_components/foto_upload` der Home-Assistant-Installation kopieren.
3. Home Assistant vollständig neu starten.
4. Unter **Einstellungen → Geräte & Dienste → Integration hinzufügen** nach `Foto-Upload` suchen.
5. Die vollständige Serveradresse eintragen, beispielsweise `http://192.168.1.20:8080`.

## Add-on privat testen

Ein privates GitHub-Repository lässt sich nicht allgemein als Add-on-Quelle eintragen. Für den Test den Ordner `foto_upload_addon` nach `/addons/foto_upload` kopieren, den Add-on-Store neu laden und das lokale Add-on installieren. Die Daten liegen anschließend unter `/share/foto-upload`.

Vor jedem Update eine Kopie dieses Ordners erstellen. Für externe QR-Codes wird weiterhin eine eigene HTTPS-Adresse oder ein vorhandener Tunnel benötigt.
