# Richtlinie für Business Continuity 

| |                                                    |
|-----|---------------------------------------------   |
| Version: | 0.5                                       |
| Version vom: | 26.06.2026                            |
| Erstellt durch: | Alex Walender                      |
| Genehmigt am: | 29.06.2026 (sa), 30.06.2026 (as)     |
| durch: | Stefan Albaum (sa), Alexander Sczyrba (as)  |

# ChangeLog

- Version 0.5 vom 26.06.2026: Wechsel Threema -> Signal. Bessere Defintion von Kommunikationen.
- Version 0.4 vom 11.03.2025: Aufrechterhaltung der Informationssicherheit bei Störungen.
- Version 0.3 vom 08.02.2024: Beschreibung der möglichen Betriebszustände, Kontaktmöglichkeiten.
- Version 0.2 vom 05.02.2024: Definition einer Handlungsunfähigkeit.
- Version 0.1 vom 14.04.2021: initialer Entwurf.

# Zweck, Anwendungsbereich und Anwender

Die Richtlinie zur _Business Continuity_ kontrolliert
die auf den Geltungsbereich dieses ISMS abgestimmte
Einhaltung der IT-Sicherheit im Krisenfall.

Die de.NBI Cloud Bielefeld untersteht hierbei den
Krisenmanagementprozessen der Universität Bielefeld,
welche von der Universitätsleitung und der zuständigen
Stabstelle AGUS (Arbeits-, Gesundheits- und Umweltschutz) gepflegt
werden. Diese Prozesse sind außerhalb dem Geltungsbereichs des ISMS.

Letztendlich bedarf es einer Erweiterung der schon existierenden
Krisenmanagementprozesse um Aspekte der IT-Informationssicherheit,
welche innerhalb des Geltungsbereiches der de.NBI Cloud
Bielefeld definiert worden sind.

Ziel ist die Aufrechterhaltung der definierten Informationssicherheitsziele 
auf einem entsprechend hohen Niveau trotz einer akuten Krise.
Hierzu enthält diese Richtlinie entsprechende Informationen zur
schnellstmöglichen Wiederherstellung kritischer Geschäftsprozesse,
unabhängig von der Auswirkung oder der Tragweite der Krise/Katastrophe.

Sämtlichen Mitarbeitern der de.NBI Cloud Bielefeld
muss bewusst sein, dass zu jeder Zeit unerwartete Ereignisse unsere
Geschäftsprozesse und die definierten Ziele unserer
IT-Sicherheitsleitlinie gefährden können.

# Planung der Informationssicherheit Kontinuität

## Definition unterschiedlicher Betriebszustände

### Normalbetrieb

Ein Normalbetrieb ist gegeben, wenn alle Prozesse störungsfrei
funktionieren. Indikatoren dafür sind keine Störungsmeldungen
in den Monitoring-Systemen, keine offenen Sicherheitsvorfällen
und keine unbeantworteten Support-Mails die auf grundlegende
Störungen im System hinweisen könnten.
Dies ist der anzustrebende Zustand.

### Angekündigte Wartung

Bei unvermeidbaren Wartungsarbeiten, welche die Verfügbarkeit von Diensten
beeinträchtigen, müssen diese mit ausreichend Zeit
bei den Nutzern vorangekündigt werden. Als Richtlinie gilt hierbei mindestens
ein Monat. In Ausnahmefällen darf die Vorlaufzeit verkürzt werden wenn
die Informationssicherheit unmittelbar gefährdet ist und ein schnelles
Handeln erforderlich ist um Risikoereignisse zu vermeiden.

### Störung

Eine Störung tritt auf, wenn ein unerwartetes Ereignis oder eine 
unvorhergesehene Situation eintritt, die die normale Funktionsweise der 
IT-Infrastruktur beeinträchtigt.

Störungen sind nicht Teil der Pläne bezüglich der Informationssicherheit Kontinuität.

Beeinträchtigungen könnten sein:

- Keinen oder erschwerten Zugriff auf Nutzer-VMs
- Keinen oder erschwerten Zugriff auf Daten des Storage-Systems.
- Keinen oder erschwerten Zugriff auf die API der OpenStack-Installation.

Dies kann durch Hardwarefehler, Softwarefehler,
Konfigurationsprobleme oder menschliche Fehler verursacht werden.
Störungen können dazu führen, dass bestimmte Systeme, Dienste oder Anwendungen 
für eine Anzahl an Nutzern vorübergehend nicht verfügbar sind oder mit 
verminderter Leistung arbeiten.

Bei der Entdeckung einer Störung durch einem Mitarbeiter, ist dieser
umgehend dazu aufgefordert die Störung mit einem weiteren Mitarbeiter (4-Augen-Prinzip)
zu bearbeiten.

### Notfall

