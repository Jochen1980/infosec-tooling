# iso 27k 

## Seminarnotizen 

### Übung iNergy

Frage 1: Consider the future oepration of the infrastructure internally vs. externally

- risk analysis
    - clients are not separated

Frage 2: Refer to ISO/IEC 27001 for
- aspects of data backup 
- aspects of vulnerability management



## Buch-Review Praxisbuch iso-iec 27001 von Brenner et. al

### Einführung und Basiswissen

Cybersicherheits-News dominieren die Nachrichtenlandschaft.
KRITIS-Betreiber müssen liefern und entsprechende Maßnahmen umsetzen.
Regulatorik verlangt ebenfalls bestimmte Vorgaben (DSGVO, NIS-2, Cyber-Resilience Act).
Die Din-ISO-IEC 27001 ist hierfür eine Antwort.  

### Standardfamilie ISO-IEC 27000 im Übetrblick

Aufbau ist ein Dreiklang:
- Begriffe
- Grundlegendes Managementsystem
- Maßnahmen

KRITIS ist seit 2015 wichtig, Abkehr von Freiwilligkeit.
KRITIS betrifft bestimmte Sektoren, etwa Energie oder Ernährung.
KRITIS will Infosec nach Stand der Technik.
KRITIS muss Schutzziele (Vetraulichkeit, Integrität, Verfügbarkeit und Authentizität durch geeignete Maßnahmen sichern).
Stand der Technik ist dabei mehr als anerkannte Regeln der Technik und weniger als Stand der Wissenschaft und Technik.

DSGVO gilt auf EU-Ebene seit 2018. 
Es gibt Grundsätze zur Datenverarbeitung, diese sind:
- Rechtmäßig, Verarbeitung nach Treu und Glauben, transparent.
- Zweckbindung (definiert, eindeutig, legitim)
- Datenminimierung (auf das notwendige Maß beschränkt)
- Richtigkeit (alte Daten also abgleichen bzw. loeschen)
- Speicherbegrenzung (also nur auf bestimmte Zeit speichern)
- Integrität und Vertraulichkeit wahrend 

NIS-2 kam 2023 in der EU.
NIS-2 nimmt die Cybersicherheitsstrategien der einzelnen Länder in den Blick.
Risikomanagement, Asset Management, Meldewesen für IT-Sec-Vorfälle als Beispiele. 
Ebenso Lieferkettensicherheit und die Umsetzung des Stands der Technik im Themenfeld Infosec.
NIS-2 betrachtet 18 Sektoren.

Cyber Resilience Act ist als EU-Vorgabe für Produkte und staatliche Einrichtungen bzw. Firmen zu sehen.
Es gibt Vorgaben zu Schwachstellentests und legt kritische Produkte für den Schutz der Schutzziele fest, 
etwa Passwortmanager oder Virenscanner.

DORA ist eine EU-Vorgabe, die speziell die Finanz- und Versicherungsbranche anspricht. Diese müssen 
deren IT-Infrastruktur und -prozesse entsprechend anpassen. 

Standards sind wichtig, dass man best practices und Definitionen festhält.
ISO-27k bezeichnet entweder die gesamte Standardfamilie oder nur das 27k-Dokument mit Terminologie und Überblick.
Manchmal sind Standards normativ (muss) oder informativ (soll).
Die iso 27001 ist das zentrale Dokument mit den Anforderungen an das ISMS. 
Im Audit wird die Konformität zu diesem Dokument geprüft.
Ergänzend gibt es die ISO 27701, die den Ausbau zum Datenschutz-Management-System beleuchtet, dem Privacy Information Management System, kurz PIMS.
Im 27002 Dokument sind die ganzen Maßnahmen drin, das ist daher recht umfassend und oft verwendet.
27003 geht in eine ähnliche Richtung wie die 27002. 27004 fokussiert auf den KVP und gibt Empfehlungen 
zur Fortschrittsmessung.
27005 beinhaltet Hinweise zum Risikomanagement.
27007 und 27008 enthält Audit-Leitfäden.
27014 und 27016 Entscheidungshilfen auf Vorstandsebene.
27018 beschreibt den Umgang mit personenbezogenen Daten bei Auftragsverarbeitung.
Diese Dokumente sind universal anwendbar, es gibt noch sektorenspezifische Erweiterungen oder Leitfäden.
Kommunikationsflüsse inkl. relevanter Hardware wird dabei berücksichtigt, ebenso der Faktor Mensch.


