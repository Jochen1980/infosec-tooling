# Werte der de.NBI Cloud Bielefeld 

Das Dokument dient der **Übersicht** über alle bei der de.NBI Cloud
vorhandenen Werte.

Eine detaillierte Auflistung aller Werte und Geschäftsprozesse
findet sich im Eramba (siehe IT-14).

Die Werte der Cloud sind gemäß des ISMS den
Kategorien Hardware, Software, Personal und Daten zuzuordnen. Werte
aus den Kategorien Hardware, Software und Daten haben gemäß der RASCI-Matrix
(➝ M 2.5) einen Verantwortlichen (Responsible) sowie einen
Rechenschaftspflichtigen (Accountable). Da Werte bis auf wenige
Ausnahmen (z. B. Kabel, Server ohne Festspeicher) immer mit
Informationen verbunden sind, sind diese
gemäß der ➝ _Richtlinie zur Klassifikation und Kennzeichnung von Informationen_
durch die Kritikalität der darauf befindlichen Informationen gekennzeichnet.

## Zulässiger Gebrauch von Werten

Sämtliche Werte haben einen definierten zulässigen Gebrauch. Der zulässige
Gebrauch ist ebenfalls in der GRC-Software _Eramba_ pro Wert definiert worden.
Gemäß des ISMS haben sich alle Mitarbeiter an diese Vorgaben zu halten.

## Hardware

Die Hardware unterliegt der Verantwortlichkeit der BRF, umfasst die
zum Betrieb notwendige Server-Hardware wie Controller, Hypervisor,
Storage und Netzwerkkomponenten und ist immer in einem der beiden 
Datacenter verortet. Der genaue Standort (Schrankreihe, Einbauposition) 
jedes einzelnen erfassten Geräts ist in Zabbix (➝ IT 5) bzw. der 
Inventur-Datenbank erfasst.

| Beschreibung | Ort                            | Verantwortlichkeiten | weiterführende_Informationen | Priorität |
|--------------|--------------------------------|----------------------|------------------------------|-----------|
| Controller   | V0-200                         | BRF / AN             | ➝ Zabbix / IT-5              | Hoch      |
| Hypervisor   | V0-200                         | BRF / AN             | ➝ Zabbix / IT-5              | Mittel    |
| Service      | V0-200                         | BRF / AN             | ➝ Zabbix / IT-5              | Niedrig   |
| Ceph         | V0-200 (2/3) und W01-178 (1/3) | BRF / AN             | ➝ Zabbix / IT-5              | Mittel    |
| Switch       | V0-200 und W01-178             | BRF / AN             | ➝ InventurDB                 |           |
| Kabel        | V0-200 und W01-178             | BRF / AN             | ➝ InventurDB                 |           |

## Software

Die Software zum Betrieb der Cloud liegt im Verantwortungsbereich von 
ADM. Jegliche Software, die zum Betrieb der Cloud benötigt wird, 
wird mittels Ansible installiert und gewartet. Die dazu notwendigen
Playbooks, Rollen und Tasks sind im GitLab der Universität Bielefeld
gespeichert (siehe Daten).

| Beschreibung | Ort | Verantwortlichkeiten | weiterführende_Informationen |
|------------|--------------------------------|----------|----------|
| Openstack  | Controller / Hypervisor | ADM / JK | ➝ IT-4.10, IT-4.11, IT-9 |
| Ceph  | Ceph Server | ADM / AW | ➝ IT-4.40, IT-4.41, IT-10 |
| Services (intern)  | Service Server (intern) | ADM / diverse | ➝ M 2.5 |
| Services (extern)  | Service Server (extern) | ADM / diverse | ➝ M 2.5 |

## Personal

Das Personal der de.NBI Cloud Bielefeld stellt vor allem aufgrund der kleinen
Arbeitsgruppengröße und der damit verbundenen Mehrfachverantwortlichkeiten einzelner
Mitarbeiter einen nicht unerheblichen Wert für den Betrieb der Cloud dar.
Die RASCI-Matrix (➝ M 2.5) zeigt die verantwortlichen und unterstützenden
Mitarbeiter für die 
unterschiedlichen IT-Verfahren. Alle unter M 2.2 aufgeführten MA sind an der 
Universität Bielefeld angestellt und dort beschäftigt.

## Daten

Zu den essenziellen Werten gehören auch die zum Betrieb der
Cloud notwendigen Daten.

| Beschreibung            | Speicherort                               | Verantwortlichkeiten | 
|-------------------------|-------------------------------------------|----------------------|
| Repositories            | NoteBook, GitLab(UniBi), BITS/Band        | ➝ RASCI-Matrix       |
| Secrets                 | JumpHost/CeBiTec FS, Band                 | ➝ RASCI-Matrix       |
| Openstack               | Controller(Galera DB), Ceph, CeBiTec/Band | ➝ RASCI-Matrix       |
| Openstack (Nutzerdaten) | Hypervisor/Ceph                           |  ADM                 |
| Ceph (Betrieb)          | Ceph Monitore                             | ➝ RASCI-Matrix       |
| Ceph (Nutzerdaten)      | Ceph                                      | ADM                  |
| YouTrack                | Service Server, Ceph, CeBiTec/Band        | ➝ RASCI-Matrix       |
| Zabbix                  | Service Server, Ceph, CeBiTec/Band        | ➝ RASCI-Matrix       |
| CVE-Scans               | Service Server, Ceph                      | ➝ RASCI-Matrix       |
| OpenVAS/GVM             | Service Server, Ceph                      | ➝ RASCI-Matrix       |
| ARA                     | Service Server, Ceph                      | ➝ RASCI-Matrix       |