Ein Notfall ist ein schwerwiegender Vorfall, der die Verfügbarkeit oder 
Integrität der IT-Infrastruktur bedroht und dringende Maßnahmen erfordert,
um die Auswirkungen zu minimieren und den Betrieb wiederherzustellen. 
Notfälle können durch Naturkatastrophen, Sicherheitsverletzungen, 
schwerwiegende Hardwareausfälle oder andere Ereignisse verursacht werden,
die einen sofortigen Eingriff erfordern.

Bei der Entdeckung eines Notfalls ist die obere Leitung und sämtlichen
Mitarbeitern zu kontaktieren. Die Behebung des Notfalls hat höchste
Priorität.

### Krise

Eine Krise liegt dann vor, wenn ein Vorfall (in Teilen oder gänzlich) die Funktionalitäten
bzw. Leistungen der Universität oder der de.NBI Cloud verhindert.

Ein Vorfall zeichnet sich in der Regel durch folgende Eigenschaften aus:

- Es existieren akut gravierende Gefahren für Leib und Leben, der eigentlichen
  Einrichtung oder deren Reputation.
- Der Vorfall wird unvermeidlich eintreten und besitzt im Vorfeld das Potenzial
  sämtliche Geschäftsprozesse zu unterbinden.

Beispiele für solche Vorfälle sind unter anderem:

