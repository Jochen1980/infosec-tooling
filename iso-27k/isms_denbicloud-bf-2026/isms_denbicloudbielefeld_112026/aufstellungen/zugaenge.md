# Zugänge

Diese Aufstellung wird regelmäßig durch eprüft.
Die folgenden Zugriffslevel sind zu beachten:

- `L`: Lesezugriff
- `B`: Bearbeitungszugriff
- `A`: Administrativer Zugriff

## Zugriff auf administrative Services

Die Auflistung umfasst die folgenden Services:

- Zabbix
- Kolla Logs
- HA-Routerübersicht
- Greenbone Security Scanner
- Eramba
- ARA
- Ceph Dashboard
- Gitea

| Entität           | Begründung      | Beschränkungen | Art  |
|-------------------|-----------------|----------------|------|
| ADM               | Administratoren | -              | `A`  |
| PRT               | Administratoren | -              | `B`  |
| BRF               | Administratoren | -              | `L`  |  

## Zugriff auf sicherheitsrelevante Projekte in YouTrack

| Entität           | Begründung      | Beschränkungen | Art |
| ----------------- | --------------- | -------------- | --- |
| ADM               | Administratoren | -              | `A` |
| PRT               | Administratoren | -              | `A` |
| BRF               | Administratoren | -              | `L` |
| Alexander Sczyrba | Cloud-Leitung   | -              | `A` |
| Stefan Albaum     | BRF-Leitung     | -              | `A` |

## Zugriff auf administrative GitLab-Repositories der Cloud-Infrastruktur

| Entität | Begründung      | Beschränkungen | Art |
| ------- | --------------- | -------------- | --- |
| ADM     | Administratoren | -              | `A` |
| PRT     | Administratoren | -              | `B` |
| BRF     | Administratoren | -              | `L` |

## Zugriff auf administrative GitHUB-Repositories vom Portal/SimpleVM

| Entität | Begründung      | Beschränkungen | Art |
| ------- | --------------- | -------------- | --- |
| PRT     | Administratoren | -              | `A` |
| ADM     | Administratoren | -              | `B` |

## Zugriff auf ISMS-Repository

| Entität             | Begründung                                   | Beschränkungen     | Art |
| ------------------- | -------------------------------------------- | ------------------ | --- |
| ADM                 | Administratoren                              | -                  | `A` |
| BRF                 | Administratoren                              | -                  | `B` |
| Portal Team         | Portal/SimpleVM Administratoren              | -                  | `B` |
| Alexander Sczyrba   | Cloud-Leitung                                | -                  | `A` |
| Stefan Albaum       | BRF-Leitung                                  | -                  | `A` |
| Jens Pönninghaus    | BITS Uni Bielefeld                           | -                  | `L` |
| Michael Götting     | Techfak Uni Bielefeld                        | -                  | `L` |
| Anja Rischmüller    | ISM Uni Bielefeld                            | -                  | `L` |
| Katrin Miele        | Datenschutz- und ISK Uni Bielefeld           | -                  | `L` |
| Marc Ilgenstein     | BITS Uni Bielefeld                           | -                  | `L` |
| Björn Hagemeier     | JSC FZ Jülich                                | -                  | `L` |
| Sebastian Achilles  | JSC FZ Jülich                                | -                  | `L` |
| Ruben Simons        | JSC FZ Jülich                                | -                  | `L` |
| Thomas Schraut      | JSC FZ Jülich                                | -                  | `L` |
| Anja Schmid         | DSB Uni Bielefeld                            | -                  | `L` |
| Frank Rinkens       | ISB FZ Jülich                                | -                  | `L` |

## Zugriff auf administrativen Jump-Host und alle Maschinen im Management-Netz

| Entität | Begründung      | Beschränkungen | Art  |
|---------|-----------------|----------------|------|
| ADM     | Administratoren | -              | `B`  |
| PRT     | Administratoren | -              | `B`  |
| BRF     | Administratoren | -              | `A`  |

## Zugriff auf administrativen Netzwerk-Jump-Host

| Entität | Begründung      | Beschränkungen | Art  |
|---------|-----------------|----------------|------|
| BRF     | Administratoren | -              | `A`  |

## Zugriff auf Consulting-Jump-Host und selektive Maschinen im Management-Netz

| Entität | Begründung      | Beschränkungen | Art  |
|---------|-----------------|----------------|------|
| ADM     | Administratoren | -              | `B`  |
| PRT     | Administratoren | -              | `B`  |
| BRF     | Administratoren | -              | `A`  |

## Administrativer OpenStack-API-Zugriff

| Entität           | Begründung      | Beschränkungen     | Art  |
|-------------------|-----------------|--------------------|------|
| ADM               | Administratoren | -                  | `A`  |
| PRT               | Light-Administratoren | -            | `B`  |
| Stefan Albaum     | BRF-Leitung     | nur CeBiTec-Domäne | `A`  |

## Zugriff auf Analyse-APIs

Die Auflistung umfasst die folgenden APIs:

- GPU Resource Exporter API
- Cloud Usage Script API

| Entität     | Begründung                                   | Beschränkungen | Art |
|-------------|----------------------------------------------|----------------|-----|
| ADM         | Administratoren                              | -              | `A` |
| PRT         | Erhebung von Statistiken / Ressourcenplanung | -              | `B` |

## Zugriff auf InfluxDB mit Monitoring-Daten (IT-Verfahren 4.10.3.9)

Zugriff auf die Instanz des Cloud-Standorts Bielefeld

| Entität     | Begründung                                   | Beschränkungen | Art |
|-------------|----------------------------------------------|----------------|-----|
| ADM         | Cloud Administratoren                        | -              | `A` |
| PRT         | Light-Administratoren                        | -              | `A` |

## Zugriff auf die zentrale Datenbank mit aggregierten Nutzungsdaten

| Entität          | Begründung                              | Beschränkungen | Art |
|------------------|-----------------------------------------|----------------|-----|
| ADM              | Cloud Administratoren                   | -              | `A` |
| PRT              | Portal/SimpleVM Administratoren         | -              | `B` |
| Torben Lambrecht | Bachelorarbeit                          | -              | `L` |

## Zugriff auf das de.NBI Cloud Portal

| Entität          | Begründung                              | Beschränkungen | Art |
|------------------|-----------------------------------------|----------------|-----|
| PRT              | Portal/SimpleVM Administratoren         | -              | `A` |
| ADM              | Light Administratoren                   | -              | `B` |

## Zugriff auf das de.NBI SimpleVM

| Entität          | Begründung                              | Beschränkungen | Art |
|------------------|-----------------------------------------|----------------|-----|
| PRT              | Portal/SimpleVM Administratoren         | -              | `A` |
| ADM              | Light Administratoren                   | -              | `B` |

## Zugriff auf den HelpDesk

| Entität          | Begründung                              | Beschränkungen | Art |
|------------------|-----------------------------------------|----------------|-----|
| PRT              | Portal/SimpleVM Administratoren         | -              | `A` |
| ADM              | Light Administratoren                   | -              | `B` |
