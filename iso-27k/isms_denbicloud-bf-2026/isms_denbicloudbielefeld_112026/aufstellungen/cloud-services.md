# Externe Cloud-Services

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Version:        | 1.2                                                      |
| Version vom:    | 27.02.2025                                               |
| Erstellt durch: | Jan Krüger, Christian Henke, Alex Walender, Viktor Rudko |
| Genehmigt am:   | -                                                        |
| durch:          | -                                                        |

Die Aktualität der Aufstellung wird regelmässig durch ein REDO-Ticket überprüft. Die Bewertung bzw. Einschränkung
erfolgt im Rahmen eines REDO-Tickets und muss durch das Management genehmigt werden.

| Name        | Funktion                  | Einschränkung / Bewertung                                                   |
|-------------|---------------------------|-----------------------------------------------------------------------------|
| Zoom        | Videokonferenz            | Nicht für vertrauliche Gespräche (K4)                                       |
| Teams       | Videokonferenz            | Nicht für vertrauliche Gespräche (K4)                                       |
| DFNConf     | Videokonferenz + Kalender | keine Einschränkung                                                         |
| Sciebo      | Storage + Office          | Nur für Informationen bis einschließlich Schutzklasse K3                    |
| GoogleDrive | Storage + Office          | Nur für öffentliche Daten (K1), Ausnahme: Kooperation mit Nicht-EU Partnern |
| GitLab      | Versionsverwaltung        | Nur für Informationen ohne hohen Schutzbedarf (K2)                          |
| GitHub      | Versionsverwaltung        | Nur für Informationen ohne hohen Schutzbedarf (K2)                          |
| Office365   | Storage + Office          | Nur für Informationen bis einschließlich Schutzklasse K3                    | 
| ChatGPT     | Textgenerierung (AI)      | Nur für öffentliche Informationen (K1)                                      |
| -           | Übersetzungsdienste       | Nur für öffentliche Information (K1)                                        |
| DeepL       | Übersetzungsdienste       | Nur für Informationen ohne hohen Schutzbedarf (K2)                          |
| Matrix      | Chat                      | keine Einschränkungen (ist Ende-zu-Ende-verschlüsselt)                      |
| Threema     | Chat (Notfall)            | keine Einschränkungen (ist Ende-zu-Ende-verschlüsselt)                      |
| Signal      | Chat (Notfall)            | keine Einschränkungen (ist Ende-zu-Ende-verschlüsselt)                      |

# Interne Cloud-Services

Die internen Cloud-Services werden von uns selbst betrieben oder von der übergeordneten Organisation angeboten und
unterliegen, sofern nicht anders angegeben keinerlei Beschränkungen.

| Name                 | Funktion                      | Einschränkung                       |
|----------------------|-------------------------------|-------------------------------------|
| BigBlueButton (FZJ)  | Videokonferenz                | keine                               |
| Jitsi (BRF)          | VC                            | keine                               |
| docs.denbi.de        | Storage + Office              | keine                               |
| ThinLinc             | Remote Desktop                | keine                               |
| ai.bi.denbi.de       | Textgenerierung (AI) - Web-UI | keine (für lokal gehostete Modelle) |
| ollama.bi.denbi.de   | Textgenerierung (AI) - API    | keine (für lokal gehostete Modelle) |
| llm.bi.denbi.de ([Architektur](../assets/llm-api.png)) | Textgenerierung (AI) - API | keine (für lokal gehostete Modelle) | 

# Anhang: detaillierte Bewertung von externen Cloud-Services

## Zoom

Die Bewertung bezieht sich ausschließlich auf das Produkt Videokonferenz und *nicht*
auf andere von Zoom angebotene Services (z.B Chat, EMail). 

