# Sicherheitsrichtlinie für die Handhabung von Sicherheitsvorfällen  

|                 |                                             |
|-----------------|---------------------------------------------|
| Version:        | 0.4                                         |
| Version vom:    | 14.06.2025                                  |
| Erstellt durch: | Jan Krüger, Alex Walender                   |
| Genehmigt am:   | 29.06.2026 (sa), 30.06.2926 (as)            |
| durch:          | Stefan Albaum (sa), Alexander Sczyrba (as)  |

## ChangeLog

- Version 0.4 vom 14.06.2026: PRT hinzugefügt, Kontakte aktualisiert
- Version 0.3 vom 04.04.2025: Überarbeitung aufgrund NA (CER-557)
- Version 0.2 vom 28.01.2025: DSB Uni Bielefeld ergänzt
- Version 0.1 vom 02.02.2024: initialer Entwurf

## Zweck, Anwendungsbereich und Anwender

Die Sicherheitsrichtlinie zur Handhabung von Sicherheitsvorfällen definiert die Verfahren
und Richtlinien, die von allen Mitarbeitern und beteiligten Parteien befolgt werden müssen,
um angemessen auf Sicherheitsvorfälle zu reagieren und deren Auswirkungen zu minimieren.

Diese Richtlinie gilt für alle Mitarbeiter, Auftragnehmer, Partner und Dritte, die auf
Informationen und Ressourcen unserer Organisation zugreifen.

## Definition

Ein Sicherheitsereignis ist ein beobachtetes Ereignis, das vom normalen Betrieb abweicht
und potenziell negative Auswirkungen auf die Informationssicherheit haben könnte. Solche 
Ereignisse bergen das Risiko, sich zu einem Sicherheitsvorfall zu entwickeln.

Beispiele für Sicherheitsereignisse:

1. Mehrere fehlgeschlagene Anmeldeversuche auf ein Benutzerkonto
1. Ein Antivirus-Programm schlägt an, ohne dass Schaden entstanden ist.
1. Port-Scans auf Nutzer-Instanzen.

Ein Sicherheitsvorfall liegt vor, wenn eine tatsächliche oder vermutete Beeinträchtigung 
der Vertraulichkeit, Integrität oder Verfügbarkeit von Informationen oder IT-Ressourcen 
festgestellt wird – unabhängig davon, ob dies durch eine absichtliche, unbeabsichtigte oder 
unerlaubte Handlung verursacht wurde.

Beispiele für Sicherheitsvorfälle:

1. Eine Nutzer-Instanz wird durch böswillige Akteure übernommen.
1. Unbefugte Personen befinden sich in einem Datacenter.
1. Veröffentlichung klassifizierter Informationen auf externen Plattformen.

Nähere _mögliche_ Sicherheitsvorfälle im Kontext des Betriebs finden sich im
[Risikomanagement](../risikomanagement.md).

IT-Sicherheitsvorfälle bilden eine Teilmenge der Sicherheitsvorfälle und beziehen sich 
explizit auf Vorfälle im Zusammenhang mit IT-Systemen, Netzwerken, Anwendungen oder Datenverarbeitung.

Diese Richtlinie gilt für alle Arten von Sicherheitsvorfällen, unabhängig von ihrer Ursache oder ihrem Ursprung.

## Klassifizierung von Sicherheitsvorfällen

### Kategorien

Sicherheitsvorfälle lassen sich in folgende Kategorien einteilen.

#### Physische Sicherheitsvorfälle

Zu den physischen Sicherheitsvorfällen zählen beispielweise Einbrüche und unbefugter Zutritt
zu Gebäuden oder Einrichtungen. Diebstahl oder Verlust von physischen Vermögenswerten,
sowie Sabotage oder Vandalismus.

#### IT-Sicherheitsvorfälle

IT-Sicherheitsvorfälle umfassen Malware-Angriffe (Viren, Würmer, Trojaner, Ransomware),
Netzwerkangriffe (DoS, DDoS), unbefugter Zugriff (Hackerangriffe, Phishing-Angriffe,
Credential Stuffing), Datenlecks und Datenverlust (unbeabsichtigte Offenlegung, Datenkorruption,
Datenexfiltration), Schwachstellen und Exploits (Ausnutzen von Sicherheitslücken, Zero-Day-Exploits), sowie
Insider-Bedrohungen (Handlungen von Mitarbeitern oder Auftragnehmern, die die Sicherheit beeinträchtigen).

#### Kommunikationssicherheitsvorfälle

