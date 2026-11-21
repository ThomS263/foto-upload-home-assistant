# Automationen

Die Integration feuert bei neuen Dateien das Ereignis `foto_upload_new_files` mit diesen Feldern:

- `count`: Anzahl neuer Dateien seit der letzten Abfrage
- `total`: aktuelle Gesamtzahl
- `entry_id`: Kennung der Integration

Eine fertige Beispielautomation liegt unter `examples/new-upload-notification.yaml`. Zusätzlich gibt es Sensoren für Verbindung, Version, Gesamtzahl und jedes Album. Neu angelegte Alben erscheinen automatisch ohne erneutes Einrichten der Integration.
