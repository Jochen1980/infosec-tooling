# Arbeitsanweisung Aufbau einer Threat Intelligence

| |                                             |
|----|---------------------------------------------|
| Version: | 0.1                                         |
| Version vom: | 24.01.2024                                  |
| Erstellt durch: | Alex Walender                               |
| Genehmigt am: | 06.03.2024 (alu), 12.03.2024 (as)           |
| durch: | Alexander Sczyrba (as), Stefan Albaum (alu) |

## Ziel dieser Arbeitsanweisung

Diese Richtlinie legt die Verfahren und Anforderungen für den Aufbau und die Nutzung von Threat 
Intelligence für die de.NBI Cloud Bielefeld fest, um die Informationssicherheit zu stärken und proaktiv 
auf Bedrohungen zu reagieren. Mitarbeiter werden hier angewiesen, einen stetigen
Kompetenzaufbau bezüglich der Themen aufzubauen.

## Anwendungsbereich

Die Arbeitsanweisung gilt für alle Mitarbeiter von ADM und BRF für die de.NBI Cloud Bielefeld.

## Zuständigkeit

ADM und BRF.

## Begriffe und Abkürzungen (optional)

Threat Intelligence:
Informationen und Analysen, die dazu dienen, Bedrohungen für die 
Informationstechnologie (IT) eines Unternehmens oder einer Organisation zu 
verstehen und darauf angemessen zu reagieren. Threat Intelligence 
beinhaltet Informationen über aktuelle Bedrohungen, Angriffsmethoden,
Taktiken und Techniken von Cyberkriminellen.

## Beschreibung

Die Bedrohungslage in der IT-Sicherheit befindet in einem ständigen Wandel.
Um Bedrohung analysieren, bewerten und bewältigen zu können ist es für
jeden Mitarbeiter erforderlich, die Kompetenzen in diesen Themen
zu erweitern.

Unter anderem wird the Threat Intelligence in verschiedenen Verfahren
aufgegliedert:

### Datensammlung

Mitarbeiter sind angehalten, aktuelle Bedrohungsdaten von vertrauenswürdigen
Quellen zu sammeln, darunter öffentliche Sicherheitswarnungen,
Sicherheitsunternehmen, staatliche Behörden und branchenspezifische
Informationsaustauschplattformen.

Hierzu existieren externe Quellen:

