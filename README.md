# Foto-Upload für Home Assistant und HACS

Dieses Repository bietet zwei Wege:

1. **Home-Assistant-Add-on statt CasaOS:** Der vollständige Foto-Upload-Server läuft direkt auf Home Assistant OS oder Supervised.
2. **HACS-Integration:** Ein bereits auf CasaOS, Docker oder als Add-on laufender Server wird in Home Assistant eingebunden.

## Add-on installieren

Unter **Einstellungen → Add-ons → Add-on-Store → Repositories** diese Adresse eintragen:

`https://github.com/ThomS263/foto_upload_offiziell_hacs`

Danach **Foto-Upload** installieren, starten und die Weboberfläche öffnen. Die Daten werden unter `/share/foto-upload` gespeichert. CasaOS wird dafür nicht benötigt.

## HACS-Integration installieren

In HACS dieses Repository als benutzerdefiniertes Repository vom Typ **Integration** hinzufügen. Home Assistant neu starten und anschließend unter **Geräte & Dienste → Integration hinzufügen → Foto-Upload** die Serveradresse eintragen.

Die Integration erstellt Sensoren für Erreichbarkeit, Serverversion, Gesamtzahl der Dateien und jedes aktive Album. Mit Home-Assistant-Automationen lassen sich bei steigenden Dateizahlen Benachrichtigungen senden.

## Beispielautomation für neue Uploads

```yaml
automation:
  - alias: Foto-Upload hat neue Dateien
    triggers:
      - trigger: state
        entity_id: sensor.foto_upload_dateien_gesamt
    conditions:
      - condition: template
        value_template: "{{ trigger.to_state.state | int > trigger.from_state.state | int }}"
    actions:
      - action: notify.notify
        data:
          message: "Neue Fotos wurden hochgeladen."
```

[Foto-Upload-Server](https://github.com/ThomS263/foto_upload_offiziel) · [Android-App](https://github.com/ThomS263/foto_upload_offiziell_androidapp)
