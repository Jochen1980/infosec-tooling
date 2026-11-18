# Richtlinie für sichere Softwareentwicklung

|                 |                                             |
|-----------------|---------------------------------------------|
| Version:        | 0.8                                         |
| Version vom:    | 11.06.2026                                  |
| Erstellt durch: | Jan Krüger, Christian Henke, Alex Walender, |
|                 | Viktor Rudko                                |
| Genehmigt am:   | 29.06.2026 (sa), 30.06.2026 (as)            |
| durch:          | Stefan Albaum (sa), Alexander Sczyrba (as)  |

# ChangeLog

- Version 0.8 vom 11.06.2026: OWASP Cheat Sheets
- Version 0.7 vom 21.01.2024: Sicherheitsprüfungen
- Version 0.6 vom 20.01.2024: Externe Entwicklungen
- Version 0.5 vom 31.01.2024: Formulierungen
- Version 0.4 vom 04.04.2023: Virtuelle Umgebung als zu bevorzugende Entwicklungsumgebung
- Version 0.3 vom 28.05.2021: Einhaltung einer sicheren Vorgehensweise angepasst
- Version 0.2 vom 05.02.2021: Typos, Formulierung angepasst
- Version 0.1 vom 29.01.2021: initialer Entwurf

# Zweck, Anwendungsbereich und Anwender

Die de.NBI Cloud Bielefeld steht in einigen Bereichen vor der Herausforderung
für den Cloud-Betrieb unzureichender Standardsoftware.
In diesem Fall muss die Software individuell angepasst oder gar eigens
entwickelt werden.

Die Richtlinie zur sicheren Entwicklung von Software soll sicherstellen, dass
auch bei der Entwicklung neuer Software bzw. Anpassung bestehender Software
die Informationssicherheit über den gesamten Entwicklungsprozess hinweg
berücksichtigt wird.
Anwendungsbereich ist die Entwicklungsumgebung der Cloud-Infrastruktur.

Die Richtlinie ergänzt den IT-Basisschutz der Universität Bielefeld
und berücksichtigt ISO 27002, insbesondere Abschnitte 8.28 bis 8.31.

## Definition von Rollen und Verantwortlichkeiten

Der Leiter der Organisation legt bei einem neuen Projekt die Rollen
und Verantwortlichkeiten für dieses fest. Ein Projektteam **muss**
mindestens aus dem Projektverantwortlichen (Leiter der Entwicklung)
und einem zusätzlichen Entwickler bestehen. Für jedes Projekt **muss**
außerdem ein Sicherheitsverantwortlicher benannt werden.

## Auswahl eines Vorgehensmodells

Das Projektteam legt bei Projektbeginn ein geeignetes sicheres Vorgehensmodell
(z.B. Wasserfallmodell oder V-Modell) fest. Alle an der Projektentwicklung
beteiligten Mitarbeiter sollten mit der Methodik des gewählten Vorgehensmodells
vertraut sein.

## Auswahl einer Entwicklungsumgebung

Die Entwicklungsumgebung ist durch die Infrastruktur der Cloud vorgegeben.
Die Arbeitsumgebung der Entwickler ist das Arbeitsnotebook oder eine
Remote-Desktop-Session im CeBiTec.
Die Entwicklung sollte, sofern möglich, in einer virtuellen Umgebung
(z.B. in einem dafür vorgesehenen Openstack Projekt) erfolgen und erst
in einem fortgeschrittenen Entwicklungsstadium in der Entwicklungscloud
getestet werden.
Der Zugriff auf die Entwicklungscloud erfolgt ausschließlich aus dem
CeBiTec-Netz (ggf. via VPN) über einen dafür vorgesehen Jump-Host.
Die Entwicklung sollte, wenn möglich, mit Unterstützung durch eine
geeignete integrierte Entwicklungsumgebung (IDE) erfolgen (z.B. IntelliJ
und Abkömmlinge, VCS, ...). Die Entwickler **müssen** sich auf etablierte
und ggf. angepasste _Linting_ Standards einigen (z.B. `pylint` oder
`flake8` für Python, `ansible-lint` für ansible, ...). Moderne IDE
bieten hier i.d.R. schon sinnvolle Standards für gängige Programmier- bzw.
Auszeichnungssprachen.

