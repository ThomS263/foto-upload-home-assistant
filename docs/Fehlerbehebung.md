# Fehlerbehebung

| Problem | Prüfung und Lösung |
| --- | --- |
| Integration wird nicht gefunden | In HACS nach **Foto-Upload** suchen und herunterladen, Home Assistant neu starten und erneut unter **Geräte & Dienste** suchen. Falls sie noch nicht im Katalog erscheint, das öffentliche Repository vorübergehend als benutzerdefinierte Integration hinzufügen. |
| Server ist nicht erreichbar | In der Integration dieselbe Basisadresse testen, die im Browser funktioniert. Für einen Server im LAN beispielsweise `http://192.168.1.20:8080`, ohne zusätzlichen Pfad. |
| Add-on startet nicht | Unter **Einstellungen → Add-ons → Foto-Upload → Protokoll** nach dem ersten Fehler suchen. Freien Speicher und Port 8080 prüfen. |
| Weboberfläche bleibt leer | Add-on-Protokoll und `/health?ready=1` prüfen. Bei externer Nutzung zusätzlich Reverse Proxy oder Funnel kontrollieren. |
| Neue Uploads lösen keine Automation aus | In den Entwicklerwerkzeugen auf `foto_upload_new_files` lauschen und prüfen, ob die Integration erreichbar ist. Das Ereignis entsteht erst bei einer erhöhten Dateianzahl. |
| HACS akzeptiert das Repository nicht | Prüfen, ob der aktuelle GitHub-Release veröffentlicht ist und die HACS- sowie Hassfest-Prüfungen erfolgreich sind. |

Keine Zugangsdaten oder Diagnosearchive öffentlich in Issues hochladen. Sicherheitsprobleme nach dem vertraulichen Verfahren in [`SECURITY.md`](../SECURITY.md) melden.
