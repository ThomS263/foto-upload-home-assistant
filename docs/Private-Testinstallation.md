# Installation mit HACS

1. HACS öffnen und nach **Foto-Upload** suchen.
2. Die Integration herunterladen und Home Assistant neu starten.
3. **Einstellungen → Geräte & Dienste → Integration hinzufügen** öffnen.
4. Nach **Foto-Upload** suchen und die Basisadresse des Servers eintragen.

Falls die Integration noch nicht im Standardkatalog angezeigt wird, kann dieses
öffentliche Repository in HACS als benutzerdefiniertes Repository vom Typ
**Integration** hinzugefügt werden:

`https://github.com/ThomS263/foto-upload-home-assistant`

Für das Add-on unter **Einstellungen → Add-ons → Add-on-Store → Repositories**
dieselbe öffentliche Repository-Adresse eintragen und anschließend
**Foto-Upload** installieren.

Vor einem Add-on-Update empfiehlt sich eine Sicherung von `/share/foto-upload`.
Für externe QR-Codes wird weiterhin eine eigene HTTPS-Adresse oder ein
vorhandener Tunnel benötigt.
