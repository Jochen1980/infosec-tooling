# Arbeitsanweisung zu IT-Monitoring

|                 |                                             |
|-----------------|---------------------------------------------|
| Version:        | 0.2                                         |
| Version vom:    | 21.02.2024                                  |
| Erstellt durch: | Alex Walender, Jan Krüger                   |
| Genehmigt am:   | 06.03.2024 (alu), 12.03.2024 (as)           |
| durch:          | Alexander Sczyrba (as), Stefan Albaum (alu) |

## Ziel dieser Arbeitsanweisung

Dieses Dokument gibt eine Übersicht über die Monitoring-Aktivitäten der de.NBI Cloud Bielefeld,
und wie bei entsprechenden Anomalien vorzugehen ist.

## Anwendungsbereich

Die Arbeitsanweisung gilt für alle Mitarbeiter von ADM und BRF für
die de.NBI Cloud Bielefeld.

## Zuständigkeit

ADM und BRF.

## Beschreibung

Diese Tabelle beinhaltet eine Auflistung aller erforderlichen Applikationen die nötig
sind, um die IT-Infrastruktur zu überwachen.

| Anwendung  | Zweck                                                                                                                    | Weiterführende Informationen                                            | Aufbewahrungszeiten                         | Beinhaltet Personenbezogene Daten            |
|------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------|
| Zabbix     | Überwachung und Alarmierung zahlreicher Komponenten auf Hard- und Softwareebene. Hauptanwendung bezüglich des Monitoring | [IT-5 Zabbix](../it-verfahren.md#it-5-zabbix)                           | Variabel je nach Template, maximal 2 Jahre. | Nein                                         |
| Greenbone  | Überwachung und Alarmierung von Schwachstellen der Nutzer-VMs, welche Ports über das Internet verfügbar machen.          | [IT-7 Greenbone](../it-verfahren.md#it-7-openvasgsm)                    | 7 Tage                                      | Öffentliche IP-Adressen aus dem eigenem Netz |
| CVE-Scans  | Regelmäßige Überwachung sämtlicher Server auf neu entdeckte Schwachstellen                                               | [IT-8 CVE-Scan](it-verfahren.md#it-8-cve-scans)                         | Unbestimmt                                  | Nein                                         |
| Kolla-Logs | Sammlung sämtliche Logdaten der OpenStack-Installation mit Filteroptionen                                                | [REDO-19](https://yt.bi.denbi.de/issue/REDO-19/Sichtung-der-Kolla-Logs) | > 7 Tage                                    | Nein (Maskierung externer IP Adressen)       |
| ARA        | Log des Changemanagements (Ansible)                                                                                      | [IT 4.10.3.7](../it-verfahren.md#it-41037-ara))                         | > 7 Tage                                    | Nein                                         |

## Umgangsarten bei Anomalien

Aufgrund der Komplexität und hohen Anzahl an zu überwachenden Komponenten kann hier
keine pauschalisierte Anleitung bezüglich Eskalationen gegeben werden.

Bei der Detektierung einer Anomalie muss diese im Einzelfall bewertet werden:

1. Sind die Schutzziele (Vertraulichkeit, Verfügbarkeit und Integrität) durch die Anomalie gefährdet?
1. Wie hoch ist der potentielle Impact der Anomalie?
1. Gegebenenfalls ist die Anomalie ein Hinweis auf eine [Katastrophe](Business_Continuity.md).

Ebenfalls ist zu entscheiden, ob die detektierte Anomalie einen Sicherheitsvorfall begründet.
Die folgenden Unterkapitel geben dazu eine Hilfestellung.

Anomalien sind grundsätzlich zu dokumentieren. Bei Störungen im IT-Betrieb die eine Änderung
verlangen, sind diese wie gewohnt im [YouTrack](https://yt.bi.denbi.de) zu erfassen und
zu bearbeiten. Andernfalls werden Meldungen im Zabbix **acknowledged** und ggf. geschlossen.

## Spezifische Komponenten der Überwachung

Die folgenden Unterkapitel sind inhaltlich dem Appendix 8.16 der ISO27002-2022 angelehnt.

### Analyse des Netzwerkverkehrs sowie deren Ereignissen

Zurzeit werden quantitative Werte des Netzwerkverkehrs innerhalb des Geltungsbereiches
aufgezeichnet. Auf Hardware-Ebene werden hier die messbaren Bandbreiten der einzelnen
Netzwerkkarten erfasst. Es erfolgt hierbei eine Alarm-Meldung wenn die Bandbreiten
kurz vor der Auslastung stehen, die Bandbreite des Links sich unerwartet reduziert oder
fallen gelassene Pakete registriert werden. In Zabbix wird dies im
"Linux by Zabbix agent"-Template bereitgestellt.

Die OpenStack-Installation, sowie die Dienste der Service-Knoten werden durch HAProxy
dem Nutzer bereitgestellt. Auch diese Komponente wird durch Zabbix überwacht 
(Template -> "HAProxy by HTTP"). Hierbei wird überwacht:

1. Metriken über die Verbindungen, Reaktionszeiten und Verfügbarkeit der Backends.
1. Verfügbarkeits-Checks der Endpunkte (Zabbix Dashboard -> "SLA")
1. Alarmierung bei abnormalen Abweichungen der Metriken, unter anderem bei ungewöhnlichen Anhäufungen von HTTP-Fehlercodes.

Bezüglich eines "Intrusion Detection Systems" existiert ein
[Projekt](https://yt.bi.denbi.de/issue/COM-382/Prj-Einfuhrung-eines-Network-Monitoring-IDS-System-Masterarbeit)
welches gezielt für unsere Netzwerkinfrastruktur umgesetzt wird.

### Zugriff auf Server, Monitoring-Systemen, Kritische Anwendungen und Netzwerkhardware

Sämtliche Hardware in den Datenzentren sind mit dem IPMI-Interface ausgestattet.
Diese Schnittstelle zeichnet unter anderem auf, wenn die Gehäuse geöffnet werden
oder neue USB-Geräte detektiert werden. Diese Events werden ebenfalls über Zabbix
alarmiert (Template -> "IPMI"). Diese Events werden nicht automatisiert geschlossen und müssen von einem Administrator bestätigt werden.

(Kritische)Anwendungen werden in ihrer Verfügbarkeit durchgehend
überwacht. Dies erfolgt über Endpunktüberwachung und/oder durch
sogenannte "Heartbeat"-Checks. In containerisierten Anwendungen,
wie beispielsweise die OpenStack-Installation, werden diese
durchgehend auf Erreichbarkeit und Funktion überwacht und ggf alarmiert.

### Überwachung von kritischen Konfigurationsdateien

Die reale Anzahl von kritischen Konfigurationsdateien im Geltungsbereich ist überschaubar.
Kritische Konfigurationsdateien, wie Passwörter-Listen sind sicher abgelegt und müssen
jederzeit für die Administratoren zugreifbar sein, insbesondere für das regelmäßig
stattfindende Patchmanagement. Eine zusätzliche Überwachung auf Zugriffe seitens
der Mitarbeiter bringt dabei keinen Mehrwert.

### Logging der Anwendungen

Wesentliche Logs von Sicherheitsanwendungen werden in Zabbix mithilfe der entsprechenden
Templates gesammelt und in den konfigurierten Zeitabschnitten gespeichert.
Entspringen aus dem Logs Sicherheitsvorfälle, so werden in den einzeln dokumentierten Vorfälle
entsprechende Ausschnitte der Logs beigefügt.
Bei Sicherheitsvorfällen die durch Greenbone erkannt worden sind, wird dem Vorfall
das Greenbone-Protokoll beigefügt und somit auf unbestimmte Zeit gespeichert.
Greenbone ist so konfiguriert, dass bei Fund von neuen Schwachstellen die Administratoren
per Mail benachrichtigt werden. Bei Auftreten solch einer Alarmierung ist umgehend
das neuste Greenbone-Protokoll zu überprüfen und zu bearbeiten, siehe [IT-7.3.1](../it-verfahren.md#it-73-scan-results).

### Überwachung der Nutzung von Ressourcen

Die Ressourcen beziehen sich hierbei auf:

- Prozessorauslastung
- Hauptspeicher
- Festplattenspeicher

Jede dieser Ressourcen werden pro Server automatisiert durch Zabbix detektiert 
(Template -> "Linux by Zabbix agent") und überwacht. Erreichen die Werte einen
kritischen Schwellenwert, so werden die Administratoren durch Alarme benachrichtigt.

Erfahrungsgemäß betreffen diese Probleme hauptsächlich die Compute-Knoten der
OpenStack-Installation. In unglücklichen Fällen befinden sich mehrere Instanzen
auf einen Compute-Knoten die mit voller Last laufen. Hier bietet es sich an,
einzelne Instanzen von dem Knoten auf einen anderen zu migrieren, siehe [IT-9.2.1](../it-verfahren.md#it-921-migration-von-virtuellen-maschinen).

## Erweiterungen und Modifikationen des Monitorings

### Hinzunahme von Anwendungen

Werden Anwendungen oder Systeme dem Geltungsbereich hinzugefügt,
so muss analysiert werden, inwiefern die Funktionalität
durch die jetzigen Werkzeuge überwacht werden können.
Bei der allgemeinen Funktionalität bietet es sich an diese über Zabbix
zu überwachen.

Bietet die Anwendung eine Schnittstelle über HTTP an und ist über das Internet
zu erreichen, so sollte diese mittels Greenbone überwacht werden.

### Modifikation von Grenzwerten

Grenzwerte bezüglich der Alarmierung müssen je nach Kontext angepasst werden,
um potentielle falsch-positiv - Meldungen zu unterdrücken.
Änderungen an den Grenzwerten erfolgen im 4-Augen-Prinzip und
werden im YouTrack dokumentiert.

## ChangeLog

- Version 0.2 vom 21.02.2024: ARA ergänzt 
- Version 0.1 vom 19.01.2024: initialer Entwurf
