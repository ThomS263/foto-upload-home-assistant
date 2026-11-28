# Releases und Wartung

Foto-Upload ist im offiziellen HACS-Standardkatalog verfügbar. Nutzer installieren die Integration direkt über die HACS-Suche; ein benutzerdefiniertes Repository ist nicht erforderlich.

## Neue Version veröffentlichen

1. Versionsnummer in `custom_components/foto_upload/manifest.json` erhöhen.
2. Deutsche und englische Texte sowie die Dokumentation aktualisieren.
3. HACS-, Hassfest-, Add-on- und Sicherheitsprüfungen vollständig durchlaufen lassen.
4. Einen GitHub-Release mit semantischer Versionsnummer und verständlichen Änderungen veröffentlichen.
5. Nach einigen Stunden prüfen, ob HACS die neue Version anbietet.

Das Add-on wird weiterhin über dieses Repository zum Home-Assistant-Add-on-Store hinzugefügt. Vor Server- oder Add-on-Updates sollte `/share/foto-upload` gesichert werden.

Repository: `https://github.com/ThomS263/foto-upload-home-assistant`
