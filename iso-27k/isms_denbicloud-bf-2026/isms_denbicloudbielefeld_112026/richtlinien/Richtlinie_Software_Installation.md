# Richtlinie für die Installation und Aktualisierung von Software

|     |                                             |
|-----|---------------------------------------------|
| Version:        | 1.2                             |
| Version vom:    | 12.03.2025                      |
| Erstellt durch: | Jan Krüger, Alex Walender       |
| Genehmigt am:   | 11.04.2025 alu, as              |
| durch:          | as, alu                         |

## ChangeLog

- Version 1.2 vom 12.03.2025 : Abwechslung in der Ausführung der IT-Verfahren
- Version 1.1 vom 25.01.2025 : Container 
- Version 1.0 vom 12.11.2021 : initialer Entwurf

## Zweck, Anwendungsbereich und Anwender

Durch die Richtlinie für die Installation und Aktualisierung von Software soll
sichergestellt werden, dass die installierte Software für die jeweilige
Server-Klasse (Openstack Controller/Compute, Ceph, Service) einheitlich und auf
demselben definierten Stand ist.

Der Anwendungsbereich sind die Server der de.NBI Cloud Bielefeld und die Anwender
die Mitarbeiter von ADM und gegebenenfalls BRF.

## Dokumentierte Installation

Die Installation und Aktualisierung von Software muss dokumentiert und darf nur
mithilfe von geeigneten Provisionierungswerkzeugen durchgeführt werden.

Als geeignete Provisionierungswerkzeuge gelten Werkzeuge, welche

1. eine nachvollziehbare Beschreibungen nutzen
1. Idempotent sind
1. ggf. den Installationsprozess loggen

Änderungen an den Beschreibungen müssen durch ein Ticket in der passenden Kategorie
des Issue-Trackers dokumentiert und durch eine zweite Person reviewed werden, bevor
diese auf der Produktionsumgebung ausgerollt werden.

Als geeignete Werkzeuge gelten die bekannten Provisionierungs bzw.
Orchestrierungswerkzeuge wie Ansible, Puppet oder Chef.

## Wartung und Bedienung von Software (Day 2 Operations)

In den meisten Fällen wird die installierte Software von einem
Mitarbeiter gewartet und ist bei Problemfällen primär die erste Ansprechperson.
Da die Anzahl der Mitarbeiter überschaubar ist, sind diese dazu angehalten,
bei technischen Problemen die Lösung durch andere Mitarbeiter durchführen zu lassen.
Durch die Abwechslung in der Ausführung der IT-Verfahren werden somit auch
andere Mitarbeiter an den verschiedensten Komponenten der Infrastrukur
eingearbeitet. Dies reduziert Unsicherheiten in der Bedienung,
falls die primäre Ansprechperson akut nicht zu erreichen ist.

## Quellen

Die Installation und Aktualisierung von Software, sowohl in Form von Paketen als auch
von Containern, ist ausschließlich aus vertrauenswürdigen Quellen zulässig.

### Vertrauenswürdige Quellen

**Software-Pakete** dürfen nur aus offiziellen und verifizierten Paket-Repositories oder
internen Repositories installiert werden. Dies schließt alle Arten von Paketmanagern
ein (z.B. apt, yum, npm, pip), deren Herkunft und Integrität vorab validiert worden
sind.

**Container-Images** sind nur aus vertrauenswürdigen und verifizierten Container-Registries
zu beziehen. Hierzu zählen interne Registries sowie offizielle Quellen, die durch eine
Sicherheitsbewertung genehmigt wurden.

### Genehmigungsverfahren

Neue Quellen (Repositories oder Registries) müssen durch einen formalen Genehmigungsprozess
geprüft und autorisiert werden, bevor sie in Produktionsumgebungen verwendet werden dürfen.
Der Genehmigungsprozess umfasst eine Risikobewertung der Quelle und eine Überprüfung der
Sicherheitspraktiken des Anbieters.

### Dokumentation und Überprüfung

Alle Installationen aus externen Quellen müssen dokumentiert werden, einschließlich der
Gründe für die Wahl dieser Quelle. Änderungen oder Hinzufügungen zu den genehmigten Quellen
müssen durch ein Ticket im Issue-Tracker erfasst und von einer zweiten Person überprüft
werden.

### Regelmäßige Überprüfung

Vertrauenswürdige Quellen sind regelmäßig zu überprüfen, um sicherzustellen, dass deren
Sicherheit und Integrität weiterhin gewahrt bleibt. Bei Feststellung von Sicherheitsvorfällen
oder Zweifel an der Vertrauenswürdigkeit einer Quelle muss dieser Quellenstatus umgehend
überprüft und gegebenenfalls angepasst werden.

## Ausnahmen

Von der Richtlinie ausgenommen sind Installation in der Entwicklungsumgebung
der de.NBI Cloud Bielefeld, sowie Notfalländerungen in der
Produktionsumgebungen. Notfalländerungen müssen in einem entsprechenden Ticket
dokumentiert und gegebenenfalls im Nachgang in das Manifest eingepflegt werden.

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen
und weisen die Mitarbeiter ggf. auf Defizite hin.**
