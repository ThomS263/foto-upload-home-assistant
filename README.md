# Foto-Upload für Home Assistant und HACS

Home Assistant integration and add-on for the self-hosted [Foto-Upload server](https://github.com/ThomS263/foto-upload). The integration monitors availability, storage, albums, uploads, backups and expired guest links. The optional add-on runs the complete server directly on Home Assistant OS or Supervised.

<p align="center">
  <img src="custom_components/foto_upload/brand/icon.png" alt="Foto-Upload-Symbol" width="120">
</p>

**Aktueller Stand:** Integration **1.7.1**, Add-on/Server **3.8.0**. Das Repository ist öffentlich und über HACS installierbar.

Dieses Repository bietet zwei Wege:

1. **Home-Assistant-Add-on statt CasaOS:** Der vollständige Foto-Upload-Server läuft direkt auf Home Assistant OS oder Supervised.
2. **HACS-Integration:** Ein bereits auf CasaOS, Docker oder als Add-on laufender Server wird in Home Assistant eingebunden.

## Add-on installieren

Unter **Einstellungen → Add-ons → Add-on-Store → Repositories** diese Adresse eintragen:

`https://github.com/ThomS263/foto-upload-home-assistant`

Danach **Foto-Upload** installieren, starten und die Weboberfläche öffnen. Die Daten werden unter `/share/foto-upload` gespeichert. CasaOS wird dafür nicht benötigt.

## HACS-Integration installieren

Beim Herunterladen in HACS wird **kein Token** benötigt. Der Token wird erst nach dem Neustart beim Einrichten der Integration abgefragt.

1. In HACS nach **Foto-Upload** suchen und **Herunterladen** wählen.
2. Home Assistant neu starten.
3. Die Weboberfläche deines Foto-Upload-Servers öffnen und als Administrator anmelden.
4. **Verwaltung → Sicherheit, Funnel & Updates** öffnen.
5. Beim Feld **Home-Assistant-Status-Token** auf **Status-Token kopieren** drücken.
6. In Home Assistant **Einstellungen → Geräte & Dienste → Integration hinzufügen → Foto-Upload** öffnen.
7. Als Serveradresse die Adresse eintragen, unter der Home Assistant den Server erreicht, zum Beispiel `http://192.168.1.20:8080`.
8. In **Nur-lesbarer Status-Token** den eben kopierten Home-Assistant-Status-Token einfügen.

Verwende dort **nicht** das Adminpasswort, ein Albumpasswort, einen GitHub-Token, einen HACS-Token oder einen Home-Assistant-Zugriffstoken. Der richtige Schlüssel ist ausschließlich der automatisch erzeugte **Home-Assistant-Status-Token** aus der Foto-Upload-Verwaltung. Er erlaubt nur das Lesen der Überwachungswerte und keinen Zugriff auf Alben, Originaldateien oder Verwaltungsfunktionen.

Der Status-Token ist erst ab Foto-Upload Server **3.8.0** verfügbar. Bei einer älteren Serverversion zuerst den Server beziehungsweise das Add-on aktualisieren.

### Welche Serveradresse eintragen?

- CasaOS im Heimnetz: `http://CASAOS-IP:8080`
- Home-Assistant-Add-on: die im Add-on angezeigte lokale Adresse mit Port `8080`
- Docker mit geändertem Port: `http://SERVER-IP:DEIN-PORT`
- Extern nur über deine eigene HTTPS-Adresse, beispielsweise `https://fotos.example.org`

Keine Unterseite wie `/admin`, `/health` oder `/event/...` anhängen.

### Bestehende Integration aktualisieren

Nach dem Update auf Server 3.8.0 kann Home Assistant **Erneute Authentifizierung erforderlich** anzeigen. Dann den Status-Token aus der Verwaltung kopieren und im angezeigten Dialog einfügen. Die Integration muss nicht gelöscht werden.

Die Integration erstellt Sensoren für Erreichbarkeit, Version, Dateien, aktive und archivierte Alben, freien Speicher, letzten Upload, letzte Sicherung, Sicherungszustand und abgelaufene Gästelinks. Neue Alben erscheinen dynamisch. Bei neuen Dateien wird außerdem das Ereignis `foto_upload_new_files` mit `count`, `total` und `entry_id` ausgelöst. Über die Geräteansicht führt ein Link direkt zur Serveroberfläche; Diagnoseinformationen stehen im Home-Assistant-Download bereit.

## Beispielautomation für neue Uploads

```yaml
automation:
  - alias: Foto-Upload hat neue Dateien
    triggers:
      - trigger: event
        event_type: foto_upload_new_files
    actions:
      - action: notify.notify
        data:
          message: "{{ trigger.event.data.count }} neue Datei(en) wurden hochgeladen."
```

[Foto-Upload-Server](https://github.com/ThomS263/foto-upload) · [Android-App](https://github.com/ThomS263/foto-upload-android)

Ausführliche Dokumentation liegt versioniert unter [`docs/`](docs/Home.md). Fehler und Funktionswünsche können über [GitHub Issues](https://github.com/ThomS263/foto-upload-home-assistant/issues) gemeldet werden.

## Oberfläche des Add-ons

Das Add-on öffnet dieselbe responsive Weboberfläche wie der Foto-Upload-Server:

<p align="center">
  <img src="docs/images/addon-mobile.png" alt="Mobile Foto-Upload-Weboberfläche des Home-Assistant-Add-ons" width="320">
</p>

Die Home-Assistant-Integration selbst ergänzt Geräte, Sensoren, Diagnoseinformationen und das Ereignis `foto_upload_new_files`. Eine Übersicht steht unter [Dokumentation](docs/Home.md).

## Lizenz

Integration und Add-on stehen unter der [GNU Affero General Public License v3.0](LICENSE) (`AGPL-3.0-only`).