### Grundlagen ISMS

Kernfragen, die für ein ISMS im Zentrum stehen:
- Was soll durch das ISMS eigentlich geschützt werden?
- Welche Regeln und Vorgaben werden zu diesem Zweck eingerichtet?
- Wie wird sichergestellt, dass dieses Regelwerk schriftlich fixiert und seine Einhaltung nachvollziehbar protokolliert wird?
- Wer ist zuständig für die Planung und Durchführung der erforderlichen Aktivitäten?
- Durch welche Maßnahmen kann das erforderliche Sicherheitsniveau erreicht werden?

Informations-Assets sind wichtig für die Orga und die Nichterreichung der Schutzziele hat einen negativen Impact.
Wir haben als Tools dann Richtlinien, Prozesse und Verfahren.
Richtlinien haben Definitionscharakter und stehen oberhalb von Prozessen und Verfahren.
Prozesse sind auf Steuerungsebene und beschreiben die Abfolge von Aktivitäten und verfahren.
Verfahren sind die Durchführungsbestimmungen und wichtig für die Mitarbeiter, die direkt die Ausführung übernehmen.
iso-27k ist prozessorientiert und nicht etwa hierachisch strukturiert.
KVP ist das Ziel, PDCA als Methodik der Baukasten.
Planung - erfolgt zu Beginn bei der ISMS Planung und später bei den Maßnahmen.
Do - Phase der Umsetzung und hier stellt sich heraus, ob Budgets dann wirklich vorhanden sind.
Check - unterteilt sich in Konformität, Effektivität und Effizienz.
Act - dies ist die Verbesserungsphase in Anlehnung an Konformität, Effektivität und Effizienz. 

### iso 27k - Spezifikation und Mindestanforderungen

Grundsätzlich ist das 27001-Dokument als Überblicksdokument gedacht.
Man beginnt damit, dass man den Kontext der Organisation ausreichend tief versteht.
Anschließend klärt man den Scope des ISMS.


### Maßnahmen im Rahmen von ISMS

### Verwandte Standards und Rahmenwerke

### Zertifizierungsmöglichkeiten nach iso-27k

### Anhang

### Pruefungsfragen Buch Brenner

#### Frage 1.1:

Was versteht ISO/IEC 27000 unter dem Begriff Vertraulichkeit (engl. Confidentiality)?

A) Den Abschluss einer Vertraulichkeitsvereinbarung (Non-disclosure agreement).
B) Die Geheimhaltungsverpflichtung aller Mitarbeiter, die Zugriff auf das ISMS haben.
C) Die Vertraulichkeit schützt die Werte im Hinblick auf ihre Richtigkeit und Vollständigkeit.
D) Eine Information ist für unautorisierte Personen, Entitäten oder Prozesse nicht zugänglich.

Antwort: D 

#### Frage 1.2: 

Was versteht ISO/IEC 27000 unter dem Begriff Verfügbarkeit (engl. Availability)?

A) Die Eigenschaft einer Information oder eines Wertes, für eine berechtigte Person oder Entität zugreifbar und nutzbar zu sein.
B) Die Eigenschaft einer informationsverarbeitenden Einrichtung, genügend Ressourcen für eine Aufgabe zur Verfügung zu haben.
C) Die Eigenschaft einer Information oder eines Wertes, vor Manipulation geschützt zu sein.
D) Die Eigenschaft einer Information oder eines Wertes, vor Offenlegung geschützt zu sein.

