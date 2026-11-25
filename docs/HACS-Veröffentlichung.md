# HACS und Add-on-Repository veröffentlichen

Der öffentliche Veröffentlichungsablauf ist abgeschlossen. Diese Seite dokumentiert die wiederholbaren Prüfschritte für spätere Releases.

1. Sicherstellen, dass keine Zugangsdaten, privaten URLs oder persönlichen Daten im Repository stehen.
2. Repository muss **Public** sein.
3. Den Workflow **Prüfen** erneut starten. Nun müssen HACS, Hassfest und Add-on-Container grün sein.
4. In HACS das öffentliche Repository als benutzerdefiniertes Repository vom Typ **Integration** hinzufügen und eine frische Installation testen.
5. In Home Assistant unter **Add-on-Store → Repositories** dieselbe URL eintragen und das Add-on testen.
6. Einen GitHub-Release mit semantischer Version, Änderungen und Installationshinweisen erstellen.
7. Erst nach erfolgreichem Praxistest eine Aufnahme in HACS beziehungsweise weitere Home-Assistant-Verzeichnisse beantragen.

Die URL lautet: `https://github.com/ThomS263/foto-upload-home-assistant`.
