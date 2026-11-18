# Informationssicherheitsrichtlinie für den Umgang mit Lieferantenbeziehungen 

| | |
|-----|----|
| Version: | 1.1  |
| Version vom: | 11.05.2021 |
| Erstellt durch: | Jan Krüger, Christian Henke, Alex Walender |
| Genehmigt am: | 07.02.2021 (as), 09.12.2021 (alu) |
| durch: | Alexander Sczyrba (as), Stefan Albaum (alu)|

# ChangeLog

- Version 1.1 vom 11.05.2021: Hinweis zu verschlüsselten Datenträgern.
- Version 1.0 vom 21.04.2021
- DRAFT vom 12.03.2021 

# Zweck, Anwendungsbereich und Anwender

Der Zweck dieser Richtlinie ist die Festlegung von Vorschriften für die 
Kommunikation mit bzw. Beziehungen zu Lieferanten. Dieses Dokument gilt 
für all jene Lieferanten, welche die Vertraulichkeit, Integrität und
Verfügbarkeit schützenswerter Informationen der de.NBI Cloud 
Bielefeld beeinflussen können. Schützenswerte Informationen sind alle
Informationen die nach der Richtlinie zur Kennzeichnung und
Klassifikation von Information als intern, vertraulich oder streng
vertraulich gekennzeichnet sind. 

Anwender dieser Richtlinie sind alle Mitarbeiter von ADM und BRF, welche 
für die Ausrichtung von Ausschreibungen verantwortlich sind, sowie
die Leitung von ADM und BRF als Gesamtverantwortliche.

# Arten der Lieferanten

Die de.NBI Cloud Bielefeld unterscheidet zwischen folgenden Lieferanten:

- Lieferanten von IT-Infrastruktur-Komponenten
- Berater- und Supportleistungen zur Unterstützung und Verbesserung des Betriebs

# Lieferantenbeziehungen 

Beziehungen zu einem Lieferanten kommen entweder über die im öffentlichen Sektor 
üblichen Ausschreibungsverfahren oder
eine direkte Beauftragung von bisherigen Lieferanten zustande. 
Die Bewertung im Falle des Auschreibungsverfahrens erfolgt über festgelegte Kriterien,
die dann auch immer von der jeweiligen Beschaffungsabteilung überprüft und
durchgeführt werden.

Alle Lieferantenbeziehungen werden tabellarisch im ISMS
mit Name und Anschrift des Lieferanten, Art, Beginn und Ende der Beziehung 
und einem Verweis auf die dazugehörige Dokumentation (Ausschreibungsunterlagen,
EVB-IT Vertrag, AV-Vertrag usw.) gepflegt (siehe [Lieferanten](../aufstellungen/lieferanten.md)).

# Zugriff auf Informationen

Der Zugriff auf Informationen der de.NBI Cloud Bielefeld ist als Einrichtung der
öffentlichen Hand grundsätzlich über einen EVB-IT-Vertrag und dessen AGBs geregelt. 
Je nach Art der Lieferantenbeziehung unterscheiden sich sowohl Vertragsinhalt als auch AGBs.
Der EVB-IT-Vertrag wird bei Berater- und Supportleistungen durch einen AV-Vertrag,
eine tiefergehende Vertraulichkeitserklärung und eine
[Verpflichtung zur Informationssicherheit](../dienstvereinbarungen/Verpflichtungserklärung_Informationssicherheit_Auftragnehmer.md)
ergänzt.

## Lieferanten von IT-Infrastruktur-Komponenten