Antwort: A

#### Frage 1.3:

Was versteht ISO/IEC 27000 unter dem Begriff Nichtabstreitbarkeit (engl. Non-Repudiation)?

A) Die Eigenschaft, dass interne Sicherheitsaudits wie geplant durchgeführt werden.
B) Die Eigenschaft eines Informationswertes, für eine berechtigte Person verfügbar und nutzbar zu sein.
C) Die Fähigkeit, den Eintritt eines behaupteten Ereignisses oder einer Aktion zweifelsfrei nachweisen zu können. Der Verursacher kann den Vorgang nicht leugnen.
D) Die Eigenschaft, ein konsistentes und bestimmungsgemäßes Verhalten zu zeigen und konsistente Ergebnisse zu liefern.

Antwort: C 

#### Frage 2.4: 

Für welche Zielgruppe wurde der branchenspezifische Standard ISO/IEC 27011 entwickelt?

A) ISO/IEC 27011 definiert verbindlich umzusetzende Anforderungen für öffentliche Einrichtungen.
B) Zielgruppe dieses Standards sind Unternehmen aus dem Gesundheitssektor.
C) Der Standard stellt einen Leitfaden für Telekommunikationsunternehmen dar.
D) Dieser Standard definiert Grundsätze für die Durchführung von Audits und ist damit für Zertifizierungsstellen relevant.

Antwort: C 

#### Frage 2.5:

Bei welchem der folgenden Standards handelt es sich nicht um einen allgemeinen Leitfaden?

A) ISO/IEC 27002
B) ISO/IEC 27003
C) ISO/IEC 27005
D) ISO/IEC 27019

Antwort: D (Prozessleittechnik in der Energiebranche)

#### Frage 2.6:

Wie verhält sich ISO/IEC 27002 zu ISO/IEC 27001?

A) ISO/IEC 27002 schreibt konkrete technische Maßnahmen zur Umsetzung der in ISO/IEC 27001 definierten Mindestanforderungen vor.
B) ISO/IEC 27002 enthält branchenspezifische Erweiterungen von ISO/IEC 27001.
C) ISO/IEC 27002 wird als Grundlage für Audits durch externe Zertifizierungsunternehmen herangezogen.
D) ISO/IEC 27002 ist ein Leitfaden zur Umsetzung der Maßnahmen (Controls) aus ISO/IEC 27001.

Antwort: A

#### Frage 3.7:

Ein wichtiges Prinzip, das ISO/IEC 27001 zugrunde liegt, ist der PDCA-Zyklus. Welcher Zweck wird mit diesem Ansatz verfolgt?

A) Eindeutige Zuweisung von Verantwortlichkeiten, indem Rollen und Aktivitäten des ISMS in einer Matrix zugeordnet werden.
B) Kontinuierliche Verbesserung des ISMS, indem Prozesse und Maßnahmen geplant, nach ihrer Umsetzung überprüft und Verbesserungsmöglichkeiten identifiziert werden.
C) Festlegung des Umfangs des ISMS, indem der Anwendungsbereich definiert und eine Erklärung zur Anwendbarkeit erstellt werden.
D) Abgleich des ISMS mit dem übergeordneten Qualitätsmanagementsystem, indem Schnittmengen zwischen ISO/IEC 27000 und ISO 9001 betrachtet werden.

Antwort: B

#### Frage 3.8:

Was beschreibt am besten die Assets, die im Rahmen eines ISMS schwerpunktmäßig betrachtet werden?

A) Alle technischen Geräte, die eine Inventarnummer haben.
B) Alle Informationen, die schützenswert sind, zusammen mit den Informationsträgern, Systemen und Diensten, die diese Informationen verarbeiten.
C) Alle Gegenstände, die zum Anlagevermögen der Organisation gehören.
D) Alles, was durch den Anhang A aus DIN EN ISO/IEC 27001 abgedeckt ist.

