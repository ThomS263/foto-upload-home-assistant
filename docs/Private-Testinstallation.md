# Installation mit HACS

Für den Download in HACS ist kein Token erforderlich. Der Einrichtungsdialog nach dem Neustart fragt nach dem Token.

1. HACS öffnen, nach **Foto-Upload** suchen und die Integration herunterladen.
2. Home Assistant neu starten.
3. Foto-Upload im Browser öffnen und als Administrator anmelden.
4. **Verwaltung → Sicherheit, Funnel & Updates** öffnen.
5. Beim Feld **Home-Assistant-Status-Token** auf **Status-Token kopieren** drücken.
6. In Home Assistant **Einstellungen → Geräte & Dienste → Integration hinzufügen → Foto-Upload** öffnen.
7. Die erreichbare Basisadresse ohne zusätzlichen Pfad eintragen.
8. Den kopierten Schlüssel im Feld **Nur-lesbarer Status-Token** einfügen.

Nicht geeignet sind Admin- oder Albumpasswörter, GitHub-Tokens, HACS-Tokens und Home-Assistant-Zugriffstokens. Der Status-Token erlaubt ausschließlich das Lesen der Überwachungswerte. Er bietet keinen Zugriff auf Fotos, Alben oder die Verwaltung.

Der Server muss mindestens Version 3.8.0 verwenden. Nach einem Serverupdate kann Home Assistant eine erneute Authentifizierung verlangen; dann den aktuellen Status-Token einfügen, ohne die Integration zu löschen.

## Optionales Home-Assistant-Add-on

Wer keinen eigenen CasaOS- oder Docker-Server verwendet, trägt unter **Einstellungen → Add-ons → Add-on-Store → Repositories** diese Adresse ein:

`https://github.com/ThomS263/foto-upload-home-assistant`

Danach **Foto-Upload** installieren und starten. Die Daten liegen unter `/share/foto-upload`. Vor Updates empfiehlt sich eine Sicherung dieses Ordners. Für externe QR-Codes wird eine eigene HTTPS-Adresse oder ein vorhandener Tunnel benötigt.

Nach dem ersten Start die Add-on-Weboberfläche öffnen, das Adminpasswort festlegen und anschließend wie oben beschrieben den Home-Assistant-Status-Token kopieren.