## Einhaltung einer sicheren Vorgehensweise

Die Einhaltung einer sicheren Vorgehensweise bei der Projektentwicklung **muss**
durch den Sicherheitsverantwortlichen sichergestellt und überwacht werden.
Der sichere Betrieb des Projekts auf der Entwicklungsumgebung muss
sichergestellt werden, **bevor** das Projekt auf der Produktionsumgebung eingesetzt
werden darf.

Wird neue oder angepasste Software integriert, welche für hinreichend schwere Änderungen sorgt, die eine Prüfung
hinsichtlich der Sicherheit für den Gesamtbetrieb erfordert, ist die Test-Umgebung zu nutzen,
um von Außen erreichbare Komponenten auf mögliche Schwachstellen zu prüfen.
Wie für die Produktionsumgebung ist hier OpenVas zu nutzen.
Die Test-Umgebung umfasst ebenfalls eine Funktionsprüfung mithilfe von Rally, siehe [IT-4.10.3.6](../it-verfahren.md#it-41036-rally).
Bei der Prüfung auftretende Probleme sind zu begutachten und zu lösen, bevor eine Integration vorgenommen werden kann.

(Unit-)Tests stellen einen üblichen und nachvollziehbaren Weg dar, um eine sichere Funktionalität
in der Softwareeinwicklung zu erreichen (Test-Driven-Development).

Die Prinzipien der strukturierten Programmierung müssen umgesetzt werden.

## Sicheres Systemdesign

Die Grundregeln des sicheren Systemdesigns **müssen** eingehalten werden:

- **Systemrechte**: Das System darf nur die für den Einsatz minimal nötigen Rechte einfordern.
- **Standardkonfiguration**: Die Standardkonfiguration der Software muss einen sicheren Betrieb
  ermöglichen.
- **Abhängigkeiten**: Überprüfung aller externen Bibliotheken und Frameworks auf
  bekannte Sicherheitslücken und daraus folgende zwingende Aktualisierung.
- **Autorisierung**: Überprüfung der korrekten Implementierung der Autorisierungslogik
  korrekt implementiert ist und Benutzer nur Zugriff auf die für sie bestimmten Ressourcen haben.
- **Sensible Daten**: Sichere Speicherung sensibler Daten wie Passwörter
  und persönliche Informationen.
- **Input-Validierung**: (Serverseitige) Überprüfung aller Eingaben auf Gültigkeit
  um Injektionsangriffe zu verhindern.
- **Fehlerbehandlung**: Implementierung einer sicheren Fehlerbehandlung, die keine sensiblen
  Informationen preisgibt.
- **Kennwörter**: Fest kodierte Kennwörter im Programmcode sind grundsätzlich nicht erlaubt.
- **Penetrationstest**: Durchführung von Penetrationstests um die Wirksamkeit der
  Sicherheitsmaßnahmen zu überprüfen und Schwachstellen zu identifizieren.

Die entwickelte Software ist mittels der [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org)
aus allen sicherheitsrelevanten Perspektiven zu beleuchten.
Beispielsweise müsste eine im Docker-Container verpackte Django-Webanwendung mindestens folgende Themen berücksichtigen:

- [Docker Security](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [Django Security](https://cheatsheetseries.owasp.org/cheatsheets/Django_Security_Cheat_Sheet.html)
- [Django REST Framework](https://cheatsheetseries.owasp.org/cheatsheets/Django_REST_Framework_Cheat_Sheet.html)
- [Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [REST Security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
- [HTTP Strict Transport Security](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
- [Transport Layer Security](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

Abhängig von der verwendeten Web-Frontend-Bibliothek kämen weitere Themen hinzu.

Der Sicherheitsverantwortliche muss die mindestens zu berücksichtigende Themenliste zusammenstellen und im Ticket unter
"Software Security Topics" vermerken.

Das Systemdesign **muss** dokumentiert werden und der Sicherheitsverantwortliche
**muss** überprüfen, ob alle Sicherheitsanforderungen an das Systemdesign erfüllt
wurden.

## Versionsverwaltung des Quellcodes

Jedes Softwareprojekt **muss** in einem geeigneten Versionsverwaltungssystem
hinterlegt sein. Handelt es sich um ein nicht öffentliches Projekt, dann
**muss** das GitLab des Forschungszentrum Jülich oder der Universität Bielefeld
zur Versionsverwaltung genutzt werden.
Der Leiter der Entwickler regelt den Zugriff auf das Versionskontrollsystem.
Die Entwicklung erfolgt über einen Stamm-(= Main) und 
Entwicklungszweig (= Development), eine direkte Änderung der o.g. Zweige ist
nicht erlaubt.
Alle Änderung/Erweiterungen **müssen** über Branches und Merge-Requests in den
Entwicklungszweig durch eine zweite Person nach dem 4-Augen-Prinzip eingepflegt
werden. Bei nicht öffentlichen Projekten darf dies ausschließlich durch einen
signierten Merge-Commit erfolgen. Ein Softwareprojekt gilt als veröffentlicht,
wenn der Entwicklungszweig in den Stamm unter Anwendung des 4-Augen Prinzips
überführt wird. Versionen sollen durch entsprechende Tags markiert werden.

Die Erfassung von Änderungen, Fehlern oder Schwachstellen muss über die Lebenszeit
der Software mittels Tickets dokumentiert in dem Versionsverwaltungssystem oder
einem externen Ticketsystem erfolgen.

Repositories, welche Quellcode für sicherheitsrelevante Komponenten beinhalten,
müssen durch entsprechende Code-Scans der jeweiligen Versionsverwaltungstools
nach Schwachstellen gescannt werden.
GitLab bietet etwa [Static Application Security Testing](https://gitlab.ub.uni-bielefeld.de/help/user/application_security/sast/index#static-application-security-testing-sast)
an, ähnliche Dienste wie etwa GitHub bieten analoge Funktionalitäten.
Der Scan muss bei Vorhandensein von Abhängigkeiten in Form von Software-Dependencies auch
einen Scan dieser Software-Pakete nach bekannten Schwachstellen umfassen.
Code muss vor Überführung in einen gesicherten Stamm- oder Entwicklungszweig diese Scans
erfolgreich durchlaufen.
Treten bei diesen Scans Probleme auf, sind diese anhand des gängigen Vorgehens für die jeweiligen
Problemklassen zu behandeln und zu beheben.

## Dokumentation

Für jedes Software-Projekt ist ein Ticket im Issue-Tracker anzulegen und
zu pflegen (Kategorie "Software-Development").
Die grundlegendsten Schritte bei der Umsetzung des Projekts
(Anforderungsanalyse, Umsetzung, Implementierung, Test, Installation
und Wartung) **müssen** in diesem Ticket schriftlich festgehalten werden.

Das Repository jedes Projekts **muss** zusätzlich mindestens eine Readme-Datei -
vorzugsweise in Markdown-Notation - enthalten, welche die minimalste
Dokumentation eines Projekts außerhalb des genannten Tickets darstellt.
Die folgenden Punkte müssen mindestens dokumentiert werden:

- Beschreibung der Funktionalität
- Abhängigkeiten von anderen Softwarepaketen
- Voraussetzung zum Einsatz (z.B. bestimmte Hardware, Betriebssystemversion)
- Einsatzgebiet
- Art der Tests und deren Abdeckung
- Installationsanleitung

Der Quellcode sollte durch den Einsatz dafür geeigneter Tools (z.B. durch PyDoc,
JavaDoc, ...) dokumentiert werden. Ziel der Dokumentation muss es sein, dass
ein nicht involvierter Entwickler in die Entwicklung einsteigen und/oder die
Wartung des Projekts problemlos übernehmen kann.

## Externe Entwicklungen

Die in der Richtlinie beschriebenen Anforderungen und Richtlinien sind, so weit wie möglich, auch auf
externe Entwicklungen anzuwenden.

Die folgenden zusätzlichen oder abweichenden Anforderungen werden an eine ausgegliederte Entwicklung gestellt:

- Der Umfang des Projekts ist durch ein Lastenheft festgelegt.
  Bei Bachelor- und Masterarbeiten besteht dies
  aus der Aufgabenbeschreibung und der entsprechenden Auflistung der zu erfüllenden Anforderungen.
  Für Projekte der externen Entwicklung ist ein entsprechendes Ticket vom Typ *Project* hinterlegt, welches alle
  relevanten Informationen enthält. Dies umfasst auch eine Risikoabschätzung bezüglich der Informationssicherheit.
  Siehe [Informationssicherheit im Projektmanagement](../richtlinien/Informationssicherheit_im_Projektmanagement.md#projekte)
- Bei Entwicklungen im Zuge von Bachelor- oder Masterarbeiten sind Erst- und Zweitbetreuer
  Mitglieder innerhalb des Geltungsbereichs.
- Bei Entwicklungen durch einen externen Dienstleister wird ein Projekt- und IT-Sicherheitsverantwortlicher vorausgesetzt.
- Der Source Code (Module, Klassen, Funktionen/Methoden) *muss* verständlich dokumentiert sein.
- der Quellcode des Projekts muss unter Open-Source-Lizenzmodellen lizenziert werden.
  Dies stellt sicher, dass der Quellcode über den Zeitraum der Entwicklung- und Betreuung des externen Dienstleisters
  hinaus verfügbar und wartbar ist.
- Regelmäßige (in der Regel wöchentliche) Treffen stellen sicher, dass die
  Projektentwicklung wie im Lastenheft festgelegt und nach der Richtlinie zur
  sicheren Softwareentwicklung durchgeführt wird.
- Das [GitLab der Universität Bielefeld](https://gitlab.ub.uni-bielefeld.de/) ist für Bachelor-
  und Masterarbeiten die verpflichtende Plattform für die Versionsverwaltung.
  Für externe Projekte anderer Art ist diese Plattform ebenfalls zu bevorzugen.
- Das Gesamtprojekt muss wie beschrieben durch eine Projektdokumentation begleitet werden.
  Für Bachelor- und Masterarbeiten ist die Abgabe einer schriftlichen Arbeit sowie ein (wissenschaftlicher)
  Vortrag verpflichtend, was ebenfalls durch die Universität vorausgesetzt wird.
- Der Test der entwickelten (Teil-)Software erfolgt in einer geeigneten Umgebung.
  Dabei müssen die Anforderungen, wie in [A8.31](../erklaerung-zur-anwendbarkeit.md#a831-trennung-von-entwicklungs--prüf--und-produktionsumgebungen)
  beschrieben, eingehalten werden.
  Mögliche geeignete Umgebungen stellen dar:
  - virtualisierte Entwicklungscloud  [IT-4.14](../it-verfahren.md#it-414-virtualisierte-entwicklungscloud)
  - Entwicklungscloud [IT-4.15](../it-verfahren.md#it-415-entwicklungscloud)
- Die Bewertung und Übernahme in die Produktionsumgebung erfolgt durch die Mitarbeiter
  der de.NBI Cloud mindestens nach dem 4-Augen-Prinzip (bzw. bei Bachelor- oder Masterarbeiten
  durch die Betreuer).
  - Es muss ein (Funktions-)Test in der Entwicklungsumgebung durchgeführt werden.
  - Eine Überführung des Programmcodes in geschützte Entwicklungszweige muss wie beschrieben geprüft
    und durchgeführt werden
  - Prüfen des Projekts auf typische Sicherheitslücken je nach Scope der Anwendung
    (z.B.  [OWASP](https://owasp.org/www-project-top-ten/) für Webapplikation)
  - Die Vorgaben für die [Sicherheitsprüfung in Entwicklung und Abnahme](../erklaerung-zur-anwendbarkeit.md#a829-sicherheitsprüfung-in-entwicklung-und-abnahme)
    müssen eingehalten werden.

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen und weisen
die Mitarbeiter ggf. auf Defizite hin.**
