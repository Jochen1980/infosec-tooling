# Glossar

Dieses Glossar erläutert die wichtigsten Begriffe im Zusammenhang mit der de.NBI Cloud Bielefeld.
Der Schwerpunkt liegt auf uneindeutigen Begriffen und Abkürzungen.
Die Interpretation der Begriffe ist stets durch den Kontext der de.NBI Cloud geprägt und kann
daher von der allgemein gebräuchlichen Definition abweichen.

[[_TOC_]]

## C

### Cloud

Als Rechnerwolke betrachtete IT-Infrastruktur im Sinne des _Cloud Computing_.
Charakteristisch hierfür ist die bedarfsgerechte Selbstzuweisung von Ressourcen durch
den Nutzer. Die Hardware der Cloud wird durch die Abstraktionsebene sogenannter
**Virtuellen Maschinen** als beliebig aufteilbare Gesamtressource verfügbar gemacht.

### CVE

CVE, kurz für Common Vulnerabilities and Exposures (Häufige Schwachstellen und 
Risiken), ist eine Liste mit öffentlichen Sicherheitsschwachstellen in 
Computersystemen. Mit CVE ist in der Regel die CVE-Nummer gemeint, die einer 
bestimmten Schwachstelle zugewiesen ist. Mithilfe von CVEs können IT-Fachleute 
solche Schwachstellen leichter priorisieren und beheben, um Computersysteme 
sicherer zu machen.

## D

### DMZ

Siehe **Demilitarisierte Zone**

### Demilitarisierte Zone

Kurzform: _DMZ_. Abgeriegeltes Computernetz mit sicherheitstechnisch kontrollierten
Zugriffsmöglichkeiten auf die daran angeschlossenen Server.

## E

### Entwicklungscloud

Eine zur **Produktionscloud** weitestgehend identische aber separate, kleinere Cloud-Installation.
Sie dient als Umgebung für Probeläufe und Weiterentwicklungen mit dem Ziel der Optimierung der
**Produktionscloud**.

### Entwicklungsumgebung

Siehe **Entwicklungscloud**

## G

### Git-Repository

Dezentrales, versionskontrolliertes Projektarchiv welches in der Regel mittels eines
zentralen Servers synchronisiert wird.

## H

### Hardware

Siehe **IT-Infrastruktur-Komponenten**.

### Horizon

Siehe **OpenStack-Dashboard**.

## I

### Instanz

Vorwiegend innerhalb von OpenStack verwendeter Begriff für eine **Virtuelle Maschine**.

### IT-Infrastruktur-Komponenten

Technische Komponenten wie z.B. Server oder Switches.

## J

### Jump Host

Ein entsprechend abgesicherter Server für den Zugang aus einem öffentlichen Netzwerk hinein
in eine **Demilitarisierte Zone**.

## K

### Knoten

Gewöhnlich ist hiermit ein Hardware-Server mit dem Einsatzgebiet der _Datenspeicherung_ gemeint.
Oft wird hier im Zusammenhang mit der Speicherlösung _Ceph_ auch von _Ceph-Knoten_ gesprochen.
Der Begriff ist auf die starke Verbundenheit der Ceph-Server zurückzuführen und schwappt
gelegentlich auch auf dessen Unterkomponenten über, bspw. bei den Begriffen **Monitor-Knoten**
oder **Storage-Knoten**.

## M

### Monitor-Knoten

Steuerungskomponente eines Ceph-Clusters. Siehe auch **Knoten**.

## O

### OpenStack-Dashboard

Webbasierte Benutzeroberfläche für Kunden und Administratoren zur Nutzung bzw. Verwaltung der
bereitgestellten Rechenkapazitäten (insbesondere der Nutzung **Virtueller Maschinen**).

### OSD

Kurzform von _Object Storage Daemon_, einer Komponente der Speicherlösung _Ceph_ auf der
die eigentlichen Daten gespeichert sind. Auch bekannt als **Storage-Knoten**.

## P

### Produktionscloud

Die im Produktiveinsatz befindliche, zentrale Cloud-Installation.

### Produktionsumgebung

Siehe **Produktionscloud**

## R

### Repository

Oft ist hiermit ein **Git-Repository** gemeint, seltener auch ein **Software-Repository**.

## S

### Software-Repository

Quellort der mittels eines Paketverwaltungssystem installierten Softwarepakete.

### Storage-Knoten

Speicherkomponente eines Ceph-Clusters. Siehe auch **Knoten**.

## T

### Testumgebung

Siehe **Entwicklungscloud**

### Testcloud

Siehe **Entwicklungscloud**

### Threat Intelligence

Siehe [Arbeitsanweisung](richtlinien/Arbeitsanweisung_ThreatIntelligence.md).

## V

### VM

Siehe **Virtuelle Maschine**

### Virtuelle Maschine

Kurzform: _VM_. Softwaretechnisch gekapseltes Rechnersystem. Die Cloud bietet dem Kunden
Rechenleistung mittels VMs an.
