# Richtlinie und Verfahren zur Informationsübertragung in der de.NBI Cloud Bielefeld

|                 |                                             |
|-----------------|---------------------------------------------|
| Version:        | 2.3                                         |
| Version vom:    | 23.06.2026                                  |
| Erstellt durch: | Jan Krüger, Viktor Rudko                    |
| Genehmigt am:   | 29.06.2026 (sa), 30.06.2026 (as)            |
| durch:          | Stefan Albaum (sa), Alexander Sczyrba (as)  |

# ChangeLog

- Version 2.3 vom 23.06.2026 - Kleinere Anpassungen 
- Version 2.2 vom 01.04.2025 - Verlinkung Cloud Services 
- Version 2.1 vom 05.03.2025 - Berücksichtigung der Transfers physischer Speichermedien
- Version 2.0 vom 02.01.2024 - aktualisierte Norm / FZJ
- Version 1.0 vom 09.03.2021
- Version 1.0RC vom 08.03.2021
- DRAFT vom 05.03.2021

# Zweck, Anwendungsbereich und Anwender

Der Zweck des Dokuments ist die Gewährleistung der Sicherheit von Informationen
oder Software beim Austausch innerhalb oder außerhalb der de.NBI Cloud
Bielefeld. Das Dokument gilt für den kompletten Anwendungsbereich des 
Informationssicherheits-Management-Systems (ISMS).

Anwender dieses Dokuments sind alle Mitarbeiter, sowie
gegebenenfalls auch externe Dienstleister. 

# Referenzen

- ISO 27001/27002 A5.14

## Richtlinien der de.NBI Cloud Bielefeld

- [Klassifikation und Kennzeichnung von Informationen](Klassifizierung_Kennzeichnung_von_Informationen.md)
- [Gebrauch von kryptographischen Maßnahmen](Gebrauch_von_kryptographischen_Maßnahmen.md)

## Sonstiges