Antwort: B

#### Frage 3.9:

Was bezeichnet ISO/IEC 27000 mit dem Begriff „dokumentierte Information“ (documented information)?

A) Beschreibung dessen, was als Ergebnis umgesetzter Maßnahmen erzielt werden soll.
B) Information, die von einer Organisation gelenkt und aufrechterhalten werden muss, und das Medium, auf dem sie enthalten ist.
C) Satz von in Wechselbeziehungen stehenden Mitteln und Tätigkeiten, die Eingaben in Ergebnisse umwandeln.
D) Alles, was für eine Organisation von Wert ist.

Antwort: B 

#### Frage 3.10: 

Was wird bei der Überprüfung der Konformität beurteilt?

A) Die Einhaltung ethischer Grundsätze.
B) Die Erfüllung einer oder mehrerer Anforderungen.
C) Die Effizienz eines Prozesses.
D) Der optimale Einsatz von Ressourcen, um ein Ziel zu erreichen.

Antwort: B 

#### Frage 3.11: 

Was versteht man gemäß ISO/IEC 27000 unter einem Prozess?

A) Eine Maßnahme zur Veränderung eines Risikos.
B) Die Ausführung eines Computerprogramms durch eine informationsverarbeitende Einrichtung.
C) Ein Satz von zusammenhängenden und sich gegenseitig beeinflussenden Tätigkeiten, der Eingaben in Ergebnisse umwandelt.
D) Eine Gerichtsverhandlung.

Antwort: C

#### Frage 4.12:

Wann spricht man von einem ISMS, das zu DIN EN ISO/IEC 27001 konform ist?

A) Wenn alle Anforderungen aus den Abschnitten 4 bis 10 erfüllt und die Maßnahmen aus dem Anhang A in DIN EN ISO/IEC 27001 umgesetzt wurden, sofern anwendbar.
B) Wenn für alle Maßnahmen aus dem Anhang A in DIN EN ISO/IEC 27001 eine solide und nachvollziehbare Planung existiert.
C) Wenn alle Maßnahmen exakt nach den Vorgaben aus ISO/IEC 27002 umgesetzt wurden.
D) Wenn mindestens 80 % der identifizierten Risiken durch geeignete Maßnahmen behandelt wurden.

Antwort: A.

#### Frage 4.13:

Wobei handelt es sich nicht um einen relevanten Aspekt der Informationssicherheitsrisikobehandlung gemäß DIN EN ISO/IEC 27001?

A) Auswahl angemessener Optionen für die Risikobehandlung.
B) Erstellung einer Erklärung zur Anwendbarkeit.
C) Löschen von Restrisiken auf Basis der Risikokriterien.
D) Erstellung eines Risikobehandlungsplans.

Antwort: C. (Restrisiken werden vom Owner genehmigt oder akzeptiert)

#### Frage 4.14:

Wie definiert ISO/IEC 27000 den Begriff Risikoanalyse?

A) Koordinierte Aktivitäten zur Leitung und Kontrolle einer Organisation in Bezug auf Risiken.
B) Prozess für die Auswahl von Maßnahmen zur Behandlung identifizierter Risiken.
C) Festlegungen, um die Signifikanz eines Risikos zu bewerten.
D) Prozess, um die Beschaffenheit eines Risikos zu verstehen und das Risikoniveau zu bestimmen.

Antwort: D.

A) beschreibt das Risikomanagement (risk management).
B) beschreibt die Risikobehandlung (risk treatment).
C) beschreibt die Risikokriterien (risk criteria).

#### Frage 4.15:

Welche der folgenden Tätigkeiten ist keine von DIN EN ISO/IEC 27001 geforderte Verpflichtung des Managements?

