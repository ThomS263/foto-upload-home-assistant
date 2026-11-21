# Foto-Upload Add-on

Dieses Add-on betreibt den vollständigen Foto-Upload-Server direkt in Home Assistant. Port 8080 wird standardmäßig veröffentlicht. Alben und Originaldateien liegen unter `/share/foto-upload` und bleiben bei Add-on-Updates erhalten.

Nach dem Start **Weboberfläche öffnen** wählen. Wenn kein Adminpasswort konfiguriert wurde, steht das erzeugte Erstpasswort in `/share/foto-upload/.initial-admin-password`. Für QR-Codes außerhalb des Heimnetzes kann eine bestehende öffentliche HTTPS-Adresse eingetragen werden. Das Add-on erstellt selbst keinen Tunnel.
