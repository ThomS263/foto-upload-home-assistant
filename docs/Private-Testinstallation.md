# Installation mit HACS

1. HACS öffnen und nach **Foto-Upload** suchen.
2. Die Integration herunterladen und Home Assistant neu starten.
3. **Einstellungen → Geräte & Dienste → Integration hinzufügen** öffnen und **Foto-Upload** wählen.
4. Im Foto-Upload-Adminbereich unter **Sicherheit, Funnel & Updates** den Home-Assistant-Status-Token kopieren.
5. Die Basisadresse des Servers und den Status-Token eintragen.

Der Status-Token erlaubt ausschließlich das Lesen der Überwachungswerte. Er bietet keinen Zugriff auf Fotos, Alben oder die Verwaltung. Wird er abgelehnt, zeigt Home Assistant automatisch eine erneute Anmeldung an.

## Optionales Home-Assistant-Add-on

Wer keinen eigenen CasaOS- oder Docker-Server verwendet, trägt unter **Einstellungen → Add-ons → Add-on-Store → Repositories** diese Adresse ein:

`https://github.com/ThomS263/foto-upload-home-assistant`

Danach **Foto-Upload** installieren und starten. Die Daten liegen unter `/share/foto-upload`. Vor Updates empfiehlt sich eine Sicherung dieses Ordners. Für externe QR-Codes wird eine eigene HTTPS-Adresse oder ein vorhandener Tunnel benötigt.
