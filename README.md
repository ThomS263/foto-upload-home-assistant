# Foto-Upload für Home Assistant und HACS

Home Assistant integration and add-on for the self-hosted [Foto-Upload server](https://github.com/ThomS263/foto-upload). The integration monitors availability, storage, albums, uploads, backups and expired guest links. The optional add-on runs the complete server directly on Home Assistant OS or Supervised.

<p align="center">
  <img src="custom_components/foto_upload/brand/icon.png" alt="Foto-Upload-Symbol" width="120">
</p>

**Aktueller Stand:** Integration **1.6.0**, Add-on/Server **3.7.0**. Das Repository bleibt bis zum abgeschlossenen Praxistest privat.

Dieses Repository bietet zwei Wege:

1. **Home-Assistant-Add-on statt CasaOS:** Der vollständige Foto-Upload-Server läuft direkt auf Home Assistant OS oder Supervised.
2. **HACS-Integration:** Ein bereits auf CasaOS, Docker oder als Add-on laufender Server wird in Home Assistant eingebunden.

## Add-on installieren

Unter **Einstellungen → Add-ons → Add-on-Store → Repositories** diese Adresse eintragen:

`https://github.com/ThomS263/foto-upload-home-assistant`

Danach **Foto-Upload** installieren, starten und die Weboberfläche öffnen. Die Daten werden unter `/share/foto-upload` gespeichert. CasaOS wird dafür nicht benötigt.

## HACS-Integration installieren

In HACS dieses Repository als benutzerdefiniertes Repository vom Typ **Integration** hinzufügen. Home Assistant neu starten und anschließend unter **Geräte & Dienste → Integration hinzufügen → Foto-Upload** die Serveradresse eintragen.

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

Solange dieses Repository privat ist, muss es für Tests lokal in `/config/custom_components/foto_upload` kopiert werden; HACS und der Add-on-Store können private GitHub-Repositories nicht allgemein abrufen. Die Container- und Hassfest-Prüfungen laufen trotzdem. Erst nach deiner bewussten Veröffentlichung wird zusätzlich die offizielle HACS-Prüfung aktiv.
