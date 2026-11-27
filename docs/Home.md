# Foto-Upload für Home Assistant

Dieses private Testrepository enthält zwei getrennte Komponenten:

- Das **Home-Assistant-Add-on** betreibt den vollständigen Foto-Upload-Server anstelle von CasaOS.
- Die **HACS-Integration** verbindet Home Assistant mit einem bereits laufenden Server.

Während der privaten Testphase werden Hassfest, Python-Syntax und der Add-on-Container bei jedem Push geprüft. Die HACS-Prüfung ist bis zur bewussten Veröffentlichung deaktiviert, weil sie nur öffentliche Repositories akzeptiert.

| Komponente | Version | Aufgabe |
| --- | --- | --- |
| HACS-Integration | 1.6.1 | Überwacht Server, Speicher, Alben, Uploads, Sicherungen und Freigabelinks |
| Home-Assistant-Add-on | 3.7.0 | Betreibt den vollständigen Foto-Upload-Server auf Home Assistant OS/Supervised |

![Mobile Add-on-Weboberfläche](images/addon-mobile.png)

- [Private Testinstallation](Private-Testinstallation.md)
- [Spätere HACS-Veröffentlichung](HACS-Veröffentlichung.md)
- [Automationen](Automationen.md)
- [Fehlerbehebung](Fehlerbehebung.md)
