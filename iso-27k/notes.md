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

### Pruefungsfragen Kurs FZJ