Hardwarelieferanten haben grundsätzlich **keinen** Zugriff auf interne (oder vertrauliche)
Informationen der de.NBI Cloud Bielefeld. Die Installation (sofern Teil der Ausschreibung)
und Vor-Ort-Wartung erfolgt gemäß
[A7.2](../erklaerung-zur-anwendbarkeit.md#a72-physischer-zutritt). Muss die Hardware 
zur Reparatur zum Lieferanten zurückgeschickt werden, geschieht dies ohne Datenträger bzw. nur
nach sicherer Löschung der Datenträger. 
Ist es nicht möglich, die Datenträger der zu reparierenden Hardware auszubauen, 
so ist sicherzustellen, dass die Datenträger mittels robuster Kryptographie
verschlüsselt worden sind. Alternativ sind die Datenträger sicher zu löschen.
Die Zugangsdaten zum Service-Prozessor werden zuvor ebenfalls zurückgesetzt. 
Bei der Ausschreibung von Hardware ist zwingend darauf zu achten, dass für Wartungsverträge
defekte Datenträger nicht zum Lieferanten zurückgeschickt werden müssen (Hard-Drive-Retention). 
Die Hardware (Server, Storage, Netzwerk) **muss** zur physikalischen Trennung von Wartung
und Betrieb einen separaten Netzwerkanschluss zum Service-Prozessor haben. Die Hardware **muss**
Sensoren zur Überwachung haben (Temperatur, Intrusion Detection, Power, usw), welche vom
Service-Prozessor über eine standardisierte Schnittstelle (IPMI, Redfish) zur
Überwachung abgefragt werden können.

## Berater- und Supportleistungen

Lieferanten von Services (z.B. Support beim Betrieb der Cloud-Infrastruktur, Beratung) 
bekommen in Abhängigkeit der Dienstleistung eingeschränkten Zugriff auf die Infrastruktur 
und damit auf interne (oder auch vertrauliche) Informationen der de.NBI Cloud Bielefeld. Im
AV-Vertrag **muss** festgelegt werden, auf welche Informationen der Lieferant Zugriff 
bekommt. Vertrauliche oder streng vertrauliche Informationen
dürfen **nicht** auf der Infrastruktur des Dienstleisters bearbeitet oder gespeichert werden.
Der Dienstleister muss mit der geltenden Richtlinie zur _Klassifikation und Kennzeichnung von 
Informationen_ vertraut sein um mit internen, vertraulichen sowie streng 
vertraulichen Informationen _richtig_ umzugehen.

Der Zugriff auf die Infrastruktur der de.NBI Cloud Bielefeld erfolgt ausschließlich über
einen separaten Jump-Host mit personalisierten Accounts, die auf der Infrastruktur gegebenenfalls 
mit erweiterten Rechten (z.B. `sudoers`) ausgestattet sind.
Die Vertraulichkeitserklärung regelt u. a. den Umgang mit Informationen bei Beendigung des
Lieferantenverhältnisses.

# Identifizierung von Risiken

Sicherheitsrisiken im Zusammenhang mit Lieferanten werden während des Risikomanagementprozesses 
identifiziert. Während der Risikoanalyse muss besondere Sorgfalt walten, um sowohl Risiken im 
Zusammenhang mit Informations- und Kommunikationstechnik als auch Risiken in Verbindung mit der 
Produkt-Lieferkette zu identifizieren. Die Leitung entscheidet darüber, ob es notwendig ist, 
zusätzliche Risiken einschätzen zu müssen.

# Überprüfung von Lieferanten

Der Sicherheitsbeauftragte entscheidet darüber, ob es notwendig ist, einen Lieferanten hinsichtlich
dessen Informationssicherheitsstandards zu überprüfen. Sofern ein Lieferant nach einem der gängigen 
Informationssicherheitsstandards (z.B. ISO 27K) zertifiziert ist, wird von einer Anwendung der 
_Best Practice_ und der Befolgung der gesetzlichen Vorgaben ausgegangen. Eine tiefergehende 
Sicherheitsüberprüfung ist in diesem Fall nicht notwendig.
Eine Risikoanalyse sollte jedoch in jedem Fall durchgeführt und dokumentiert werden.

# Überwachung von Lieferanten

Lieferanten, die auf der Infrastruktur der de.NBI Cloud Bielefeld arbeiten, unterliegen den gleichen
Überwachungsmechanismen wie alle anderen Mitarbeiter von ADM und BRF.
Sämtliche administrative Eingaben von Computerbefehlen werden mitgeloggt und ggf. ausgewertet.
Der Zugang zur Infrastruktur wird auf den jeweils notwendigen dedizierten
Bereich, wie zum Beispiel die Entwicklungsumgebung, eingeschränkt. 

**Die Leitung hat die Einhaltung der Richtlinie sicherzustellen und weist die Mitarbeiter
ggf. auf Defizite hin.**
