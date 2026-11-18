# Erklärung zur Anwendbarkeit (kompakt)

| Version | 2.0 vom 05.10.2023 |
| ------- | ------------------ |

Die kompakte Darstellung wird aus der Erklärung zur Anwendbarkeit **automatisiert**
per Skript generiert und dient vor allem der Leitung der de.NBI Cloud
Bielefeld, sowie einem externen Auditor zur Übersicht in welchem Status der
Umsetzung sich die Maßnahmen aus dem Anhang der ISO 27001 befinden. Der Status
ergibt sich hierbei aus der automatisierten Analyse der Maßnahme und, sofern
definiert, aus der Selbsteinschätzung. Neben dem Status der Umsetzung ist der Grund
für die Einbeziehung bzw. den Ausschluss der jeweiligen Maßname aufgeführt.

|      | Status | Beschreibung |
|------|--------------|--------------|
| 0 | ausgeschlossen | Maßnahme wird ausgeschlossen, Begründung erforderlich |
| 1 | nicht vorhanden | Maßnahme fehlt |
| 2 | in Bearbeitung | Maßnahme fehlt oder unvollständig, ein Ticket existiert |
| 3 | definiert | Maßnahme beschrieben |
| 4 | etabliert | Maßnahme wird gelebt |
| 5 | überwacht | Maßnahme wurde (intern) auditiert |
| 6 | verbessert | Maßnahme wurde aufgrund eine Assessments verbessert | 

```
commit 9e515095218922656c57527849754d1638bf2559
Author: Jan Krueger <jkrueger@cebitec.uni-bielefeld.de>
Date:   Mon Jun 29 17:06:11 2026 +0200
Branch: update_soa_kompakt
```