A) Sicherstellung, dass interne ISMS-Audits durchgeführt werden.
B) Bestimmung der Aufgaben und Verantwortlichkeiten für Informationssicherheit.
C) Lenkung von Dokumenten und Aufzeichnungen.
D) Festlegen der ISMS-Leitlinie.

Antwort: C. (Lenkung der Dokumente macht wer anders.)

#### Frage 4.16:

Welche Arten von Audits sind in der Regel nach DIN EN ISO/IEC 27001 zu unterscheiden?

A) Vollständige und unvollständige.
B) Interne und externe.
C) Objektive und subjektive.
D) Angekündigte und unangekündigte.

Antwort: B.

#### Frage 4.17:

Im Verlauf der Festlegung des ISMS sind nach DIN EN ISO/IEC 27001 die Definition der ISMS-Leitlinie und der Vorgehensweise zur Risikoeinschätzung zu erstellen. Welcher Schritt muss nach DIN EN ISO/IEC 27001 bereits zuvor erfolgt sein?

A) Das Budget für das ISMS-Vorhaben muss geklärt werden.
B) Das Management muss die Umsetzung und Durchführung des ISMS genehmigen.
C) Im Rahmen eines Audits müssen Verbesserungsmöglichkeiten identifiziert werden.
D) Der Anwendungsbereich (Scope) des ISMS muss festgelegt werden.

Antwort: D. (die ISO hat eine Reihenfolge, die Kapitel und die anderen kommen erst danach)

#### Frage 4.18:

Welche Aufgabe hat ein Risikoeigentümer im Hinblick auf die Informationssicherheitsrisikobehandlung?

A) Der Risikoeigentümer muss alle Restrisiken identifizieren und beseitigen.
B) Der Risikoeigentümer muss den vorgeschlagenen Restrisiken zustimmen.
C) Der Risikoeigentümer ist für die (technische) Umsetzung der Maßnahmen zur Risikobehandlung zuständig.
D) Der Risikoeigentümer dokumentiert die Risiken in den internen Auditberichten.

Antwort: B.

Begründung gemäß DIN EN ISO/IEC 27001 (Abschnitt 6.1.3 f):

Die Norm fordert explizit, dass die Organisation die Zustimmung (Freigabe/Akzeptanz) der Risikoeigentümer zum Risikobehandlungsplan und zu den verbleibenden Informationssicherheits-Restrisiken einholen muss.
Zu A: Restrisiken lassen sich fast nie vollständig (auf null) beseitigen – sie müssen auf ein akzeptables Maß reduziert und dann vom Risikoeigentümer getragen/akzeptiert werden.
Zu C: Der Risikoeigentümer trägt die Verantwortung (Rechenschaftspflicht) für das Risiko und entscheidet über die Behandlung, führt die technische Umsetzung der Maßnahmen aber in der Regel nicht selbst durch (das machen z. B. IT-Administratoren oder Fachabteilungen).
Zu D: Interne Auditberichte werden von unabhängigen internen Auditoren erstellt, nicht vom Risikoeigentümer.

#### Frage 4.19:

Welcher Schritt gehört nicht zur Beurteilung von Informationssicherheitsrisiken?

A) Identifizierung der Risiken und zugehörigen Risiokoeigentümer.
B) Analyse der Risiken einschließlich Bestimmung der Risikoniveaus.
C) Bewertung der Risiken einschließlich Priorisierung für die Risikobehandlung.
D) Festlegung der Maßnahmen zur Risikobehandlung.

Antwort: D

#### Frage 4.20:

Worauf ist im Zusammenhang mit internen Audits des ISMS zu achten?

A) Dass in jedem internen Audit alle Anforderungen der Norm DIN EN ISO/IEC 27001 vollumfänglich geprüft werden.
B) Dass die Ergebnisse der Audits gegenüber der zuständigen Leitung berichtet werden.
C) Dass die Auditkriterien im Vorfeld gegenüber den auditierten Personen und Bereichen nicht offengelegt werden.
D) Dass als Auditoren nur Personen ausgewählt werden, die selbst in dem auditierten Bereich tätig sind.