- [IT-Verfahren 6.1 - Administrativer Zugang zum Management Netz](../it-verfahren.md#it-61-administrativer-zugang-zum-management-netzwerk)
- [Cloud Services](../aufstellungen/)
- [Aufstellung Videokonferenzsysteme](../aufstellungen/Videokonferenzsysteme.md)

# Übertragung von Informationen

Es ist stets darauf zu achten, dass Übertragung von Informationen nur über sichere
Kommunikationskanäle erfolgt. Werden Informationen über ein elektronisches
Kommunikationsmedium übertragen, müssen DSGVO-konforme Dienste genutzt werden. Dienste 
wie z. B. WhatsApp, Facebook, Google-Mail oder DropBox/Google-Drive dürfen daher 
für den Informationsaustausch nicht benutzt werden. Unabhängig vom verwendeten
Medium ist immer darauf zu achten, dass die Richtlinie zur 
[Kennzeichnung und Klassifikation von Informationen](Klassifizierung_Kennzeichnung_von_Informationen.md)
eingehalten wird.

Je nach Art der zu übertragenden Information ist darauf zu achten, das Maßnahmen zur 
Rückverfolgbarkeit bzw. Nichtabstreitbarkeit genutzt werden. Geeigneten Maßnahmen
wie z.B. digitale Signaturen, Hash-Funktionen, Zeitstempel und ein zentrales 
Protokollierungssystem hängen von dem verwendeten Kommunikationmedium ab. 

Eingehende digitale Informationen sollte auf Schadsoftware überprüft werden (z.B.
Scannen von E-Mail Anhängen auf Schadsoftware).

## Analoge Kommunikationswege

- **Telefon:** Interne oder vertrauliche Informationen dürfen niemals auf 
  Anrufbeantwortern hinterlassen werden, da nicht sichergestellt werden kann, dass die 
  auf diesem Wege übertragenen Informationen nur von berechtigten Personen empfangen 
  werden.
- **Fax:** Aufgrund seiner inhärenten Sicherheitsmängel und der Anfälligkeit für
  unautorisierten Zugriff oder Manipulation darf das Fax als Medium zur Übermittlung 
  von Informationen nicht genutzt werden.
- **Meetings:** In der Öffentlichkeit, in offenen Büros sowie an Versammlungsorten 
  (z.B. Kaffeemaschine oder Mensa) dürfen keine vertraulichen Gespräche geführt werden,
  da diese von unbefugten Personen mitgehört werden könnten. Bei vertraulichen Gesprächen
  sind alle beteiligten Personen auf die Vertraulichkeit hinzuweisen. Es ist darauf zu 
  achten, dass eine geeignete Gesprächslautstärke gewählt wird und Türen, sowie Fenster
  geschlossen sind.
- **Briefpost:** Interne Informationen dürfen in verschlossenen 
  Versandmappen per Briefpost innerhalb des Hauses bzw. innerhalb Deutschlands verschickt
  werden. Bei vertraulichen Informationen ist dieses Vorgehen nicht gestattet.

## Digitale physische Speichermedien

Als mögliche Speichermedien, welche für die physische Übertragung, wie etwa durch einen Versanddienstleister,
infrage kommen können sowohl die Festplatten des CEPH-Storage als auch die Root-Platten der
Compute-Knoten betrachtet werden.

Mögliche Szenarien für die physische Übertragung dieser Speichermedien stellen folgende Situationen dar:

- Hardware ist beschädigt
- Hardware wird an ein anderes Datacenter transferiert

Die Verantwortung für die Abwicklung eines möglichen Transfers liegt hierbei in Händen der BRF
(siehe [RASCI-Matrix der Aufgabenverteilung und Verantwortlichkeiten](../organisation.md#rasci-matrix-der-aufgabenverteilung-und-verantwortlichkeiten)).

Im Falle einer Beschädigung von Hardware ist durch die Gegebenheiten von bestehenden Wartungsverträgen
folgendes zu beachten:

- Handelt es sich bei der beschädigten Hardware um Datenträger, so werden diese durch
  entsprechende Dienstleister vernichtet. 
  Ein Versand der Hardware zu Reparaturzwecken an den Hersteller findet nicht statt. 
  Die Vernichtung wird entsprechend protokolliert und 
  der Hersteller sorgt nach Protokollierung der Vernichtung für entsprechenden Ersatz.
  Sollte für die betroffene Komponente kein laufender Wartungsvertrag bestehen, so wird die Hardware
  ersatzlos vernichtet.
- Handelt es sich um Hardware der Informationsverarbeitung, welche ebenfalls über Komponenten
  zur dauerhaften Speicherung von Daten verfügt, wie etwa die Root-Disks der Compute-Knoten,
  so werden die Datenträger vor Versenden der betroffenen Hardware entfernt und einbehalten. 

Somit findet bei Beschädigung von Hardware keine physische Übertragung von Datenträgern statt.

Im Falle eines Transfers an andere Datacenter ist ein hinreichend vertrauenswürdiger
Spediteur/Kurier für den Transport zu wählen, welcher ausreichend für die Sicherheit
des Transports garantieren kann. Wenn möglich, ist der Transport der Hardware zu begleiten.

### Kriterien für Kurier

Die Definition eines vertrauenswürdigen Kuriers für physikalische Datenträger im Rahmen des
ISMS ist wichtig, um die Vertraulichkeit, Integrität und Verfügbarkeit der darauf gespeicherten
Daten zu gewährleisten. Die folgenden Schritte sind verpflichtend bei der Auswahl eines
Kuriers zu berücksichtigen.

- **Verschlüsselung der Daten:**
  Die Daten sind in jedem Fall mit einem geeigneten Verfahren zu verschlüsseln, um die
  Vertraulichkeit selbst im Falle eines physischen Verlustes während des Transports zu
  schützen.
- **Zertifizierungen und Referenzen:**
  Der Kurierdienst sollte über eine anerkannte Zertifizierungen verfügen, wie z.B. ISO 27001,
  die internationale Norm für Informationssicherheitsmanagement. Es macht ggf. Sinn sich
  Referenzen von anderen Unternehmen einzuholen, die ähnliche Dienstleistungen in Anspruch
  genommen haben.
- **Vertragliche Vereinbarungen:**
  Es müssen Verträge abgeschlossen werden, welche die Sicherheitsanforderungen und
  Verantwortlichkeiten klar definieren. Es muss eine Vertraulichkeitsvereinbarung (NDA) 
  unterzeichnet werden.
- **Risikoanalyse:**
  Ein Transfer von physikalischen Datenträgern ist als Projekt mit Projektverantwortlichen und
  Sicherheitsverantwortlichen mit der ensprechenden Risikoanalyse zu dokumentieren
- **Versicherungen:**
  Der Kurierdienst sollte über geeignete Versicherungen für den Verlust
  oder die Beschädigung von Datenmedien verfügen.
- **Protokollierung und Überwachung:**
  Der Transfer ist gründlich zu dokumentieren (beispielsweise in dem Projektprotokoll)

Der nachfolgenden Schritte ist optional, aber empfehlenswert bei der Auswahl zu berücksichtigen:

- **Sicherheitsprotokolle:**
  Der Kurierdienst sollte spezifische Sicherheitsprotokolle umsetzen, wie z.B. GPS-Tracking von
  Fahrzeugen, versiegelte Verpackungen und das „Vier-Augen-Prinzip“ beim Transport vor allem bei
  sensitiven Daten.

## Digitale Kommunikationswege

- **JumpHost:** Der Zugang zum Management-Netz der Cloud-Infrastruktur erfolgt über
  verschlüsselt über einen JumpHost. 
  (➝ [IT 6.1](../it-verfahren.md#it-61-administrativer-zugang-zum-management-netzwerk))
- **E-Mail:** Die Kommunikation erfolgt intern ausschließlich über E-Mail-Accounts der
- Institute (`*.fz-juelich` `*.uni-bielefeld.de`). Eine Weiterleitung von diesen 
  E-Mail-Adressen an externe Anbieter wie z. B. Google oder Apple ist nicht gestattet.
  E-Mails müssen signiert werden.  Die Vorgaben der übergeordneten Organisation müssen
  berücksichtigt werden Je nach Klassifikation der zu verschickenden Information muss die
  E-Mail verschlüsselt werden. (➝ Klassifikation und Kennzeichnung von Informationen)
- **Chat:** Zum schnellen und direkten Austausch von Informationen nutzen
  die Mitarbeiter Matrix, sowie Signal/Threema für Notfälle. 
  Die Kommunikation ist in jedem Fall Ende-zu-Ende-verschlüsselt.
- **Videokonferenzen:** 
  Es kommen mehrere Systeme zum Einsatz. Bei der Auswahl ist unbedingt darauf zu achten,
  dass die ausgewählte Software den Bestimmungen der Datenschutzgrundverordnung sowie 
  der IT-Sicherheitsrichtlinie entspricht. Bei der Auswahl sind der Zweck der Veranstaltung
  sowie die technischen Möglichkeiten der Teilnehmenden zu berücksichtigen.
  (➝ [Aufstellung Videokonferenzsysteme](../aufstellungen/Videokonferenzsysteme.md) 
- **Cloud-Services:** Cloud-Services werden zum Austausch und zum gemeinsamen 
  Bearbeiten von Informationen genutzt. Hierfür dürfen nur Services in
  der entsprechend freigegebenen Klassifikationklasse genutzt werden.
  (➝ [Aufstellung Cloud Servcies](../aufstellungen/cloud-services.md) 
- **Repository Hosting:** Für das Hosting von Repositories muss für als intern 
  oder vertraulich klassifizierte Informationen das GitLab der Universität 
  Bielefeld bzw. der Forschungszentrum Jülich genutzt werden. Öffentliche
  Informationen können ausserdem auf öffentlichen Software-Repository-Services
  wie z.B. GitHub gehosted werden. (➝ GitLab UB, JuGit)

## Beziehungen zu externen Parteien

Die Kommunikation zu anderen de.NBI Cloud-Standorten oder Dienstleistern
(= externen Parteien) erfolgt grundsätzlich über die beschriebenen 
Kommunikationskanäle unter Berücksichtigung der Richtlinie zur
[Kennzeichnung und Klassifikation von Informationen](Klassifizierung_Kennzeichnung_von_Informationen.md).
Zusätzlich kann ein vom Dienstleister
zur Verfügung gestelltes Kommunikationssystem genutzt werden, sofern über dieses 
nur die zur Zusammenarbeit notwendigen Informationen ausgetauscht werden
(z.B. Ticketsystem).

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen
und weisen die Mitarbeiter ggf. auf Defizite hin.**
