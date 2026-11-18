# Richtlinie für das Identitätsmanagement 

|                   |                                             |
|-------------------|---------------------------------------------|
| Version:          | 0.1                                         |
| Version vom:      | 10.01.2024                                  |
| Erstellt durch:   | Jan Krüger                                  |
| Genehmigt am:     | 06.03.2024 (alu), 12.03.2024 (as)           |
| durch:            | Alexander Sczyrba (as), Stefan Albaum (alu) |

# ChangeLog

- Version 0.1 vom 10.01.2024: initialer Entwurf

# Zweck, Anwendungsbereich und Anwender

Die Identitäten von Personen und Entitäten sind von entscheidender Bedeutung
für die Sicherheit und Integrität der Informationssysteme. Die effektive
Verwaltung von Identitäten bildet das Fundament eines robusten 
Informationssicherheitsmanagementsystems (ISMS). Diese Richtlinie zum 
Identitätsmanagement legt die Grundsätze, Verfahren und Verantwortlichkeiten 
fest, um sicherzustellen, dass Identitäten in unserer Organisation sicher 
und effizient erstellt, verwaltet, aktualisiert und beendet werden.

Der Zweck des Dokuments ist es, sicherzustellen, dass Identitäten angemessen 
und risikobasiert verwaltet werden, um den Schutz unserer Informationen, 
Systeme und Ressourcen zu gewährleisten. Diese Richtlinie dient als Leitfaden
für alle Mitarbeiter, Dienstleister und sonstigen berechtigten Nutzer, 
um sicherzustellen, dass Identitätsmanagementprozesse den höchsten 

# Referenzen

- ISO 27001/27002 A5.16
- [Richtlinie zur Authentifizierung](Richtlinie_Authentifizierung.md)
- [Richtlinie zur Erteilung von Zugangsrechten](Richtlinie_Zugangsrechte.md)

# Identitätsmanagement

## Grundsätze des Identitätsmanagements

Eine Identität sollte nur mit einer Person bzw. Entität verknüpft sein. Identitäten,
die mehreren Personen zugeordnet sind, sind nur zulässig, wenn diese für den Betrieb
unabdingbar sind (z.B. Notfall Identität). Nicht mehr benötigte Identitäten werden 
deaktiviert oder entfernt. Innerhalb einer Domäne darf es keine doppelten Identitäten
geben.

## Verantwortlichkeiten und Rollen im Identitätsmanagement

Es muss eine klare Zuweisung von Verantwortlichkeiten für Identitätsmanagementprozesse
und -aufgaben, sowie eine Festlegung von Rollen, wie Identitätsverwalter, Genehmigungsinstanzen
und Überwachungsverantwortliche geben.

Eine Rollentrennung sollte angestrebt werden, sofern die Struktur der Organisation dies
zulässt.

## Identitätsverifikation und Authentifizierung

Bei der Verifikation einer Identität muss sichergestellt werden, das diese nur mit
einer Person verknüpft ist. Ausnahmen von der Regel sind Identitäten, die für
Betrieb unbedingt erforderlich sind, wie z.B. ein lokaler Notfallaccount oder ein Service
Account.
Das Feststellen einer Identität muss mit einem dafür geeigneten als sicher geltenden
Verfahren (z.B. Video-Ident) durchgeführt werden.

Die Authentifizierung von Identitäten sollte der Richtlinie zur Authentifizierung
folgen.

## Autorisierung und Zugriffskontrolle

Die Zugriffskontrolle muss der Richtlinie für Zugangsrechte folgen.

## Protokollierung

Änderungen (Hinzufügen, Löschen und Anpassen von Identitäten) sind zu
protokollieren.

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen
und weisen die Mitarbeiter ggf. auf Defizite hin.**
