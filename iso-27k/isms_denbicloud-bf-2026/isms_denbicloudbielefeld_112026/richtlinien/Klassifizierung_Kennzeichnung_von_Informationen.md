# Richtlinie zur Klassifizierung und Kennzeichnung von Informationen in der de.NBI Cloud Bielefeld

|                 |                                             |
|-----------------|---------------------------------------------|
| Version:        | 1.1                                         |
| Version vom:    | 08.03.2024                                  |
| Erstellt durch: | Jan Krüger, Christian Henke, Alex Walender  |
| Genehmigt am:   | 11.04.2025 (alu), 12.03.2024 (as)           |
| durch:          | Alexander Sczyrba (as), Stefan Albaum (alu) |

# ChangeLog

- Version 1.1 vom 08.03.2024: Verarbeitung personenbezogener Daten
- Version 1.0 vom 08.02.2024: Umgang mit Kopie von Informationen
- Version 0.4 vom 24.05.2022: Zugang zu internen Informationen angepasst
- Version 0.3 vom 14.03.2022: Hinweis auf Disclaimer entfernt; Tabellenformatierung
- Version 0.2 vom 07.04.2021: überarbeiteter Entwurf
- Version 0.2-beta vom 02.12.2020: überarbeiteter Entwurf
- Version 0.1-alpha vom 18.11.2020: initialer Entwurf

# Zweck, Anwendungsbereich und Anwender

Zweck dieses Dokuments ist die Sicherstellung des Schutzes von Informationen auf einem angemessenen
Niveau. Hierfür gilt es Informationen hinsichtlich ihrer Vertraulichkeit angemessen
zu klassifizieren. Die Richtlinie gilt für den kompletten Anwendungsbereich des
Informationssicherheits-Management-Systems (ISMS) der de.NBI Cloud Bielefeld, d.h.
für alle Arten von Informationen, unabhängig von deren Form - Papier oder elektronische
Dokumente, Anwendungen und Datenbanken, "Wissen", usw.

Kopien von Informationen sind immer in der gleichen Klassifikationsstufe einzuordnen wie das
Original.

Anwender dieses Dokuments sind alle Mitarbeiter von BRF und ADM sowie gegebenenfalls auch externe 
Dienstleister. Eine gewissenhafte Klassifizierung soll sowohl eine zu niedrige Einstufung und 
damit die Gefahr des Missbrauchs auf der einen Seite, als auch eine zu hohe Einstufung mit
einem nicht zu rechtfertigenden Aufwand auf der anderen Seite vermeiden.

## Klassifizierung von Informationen

### Klassifizierungskriterien

Die Vertraulichkeitsstufe wird auf der Basis folgender Kriterien festgelegt:

- Wert der Information, basierend auf der in der Risikoeinschätzung festgestellten
  Auswirkung (-> Risikomanagement)
- Trennung zwischen der Vertraulichkeitsklasse und der Verteilerliste
- Art der Information

Bei der Klassifizierung von Informationen wird zwischen 4 verschiedenen Vertraulichkeitsklassen 
K1 bis K4 (öffentlich, eingeschränkt/intern, vertraulich und streng vertraulich) unterschieden:

1. **öffentlich (K1)**: Informationen zur uneingeschränkten Veröffentlichung. Zu diesen 
  Informationen gehört beispielsweise die Dokumentation zur Nutzung der de.NBI Cloud für 
  Endanwender, Tutorials und öffentliche Repositories in GitHub/GitLab. 

1. **eingeschränkt/intern (K2)**: Informationen, die nur für Mitarbeiter
  von BRF und ADM bestimmt sind und für den alltäglichen Dienstbetrieb notwendig sind. Nicht 
  gekennzeichnete Informationen gelten grundsätzlich als *eingeschränkt*, soweit deren Inhalte 
  nicht einen noch höheren Schutz erforderlich machen oder es sich um öffentliche 
  Informationen (K1) handelt. 
  Zu diesen Informationen gehören beispielsweise das ISMS, Arbeitsanweisungen und die privaten 
  Repositories in GitHub/GitLab inklusive der Ansible Playbooks zur Initialisierung und Wartung 
  der Cloud-Infrastruktur ohne Zugangsdaten (u.a. Passwörter und private Schlüssel).

