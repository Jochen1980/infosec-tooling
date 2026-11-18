# Software-Quellen

Aufstellung der zulässigen Repositories und Registries zur Installation von Paketen und Containern. Die
Pflege der Aufstellung erfolgt durch das Ticket REDO-27. Software oder Container die **nicht** aus den
unten aufgeführten Quellen kommen, müssen gemäß der Richtlinie zur Installation von Software nach dem 4-Augen
geprüft werden.

## Repositories

| Name            | Beschreibung                   | Datum      | Ticket        | Kommentar                                                                                                   |
| --------------- | ------------------------------ | ---------- | ------------- | ----------------------------------------------------------------------------------------------------------- |
| Canonical       | Offizielle Ubuntu Repositories | 28.01.2025 | siehe COM-483 | ohne Einschränkungen                                                                                        |
| Ceph            | Offizielle Ceph Repositories   | 28.01.2025 | siehe COM-483 | ohne Einschränkungen                                                                                        |
| Zabbix          | Offizielle Zabbix Repositories | 28.01.2025 | siehe COM-483 | ohne Einschränkungen                                                                                        |
| PyPi            | Python Package Repository      | 29.01.2025 | siehe COM-483 | mit Einschränkungen, Ticket + Freigabe erforderlich                                                         |
| NPM             | Node Package Repository        | 29.01.2025 | siehe COM-483 | mit Einschränkungen, Ticket + Freigabe erforderlich                                                         |
| OPM             | OpenResty-Package-Manager      | 20.03.2026 | siehe COM-581 | mit Einschränkungen, Ticket + Freigabe erforderlich, z.Z beschränkt auf Paket `zmartzone/lua-resty-openidc` |
| de.NBI Cloud Bi | gitlab.ub.uni-bielefeld.de     | 29.01.2025 | siehe COM-483 | ohne Einschränkungen                                                                                        |
| de.NBI          | github.com/denbi               | 29.01.2025 | siehe COM-483 | ohne Einschränkungen                                                                                        |
| GitHub          | Einzelne Repositorien          | 20.03.2026 | siehe COM-581 | mit Einschränkungen, Ticket + Freigabe erforderlich, z.Z beschränkt auf `OpenIDC/mod_auth_openidc`          |

## Registries

| Name                       | Beschreibung                                | Datum      | Ticket        | Kommentar                                                                |
| -------------------------- | ------------------------------------------- | -----------| ------------- | ------------------------------------------------------------------------ |
| dockerhub.com              | Registry von docker                         | 28.01.2025 | siehe COM-483 | für "offizielle" Container ohne Einschränkungen, sonst Ticket + Freigabe |
| quay.io                    | Alternative Registry von RedHat             | 29.01.2025 | siehe COM-483 | Ticket + Freigabe erforderlich                                           |
| gitlab.ub.uni-bielefeld.de | de.NBI eigene Registry für Kolla Container  | 28.01.2025 | siehe COM-483 | ohne Einschränkungen                                                     |

## Weitere Quellen

| Name            | Beschreibung                                      | Datum      | Ticket        | Kommentar                                                                             |
| --------------- | ------------------------------------------------- | ---------- | ------------- | ------------------------------------------------------------------------------------- |
| Apache          | Software verwaltet von Apache Software Foundation | 20.03.2026 | siehe COM-581 | mit Einschränkungen, Ticket + Freigabe erforderlich, z.Z beschränkt auf Apache Thrift |