Zu den Kommunikationssicherheitsvorfällen gehört das Abhören von vertraulicher Kommunikation, sowie die
Manipulation von Datenübertragungen.

#### Personenbezogene Sicherheitsvorfälle

Der Identitätsdiebstahl, sowie die Verwendung von persönlichen Informationen gehört in die Kategorie der
personenbezogenen Sicherheitsvorfälle.

#### Compliance- und Rechtsverletzungen

Unter Compliance- und Rechtsverletzungen fallen zum Beispiel Verstöße gegen Datenschutzbestimmungen und das
Nicheinhalten von Sicherheitsrichtlinien oder gesetzlichen Vorschriften.

#### Pishing und Social Engineering

Sicherheitsvorfällen könne auch durch Täuschung von Mitarbeitern durch gefälschte E-Mails oder
soziale Manipulation ausgelöst werden.

#### Systemausfälle, technische Störungen und "Human Error"

In diese Kategorie von Sicherheitsvorfällen fallen beispielsweise
Hard- und Softwarefehler, Netzwerkausfälle, Systemabstürze, sowie unbeabsichtigte
Aktionen, die zu Sicherheitsvorfällen führen.

## Melden von Sicherheitsvorfällen

### IT-Sicherheitsvorfälle

Alle Mitarbeiter sind verpflichtet, verdächtige Aktivitäten oder Sicherheitsvorfälle sofort
ADM bzw. BRF zu melden (siehe Personen). Die Meldung sollte so schnell wie möglich und auf
angemessene Weise erfolgen, um eine rasche Reaktion zu ermöglichen.

IT-Sicherheitsvorfälle, deren Beeinträchtigung als "mittel" oder "hoch" eingestuft sind, sind
unverzüglich nach Bekanntwerden an den IT-Informationssicherheitsbeauftragte der 
Universität Bielefeld bzw. des Forschungszentrum Jülich weiterzuleiten.

### Sonstige Sicherheitsvorfälle

Die Meldung allgemeine Sicherheitsvorfälle erfolgt umgehend und durch mehrere Kanäle.