1. **vertraulich (K3)**: Informationen, deren Veröffentlichung oder Verlust zu einem Schaden
  oder Imageverlust der Organisation führt, sowie alle sensiblen personenbezogenen und -beziehbaren
  Daten im Sinne der geltenden datenschutzrechtlichen Bestimmungen (§9 DSGVO).
  Zu den Informationen gehören in Bezug auf die de.NBI Cloud Bielefeld
  beispielsweise die Zugangsdaten der Cloud-Infrastruktur 
  (u.a. Passwörter und private Schlüssel), sämtliche in der Infrastruktur genutzten Systeme zur
  elektronischen Datenverwaltung (u.a. Cloud Datenbanken und Key-Value-Speicher), die Systemplatten der
  Cloud-Infrastruktur-Systeme, sowie die virtuellen Instanzen und der Speicher des Cloud-Storage-Systems,
  sofern keine besonders schützenswerten Informationen darauf abgelegt sind (siehe K4).

1. **streng vertraulich (K4)**: Informationen, deren Veröffentlichung oder Verlust einen
  erheblichen Schaden oder Imageverlust der Organisation zur Folge hat. Hierzu
  gehören beispielsweise sensible personenbezogene oder -beziehbare medizinische Daten (§9 DSGVO),
  der Geheimhaltung unterliegende Daten sowie eine Datenverarbeitung in Zusammenarbeit mit
  Dritten gemäß einer entsprechenden vertraglichen Verpflichtung.
 
Die Kriterien zur Einstufung des Schadensmaßes sind der jeweils aktuellen
Risikomanagementdokumentation zu entnehmen.

## Kennzeichnung von Informationen

Informationen, die im Betrieb der de.NBI Cloud Bielefeld verarbeitet, transportiert 
oder gespeichert werden, sind den Vertraulichkeitsklassen K1 bis K4 zuzuordnen. 
Bei der Erstellung, Änderung oder Übertragung von Informationen im Betrieb der 
de.NBI Cloud Bielefeld sind diese durch Angabe der Vertraulichkeitsklasse je nach verwendetem 
Medium geeignet zu kennzeichnen. Informationen, die der Vertraulichkeitsklasse K2
zuzuordnen sind, müssen nicht gesondert gekennzeichnet werden. Bei einer nicht eindeutigen 
Zuordenbarkeit von Informationen zu einer Klasse sind diese *immer* der jeweils höheren Klasse
zuzuordnen.

### Papierdokumente

Die Vertraulichkeitsstufe wird auf jeder Seite des Dokuments
angegeben; ebenso wird sie auf der Vorderseite des Deckblatts sowie ggf. dem
Aktenordner angegeben, in dem das Dokument abgelegt ist. 

### Elektronische Dokumente

Elektronische Dokumente sind durch Wasserzeichen bzw. Textmarken in Kopf- und Fußzeile
gekennzeichnet.

### Elektronische Post (E-Mail)

Die Vertraulichkeitsstufe wird in der ersten Zeile des E-Mail-Inhalts angegeben.

### Elektronische Datenträger

Bei der Kennzeichnung von elektronischen Datenträgern wird an dieser Stelle zwischen
Medien unterschieden, die zum Transport von Informationen genutzt werden
(Speicherkarten, USB-Sticks, "externe" Festplatten, usw .)
und Datenträgern (HDD/SSD), die fest in Servern verbaut sind.

#### Speicherkarten, USB-Sticks, "externe" Festplatten, usw

Mobile Datenträger müssen gemäß der Vertraulichkeitsstufe der auf ihnen gespeicherten
Informationen sichtbar gekennzeichnet sein.

#### Festplatten

Datenträger (Festplatten - HDDs bzw. SSDs) die in Servern verbaut sind, welche in den
genutzten Datacentern der Universität Bielefeld (V0-200 oder W01-178) stehen, müssen 
– sofern sie nicht vorher sicher gelöscht wurden – beim Verlassen des Datacenters
entsprechend der Vertraulichkeitsstufe gekennzeichnet werden.