- [BSI-Jahresreports](https://www.bsi.bund.de/DE/Service-Navi/Publikationen/Lagebericht/Archiv-Lageberichte/archiv-lagebericht_node.html)
  als Überblick über die Landschaft der Gefahren bezüglich der IT-Sicherheit. Abbonierbar.
- [Heise Security](https://www.heise.de/security/) bietet aktuelle Beiträge über Gefahren
  und Schwachstellen auch hinsichtlich einzelner Applikationen. Im Matrix-Chat ist dazu ein
  Kanal abbonierbar.
- Das [DFN-CERT](https://www.dfn-cert.de/index.html) bietet ein Netzwerk bezüglich Beratung
  und Dienstleistungen für IT-Sicherheit an.

Ebenso bieten sich die existierenden Sicherheitstools als eine mögliche Quelle an:

| Anwendung | Weiterführende Informationen |
| --------- | ---------------------------- |
| Greenbone | [IT-7](../it-verfahren.md#it-7-openvasgsm) |
| Zabbix    | [IT-5](../it-verfahren.md#it-5-zabbix) |
| CVE-Scans | [IT-8](../it-verfahren.md#it-8-cve-scans) |
| ClamAV    | Automatisierte Ausführung und Reporting durch Zabbix |

Selbst wenn die aufgeführten Applikationen keine **direkten**
Informationen über eine Bedrohungslage darstellen,
so können diese genutzt werden um Bedrohungen
auf der Spur zu kommen. Beispielsweise könnte Zabbix
muster-spezifische Fehler einer Anwendung melden, welche
aufgrund eines aktuell durchgeführten Angriffs ausgelöst worden sind.

### Analyse, Bearbeitung und Protokollierung

Sollten in den Quellen Themen auftauchen, die im Geltungsbereich eine Relevanz haben,
so werden diese Themen in den entsprechenden internen Kanälen den anderen Mitarbeitern
kommuniziert. Ebenfalls werden entsprechende Meldungen gemeinsam in der Montagsbesprechung
diskutiert und protokolliert.

Ebenso wird die Situation bei ähnlichen IT-Infrastrukturen im Umfeld beobachtet,
da die Bedrohungslage sich im selben Kontext befindet.
Dies betrifft insbesondere öffentliche Einrichtung wie:

1. Universitäten und andere Bildungseinrichtungen.
1. Forschungszentren.
1. Stadt-Verwaltungen.
1. Krankenhäuser.

Bei entsprechender Relevanz wird das Thema als Ticket mit einer höheren Priorität
gekennzeichnet. Im Härtefall begründet die Erkenntnis einen Sicherheitsvorfall
und muss dementsprechend, nach den Richtlinien, eskaliert werden.

Neue Erkenntnisse gelten nicht als Betriebsgeheimnis und sollten mit relevanten
Parteien **geteilt** werden:

1. Andere de.NBI Cloud Standorte, da diese eine sehr ähnlich technische Infrastruktur aufbieten.
1. Die IT-Sicherheitsbeauftragten. Diese sind, in der Regel, gut mit anderen IT-Kräften anderer Abteilungen vernetzt.
1. Andere technische Verantwortliche außerhalb des Geltungsbereichs. Dies beinhaltet Administratoren (oder technisch verantwortliche Personen)
   anderer Abteilungen.
1. Bei anwendungsspezifischen Schwachstellen erfolgt eine detailierte Meldung an die spezifischen "Issue-Tracker" der Betreiber.

Wichtig ist hierbei, dass Meldungen einen leicht verständlichen Teil beinhalten müssen, da gegebenenfalls technisch unversierte
Personen die Bedrohungslage verstehen müssen.
Bevor Meldungen an Externe vergeben werden, muss sichergestellt werden, dass entsprechende Stellen mit
personenbezogenen Daten (z.B. IP-Adressen, Email-Adressen, Namen, ...) geschwärzt werden.

### Weiterführende Nutzung von Threat Intelligence

Neue Erkenntnisse bezüglich der Threat Intelligence werden verarbeitet:

1. Erkenntnisse werden in den Test-Umgebungen ausprobiert.
1. Gegebenenfalls muss hierfür eine Risikobetrachtung vorgenommen werden. Siehe [Risikomanagement](../risikomanagement.md).
1. Die oben genannten Sicherheitstools sind flexibel konfigurierbar und neue Erkenntnisse sollten in diese eingebettet werden.
  1. In Greenbone lassen sich eigene Definitionen einarbeiten. Siehe [VT-Development](https://forum.greenbone.net/t/vt-development/226).
  1. In Zabbix können neue [Templates](https://www.zabbix.com/documentation/guidelines/en/thosts) entwickelt werden.
  1. ClamAV unterstützt eigen hinzugefügte [Signaturen](https://blog.clamav.net/2016/06/create-your-own-anti-virus-signatures.html)

### Kompetenzaufbau

Alle Mitarbeiter sind aufgefordert, sich regelmäßig über aktuelle Bedrohungen zu informieren,
verdächtige Aktivitäten zu melden und an Schulungen zur Erhöhung des Sicherheitsbewusstseins teilzunehmen.

Hierfür hilfreich sind:

1. IT-Sicherheits-Veranstaltungen, beispielsweise vom [DFN-Cert](https://www.dfn-cert.de/veranstaltungen.html).
1. Penetrationtesting Kurse
1. Online Cyber Security Training durch freie Plattformen:
  1. [Hack The Box](https://www.hackthebox.com)
  1. [TryHackMe](https://tryhackme.com)

Nachweise sind in den [Aufstellungen](../aufstellungen/schulungen-und-fortbildungen.md) einzutragen.

## Changelog

- Version 0.1 vom 24.01.2024 : initialer Entwurf
