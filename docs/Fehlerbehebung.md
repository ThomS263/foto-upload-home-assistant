# Fehlerbehebung

| Problem | Prüfung und Lösung |
| --- | --- |
| Integration wird nicht gefunden | HACS-Daten aktualisieren, nach **Foto-Upload** suchen und herunterladen, Home Assistant neu starten und erneut unter **Geräte & Dienste** suchen. Nach einer neuen Katalogaufnahme kann die Anzeige laut HACS bis zu acht Stunden dauern. |
| Server ist nicht erreichbar | In der Integration dieselbe Basisadresse testen, die im Browser funktioniert. Für einen Server im LAN beispielsweise `http://192.168.1.20:8080`, ohne zusätzlichen Pfad. |
| Welcher Token wird verlangt? | Den **Home-Assistant-Status-Token** unter **Foto-Upload → Verwaltung → Sicherheit, Funnel & Updates** kopieren. Kein Adminpasswort, Albumpasswort, GitHub-, HACS- oder Home-Assistant-Token verwenden. |
| Das Feld „Home-Assistant-Status-Token“ fehlt | Der Foto-Upload-Server ist älter als 3.8.0. Zuerst Server beziehungsweise Add-on aktualisieren und die Verwaltung neu laden. |
| Status-Token wird abgelehnt | Token erneut vollständig kopieren, auf unsichtbare Leerzeichen achten und prüfen, ob Serveradresse und Token vom selben Foto-Upload-Server stammen. Bei einer bestehenden Integration die angebotene erneute Authentifizierung verwenden. |
| Add-on startet nicht | Unter **Einstellungen → Add-ons → Foto-Upload → Protokoll** nach dem ersten Fehler suchen. Freien Speicher und Port 8080 prüfen. |
| Weboberfläche bleibt leer | Add-on-Protokoll und `/health?ready=1` prüfen. Bei externer Nutzung zusätzlich Reverse Proxy oder Funnel kontrollieren. |
| Neue Uploads lösen keine Automation aus | In den Entwicklerwerkzeugen auf `foto_upload_new_files` lauschen und prüfen, ob die Integration erreichbar ist. Das Ereignis entsteht erst bei einer erhöhten Dateianzahl. |

Keine Zugangsdaten oder Diagnosearchive öffentlich in Issues hochladen. Sicherheitsprobleme nach dem vertraulichen Verfahren in [`SECURITY.md`](../SECURITY.md) melden.