Antwort: B.

#### Frage 4.21:

Wobei handelt es sich nicht um eine Aktivität, die gemäß DIN EN ISO/IEC 27001 umgesetzt werden muss, um ein ISMS zu planen oder zu betreiben?

A) Bestimmung von Chancen und Risiken in Verbindung mit dem ISMS.
B) Festlegung von Informationssicherheitszielen.
C) Etablierung eines Prozesses zur Ermittlung der Mitarbeiterzufriedenheit in Bezug auf die festgelegten Sicherheitsrichtlinien.
D) Erstellung einer Erklärung zur Anwendbarkeit des ISMS.

Antwort: C.

#### Frage 5.22:

Durch welche Maßnahme gemäß Anhang A aus DIN EN ISO/IEC 27001 wird am ehesten vermieden, dass beispielsweise Entwickler von Software versehentlich oder absichtlich produktive Systeme kompromittieren?

A) Sichere Authentisierung
B) Redundanz von informationsverarbeitenden Einrichtungen
C) Trennung von Netzwerken
D) Trennung von Entwicklungs-, Test- und Produktivumgebungen

Antwort: D.

#### Frage 5.23:

Welche der folgenden Aspekte und Anforderungen sind im Zusammenhang mit Betriebsmitteln und unterstützenden Versorgungseinrichtungen nicht Teil der Maßnahmen zur physischen Sicherheit gemäß Abschnitt A.7 in DIN EN ISO/IEC 27001?

A) Betriebsmittel müssen sicher und geschützt platziert werden.
B) Die Konfigurationen, einschließlich der Sicherheitskonfigurationen, von Hardware, Software, Diensten und Netzwerken müssen festgelegt, dokumentiert, umgesetzt, überwacht und überprüft werden.
C) Kabel zur Stromversorgung, Datenübertragung oder Anbindung an Informationsdienste müssen vor Abhören, Manipulation oder Beschädigung geschützt werden.
D) Betriebsmittel müssen sachgerecht gewartet werden, um die Verfügbarkeit, Integrität und Vertraulichkeit von Informationen zu gewährleisten.

Antwort: B.

#### Frage 5.24:

Was muss gemäß Maßnahme A.6.5 aus DIN EN ISO/IEC 27001 im Zusammenhang mit Beendigung oder Wechsel des Beschäftigungsverhältnisses festgelegt werden?

A) Kennungen der Nutzerendgeräte, die nach Beendigung oder Wechsel des Beschäftigungsverhältnisses zurückgegeben werden müssen
B) Verantwortlichkeiten und Pflichten im Zusammenhang mit der Informationssicherheit, die nach Beendigung oder Wechsel des Beschäftigungsverhältnisses fortbestehen
C) Verträge, die nach Beendigung oder Wechsel des Beschäftigungsverhältnisses neu ausgehandelt werden müssen
D) Gültigkeitsdauer von digitalen Identitäten, Benutzerkennungen und Zertifikaten, die auch nach Beendigung oder Wechsel des Beschäftigungsverhältnisses noch verwendet werden

Antwort: B.

#### Frage 5.25:

Wobei handelt es sich um eine technologische Maßnahme gemäß DIN EN ISO/IEC 27001, Anhang A.8?

A) Aufgabentrennung
B) Sicherheitsüberprüfung
C) Sicherung von Informationen
D) Remote-Arbeit

Antwort: C.

#### Frage 5.26:

Was ist Gegenstand der Maßnahme Überwachung von Aktivitäten (A.8.16) gemäß Anhang A in DIN EN ISO/IEC 27001?