Besteht durch das Ereignis eine Gefahr für Leib und Leben, so sind umgehend die Notfall-Prozesse
der [Universität Bielefeld](https://www.uni-bielefeld.de/themen/hilfe-notfall/) zu befolgen.

Bei dringenden und akuten Ereignissen ist primär die Leitwarte der Universität Bielefeld
zu kontaktieren. Dies betrifft Verstöße gegen Sicherungsvorkehrungen sowie Zugangsverstöße
bei offenen Türen bzw. Zutritt durch unberechtigte Personen.

Ist das Ereignis akut nicht mehr bedrohlich, so wird der Vorfall dem Facility Management (FM) gemeldet.

Im Weiteren wird die obere Leitung sowie der Informationssicherheitsbeauftragte der Universität
von dem Vorfall unterrichtet. Mitteilungen erfolgen unverzüglich.

## Allgemeines Verfahren

### Erkennung und Meldung

Ein Vorfall kann aus unterschiedlichen Quellen erkannt werden:

| Quelle          | Beschreibung                     | Erkennende Einheit / Partei |   Weiteres  |
| --------------- | -------------------------------- | --------------------------- | ----------  |
| Monitoring Systeme | Systeme, wie Greenbone, Zabbix oder der CVE Scanner entdecken Vorfälle | ADM, PRT | Siehe dazugehörige IT-Verfahren |
| Log-Systeme     | Log-Einträge diverser Systeme und ihre regelmäßige Analyse können Hinweise auf Sicherheitsvorfälle geben | ADM, PRT | [REDO-19](https://yt.bi.denbi.de/issue/REDO-19/Sichtung-der-Kolla-Logs) |
| Meldungen des BITS | Das BITS ist Provider für die externen IP-Addressen und erhält Meldungen bezüglich böswilligen Aktivitäten vom DFN. Diese leitet die Meldungen weiter an die BRF | BRF | --- | 
| Meldungen der Nutzer | Nutzer sind dazu verpflichtet, ungewöhnliche Ereignisse und Vorfälle den Administratoren zu melden. | Nutzer -> ADM, PRT | [Nutzungsbestimmungen der Cloud](https://cloud.denbi.de/documents/8/Nutzungsbestimmungen_de.NBI_Cloud_V1.3-1.pdf) |
| Externe Behörden (BSI, UBICERT) | Diese geben entsprechende Meldung über ggf. beobachtete Ausnutzung von Schwachstellen | ADM, PRT, BRF | Siehe [Threat-Intelligence](Arbeitsanweisung_ThreatIntelligence.md) | 

Es muss sichergestellt werden, dass die Meldekette **alle** Mitarbeiter von ADM, PRT und BRF erreichen kann.
Erreicht die Kenntnis über ein Sicherheitsvorfall eine Arbeitsgruppe (oder nur eine Person), so ist diese
verpflichtet den Vorfall zu kommunizieren. Die mögliche Kommunikation ist hierbei Vor-Ort oder über
gängige [Kommunikationskanäle](Informationsuebertragung.md) durchzuführen.

Aufgrund der geringen Anzahl der Mitarbeiter existiert in diesem Kontext kein
gesondertes _Incident Response Team_. Wird ein Sicherheitsvorfall gemeldet, so
bearbeiten beide Gruppen diesen gemeinsam koordiniert.

Erkannte Sicherheitsvorfälle werden als gesondertes Ticket (Typ INC) dokumentiert.
Entsprechend vorgefertigte Felder sind, im 4-Augen-Prinzip auszufüllen.

### Reaktionszeiten

Aufgrund der definierten Arbeitszeiten in den Arbeitsverträgen der Mitarbeitern ist eine Reaktion
_rund um die Uhr_ nicht gegeben. Wird ein Sicherheitsvorfall in der regulären Arbeitszeit erkannt,
so wird diese **umgehend** bearbeitet. Hierbei sind aktuelle Arbeiten einzustellen. Die Analyse und
Bearbeitung von Sicherheitsvorfällen hat vorrang.

Sofern personenbezogene Daten nach DSGVO von dem Vorfall betroffen sind, muss zusätzlich der
Datenschutzbeauftragte informiert werden. Die in DSGVO Artikel 33 festgelegten Fristen sind
in jedem Fall einzuhalten.

### Bewertungsschema zur Einschätzung der Schwere von Sicherheitsvorfällen

Die Schwere eines Vorfalls ist ein subjektes Maß, um die Auswirkung auf (und die Bedrohung für)
die Integrität, Verfügbarkeit und Vertraulichkeit der de.NBI Cloud Bielefeld zu ermitteln.
Die Einstufung legt fest, mit welcher Priorität und welchem Umfang auf den Sicherheitsvorfall
reagiert werden muss.

Die folgende (unvollständige) Liste dient zur Einschätzung des Vorfalls anhand von Beispielen. Treffen für einen
Vorfall mehrere Beeinträchtigungen zu, so wird die Beeinträchtigung mit der höchsten
Einstufung für die Einstufung des Vorfalls herangezogen.

1. **Beeinträchtigung der Aufgabenerfüllung**
   - **Niedrig**: ... führt maximal zum Ausfall einzelner Arbeitsabläufe
   - **Mittel**: ... schränkt die Aufgabenerfüllung in einem Teilbereich ein
   - **Hoch**: ... gefährdet dem Betrieb der de.NBI Cloud Bielefeld ein
2. **Negative Innen- und Aussenwirkung**
   - **Niedrig**: ... könnte höchstens zu einem geringen Ansehen und Vertrauensverlust der de.NBI
     Cloud Bielefeld bei einer eingeschränkten Öffentlichkeit führen
   - **Mittel**: ...  könnte zu einem Ansehen und Vertrauensverlust bei einer eingeschränkten
     Öffentlichkeit führen bzw. einem geringen Ansehen und Vertrauensverlust bei einer breiten
     Öffentlichkeit
   - **Hoch**:  ... könnte zu einen Ansehen und Vertrauensverlust bei einer breiten Öffentlichkeit
     führen
3. **Finanzielle Auswirkung**
   - **Niedrig**: Geschätzte Summe der Auswirkung ist weniger als 100.000 Euro.
   - **Mittel**: Die geschätzte Summe der Auswirkung ist weniger als 1 Millionen Euro
   - **Hoch**: Die geschätzte Summe der Auswirkung ist mehr als 1 Million Euro.
4. **Datenschutz**
   - **Niedrig**: ... kann durch Betroffene als tolerable Beeinträchtigung des informationellen
     Selbstbestimmungsrechts eingeschätzt werden. Ein Missbrauch hätte nur geringfügige Auswirkung
     auf die gesellschaftliche Stellung und/oder wirtschaftliche Verhältnisse Betroffener.
   - **Mittel**: ... könnte zu einer eheblichen Beeinträchtigung des informationellen Selbstbestimmungsrechts
     Betroffener führen. Ein Missbrauch hätte erhebliche Auswirkung auf gesellschaftliche Stellung
     und/oder wirtschaftliche Verhältnisse Betroffener.
   - **Hoch**: ... könnte zu einer gravierenden Beeinträchtigung des informationellen Selbstbestimmungsrechts
     führen. Ein Missbrauch könnte für die Betroffenen den gesellschaftlichen und/oder wirtschaftlichen Ruin
     bedeuten.
5. **Verstoß gegen Gesetze, Vorschrifte und/oder Verträge**
   - **Niedrig**: Geringfügige Vertragsverletzung mit maximal geringen Konventionalstrafen. Verstoß gegen Gesetze
     bzw. Vorschriften mit maximal geringen Konsequenzen.
   - **Mittel**: Vertragsverletzugen mit hohen Konventialstrafen. Verstoß gegen Gesetze bzw. Vorschriften mit
     erheblichen Konsequenzen.
   - **Hoch**: Vertragsverletzung mit für die de.NBI Cloud Bielefeld ruinösen Haftungsschäden. Verstoß gegen 
      Gesetze bzw. Vorschriften mit fundamentalen Konsequenzen.
6. **Zugangsverstöße**
   - **Niedrig**: Offenstehende Tür zu nicht sensiblen Bereiche (z.B. Büro).
   - **Mittel**: Offenstehende Tür zu sensiblen Bereichen (z.B. Serverraum). 
   - **Hoch**: Dauerhaft offenstehende/verkeilte und unbewachte Tür zu sensiblen Bereichen (z.B. Serverraum,
     zu Wartungszwecken)
7. Verlust/Diebstahl
   - **Niedrig**: Nach Richtlinie verschlüsseltes Notebook oder verschlüsselte externer Datenträger. Verlust eines
     Schließtoken oder physikalischen Schlüssel (Büroschlüssel)
   - **Mittel**: Einzelne Datenträger aus Servern. Komplette Server auf denen keine VM's gehostet sind. Verlust
     eines physikalischen Schlüssel (Gruppen bzw. Bereichsschlüssel).
   - **Hoch**: Komplette Server auf denen VM's gehostet werden. Verlust
     eines physikalischen Schlüssel (Generalschlüssel).

### Reaktion: Sofortmaßnahmen

Um potenzielle Folgeschäden zu begrenzen, sind alle betroffenen Mitarbeitenden und Teams dazu angehalten,
unverzüglich koordinierte Sofortmaßnahmen einzuleiten.

Bei IT-bezogenen Sicherheitsvorfällen sind folgende Maßnahmen zu ergreifen:

1. Notfalländerungen im Sinne von [IT-17.4](../it-verfahren.md#notfalländerungen)
1. Notfallabschaltung. Siehe [BCM](Business_Continuity.md).
1. Isolation von Systemen oder Nutzer-VMs.
1. Temporäre Sperrung von Benutzerkonten, Zugängen oder betroffenen Schnittstellen.

Bei physischen oder allgemeinen Sicherheitsvorfällen:

1. Unverzügliche Benachrichtigung der Leitwarte, beispielsweise bei unbefugten Personen und offenen Türen in den Datacenter.
1. Bei Gefahr von Leib und Leben ist die Polizei bzw. Rettungsdienste zu rufen.

In Fällen mit möglichem strafrechtlichem Bezug ist – sofern möglich – in Rücksprache mit der obersten Leitung die Polizei zu verständigen.

### Analyse und Ursachenforschung

Nach Umsetzung der Sofortmaßnahmen ist eine unverzügliche technische und organisatorische Analyse
des Vorfalls durchzuführen. Ziel ist die Identifikation der Ursachen und der betroffenen Systeme oder Daten.

1. Die Analyse ist im zugehörigen YouTrack-Ticket nachvollziehbar zu dokumentieren.

1. Je nach Art des Vorfalls sind forensische Maßnahmen durchzuführen.

Für Vorfälle im Kontext von Benutzer-Instanzen sind die Verfahren gemäß
[A5.28-Digitale-Beweissicherung](../erklaerung-zur-anwendbarkeit.md#digitale-beweismittelsicherung) zu beachten.

In strafrechtlich relevanten Fällen, bei denen die Polizei involviert ist, werden die Beweise
gesichert und entsprechend den rechtlichen Vorgaben übergeben.

In Fällen bei Verletzungen des Datenschutzes, sind die Informationssicherheitsbeuaftragten zu kontaktieren.
Siehe Auflistung weiter unten.

### Behebung und Wiederherstellung

Falls im Rahmen der Sofortmaßnahmen keine vollständige Wiederherstellung erfolgen konnte,
sind die zur Behebung des Vorfalls notwendigen technischen oder organisatorischen Maßnahmen
im Rahmen des regulären Change-Management-Prozesses umzusetzen und vollständig zu dokumentieren.

1. Dazu gehören z. B. Konfigurationsänderungen, Patches, Re-Deployment von Systemen, Bereinigungen von Logfiles oder Policies.

1. Der Wiederherstellungsstatus ist im YouTrack-Ticket festzuhalten.

### Verbesserungspotentiale

Das Auftreten eines Sicherheitsvorfall gibt Hinweise
auf das Versagen von scheinbar etablierten Prozessen und
Verfahren. Je nach Vorfall sollten gemeinsam
Verbesserungsmöglichkeiten dokumentiert und umgesetzt werden.

Sind die Ursachen auf die Nutzer zurückzuführen, so werden
diese Umfassend belehrt.

### Personen

| Name           | Funktion                         | Adresse                                 | Telefon            |
|----------------|----------------------------------|-----------------------------------------|--------------------|
| ADM            | Cloud-Administratoren            | service@bi.denbi.de                     | +49 521/106-2494   |
| PRT            | Portal-/SimpleVM Administratoren | cloud-helpdesk@denbi.de                 | +49 521/106-2494   |
| BRF            | CeBiTec Support                  | support@cebitec.uni-bielefeld.de        | +49 521/106-5662   |
| A. Sczyrba     | Leitung de.NBI Cloud             | sczyrba@fz-juelich.de                   | +49 521/106-2910   |
| S. Albaum      | Leitung BRF                      | alu@cebitec.uni-bielefeld.de            | +49 521/106-4821   |
| DISM Team      | Datenschutz- und Informationssicherheitsmanagement Universität Bielefeld   | dism@uni-bielefeld.de | - |
| Informationssicherheit | Informationssichheit Universität Bielefeld                         | informationssicherheit@uni-bielefeld.de | - |
| A. Rischmüller | Informationssicherheitsmanagerin | anja.rischmueller@uni-bielefeld.de      | +49 521 106-86401  |
| A. Schmid      | DSB Universität Bielefeld        | datenschutzbeauftragte@uni-bielefeld.de | +49 521/106-5225   |
| F. Rinkes      | ISB Forschungszentrum Jülich     | f.rinkens@fz-juelich.de                 | +49 2461/61-9005   |
| M. Weuthen     | DSB Forschungszentrum Jülich     | m.weuthen@fz-juelich.de                 | +49 2461/61-96049  |
| Leitwarte      | Leitwarte                        | leitwarte@uni-bielefeld.de              | +49 521/106-7777   |

## Dokumentation von IT-Sicherheitsvorfällen

Alle Schritte und Maßnahmen während eines Sicherheitsvorfalls werden unabhängig von der Einstufung der Schwere, 
sorgfältig dokumentiert. Die folgenden Informationen sollten mindestens festgehalten werden:

- Kurzbezeichnung
- Detaillierte Beschreibung
- Klassifizierung und Einordnung des Vorfalls (niedrig, mittel, hoch)
- Wer hat den IT-Sicherheitsvorfall wann gemeldet?
- Wann ist der IT-Sicherheitsvorfall aufgetreten?
- Wer war von dem IT-Sicherheitsvorfall betroffen?
- Wann wurde der IT-Sicherheitsvorfall gelöst?
- Was wurde zur Lösung des IT-Sicherheitsvorfalls unternommen?
- Was wurde unternommen, um ein erneutes Auftreten des Vorfalls in Zukunft wirksam zu verhindern?

Informationssicherheitsvorfälle werden im Issue Tracker innerhalb der Kategorie "Security Incidents" dokumentiert.

## Sensibilisierung

Aktuelle Sicherheitsvorfälle sind ein fester Themenpunkt in der wöchentlichen
Besprechung von ADM, PRT und BRF. Die Kenntnisnahme eines Vorfalls durch zu informierende
Personen wird im Issue Tracker als Teil der Vorfallsdokumentation registriert.

Die Nutzer der Cloud sind durch die Nutzungsbestimmungen der Cloud angehalten,
bekannt gewordene Sicherheitslücken oder Informationen über augenscheinlich
irrtümlich zugängliche Daten unverzüglich an den Betreiber zu melden.

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen
und weisen die Mitarbeiter ggf. auf Defizite hin.**