### Software-Repositories

Werden Software-Repositories auf Basis von GitLab oder vergleichbar zur Speicherung 
von Informationen genutzt so ist darauf zu achten, dass die Zugriffsrechte dem
Erforderlichkeitsprinzip folgen.

### Mündlich weitergegebene Informationen

Werden Informationen in einem Gespräch weitergegeben, so ist *vorher* die 
Vertraulichkeitsklasse zum Ausdruck zu bringen. 

# Sicherheitsmaßnahmen zum Schutz der Vertraulichkeit

Die Sicherheitsmaßnahmen zum Schutz der Vertraulichkeit richten sich nach der 
Informationsklassifizierung. Die beschriebenen Maßnahmen stellen die Mindestanforderungen
an den Schutz der entsprechenden Informationen dar und schließen grundsätzlich strengere
oder alternative Maßnahmen, die zum Beispiel aus Verträgen mit dritten resultieren, nicht
aus.

Bei Speicherung, Verarbeitung und Übermittlung personenbezogener und
personenbeziehbarer Daten sind die geltenden Datenschutzbestimmungen zu beachten.

## Maßnahmen für Informationen 

| Vertraulichkeitsstufe | K1                  | K2            | K3              | K4               |
|-----------------------|---------------------|---------------|-----------------|------------------|
| Zugriffsschutz/Zugang | keine Einschränkung | eingeschränkt | eingeschränkt** | eingeschränkt*** |
| Speichern (intern)    | unverschlüsselt     | ⇐             | ⇐               | verschlüsselt    |
| Speichern (extern)    | unverschlüsselt     | verschlüsselt | ⇐               | nicht erlaubt    |
| Speichern (mobil)     | unverschlüsselt     | verschlüsselt | ⇐               | nicht erlaubt    |
| E-Mail (intern)       | unverschlüsselt     | ⇐             | verschlüsselt   | ⇐                |
| E-Mail (extern)       | unverschlüsselt     | verschlüsselt | ⇐               | nicht erlaubt    |

- ⇐ es gelten die Einschränkungen/Eigenschaften der nächstkleineren Klasse
- ** Erforderlichkeitsprinzip
- *** Genehmigung vom Informationseigentümer; definierter und protokollierter Personenkreis

## Maßnahmen von Personen

| Vertraulichkeitsstufe       | K1                  | K2                        | K3                          | K4                       |
|-----------------------------|---------------------|---------------------------|-----------------------------|--------------------------|
| Umgang mit mobilen Geräten  | keine Einschränkung | verschlüsselt speichern   | verschlüsselte Geräte       | ⇐                        | 
| Bildschirmsperre            | keine Einschränkung | automatische Sperre       | ⇐                           | ⇐                        |
| Zutrittskontrolle           | keine Einschränkung | allgemeines Schließsystem | protokollierter Zugang      | ⇐+ Videoüberwachung      |
| Telearbeit                  | keine Einschränkung | Dienstgerät               | verschlüsseltes Dienstgerät | ⇐+ kontrollierter Zugang |
| Softwareinstallation        | keine Einschränkung | vertrauenswürdige Quelle  | ⇐                           | freigegebene Software    | 
| Entsorgung von Datenträgern | keine Einschränkung | Sicheres Löschen          | ⇐                           | ⇐                        |

- ⇐ es gelten die Einschränkungen/Eigenschaften der nächstkleineren Klasse
- ⇐+ die Einschränkungen/Eigenschaften der nächstkleineren Klasse werden erweitert um ...

# Zugang zu Informationen

## Eingeschränkte / Interne Information

Eingeschränkte bzw. interne Informationen sind grundsätzlich allen Mitarbeitern der Gruppen ADM 
und BRF im jeweils notwendigen Umfang zugänglich. Sollten interne Informationen Externen 
(z.B. Interner Auditor) zugänglich gemacht werden müssen, so sind diese entsprechend zu kennzeichnen.

## Vertrauliche Informationen

Vertrauliche Informationen sind grundsätzlich nur den Mitarbeitern der Gruppen ADM und BRF
zugänglich, die diese regelmäßig zur Bearbeitung zwingend benötigen 
(Erforderlichkeitsprinzip).