A) Überwachung des Personals im Hinblick auf vorsätzliche Verletzungen der Informationssicherheit
B) Überwachung des Umsetzungsstands von Maßnahmen zur Risikobehandlung
C) Überwachung von Netzwerken, Systemen und Anwendungen im Hinblick auf Anomalien
D) Überwachung von Sicherheitsbereichen mithilfe von Videokameras

Antwort: C.

#### Frage 5.27:

Wobei handelt es sich um eine organisatorische Maßnahme gemäß DIN EN ISO/IEC 27001, Anhang A.5?

A) Aufgeräumter Schreibtisch und Gerätesperre
B) Schutz vor Schadsoftware
C) Reaktion auf Informationssicherheitsvorfälle
D) Einsatz von Kryptographie

Antwort: C.

#### Frage 5.28: 

Wodurch muss eine übergeordnete Informationssicherheitsrichtlinie gemäß der Maßnahme A.5.1. aus DIN EN ISO/IEC 27001 ergänzt werden?

A) Durch den Risikobehandlungsplan
B) Durch eine Erklärung zur Anwendbarkeit der Richtlinie
C) Durch themenspezifische Informationssicherheitsrichtlinien
D) Durch eine validierte Kostenplanung

Antwort: C.

#### Frage 5.29:

Welche Schutzziele müssen bei der Klassifizierung von Informationen gemäß Anhang A.5.12 aus DIN EN ISO/IEC 27001 berücksichtigt werden?

A) Keine, da die Organisation selbst festlegen kann, auf welcher Grundlage Informationen klassifiziert werden
B) Nur Vertraulichkeit und Verfügbarkeit
C) Nur Vertraulichkeit und Integrität
D) Vertraulichkeit, Integrität und Verfügbarkeit

Antwort: D.

#### Frage 5.30:

Wobei handelt es sich nicht um eine der Maßnahmen, die DIN EN ISO/IEC 27001 im Anhang A im Zusammenhang mit Informationssicherheitsvorfällen fordert?

A) Planung und Vorbereitung des Managements von Informationssicherheitsvorfällen
B) Reaktion auf Informationssicherheitsvorfälle
C) Analyse von Informationssicherheitsvorfällen durch unabhängige externe Forensik-Dienstleister
D) Lernen aus Informationssicherheitsvorfällen

Antwort: C.

#### Frage 5.31:

Was ist kein geforderter Bestandteil der Maßnahme A.8.13 (Sicherung von Informationen) gemäß DIN EN ISO/IEC 27001, Anhang A?

A) Vorhalten von Sicherungskopien von Informationen
B) Vorhalten von Sicherungskopien von Software und Systemen
C) Regelmäßiges Testen der Sicherungskopien
D) Hinreichend redundante Auslegung informationsverarbeitender Systeme

Antwort: D.

#### Frage 5.32:

Was ist neben Regeln für den wirksamen Einsatz von Kryptographie ebenfalls Gegenstand der Maßnahme Verwendung von Kryptographie (A.8.24) gemäß Anhang A in DIN EN ISO/IEC 27001?

A) Löschung unverschlüsselter Aufzeichnungen zu Transaktionen
B) Penetrationstests der eingesetzten Verschlüsselungstechniken
C) Verwaltung kryptographischer Schlüssel
D) Filterung des Netzverkehrs über einen Proxy

Antwort: C.

#### Frage 6.33:

Wie hängen die drei Standards ISO 9000, ISO/IEC 20000 und ISO/IEC 27001 zusammen?

A) ISO/IEC 27001 ist eine Kombination aus ISO 9000 und ISO/IEC 20000.
B) Diese drei Normen behandeln Managementsysteme in zum Teil überlappenden Anwendungsbereichen.
C) Diese drei Normen behandeln Management und Qualitätssicherung für drei unterschiedliche Branchen.
D) Die Zertifizierungen für diese Standards bauen aufeinander auf, d. h. eine Zertifizierung nach ISO/IEC 27001 ist nur möglich, wenn das Unternehmen auch nach ISO 9000 zertifiziert wurde.