## Governance (Steuerung der Informationssicherheit)

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A5.1](erklaerung-zur-anwendbarkeit.md#a51-informationssicherheitsrichtlinien) | Informationssicherheitsrichtlinien | überwacht | Die de.NBI Cloud Bielefeld hat eine Informationssicherheitsrichtlinie. |  |  |
| [A5.2](erklaerung-zur-anwendbarkeit.md#a52-informationssicherheitsrollen-und--verantwortlichkeiten) | Informationssicherheitsrollen und -verantwortlichkeiten | überwacht | Die de.NBI Cloud Bielefeld definiert Informationssicherheitsrollen und -verantwortlichkeiten. Die Cloud betreibt hierbei Systeme und Technologien verschiedener Bereiche, dementsprechend müssen die Verantwortungen der Mitarbeitern mit den erforderlichen Kompetenzen festgelegt werden. |  |  |
| [A5.3](erklaerung-zur-anwendbarkeit.md#a53-aufgabentrennung) | Aufgabentrennung | überwacht | Die de.NBI Cloud Bielefeld überwacht Prozesse nach dem 4-Augen-Prinzip. Durch die Größe der Organisation ist eine strikte Aufgabentrennung nicht durchgängig realisierbar. |  |  |
| [A5.4](erklaerung-zur-anwendbarkeit.md#a54-verantwortlichkeiten-der-leitung) | Verantwortlichkeiten der Leitung | überwacht | Die Leitung der de.NBI Cloud Bielefeld ist sich der Verantwortlichkeit gegenüber dem Personal bewusst. Es werden komplexe Systeme betrieben und sie muss sicherstellen, dass Beschäftigte sich der Informationssicherheit bewusst sind und entsprechende Kompetenzen besitzen. |  |  |
| [A5.5](erklaerung-zur-anwendbarkeit.md#a55-kontakt-mit-behörden) | Kontakt mit Behörden | überwacht | Über den ISB besteht Kontakt zu Behörden. Da die Kontaktstellen oftmals autark voneinander arbeiten, ist der initiale Aufbau und die Pflege solcher Kontakte von großer Bedeutung. |  |  |
| [A5.6](erklaerung-zur-anwendbarkeit.md#a56-kontakt-mit-speziellen-interessensgruppen) | Kontakt mit speziellen Interessensgruppen | überwacht | Die Mitarbeiter de.NBI Cloud Bielefeld nehmen an Veranstaltungen zur IT-Sicherheit teil. Dies ist besonders im IT-Umfeld und insbesondere im Bereich des Cloud Computing von wesentlicher Bedeutung, da diese Technologie relativ neu ist und im IT-Bereich zunehmend an Bedeutung gewinnt. |  |  |
| [A5.8](erklaerung-zur-anwendbarkeit.md#a58-informationssicherheit-im-projektmanagement) | Informationssicherheit im Projektmanagement | überwacht | Die de.NBI Cloud Bielefeld betreibt Projektmanagement. Aufgrund der technischen Komplexität werden im Bereich des Cloud Computing immer wieder größere (Änderungs-)Projekte geplant. Hierbei können Informationssicherheitsziele aus dem Fokus geraten, daher muss das Projektmanagement dies berücksichtigen. |  | ch |
| [A5.24](erklaerung-zur-anwendbarkeit.md#a524-planung-und-vorbereitung-der-handhabung-von-informationssicherheitsvorfällen) | Planung und Vorbereitung der Handhabung von Informationssicherheitsvorfällen | überwacht | Die Handhabung von Informationssicherheitsvorfällen ist durch eine IT-Sicherheitsleitlinie der Universität geregelt. Informationssicherheitsvorfälle können gehäuft im Zusammenhang mit Cloud-Computing auftreten, insbesondere da unsere Nutzer in der Regel unerfahrene IT-Nutzer sind. |  |  |

## Asset Management (Verwaltung der Werte)

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A5.9](erklaerung-zur-anwendbarkeit.md#a59-inventar-der-informationen-und-anderen-damit-verbundenen-werten) | Inventar der Informationen und anderen damit verbundenen Werten | überwacht | Die de.NBI Cloud inventarisiert Werte. |  |  |
| [A5.10](erklaerung-zur-anwendbarkeit.md#a510-zulässiger-gebrauch-von-informationen-und-anderen-damit-verbundenen-werten) | Zulässiger Gebrauch von Informationen und anderen damit verbundenen Werten | überwacht | die de.NBI Cloud Bielefeld arbeitet mit Informationen und dazugehörigen Werten. |  |  |
| [A5.11](erklaerung-zur-anwendbarkeit.md#a511-rückgabe-von-werten) | Rückgabe von Werten | überwacht | Die Rückgabe von Werten der de.NBI Cloud Bielefeld ist geregelt. |  |  |
| [A5.14](erklaerung-zur-anwendbarkeit.md#a514-informationsübertragung) | Informationsübertragung | überwacht | Die de.NBI Cloud Bielefeld überträgt Daten innerhalb ihrer Kommunikationseinrichtungen. Die de.NBI Cloud Bielefeld tauscht Geschäftsinformationen mit externen Parteien aus. Um die übertragenen Informationen zu schützen, müssen entsprechende Vereinbarungen definiert werden. |  | jk |
| [A5.37](erklaerung-zur-anwendbarkeit.md#a537-dokumentierte-bedienabläufe) | Dokumentierte Bedienabläufe | überwacht | Die de.NBI Cloud Bielefeld hat Betriebsabläufe, die eine Dokumentation erfordern. Dies ist von entsprechender Wichtigkeit, da die Abläufe relativ komplex sein können und durch menschliche Fehler sonst die Informationssicherheit gefährdet werden könnte. |  |  |
| [A6.7](erklaerung-zur-anwendbarkeit.md#a67-telearbeit) | Telearbeit | überwacht | Die Mitarbeiter der de.NBI Cloud Bielefeld können mobil arbeiten, daher bedarf es Richtlinien, welche die Informationssicherheit in Bezug auf Telearbeit schützen. |  |  |
| [A8.1](erklaerung-zur-anwendbarkeit.md#a81-endpunktgeräte-des-benutzers) | Endpunktgeräte des Benutzers | überwacht | Die Mitarbeiter der de.NBI Cloud Bielefeld haben Dienstnotebooks. |  |  |

## Informationsschutz

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A5.12](erklaerung-zur-anwendbarkeit.md#a512-klassifizierung-von-information) | Klassifizierung von Information | überwacht | Die de.NBI Cloud Bielefeld klassifiziert und kennzeichnet Informationen. Aufgrund der Verwendung unterschiedlicher Arten von Informationen müssen klare Handhabungsregeln definiert sein. |  |  |
| [A5.13](erklaerung-zur-anwendbarkeit.md#a513-kennzeichnung-von-information) | Kennzeichnung von Information | etabliert | Siehe A5.12 |  |  |
| [A5.34](erklaerung-zur-anwendbarkeit.md#a534-privatsphäre-und-schutz-von-personenbezogenen-daten-pbd) | Privatsphäre und Schutz von personenbezogenen Daten (PbD) | definiert | Die de.NBI Cloud Bielefeld verarbeitet für den Betrieb personenbezogene Daten. |  |  |
| [A8.10](erklaerung-zur-anwendbarkeit.md#a810-löschung-von-informationen) | Löschung von Informationen | etabliert | Die de.NBI Cloud Bielefeld verarbeitet Informationen. |  |  |
| [A8.11](erklaerung-zur-anwendbarkeit.md#a811-datenmaskierung) | Datenmaskierung | etabliert | Siehe A8.10 |  |  |
| [A8.12](erklaerung-zur-anwendbarkeit.md#a812-verhinderung-von-datenlecks) | Verhinderung von Datenlecks | etabliert | Siehe A8.10 |  |  |
| [A8.33](erklaerung-zur-anwendbarkeit.md#a833-informationen-zur-prüfung) | Informationen zur Prüfung | überwacht | Die de.NBI Cloud Bielefeld verfügt über eine Testumgebung, in der Prüfdaten verwendet werden. |  |  |

## Personalsicherheit

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A6.1](erklaerung-zur-anwendbarkeit.md#a61-sicherheitsüberprüfung) | Sicherheitsüberprüfung | in Bearbeitung | Es werden komplexe Systeme betrieben und daher muss sichergestellt werden, dass Beschäftigte sich der geforderten Informationssicherheit bewusst sind und entsprechende Kompetenzen besitzen. | [CER-572](https://yt.bi.denbi.de/issue/CER-572) | jk |
| [A6.2](erklaerung-zur-anwendbarkeit.md#a62-beschäftigungs--und-vertragsbedingungen) | Beschäftigungs- und Vertragsbedingungen | etabliert | Der Betrieb der de.NBI Cloud erfordert die Verteilung von Verantwortlichkeiten in Bezug auf Informationssicherheit. |  |  |
| [A6.3](erklaerung-zur-anwendbarkeit.md#a63-informationssicherheitsbewusstsein--ausbildung-und--schulung) | Informationssicherheitsbewusstsein, -ausbildung und -schulung | etabliert | Das Personal muss ein angemessenes Bewusstsein für Informationssicherheit besitzen. |  |  |
| [A6.4](erklaerung-zur-anwendbarkeit.md#a64-maßregelungsprozess) | Maßregelungsprozess | etabliert | Die Leitung der de.NBI Cloud Bielefeld muss Möglichkeiten zur Maßregelung besitzen. |  |  |
| [A6.5](erklaerung-zur-anwendbarkeit.md#a65-verantwortlichkeiten-nach-beendigung-oder-änderung-der-beschäftigung) | Verantwortlichkeiten nach Beendigung oder Änderung der Beschäftigung | überwacht | Die Beendigung von Beschäftigungsverhältnissen ist geregelt. Da die Administratoren der de.NBI Cloud Bielefeld weitreichende administrative Befugnisse besitzen, müssen klare Prozesse definiert werden um die Interessen der Organisation (sowie die der Nutzer) schützen zu können. |  |  |
| [A6.6](erklaerung-zur-anwendbarkeit.md#a66-vertraulichkeits--oder-geheimhaltungsvereinbarungen) | Vertraulichkeits- oder Geheimhaltungsvereinbarungen | überwacht | Die de.NBI Cloud Bielefeld hat Vertraulichkeitsvereinbarungen mit externen Parteien. |  |  |

## Physische Sicherheit

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A7.1](erklaerung-zur-anwendbarkeit.md#a71-physische-sicherheitsperimeter) | Physische Sicherheitsperimeter | überwacht | Die de.NBI Cloud Bielefeld betreibt Systeme, die sensible Informationen enthalten können und daher physischen Schutz benötigen. |  |  |
| [A7.2](erklaerung-zur-anwendbarkeit.md#a72-physischer-zutritt) | Physischer Zutritt | in Bearbeitung | Die de.NBI Cloud Bielefeld betreibt Systeme, die physischen Schutz vor Unbefugten benötigen. Die de.NBI Cloud Bielefeld hat keinen Anlieferungs- und Ladebereich. | [CER-558](https://yt.bi.denbi.de/issue/CER-558) | jk |
| [A7.3](erklaerung-zur-anwendbarkeit.md#a73-sichern-von-büros-räumen-und-einrichtungen) | Sichern von Büros, Räumen und Einrichtungen | überwacht | Zu der de.NBI Cloud Bielefeld gehören Büros, Besprechungsräume und Serverräume. |  |  |
| [A7.4](erklaerung-zur-anwendbarkeit.md#a74-physische-sicherheitsüberwachung) | Physische Sicherheitsüberwachung | etabliert | Siehe 7.2 |  |  |
| [A7.5](erklaerung-zur-anwendbarkeit.md#a75-schutz-vor-physischen-und-umweltbedingten-bedrohungen) | Schutz vor physischen und umweltbedingten Bedrohungen | überwacht | Die de.NBI Cloud Bielefeld ist externen und umweltbedingten Bedrohungen ausgesetzt. |  |  |
| [A7.6](erklaerung-zur-anwendbarkeit.md#a76-arbeiten-in-sicherheitsbereichen) | Arbeiten in Sicherheitsbereichen | überwacht | Die de.NBI Cloud verfügt über Sicherheitsbereiche (Parzelle im Datacenter). |  |  |
| [A7.7](erklaerung-zur-anwendbarkeit.md#a77-aufgeräumte-arbeitsumgebung-und-bildschirmsperren) | Aufgeräumte Arbeitsumgebung und Bildschirmsperren | überwacht | Die de.NBI Cloud Bielefeld stellt den Mitarbeitern eine Arbeitsumgebung zur Verfügung. Da diese Arbeitsumgebung nicht ausschließlich von Mitarbeitern betreten werden kann (beispielsweise auch durch Reinigungskräfte), muss die Arbeitsumgebung aufgeräumt sein und Informationen geschützt werden. |  |  |
| [A7.8](erklaerung-zur-anwendbarkeit.md#a78-platzierung-und-schutz-von-geräten-und-betriebsmitteln) | Platzierung und Schutz von Geräten und Betriebsmitteln | überwacht | Die de.NBI Cloud Bielefeld betreibt eine IT-Hardware-Infrastruktur im Datacenter der Universität Bielefeld. |  |  |
| [A7.9](erklaerung-zur-anwendbarkeit.md#a79-sicherheit-von-werten-außerhalb-der-räumlichkeiten) | Sicherheit von Werten außerhalb der Räumlichkeiten | überwacht | Die de.NBI Cloud Bielefeld stellt den Mitarbeitern Dienstgeräte zur Verfügung, die gesichert werden müssen. |  |  |
| [A7.10](erklaerung-zur-anwendbarkeit.md#a710-speichermedien) | Speichermedien | überwacht | Die de.NBI Cloud Bielefeld nutzt (Wechsel-)Datenträger. |  |  |
| [A7.11](erklaerung-zur-anwendbarkeit.md#a711-versorgungseinrichtungen) | Versorgungseinrichtungen | überwacht | Die de.NBI Cloud Bielefeld nutzt Versorgungsgeinrichtungen (USV, NEA, Klima, usw.) der Universität Bielefeld. |  |  |
| [A7.12](erklaerung-zur-anwendbarkeit.md#a712-sicherheit-der-verkabelung) | Sicherheit der Verkabelung | überwacht | Die de.NBI Cloud Bielefeld betreibt eine umfangreiche IT-Hardware-Infrastruktur, welche durch eine komplexe Verkabelung, Netzwerk und Strom miteinander verbunden ist. |  |  |
| [A7.13](erklaerung-zur-anwendbarkeit.md#a713-instandhalten-von-geräten-und-betriebsmitteln) | Instandhalten von Geräten und Betriebsmitteln | überwacht | Die de.NBI Cloud Bielefeld betreibt eine umfangreiche IT-Hardware-Infrastruktur, welche für einen sicheren Betrieb entsprechend gewartet wird. |  |  |
| [A7.14](erklaerung-zur-anwendbarkeit.md#a714-sichere-entsorgung-oder-wiederverwendung-von-geräten-und-betriebsmitteln) | Sichere Entsorgung oder Wiederverwendung von Geräten und Betriebsmitteln | überwacht | Die de.NBI Cloud Bielefeld betreibt Systeme, bei deren Wiederverwendung bzw. Entfernung Sorgfalt walten muss, insbesondere da diese klassifizierte Informationen beinhalten können. |  |  |

## System- und Netzwerksicherheit

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A8.7](erklaerung-zur-anwendbarkeit.md#a87-schutz-gegen-schadsoftware) | Schutz gegen Schadsoftware | überwacht | Die de.NBI Cloud Bielefeld betreibt eine IT-Infrastruktur, welche vor Schadsoftware zu schützen ist. |  |  |
| [A8.18](erklaerung-zur-anwendbarkeit.md#a818-gebrauch-von-hilfsprogrammen-mit-privilegierten-rechten) | Gebrauch von Hilfsprogrammen mit privilegierten Rechten | etabliert | Die de.NBI Cloud Bielefeld verwendet Hilfsprogramme mit erhöhten Rechten. |  |  |
| [A8.20](erklaerung-zur-anwendbarkeit.md#a820-netzwerksicherheit) | Netzwerksicherheit | überwacht | Die de.NBI Cloud Bielefeld betreibt komplexe Computernetzwerke. Daher müssen Informationen innerhalb des Netzwerks entsprechend geschützt werden. |  |  |
| [A8.21](erklaerung-zur-anwendbarkeit.md#a821-sicherheit-von-netzwerkdiensten) | Sicherheit von Netzwerkdiensten | überwacht | Die de.NBI Cloud Bielefeld betreibt Netzwerkdienste. |  |  |
| [A8.22](erklaerung-zur-anwendbarkeit.md#a822-trennung-von-netzwerken) | Trennung von Netzwerken | überwacht | Die de.NBI Cloud Bielefeld betreibt Computernetzwerke für unterschiedliche Komponenten der IT-Infrastruktur. Um Schutzziele der Informationssicherheit einzuhalten müssen diese nach "state-of-the-art" separiert sein. |  |  |
| [A8.23](erklaerung-zur-anwendbarkeit.md#a823-webfilterung) | Webfilterung | etabliert | Das Personal hat Zugang zu externen Webseiten. |  |  |
| [A8.30](erklaerung-zur-anwendbarkeit.md#a830-ausgegliederte-entwicklung) | Ausgegliederte Entwicklung | überwacht | Die Mitarbeiter der de.NBI Cloud Bielefeld betreuen Bachelor- und Masterarbeiten. Die so ausgegliederten Entwicklungen können hierbei in den Produktionsbetrieb einfließen. |  |  |
| [A8.34](erklaerung-zur-anwendbarkeit.md#a834-schutz-der-informationssysteme-während-der-überwachungsprüfung) | Schutz der Informationssysteme während der Überwachungsprüfung | etabliert | Die de.NBI Cloud Bielefeld führt Auditprüfungen durch. |  |  |

## Anwendungs- und Systemsicherheit

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A8.25](erklaerung-zur-anwendbarkeit.md#a825-lebenszyklus-einer-sicheren-entwicklung) | Lebenszyklus einer sicheren Entwicklung | überwacht | Die de.NBI Cloud Bielefeld entwickelt Software/Systeme. Die Entwicklung kann die Informationssicherheit gefährden. |  |  |
| [A8.26](erklaerung-zur-anwendbarkeit.md#a826-anforderungen-an-die-anwendungssicherheit) | Anforderungen an die Anwendungssicherheit | überwacht | Die de.NBI Cloud Bielefeld entwickelt und beschafft Anwendungen. |  |  |
| [A8.27](erklaerung-zur-anwendbarkeit.md#a827-sichere-systemarchitektur-und-technische-grundsätze) | Sichere Systemarchitektur und technische Grundsätze | etabliert | Die de.NBI Cloud Bielefeld betreibt sichere Systeme. |  |  |
| [A8.28](erklaerung-zur-anwendbarkeit.md#a828-sichere-kodierung) | Sichere Kodierung | etabliert | Im Zuge des Betriebs der de.NBI Cloud Bielefeld wird Software entwickelt. |  |  |
| [A8.29](erklaerung-zur-anwendbarkeit.md#a829-sicherheitsprüfung-in-entwicklung-und-abnahme) | Sicherheitsprüfung in Entwicklung und Abnahme | überwacht | Die de.NBI Cloud Bielefeld entwickelt/installiert/aktualisiert Software und Systeme. Neue Systeme durchlaufen einen Abnahmetest. |  | vr |
| [A8.31](erklaerung-zur-anwendbarkeit.md#a831-trennung-von-entwicklungs--prüf--und-produktionsumgebungen) | Trennung von Entwicklungs-, Prüf- und Produktionsumgebungen | überwacht | Die de.NBI Cloud Bielefeld betreibt Entwicklungs- sowie Produktionsumgebungen, die strikt getrennt werden müssen. |  |  |
| [A8.32](erklaerung-zur-anwendbarkeit.md#a832-änderungssteuerung) | Änderungssteuerung | überwacht | Die de.NBI Cloud Bielefeld hat Betriebsabläufe, die stetigen (teils komplexen) Änderungen unterliegen. Bei der hohen Serveranzahl muss dies kontrolliert und geregelt geschehen. |  |  |

## Sichere Konfiguration

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A8.9](erklaerung-zur-anwendbarkeit.md#a89-konfigurationsmanagement) | Konfigurationsmanagement | überwacht | Die de.NBI Cloud Bielefeld verfügt über Hardware, Software, Dienste und Netzwerke, welche konfiguriert werden müssen. |  |  |
| [A8.19](erklaerung-zur-anwendbarkeit.md#a819-installation-von-software-auf-systemen-im-betrieb) | Installation von Software auf Systemen im Betrieb | überwacht | Die de.NBI Cloud Bielefeld installiert Software auf Systemen im Betrieb. |  |  |
| [A8.24](erklaerung-zur-anwendbarkeit.md#a824-verwendung-von-kryptographie) | Verwendung von Kryptographie | überwacht | Die de.NBI Cloud Bielefeld nutzt angemessene kryptographische Maßnahmen zur Verschlüsselung. Als Betreiber einer öffentlich erreichbaren Cloud ist dies von fundamentaler Wichtigkeit um sämtliche gespeicherten (bzw. übertragenen) Informationen schützen zu können. |  |  |

## Identitäts- und Zugangsverwaltung

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A5.15](erklaerung-zur-anwendbarkeit.md#a515-zugangssteuerung) | Zugangssteuerung | überwacht | Der Zugang zur de.NBI Cloud Bielefeld ist gesteuert, da die informationsverarbeitenden Einrichtungen klassifizierte Informationen beinhalten, die einer entsprechenden Handhabung bedürfen. |  |  |
| [A5.16](erklaerung-zur-anwendbarkeit.md#a516-identitätsmanagement) | Identitätsmanagement | etabliert | Die de.NBI Cloud Bielefeld verwaltet Identitäten. |  |  |
| [A5.17](erklaerung-zur-anwendbarkeit.md#a517-informationen-zur-authentifizierung) | Informationen zur Authentifizierung | überwacht | Die de.NBI Cloud Bielefeld nutzt Passwörter bzw. private Schlüssel sowie 2FA zur Authentisierung. |  |  |
| [A5.18](erklaerung-zur-anwendbarkeit.md#a518-zugangsrechte) | Zugangsrechte | überwacht | Die de.NBI Cloud Bielefeld nutzt eine Benutzerverwaltung, sodass nur authorisierte Personen Zugriff auf ihre zugeteilten Ressourcen haben. |  |  |
| [A8.2](erklaerung-zur-anwendbarkeit.md#a82-privilegierte-zugangsrechte) | Privilegierte Zugangsrechte | überwacht | Siehe A5.18 |  |  |
| [A8.3](erklaerung-zur-anwendbarkeit.md#a83-informationszugangsbeschränkung) | Informationszugangsbeschränkung | überwacht | Die de.NBI Cloud Bielefeld verwaltet Informationen. |  |  |
| [A8.4](erklaerung-zur-anwendbarkeit.md#a84-zugriff-auf-den-quellcode) | Zugriff auf den Quellcode | etabliert | Die de.NBI Cloud Bielefeld verwaltet Quellcode in Repositories. |  |  |
| [A8.5](erklaerung-zur-anwendbarkeit.md#a85-sichere-authentifizierung) | Sichere Authentifizierung | etabliert | Die de.NBI Cloud Bielefeld beschränkt den Zugang auf gewisse Informationen. |  |  |

## Bedrohungs- und Schwachstellenmanagement

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A5.7](erklaerung-zur-anwendbarkeit.md#a57-erkenntnisse-über-bedrohungen) | Erkenntnisse über Bedrohungen | etabliert | Die de.NBI Cloud ist Bedrohungen im Kontext der Informationssicherheit ausgesetzt. |  |  |
| [A5.8](erklaerung-zur-anwendbarkeit.md#a58-informationssicherheit-im-projektmanagement) | Informationssicherheit im Projektmanagement | überwacht | Die de.NBI Cloud Bielefeld betreibt Projektmanagement. Aufgrund der technischen Komplexität werden im Bereich des Cloud Computing immer wieder größere (Änderungs-)Projekte geplant. Hierbei können Informationssicherheitsziele aus dem Fokus geraten, daher muss das Projektmanagement dies berücksichtigen. |  | ch |

## Aufrechterhaltung der Informationssicherheit

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A5.29](erklaerung-zur-anwendbarkeit.md#a529-informationssicherheit-bei-störungen) | Informationssicherheit bei Störungen | überwacht | Im Betrieb der de.NBI Cloud Bielefeld können Störungen auftreten. |  |  |
| [A5.30](erklaerung-zur-anwendbarkeit.md#a530-ikt-bereitschaft-für-business-continuity) | IKT-Bereitschaft für Business Continuity | überwacht | Die de.NBI Cloud Bielefeld betreibt IKT. |  |  |
| [A8.6](erklaerung-zur-anwendbarkeit.md#a86-kapazitätssteuerung) | Kapazitätssteuerung | überwacht | Die de.NBI Cloud Bielefeld verwaltet Cloud-Ressourcen, deren Kapazitäten zwecks kontinuierlichen Betriebs überwacht und gesteuert werden müssen. |  |  |
| [A8.13](erklaerung-zur-anwendbarkeit.md#a813-sicherung-von-information) | Sicherung von Information | überwacht | Die de.NBI Cloud Bielefeld umfasst Daten, deren Sicherung für den Betrieb notwendig ist. |  |  |
| [A8.14](erklaerung-zur-anwendbarkeit.md#a814-redundanz-von-informationsverarbeitenden-einrichtungen) | Redundanz von informationsverarbeitenden Einrichtungen | etabliert | Die de.NBI Cloud Bielefeld betreibt IT-Systeme. |  |  |

## Sicherheit der Lieferantenbeziehungen

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A5.19](erklaerung-zur-anwendbarkeit.md#a519-informationssicherheit-in-lieferantenbeziehungen) | Informationssicherheit in Lieferantenbeziehungen | überwacht | Die de.NBI Cloud Bielefeld pflegt Lieferantenbeziehungen, über die schützenwerte Werte bezogen und administriert werden. |  | jk |
| [A5.20](erklaerung-zur-anwendbarkeit.md#a520-behandlung-von-informationssicherheit-in-lieferantenvereinbarungen) | Behandlung von Informationssicherheit in Lieferantenvereinbarungen | überwacht | Siehe 5.19 |  | jk |
| [A5.21](erklaerung-zur-anwendbarkeit.md#a521-umgang-mit-der-informationssicherheit-in-der-lieferkette-der-informations--und-kommunikationstechnologie-ikt) | Umgang mit der Informationssicherheit in der Lieferkette der Informations- und Kommunikationstechnologie (IKT) | überwacht | Die de.NBI Cloud Bielefeld pflegt Lieferantenbeziehungen und der Umgang mit Informationssicherheitsrisiken muss mit den entsprechenden Parteien geklärt werden. |  |  |
| [A5.22](erklaerung-zur-anwendbarkeit.md#a522-überwachung-überprüfung-und-änderungsmanagement-von-lieferantendienstleistungen) | Überwachung, Überprüfung und Änderungsmanagement von Lieferantendienstleistungen | überwacht | Die de.NBI Cloud Bielefeld pflegt Lieferantenbeziehungen, deren Dienstleistungen und Anforderungen sich ändern können. |  |  |
| [A5.23](erklaerung-zur-anwendbarkeit.md#a523-informationssicherheit-für-die-nutzung-von-cloud-diensten) | Informationssicherheit für die Nutzung von Cloud-Diensten | etabliert | Die de.NBI Cloud Bielefeld nutzt externe Cloud-Dienste. |  |  |

## Recht und Einhaltung (Compliance)

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A5.31](erklaerung-zur-anwendbarkeit.md#a531-rechtliche-gesetzliche-regulatorische-und-vertragliche-anforderungen) | Rechtliche, gesetzliche, regulatorische und vertragliche Anforderungen | überwacht | Die de.NBI Cloud Bielefeld unterliegt rechtlichen, gesetzlichen, regulatorischen und vertraglichen Anforderungen. |  |  |
| [A5.32](erklaerung-zur-anwendbarkeit.md#a532-geistige-eigentumsrechte) | Geistige Eigentumsrechte | überwacht | Die de.NBI Cloud Bielefeld und in ihr verarbeitete Daten können geistiges Eigentum beinhalten. |  |  |
| [A5.33](erklaerung-zur-anwendbarkeit.md#a533-schutz-von-aufzeichnungen) | Schutz von Aufzeichnungen | überwacht | Die de.NBI Cloud Bielefeld besitzt Aufzeichnungen. |  |  |
| [A5.35](erklaerung-zur-anwendbarkeit.md#a535-unabhängige-überprüfung-der-informationssicherheit) | Unabhängige Überprüfung der Informationssicherheit | überwacht | Die de.NBI Cloud Bielefeld überprüft regelmäßig die Informationssicherheit. |  |  |
| [A5.36](erklaerung-zur-anwendbarkeit.md#a536-einhaltung-von-richtlinien-vorschriften-und-normen-für-die-informationssicherheit) | Einhaltung von Richtlinien, Vorschriften und Normen für die Informationssicherheit | definiert | Die de.NBI Cloud Bielefeld betreibt Informationsicherheitsmanagement. |  |  |

## Umgang mit Informationssicherheitsereignissen

| Maßnahme | Beschreibung | Status | Gründe für die Einbeziehung bzw. den Ausschluss | Ticket(s) | Kommentare |
|----------|--------------|--------|-------------------------------------------------|-----------|------------|
| [A5.25](erklaerung-zur-anwendbarkeit.md#a525-beurteilung-und-entscheidung-über-informationssicherheitsereignisse) | Beurteilung und Entscheidung über Informationssicherheitsereignisse | überwacht | Die de.NBI Cloud Bielefeld kann von Informationssicherheitsvorfällen betroffen sein. |  |  |
| [A5.26](erklaerung-zur-anwendbarkeit.md#a526-reaktion-auf-informationssicherheitsvorfälle) | Reaktion auf Informationssicherheitsvorfälle | überwacht | Die Handhabung von Informationssicherheitsvorfällen ist durch eine IT-Sicherheitsleitlinie geregelt. Da die de.NBI Cloud Bielefeld anderen Parteien (BITS, DFN, usw.) Vorfälle mitteilen muss, ist es notwendig, diese zu dokumentieren. |  |  |
| [A5.27](erklaerung-zur-anwendbarkeit.md#a527-erkenntnisse-aus-informationssicherheitsvorfällen) | Erkenntnisse aus Informationssicherheitsvorfällen | überwacht | Die Handhabung von Informationssicherheitsvorfällen ist durch eine IT-Sicherheitsleitlinie geregelt. Beispielsweise sind die Nutzer der Cloud teilweise unerfahren in Bezug auf IT-Sicherheit, daher sollten aufgetretene Vorfälle genutzt werden, um Nutzer bei der Verwendung der Cloud-Dienste auf etwaige Gefahren hinzuweisen. Gewonnene Erkenntnisse können zudem in die stetige Verbesserung der Sicherheit der Cloud einfließen und so Wiederholungsfälle vermeiden. |  |  |
| [A5.28](erklaerung-zur-anwendbarkeit.md#a528-sammeln-von-beweismaterial) | Sammeln von Beweismaterial | überwacht | Die Services der de.NBI Cloud Bielefeld loggen Daten. Log-Daten sind bei Eintreten eines Sicherheitsvorfalls Beweismaterial. |  |  |
| [A6.8](erklaerung-zur-anwendbarkeit.md#a68-meldung-von-informationssicherheitsereignissen) | Meldung von Informationssicherheitsereignissen | überwacht | In einer öffentlich-erreichbaren Cloud können regelmäßig Informationssicherheitsereignisse auftreten, welche erheblichen Einfluss auf den Betrieb der de.NBI Cloud haben. Bei Erkennung solcher Ereignisse ist eine schnelle Meldung unerlässlich. |  |  |
| [A8.15](erklaerung-zur-anwendbarkeit.md#a815-protokollierung) | Protokollierung | überwacht | Die de.NBI Cloud Bielefeld fertigt zur Wahrung der Systemsicherheit Ereignisprotokolle an, welche durch die hohe Anzahl von Komponenten in der IT-Infrastruktur unabdingbar sind. |  |  |
| [A8.16](erklaerung-zur-anwendbarkeit.md#a816-überwachung-von-aktivitäten) | Überwachung von Aktivitäten | in Bearbeitung | Siehe A8.15. | [CER-552](https://yt.bi.denbi.de/issue/CER-552) | jk |
| [A8.17](erklaerung-zur-anwendbarkeit.md#a817-uhrensynchronisation) | Uhrensynchronisation | überwacht | Die de.NBI Cloud Bielefeld betreibt mehrere Host-Systeme, die im Verbund arbeiten. Einige Komponenten der IT-Infrastruktur arbeiten hierbei zeitkritisch (beispielsweise das Storage-System Ceph). |  |  |
