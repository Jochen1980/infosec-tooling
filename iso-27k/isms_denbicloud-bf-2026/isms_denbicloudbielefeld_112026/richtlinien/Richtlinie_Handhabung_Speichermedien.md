# Richtlinie für die Handhabung von Speichermedien 

|                 |                                             |
|-----------------|---------------------------------------------|
| Version:        | 0.1                                         |
| Version vom:    | 15.12.2023                                  |
| Erstellt durch: | Jan Krüger                                  |
| Genehmigt am:   | 06.03.2024 (alu), 12.03.2024 (as)           |
| durch:          | Alexander Sczyrba (as), Stefan Albaum (alu) |

## ChangeLog

- Version 0.1 vom 15.12.2023: initialer Entwurf

## Referenzen

- [Klassifikation und Kennzeichnung von Informationen](Klassifizierung_Kennzeichnung_von_Informationen.md)
- [Gebrauch von kryptographischen Maßnahmen](Gebrauch_von_kryptographischen_Maßnahmen.md)
- [Merkblatt zur sicheren Datenträgerentsorgung](FZJ/Datentraegerentsorgung-Merkblatt.pdf)

## Zweck, Anwendungsbereich und Anwender

Diese Richtlinie für die Handhabung von Speichermedien soll sicherstellen, dass
alle Speichermedien ordnungsgemäß behandelt und verwaltet werden, um die Sicherheit 
und Integrität der darauf gespeicherten Informationen zu gewährleisten.

Speichermedien im Sinne dieser Richtlinie sind die in den Servern sowie
den mobilen IT-Geräten (Notebooks) fest verbauten HDDs/SSDs
sowie entfernbare Speichermedien wie Speicherkarten, USB-Sticks und
externe Festplatten.

### Registrierung

Alle Speichermedien sind vor der Nutzung zu erfassen.
Ist durch Art und Zweck der Verwendung des Speichermediums nicht gegeben, welche Personen für die Verwendung des 
Mediums autorisiert sind (gegeben ist dies beispielsweise für festverbaute Speichermedien oder Speichermedien in mobilen IT-Geräten), 
so sind die berechtigten Personen ebenfalls zu erfassen. 

### Kennzeichnung

Nach der Richtlinie zur Klassifikation und Kennzeichnung von Informationen
sind Speichermedien gemäß ihrer Vertraulichkeitsstufe
äußerlich gut sichtbar zu kennzeichnen. Fest 
verbaute Datenträger (z.B. in Servern oder Notebooks) sind erst beim Ausbau aus diesen 
entsprechend zu kennzeichnen.
Werden Daten mit höherer Vertraulichkeitsstufe als auf der Kennzeichnung des Speichermediums angegeben
auf das Gerät übertragen, muss die entsprechende Kennzeichnung umgehend angepasst werden.

### Handhabung und Transport

Je nach Art des Speichermediums sollte sichergestellt sein, dass keine großen Kräfte auf dieses einwirken.
Der Datenträger sollte von Flüssigkeiten und Magneten ferngehalten werden sowie
keinen extremen Witterungsverhältnissen ausgesetzt sein (wie etwa Temperatur, Luftfeuchtigkeit).
Die Spezifikationen für Betrieb, Transport und Lagerung des Datenträgers
sind in jedem Fall einzuhalten.

Um das Risiko von Datenverlust bei sichtbarer Alterung/Degradation des physikalischen
Speichermediums zu mindern, wird empfohlen, die Informationen auf ein frisches
Speichermedium zu übertragen, bevor das ursprüngliche Medium unlesbar wird.

Für den Transport sind geeignete Maßnahmen zum Schutz des Datenträgers zu
treffen. Datenträger mit Inhalten der Vertraulichkeitsstufe K3 oder
höher dürfen nur durch mindestens 2 Personen
(4-Augen-Prinzip) transportiert werden. Datenträger der Stufe K4 darüber hinaus nur
in einem abschließbaren Behälter.

Einmal in Betrieb genommene, fest eingebaute Datenträger dürfen das Datacenter
nur verlassen, wenn sichergestellt ist, dass auf den Inhalt nicht zugegriffen
werden kann (Verschlüsselung) oder der Inhalt sicher gelöscht ist.
Eine Ausnahme stellt der Transport zwischen den Datenzentren der Einrichtung
unter den oben genannten Bedingungen dar.

### Sicherheit und Zugriffskontrolle

Der Zugriff auf Speichermedien sollte auf die jeweiligen autorisierten Mitarbeiter
beschränkt sein.

Unabhängig von der Vertraulichkeitsstufe der auf dem Speichermedium hinterlegten
Informationen sind Speichermedien in mobilen IT-Geräten (Notebooks) bzw.
mobile Datenträger die zu Backupzwecken genutzt werden (z.B. externe Festplatten)
grundsätzlich zu verschlüsseln.

Die Vertraulichkeitsstufe der auf dem Datenträger enthaltenen Informationen
entscheidet über die Art der Verwahrung. Datenträger sind immer unabhängig
von der Vertraulichkeitsstufe in einem abschließbaren Raum aufzubewahren,
Datenträger der Stufe K3 und höher darüber hinaus in einem abschließbaren
Behälter. Als abschließbarer Behälter gelten auch gesondert abschließbare
Vorbereitungsräume.

Speichermedien/Datenträger mit Information der Vertraulichkeitsstufe 2 oder höher
dürfen nur nach Absprache mit dem Vorgesetzten mit einem Postdienstleister 
verschickt werden. Es sollten geeigneten Maßnahmen eingesetzt werden um die
Vertraulichkeit (Verschlüsselung!) und Integrität (Prüfsummen!) der 
Information zu wahren.

### Backup und Redundanz

Kritische Daten auf Speichermedien sollten regelmäßig gesichert werden. Es sollte 
redundante Kopien wichtiger Informationen auf unterschiedlichen Speichermedien geben.

### Entsorgung, Wiederverwendung und Umgang mit beschädigten Geräten

Veraltete oder nicht mehr benötigte Speichermedien müssen sicher entsorgt werden.
Sollte für die Entsorgung ein externer Dienstleister genutzt werden, ist sicherzustellen,
dass dieser die Anforderungen im Hinblick auf notwendige Sicherheitsmaßnahmen erfüllt.

Vor der Entsorgung der Speichermedien sind die Daten auf den Speichermedien sicher zu löschen, 
insofern die Art der Entsorgung des Speichermediums nicht hinreichend sicherstellt, 
dass ein Zugriff auf die Daten auf dem entsorgten Medium ausgeschlossen ist.

Bei Wiederverwendung von Speichermedien ist durch Maßnahmen wie etwa das sichere Löschen sicherzustellen, 
dass kein Zugriff auf sensible Daten durch nicht dafür autorisierte Personen erfolgt.

Die Entsorgung sowie Wiederverwendung von Speichermedien ist entsprechend zu protokollieren.

Sind Speichermedien beschädigt, 
ist anhand der Vertraulichkeitsstufe der darauf gespeicherten Daten zu entscheiden,
ob eine Reparatur oder Entsorgung des Geräts vorgenommen wird.

Siehe außerdem das [Merkblatt zur sicheren Datenträgerentsorgung](FZJ/Datentraegerentsorgung-Merkblatt.pdf).

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen
und weisen die Mitarbeiter ggf. auf Defizite hin.**
