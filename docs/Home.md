# Foto-Upload für Home Assistant

Dieses öffentliche Repository enthält zwei getrennte Komponenten:

- Das **Home-Assistant-Add-on** betreibt den vollständigen Foto-Upload-Server anstelle von CasaOS.
- Die **HACS-Integration** verbindet Home Assistant mit einem bereits laufenden Server.

HACS, Hassfest, Python-Syntax und der Add-on-Container werden bei Änderungen automatisch geprüft.

| Komponente | Version | Aufgabe |
| --- | --- | --- |
| HACS-Integration | 1.6.2 | Überwacht Server, Speicher, Alben, Uploads, Sicherungen und Freigabelinks |
| Home-Assistant-Add-on | 3.7.0 | Betreibt den vollständigen Foto-Upload-Server auf Home Assistant OS/Supervised |

![Mobile Add-on-Weboberfläche](images/addon-mobile.png)

- [Installation mit HACS](Private-Testinstallation.md)
- [HACS-Veröffentlichung](HACS-Veröffentlichung.md)
- [Automationen](Automationen.md)
- [Fehlerbehebung](Fehlerbehebung.md)
