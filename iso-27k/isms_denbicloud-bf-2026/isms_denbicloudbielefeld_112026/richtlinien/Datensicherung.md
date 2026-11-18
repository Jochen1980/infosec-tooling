# Richtlinie zur Sicherung von Daten 

| |                                             |
|-----|---------------------------------------------|
| Version: | 1.1                                         |
| Version vom: | 22.03.2021                                  |
| Erstellt durch: | Jan Krüger, Viktor Rudko                    |
| Genehmigt am: | 12.03.2024 (as), 11.04.2025 (alu)                  |
| durch: | Alexander Sczyrba (as), Stefan Albaum (alu) |

# ChangeLog

- 1.1 vom 08.03.2024: Anpassung an 27001:2022
- 1.0 vom 21.04.2021
- DRAFT vom 22.03.2021 : initialer Entwurf

# Zweck, Anwendungsbereich und Anwender

Die Richtlinie zur Sicherung von Daten soll dem Verlust von Daten vorbeugen.
Der Verlust von Daten kann erhebliche Auswirkungen auf die Geschäftstätigkeit 
haben. Sind Anwendungsdaten oder Kundendaten verloren oder verfälscht, kann 
dies für ein Unternehmen existenzbedrohend sein oder zumindest das öffentliche
Ansehen schädigen.

Die Gründe für den Verlust gespeicherter Daten können vielfältiger Art sein:

- Zerstörung von Datenträgern durch höhere Gewalt wie z. B. Feuer
- Versehentliches Löschen oder Überschreiben von Dateien
- Vorsätzliches oder versehentliches Setzen von Löschmarkierungen in Archivsystemen
- Fehlerhafte Datenträger 
- Unkontrollierte Veränderungen gespeicherter Daten 
- Datenzerstörung durch Computer-Viren

Ein kompletter Ausschluss der aufgeführten Risiken ist nahezu unmöglich, sodass Maßnahmen
ergriffen werden müssen, welche die Folgen eines Datenverlusts mindern. Eine Datensicherung
soll gewährleisten, dass der IT-Betrieb kurzfristig wieder aufgenommen werden kann, falls
Daten *verloren* gehen.

Der Anwendungsbereich dieser Richtlinie ist die de.NBI Cloud Bielefeld. Die Anwender
sind alle Mitarbeiter von ADM und BRF.

## Richtlinien der de.NBI Cloud Bielefeld

- [Gebrauch von kryptographischen Maßnahmen](Gebrauch_von_kryptographischen_Maßnahmen.md)
- [Klassifikation und Kennzeichnung von Informationen](Klassifizierung_Kennzeichnung_von_Informationen.md)
- [Richtlinie und Verfahren zur Informationsübertragung](Informationsuebertragung.md)

## Richtlinien der Universität Bielefeld

- [Informationssicherheitsleitlinie](UniBi/2019-06-14_Informationssicherheitsleitlinie_Universitat_Bielefeld.pdf)

# Grundsätzliches

Die de.NBI Cloud Bielefeld nimmt zur Datensicherung den zentralen Datensicherungsdienst
des Rechenzentrums der Universität Bielefeld über die BRF in Form von zwei virtuellen
Tape-Libraries in Anspruch. Die beiden Tape-Libraries sind jeweils in einem anderen
Gebäude (anderer Brandabschnitt) verortet.

Datensicherungen sollten generell automatisiert ablaufen. In Abhängigkeit der zu sichernden 
Daten sind diese gemäß der Richtlinie zur Kennzeichnung und Klassifikation von Daten zu
behandeln (z.B. Verschlüsselung der Sicherungskopie).

# Durchführung von Datensicherungen

Bei der Durchführung einer Datensicherung werden Daten über ein Netz übertragen. Zum Zeitpunkt
der Datensicherung ist eine ausreichende Datenübertragungskapazität sicherzustellen. Es ist zu
verhindern, dass die Daten während der Übertragung unbefugt mitgelesen, kopiert oder manipuliert
werden. In Abhängigkeit vom Schutzbedarf ist eine geeignete Verschlüsselung zu benutzen.
Das entsprechende [IT-Verfahren für Backups](../it-verfahren.md#it-18-backup) ist anzuwenden.

# Kontrolle der Datensicherung

Der Verantwortliche für die Datensicherung muss regelmäßig überprüfen, ob die Datensicherung
tatsächlich korrekt durchgeführt wurde. Besonders bei automatischen Prozeduren ist diese 
Prüfung notwendig. Prüfpunkte können dabei die Auswertung von Logdateien und 
Fehlerprotokollen, das Datum der Sicherungsdatei, die Stichprobenprüfung der Dateiinhalte, 
die Plausibilität der Dateigröße etc. sein. In Einzelfällen, z. B. wenn kryptographische 
Verfahren eingesetzt werden, kann ein Dateivergleich notwendig sein.

## Übungen zur Datenrekonstruktion

Für die Rekonstruktion eines Datenbestandes muss geprüft werden, ob mit den vorhandenen
Sicherungskopien der Daten ein solches Vorhaben durchgeführt werden kann. Technische Defekte,
falsche Parametrisierung, eine unzureichende Datenträgerverwaltung o. ä. können eine 
Rekonstruktion von gesicherten Daten unmöglich machen. Die Rekonstruktion von Daten mit 
Hilfe von Datensicherungsbeständen muss auf jeden Fall nach jeder Änderung des 
Datensicherungsverfahrens getestet werden. Hierbei 
ist sicherzustellen, dass eine vollständige Datenrekonstruktion möglich ist.

## Revision

Die Erkenntnisse aus den Übungen sollten dazu verwendet werden, das Datensicherungskonzept
zu verbessern.

# Verfahren zur Wiederherstellung

Wiederherstellungsverfahren müssen als Prozesse (zum Beispiel als IT-Verfahren) dokumentiert 
werden.

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen
und weisen die Mitarbeiter ggf. auf Defizite hin.**
