# Richtlinie für Maßnahmen für Audits von Informationssystemen

| | |
|-----|----|
| Version: | 0.2                                        |
| Version vom: | 24.03.2025                             |
| Erstellt durch: | Jan Krüger                          |
| Genehmigt am: | 11.04.2025 alu, as                    |
| durch: | Alexander Sczyrba (as), Stefan Albaum (alu)  |

# ChangeLog

- Version 0.2 vom 24.03.2025 : IT-Basisschutz nicht mehr gegeben.
- Version 0.1 vom 26.05.2021 : initialer Entwurf

# Zweck, Anwendungsbereich und Anwender

Durch die Richtlinie für Maßnahmen für Audits von Informationssystemen soll 
sichergestellt werden, dass die Dienste der Cloud-Infrastruktur und die 
öffentlichen erreichbaren virtuellen Instanzen der Kunden in regelmäßigen 
Abständen auf Schwachstellen getestet werden, um einem möglichen 
Sicherheitsvorfall vorzubeugen. 

Der Anwendungsbereich dieser Richtlinie umfasst die de.NBI Cloud Bielefeld. 
Die Anwender sind alle Mitarbeiter von ADM und BRF.

## Infrastruktur

Die öffentlich zugänglichen Dienste der Cloud-Infrastruktur müssen in regelmäßigen
Abständen auf (bekannte) Schwachstellen geprüft werden. Hierfür gelten die folgenden
Regeln:

- Die Schwachstellen-Prüfung muss grundsätzlich **immer** mit der Leitung abgesprochen
  werden.
- Der Umfang einer Schwachstellen-Prüfung muss festgelegt und nachvollziehbar sein.
- Der reguläre Betrieb darf durch die Schwachstellen-Prüfung nicht gefährdet werden und 
  sollte – wenn möglich – außerhalb der Hauptnutzungszeiten durchgeführt werden.
- Sämtliche Zugriffe müssen überwacht und protokolliert werden.
- Die Schwachstellen-Prüfung darf den zu überprüfenden Zielhost nicht verändern
  (nur lesen).
- Über neu detektierte Schwachstellen werden die Administratoren automatisch per E-Mail
  benachrichtigt.

## Virtuelle Instanzen

Neben den Regeln für das Audit der Infrastruktur gilt für das Scannen von öffentlich
erreichbaren Kundeninstanzen darüber hinaus folgendes:

- Die Kunden müssen darüber in Kenntnis gesetzt werden, dass öffentlich erreichbare
  virtuelle Instanzen in regelmäßigen Abständen auf Schwachstellen getestet werden.
- Gefundene Schwachstellen mit geringem oder mittlerem Gefährdungspotential sind 
  durch die Mitarbeiter von ADM/BRF auf ihre Dringlichkeit zu beurteilen und die 
  betroffenen Kunden zeitnah zu informieren.
- Sicherheitslücken mit einem hohen Gefährdungspotential berechtigen die Mitarbeiter 
  von ADM/BRF dazu, die betroffenen virtuellen Instanzen sofort vom Netz zu trennen. Sowohl der
  Kunde, als auch die Leitung sind im Nachgang zu informieren.

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen
und weisen die Mitarbeiter ggf. auf Defizite hin.**