- [Großflächiger Brand](https://www.reuters.com/article/us-france-ovh-fire-idUSKBN2B20NU)
- Ausbruch einer [Pandemie](https://www.cdc.gov/coronavirus/2019-nCoV/index.html)
- Gravierende Auswirkungen einer [Hacker-Attacke](https://www.hessenschau.de/panorama/moeglicher-hackerangriff-legt-uni-giessen-lahm,uni-giessen-vom-netz-100.html)

Identifiziert eine Person die Anbahnung bzw. den Eintritt einer Krise,
welche sämtliche Geschäftsprozesse der Cloud bedroht, meldet sie dies
umgehend der obersten Leitung.
Ist akut eine Gefahr für Leib oder Leben gegeben, so sind die [Notfallmaßnahmen](https://www.uni-bielefeld.de/themen/hilfe-notfall/)
der Uni Bielefeld einzuhalten.

Die oberste Leitung koordiniert hierbei die Kommunikation der Mitarbeiter
und stellt bei Notwendigkeit den Kontakt zu entsprechenden Stellen auf:

- Stabsstelle [AGUS](https://www.uni-bielefeld.de/einrichtungen/agus/)
- Stabsstelle [Datenschutz und Informationssicherheit](https://ekvv.uni-bielefeld.de/pers_publ/publ/EinrichtungDetail.jsp?orgId=124130908)

Je nach Krise werden die Vorfälle durch die Stabsstellen der Universität Bielefeld 
weiter eskaliert, beispielsweise:

- Polizei, Landeskriminalamt, Bundeskriminalamt
- Aufsichtsbehörden
- usw.

Den Anweisungen der Stabsstellen ist Folge zu leisten. Die oberste Leitung der de.NBI Cloud Bielefeld
koordiniert und protokolliert hierbei gemeinsam mit den Mitarbeitern das weitere Vorgehen.

## Definition Handlungsunfähigkeit

Eine Handlungsunfähigkeit ist gegeben, wenn primäre Geschäftsprozesse aufgrund von
externen Ursachen oder Krisen nicht mehr aufrechterhalten werden können.

Im Konkreten Fall beinhaltet das:

- Die Außenanbindung ist ausgefallen.
- Es existieren nicht genügend Mitarbeiter um den Wiederanlaufplan fortzuführen.
- Die Verfügbarkeit bzw. Lieferung von essentiellen Komponenten ist eingeschränkt.
- Räumliche Kapazitäten sind nicht (mehr) gegeben, mitsamt dazugehörigen Komponenten.
  - Energie / Kühl-Versorgung
  - Netzwerkgerätschaften sowie Anbindungen

## Universitätsweiter Plan der _Business Continuity_

Die Leitung der Universität Bielefeld bzw. die AGUS unterhalten ein
allgemeingültiges Krisenmanagement, welche für sämtliche Bereiche
der Universität gilt. Dementsprechend gilt dieses Krisenmanagement auch
für die de.NBI Cloud Bielefeld.

## Spezifische Pläne der de.NBI Cloud Bielefeld

Folgende Maßnahmen der de.NBI Cloud Bielefeld sind in Kraft, um die
Geschäftsprozesse und Ziele der Informationssicherheit während einer
Krise aufrechtzuerhalten:

- **Nutzer werden umgehend kontaktiert.** Ist die Aufrechterhaltung der 
  Geschäftsprozesse bezüglich der Cloud-Nutzer gefährdet, 
  so werden diese umgehend und umfassend darüber unterrichtet.
- **Nutzer werden Alternativen angeboten**. Wenn dieser Standort die
  Geschäftsprozesse nicht mehr aufrechterhalten kann, so wird der
  Kontakt zur _de.NBI Cloud Governance_ aufgebaut. Nutzer können dadurch kurzfristig
  Compute und Storage-Ressourcen bei anderen de.NBI Cloud Standorten erhalten.
- **Nutzer können Cloud-Daten extrahieren**. In einigen Fällen kann dem Nutzer angeboten
  werden, Zugriff auf extrahierte Daten der Cloud zu bekommen. Dies kann jedoch
  nicht immer gewährleistet werden und hängt von der Auswirkung der Krise ab.
- **Backup-Prozesse der de.NBI Cloud Bielefeld.** Die de.NBI Cloud Bielefeld besitzt
  Backups der kritischen Infrastruktur und kann somit die Wiederaufnahme der
  Geschäftsprozesse beschleunigen.
- **Remote-Zugriff und Heimarbeit auf der Infrastruktur sind gewährleistet.** 
  Ist das Hauptgebäude der Universität Bielefeld nicht betretbar, so haben die Mitarbeiter dennoch
  eine Möglichkeit die Geschäftsprozesse und Ziele der Informationssicherheit
  aufrechtzuerhalten durch entsprechende Regelungen (Heimarbeit) und Technologien
  (Remote-Zugriffe).
  
Die praktische Umsetzung der Maßnahmen ist im Katalog der IT-Verfahren dokumentiert.
Die Umsetzung erfolgt durch die `ADM`-Gruppe.

Diese Verfahren unterliegen dem jährlichen Review-Prozess.

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen
und weisen die Mitarbeiter ggf. auf Defizite hin.**

## Aufrechterhaltung der Informationssicherheit

Unabhängig vom Schweregrad des Ereignisses hat die
Aufrechterhaltung der Informationssicherheit oberste Priorität.
Um ein hohes Schutzniveau beizubehalten, sind die folgenden Maßnahmen
mitsamt ihren IT-Verfahren zu befolgen:

- Notwendige Dienste werden regelmäßig gesichert und ihre Wiederherstellung
  geübt, sodass diese bei schwerwiegenden Störungen schnell wieder
  Betriebsbereit sind.
- Dazugehörige Notfallpläne sind verfasst, aktuell und regelmäßig überarbeitet
  bzw. überprüft.
- (Sicherheits-)Vorfälle werden entsprechend dokumentiert, analysiert und bearbeitet.
- Die Zugriffs- und Berechtigungskontrolle ist nach dem "Least-Privilege" Schema
  angelegt, sodass bei Störungen die Anzahl an Zugriffsvektoren minimiert wird.
- Sämtliche Nutzerdaten sind nach modernen Standards verschlüsselt, sodass
  beispielsweise bei Störungen der Schließsysteme keine Informationen an unbefugte zugänglich
  gemacht werden.
- Systeme werden dauerhaft auf Fehler und unbefugtes Eindringen überwacht. Die Administratoren
  werden umgehen benachrichtigt, auch bei akuten Ereignissen.
- Mitarbeiter sind sensibilisiert zum Thema der Informationssicherheit und bilden sich
  durchgehend fort.

## Kommunikation

### Kommunikation mit den Nutzern bei Ereigniseintritt

Die Nutzer der Dienste sind bei Änderungen des Betriebszustands, über die entsprechenden
IT-Verfahren, zu benachrichtigen. Inhalte der Benachrichtigung sind:

- Beschreibung des Ereignis
  - Wartung, Störung, Notfall ect.
- Geschätzte Dauer des Ereignisses
- Updates zu bestehenden Ereignissen
- Möglichkeit zur Kommunikation mit den Administratoren anbieten

Bei angekündigten Wartungen wird die Ankündigung wiederholt versendet.
Ist die Vorankündigung einer Wartung auf einen Monat angesetzt, so erfolgt
die wiederholte Benachrichtigung eine Woche vor Eintritt, sowie ein Tag davor.

### Kommunikatioskanäle Mitarbeiter

Sämtliche Mitarbeiter stehen im Kontakt durch sichere und externe Kanäle.
Mitarbeiter sind dazu angehalten [Signal](https://signal.org) zu verwenden
und sich der Administratoren-Gruppe anzuschließen. Die Einladung
in die entsprechende Signal-Gruppe kann jeder in der Gruppe ADM durchführen.

## Übungen bezüglich der Notfallabschaltung und des Disaster-Recoverys

Im jährlichen Rythmus wird die Notfallabschaltung und das Einspielen
der Backups in einem blanken System geübt und gegebenenfalls
die IT-Verfahren dazu überarbeitet.

Ein Protokoll ist in [REDO-22](https://yt.bi.denbi.de/issue/REDO-22/Ubungen-zu-Disaster-Recovery-und-Notfallabschaltung)
festzuhalten.