## Streng vertrauliche Informationen

Streng vertrauliche Informationen sind ausschließlich einem definierten und dokumentierten
Personenkreis zugänglich.

# Verschlüsselung von Informationen

Die Anwendung von Verschlüsselungstechnologien dient zur Sicherstellung der Vertraulichkeit 
von Informationen bei Übertragung und Speicherung.
Die Mindeststandards des BSI sind hierbei insbesondere für TLS einzuhalten
(<https://www.bsi.bund.de/mindeststandards>).

Die Aufbewahrung der Informationen in Applikationen oder Datenbanken mit restriktivem
Zugriffsschutz und Zutrittskontrollen auf allen Ebenen stellt eine sinnvolle
Ergänzung zur Verschlüsselung dar.

Ein vom Rest des Netzwerks abgeschirmtes Teilnetz stellt eine Alternative zur 
Transportverschlüsselung dar, sofern ein restriktiver Zugriffsschutz und Zutrittskontrollen 
gewährleistet sind. 

Es dürfen keine Informationen über den Schlüssel mitgespeichert oder übertragen werden.

Ein nicht verschlüsselter Textteil einer E-Mail soll keinen Hinweis auf den vertraulichen Inhalt 
der verschlüsselten Informationen oder auf den Schlüssel geben.

# Entsorgung von Information

Die Entsorgung von Information muss gemäß ihrer Klassifikation erfolgen.

| Vertraulichkeitsstufe     | K1         | K2                              | K3  | K4       |
|---------------------------|------------|---------------------------------|-----|----------|
| Elektronische Datenträger | Entsorgung | Sicher löschen **^**            | ⇐   | ⇐        |
| Papierdokumente           | Entsorgung | Sicher entsorgen (> P2)  **^^** | ⇐   | ⇐ (> P5) |
| Repositories / Volumes    | Löschen    | Sicher löschen **^^^**          | ⇐   | ⇐        |

- **^** Sicher löschen: Falls eine Festplatte nicht sicher gelöscht werden kann, z.B. wegen eines
  Defekts, so muss diese Festplatte physisch beschädigt oder zerstört werden. Dies gilt auch für 
  Speichermedien wie CD/DVDs oder USB-Sticks.
- **^^** Sicher entsorgen: Je höher die Klassifikationsklasse der Dokumente, desto höher muss die
  Sicherheitsstufe/Zerkleinerungsklasse (P1 - P7) des verwendeten Aktenvernichters sein.
  Ausdrucke und Akten können ebenso wie Datenträger vertrauliche Daten enthalten. Diese
  sind so zu vernichten, dass die ursprünglichen Informationen nicht wiederhergestellt
  werden können. Beachten Sie vor der Vernichtung von Akten der Universität unbedingt
  die „Richtlinien über Aufbewahrung, Aussonderung, Archivierung und Vernichtung von Akten“.
  Für grössere Mengen wird mehrfach jährlich nach Bedarf eine Aktenvernichtung durch die
  Sachbearbeitung Abfallwirtschaft (abfallwirtschaft@uni-bielefeld.de) organisiert. Für
  kleine Aktenmengen steht in den Dienstzeiten in der Zentralverwaltung ein Aktenvernichter
  zur Verfügung, der eine ausreichend hohe Sicherheitsstufe besitzt. Nähere Hinweise zur
  Aktenvernichtung finden sich auf den [Internetseiten der Abfallwirtschaft](http://www.uni-bielefeld.de/abfall).
  Bei der Beschaffung eines eigenen Aktenvernichters
  sind die DIN 32757 bzw. mindestens die Sicherheitsstufe 3 zu beachten.
- **^^^** Löschen von Repositories oder Volumes: Sofern das unterliegende Dateisystem sicheres 
  Löschen nicht unterstützt, müssen Repositories oder Volumes mit spezieller 
  Software durch Überschreiben vollständig und nicht wiederherstellbar gelöscht werden. Dabei 
  werden die Daten einmal oder mehrfach mit Zufallsdaten überschrieben.