- [Datenschutzerklärung](https://explore.zoom.us/de/privacy/) 
- Zoom ist ein US-Unternehmen mit Servern, die nicht zwingend in Europa stehen. Es ist unklar, ob z.B. Metadaten
  auch auf Servern in den USA gespeichert werden, bzw. ob das Unternehmen bei
  entsprechendem Druck seitens der Regierung nicht auch Daten aushändigt, die auf europäischen
  Servern gespeichert sind.
- Erlaubt den Austausch von Metadaten auch mit Dritten, sofern diese für den Betrieb
  erforderlich sind oder Zoom in Frameworks von Dritten integriert ist.
- Ende-zu-Ende Verschlüsslung ist möglich, wenn alle Teilnehmer den Desktop-Client oder
  die Mobile-App nutzen.

**Der Service ist durch die übergeordnete Organisationen (FZJ, UniBi) für nicht
vertrauliche Gespräche freigegeben. Dieser Bewertung schließt sich die 
de.NBI Cloud Bielefeld an.**

## Teams / Office 365

Die Bewertung bezieht sich auf das Produkt Office 365 inkl. Teams.

- [Datenschutzerklärung](https://privacy.microsoft.com/de-de/privacystatement)
- Microsoft ist ein US-Unternehmen mit Servern in Deutschland/Europa und unterliegt
  damit der DSGVO. Aber vermutlich muss Microsoft bei Anfragen bzw. auf Druck der US-Regierung auch Daten weitergeben
  die auf europäischen Servern gespeichert sind.
- Teams bietet eine Ende-zu-Ende-Verschlüsselung bei Einzelanrufen.

**Der Service ist durch die übergeordnete Organisation (FZJ) für nicht
vertrauliche Gespräche bzw. Informationen freigegeben. Dieser Bewertung schließt
sich die de.NBI Cloud Bielefeld an.**

## DFN Conf

Die Bewertung bezieht sich auf die Kalender- und Videokonferenzfunktion.

- [Datenschutzerklärung](https://www.conf.dfn.de/datenschutz)
- Login/Anmeldung über DFN-AAI (als IDP-Proxy)
- Server in Deutschland

**Der Service ist ohne Einschränkung für die Nutzung freigegeben.**

## Sciebo

- [Datenschutzerklärung](https://hochschulcloud.nrw/de/datenschutz/dienst.html)
- Server in NRW/Deutschland
- Login/Anmeldung über das universitäre bzw. forschungszentrumseigene SSO

**Der Service ist durch die übergeordnete Organisationen (FZJ, UniBi) für nicht
vertrauliche Informationen freigegeben. Dieser Bewertung schließt sich die de.NBI
Cloud Bielefeld an.**

## Google Drive

Die Bewertung bezieht sich ausschliesslich auf Google Drive / Google Docs.

- [Datenschutzerklärung](https://policies.google.com/privacy?hl=de)
- Google ist ein US-Unternehmen mit Servern, die nicht zwingend in Europa stehen. 
  Es ist unklar, ob das Unternehmen bei entsprechendem Druck seitens der Regierung
  nicht auch Daten aushändigt, die auf europäischen Servern gespeichert sind.

**Der Service ist durch die übergeordnete Organisationen (FZJ, UniBi) nur für
Kooperationen mit Dritten für nicht vertrauliche Informationen freigegeben. 
Die de.NBI Cloud Bielefeld erlaubt darüber hinaus die Nutzung in Ausnahmefällen
(Kooperatives Arbeiten) für Informationen bis einschliesslich K1**

## GitLab (UniBi, FZJ)

Für Teile der relevanten Repositorien wird die von der Universität Bielefeld 
betriebene GitLab-Installation als Platform für die Versionsverwaltung
genutzt.  Einzelne Repositories sind in das GitLab des Forschungszentrum Jülich 
gespiegelt.

Von beiden Organisationen wird die Open-Source-Variante *Community Edition* 
betrieben.

Da es sich um einen von einer zugehörigen Organisation betriebenen Dienst
handelt, ist die Nutzung für Daten bis zur Stufe K2 (eingeschränkt/intern)
ohne weitere Einschränkungen freigegeben.

## GitHub

- [Datenschutzerklärung](https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement)
- GitHub ist durch die Zugehörigkeit zum Microsoft-Konzern ein
  US-Unternehmen, welches Server primär in den USA betreibt.
  Es ist unklar, ob das Unternehmen bei entsprechendem Druck seitens der Regierung
  nicht auch Daten aushändigt.

Ein weiteres Git-basiertes Versionsverwaltungssystem ist die, mittlerweile
dem Microsoft-Konzern zugehörige Platform GitHub.
In der dort angelegten de.NBI Organisation befinden sich zahlreiche,
mehrheitlich öffentliche Repositorien, aber auch ebenfalls private
Repositorien, welche mitunder den Quell-Code und Konfigurationen,
aber keine kritischen Variablen und/oder Secrets für die jeweilige
Software bzw. Software-Komponente des Repositoriums behinhaltet.
Dies betrifft private Repositorien für das de.NBI Cloud Portal,
die dazugehörige Landing-Page als auch die Repositorien
für die Komponenten von SimpleVM.
Die in GitHub abgelegten Informationen sind also als Daten
bis zur Stufe K2 (eingeschränkt/intern) zu betrachten. 
Legt man GitHubs [General Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement#private-repositories-github-access)
(Stand: 01.02.2024) zugrunde, gilt für private Repositorien:
Mitarbeitende von GitHub haben ohne die entsprechende Erlaubnis
keinen Zugriff auf als *privat* deklarierte Repositorien.
Ausnahmen sind automatische Scans auf mögliche Schwachstellen,
Schadsoftware oder Inhalte, welche den Nutzungsbestimmungen
der Platform wiedersprechen.
**Die de.NBI Cloud Bielefeld erlaubt die Nutzung für Daten bis
zur Stufe K2 (eingeschränkt/intern).**

## ChatGPT

- [Datenschutzerklärung](https://openai.com/policies/privacy-policy)
- Der Anbieter OpenAI beschreibt in seinen Datenschutzrichtlinien, wie die 
  verarbeiteten Daten geschützt und verwendet werden – die Sicherheit der Daten ist
  jedoch nicht garantiert.
- Aktuell unterliegt ChatGPT einer datenschutzrechtlichen Prüfung durch die deutschen
  Aufsichtsbehörden und es ist unklar, inwieweit der Einsatz mit Blick auf die DSGVO
  überhaupt zulässig ist.
- Die Technologie gilt für Datenschützer als Blackbox – solange die Verarbeitung und
  Verwendung eingegebener Daten unklar ist, sollte auf die Eingabe persönlicher Daten
  verzichtet werden.

**Der Service ist durch die übergeordneten Organisationen (FZJ, UniBi) für die Nutzung
eingeschränkt freigegeben (keine Eingabe persönlicher oder nicht öffentliche 
Informationen). Dieser Einschätzung schließt sich die de.NBI Cloud Bielefeld an.**

## Übersetzungsdienste

Die üblichen Online-Übersetzungsdienste wie z.B. leo.org oder Google Translate werden 
*nicht* im Einzelnen bewertet, sondern sind für öffentliche Informationen freigegeben,
solange keine vollständigen Texte bzw. zusammenhängenden Abschnitte übertragen werden.

## DeepL

Der Übersetzungsservice DeepL wurde ins BIS integriert, um den MA der Universität
Bielefeld eine verlässliche Übersetzungsressource anbieten zu können. Desweiteren
verfügen alle Mitarbeitenden des Forschungszentrum Jülich über eine Pro-Lizenz,
welche sowohl die Übersetzungs- als auch die Texttransformierungsfunktionalität
auf der Platfrom [deepl](deepl.com) beinhaltet.

- [Nutzungshinweise](https://www.uni-bielefeld.de/einrichtungen/bits/ueber-uns/benutzungsordnung/deepl/nutzungshinweise/)

**Der Service ist durch die übergeordneten Organisationen (UniBi, FZJ) für die Nutzung
eingeschränkt freigegeben (keine Eingabe persönlicher oder nicht öffentliche
Informationen). Dieser Einschätzung schließt sich die de.NBI Cloud Bielefeld an.**

## Matrix

_Matrix_ ist ein offener, dezentraler Kommunikationsdienst für die Echtzeitkommunikation (Chat).
Die Universität Bielefeld betreibt einen Matrix-Server unter Einhaltung der einschlägigen 
gesetzlichen und rechtlichen Bestimmungen zum Datenschutz und zur IT-Sicherheit.

- [Datenschutzerklärung](https://www.uni-bielefeld.de/einrichtungen/bits/services/kommunikation/teamchat/policy/datenschutzhinweise/)
- Alle Nutzdaten sind vollständig Ende-zu-Ende verschlüsselt.

**Der Service ist ohne Einschränkung für die Nutzung freigegeben.**

## Threema

_Threema_ ist mit der Europäischen Datenschutz-Grundverordnung (DSGVO) konform. Als Schweizer
Unternehmen ist Threema zusätzlich dem strengen Schweizer Datenschutzgesetz (DSG) sowie der
Verordnung zum Bundesgesetz über den Datenschutz (VDSG) unterworfen. 

- [Datenschutzerklärung](https://threema.ch/de/privacy-policy)
- Alle Nutzdaten sind vollständig Ende-zu-Ende verschlüsselt.

**Der Service ist ohne Einschränkung für die Nutzung freigegeben.**

## Signal

_Signal_ gilt als ein sehr sicherer, DSGVO-konformer Kommunikationsdienst für die Echtzeitkommunikation.

- [Datenschutzerklärung](https://signal.org/legal/)
- Sämtliche Kommunikation ist Ende-zu-Ende verschlüsselt.

**Der Service ist ohne Einschränkung für die Nutzung freigegeben.**