Antwort: B.

#### Frage 6.34:

Mit welchem Themengebiet befasst sich die Norm ISO 9000 schwerpunktmäßig?

A) Bewertung der Informationssicherheit
B) Informationssicherheitsleitlinie
C) IT-Service-Management
D) Qualitätsmanagement

Antwort: D.

#### Frage 6.35:

Welcher der nachfolgend genannten Standards behandelt nicht den Themenbereich IT- oder Informationssicherheit?

A) ISO/IEC 15408
B) ISO/IEC 20000
C) ISO/IEC 27000
D) ISO 9000

Antwort: D.

#### Frage 6.36:

Welche Organisation ist Herausgeber des IT-Grundschutz-Kompendiums?

A) IT-Sicherheitscluster e.V.
B) National Institute of Standards and Technology (NIST)
C) International Electrotechnical Commission (IEC)
D) Deutsches Bundesamt für Sicherheit in der Informationstechnik (BSI)

Antwort: D.

#### Frage 6.37:

Zu welchem Zweck wurde die Normenreihe ISO/IEC 15408 (Common Criteria)
entwickelt?

A) ISO/IEC 15408 definiert ein formales Verfahren zur Bewertung von Sicherheitseigenschaften von IT-Produkten.
B) Die Common Criteria enthalten Kriterien, die es bei der Speicherung von Logdaten zu berücksichtigen gilt.
C) Die Normenreihe ISO/IEC 15408 wurde entwickelt zur Bewertung der Netzsicherheit und enthält eine dafür geeignete Sammlung von Evaluationskriterien.
D) ISO/IEC 15408 definiert ein international anerkanntes Format für die Beschreibung von sicherheitsrelevanten Ereignissen.

Antwort: A.

#### Frage 6.38:

Welche Aussage zur Standardfamilie ISO/IEC 20000 trifft zu?

A) ISO/IEC 20000-1 definiert Anforderungen an ein Service-Management-System (SMS).
B) Die Bewertung der Informationssicherheit ist das maßgebliche Ziel, das ISO/IEC 20000-2 verfolgt.
C) ISO/IEC 20000-3 steht in direkter Konkurrenz zu ISO/IEC 27000, da die beiden Standards das gleiche Ziel des Managements der Informationssicherheit verfolgen.
D) ISO/IEC 20001 legt Anforderungen für ISMS-Konformitätsbewertungsstellen fest.

Antwort: A. 

#### Frage 7.39:

Was lässt sich nach ISO/IEC 27001 zertifizieren?

A) Ein durch eine Organisation betriebenes ISMS.
B) Nichts – ISO/IEC 27001 ist informativ und lässt sich nicht zertifizieren.
C) Sicherheit von Infrastruktur-Komponenten, wie Server.
D) Schutz von Daten in Clouddiensten.

Antwort: A.

#### Frage 7.40:

Welcher Schritt gehört nicht zu einem typischen Ablauf eines Zertifizierungsaudits nach ISO/IEC 27001?

A) Prüfung von Unterlagen bzw. Dokumentation.
B) Personenzertifizierung des Managements.
C) Vor-Ort-Audit.
D) Erstellung und Verteilung eines Auditberichts.

Antwort: B. 

#### Fragen an Jan

- Wo stehen bei dir die interessierten Parteien?
- Wo ist der ISB benannt? 
- Warum ist das Organigramm nicht abgebildet in der Security Leitlinie? 
- Wo sind die Risiken entsprechend beschrieben und in die Risikomatrix eingereiht, also der Wert? 
- Welcher Thread-katalog wurde genutzt, um die Risiken zu identifizieren? 
- Ich sehe, dass die SOA der ISO-27001-Anhang normalerweise entsprechen kann.
- Wo sind die Risikoszenarien gelistet? Wo erfolgt der Einbau? 




### Pruefungsfragen Kurs FZJ
