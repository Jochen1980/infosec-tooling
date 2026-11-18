# Messungen zur Informationssicherheitsleistung und ISMS-Wirksamkeit

Die de.NBI Cloud Bielefeld misst regelmäßig die Informationssicherheitsleistung und die Wirksamkeit
des ISMS um die in der Leitlinie festgelegten Informationssicherheitsziele zu ereichen. 
Die Messpunkte werden jeweils im  Rahmen des nächsten Besprechungstermins zur kontinuierlichen
Verbesserung des ISMS gemeinsam mit der obersten Leitung analysiert und bewertet.

## Metriken

| Kategorie                  | Messobjekt                              | Metrik                                                                    | Quelle                              | Zielwert | Begründung |
|----------------------------|-----------------------------------------|---------------------------------------------------------------------------|-------------------------------------|----------| ---------- |
| Fortbildung                | Fortbildungen pro MA                    | Anzahl der Fortbildungen pro 100% MA Stelle im Scope                      | ISMS (Liste der Fortbildungen)      | ≥ 2      | Die MA im Scope müssen adequart geschult werden. |
| Sicherheitsvorfälle        | Reaktionszeit auf Sicherheitsvorfälle   | Tage zwischen Bekanntwerden und erster Reaktion auf Sicherheitsvorfälle   | Ticketsystem (YouTrack)             | 0        |            |
| Schwachstellen A           | Detektierte Schwachstellen              | Anzahl der als High oder Medium detektierten Schwachstellen               | Schwachstellenscanner(GVM)          | 0        | Idealerweise gibt es keine offene Schwachstellen |
| Schwachstellen B           | Durchgeführte Pentests                  | Anzahl Tage pro Jahr mit erfolgtem Pentest                                | Schwachstellenscanner(GVM)          | 365      | Der Scanner sollte jeden Tag laufen              |
| Notfallmanagement / BCM    | Krisenübung                             | Anzahl Übungen pro Jahr                                                   | [REDO-22](https://yt.bi.denbi.de/issue/REDO-22)| 1          | Vorgabe                             |
| Patchmanagement            | Regelmäßigkeit der Playbookruns         | Anzahl 14 tägiger Playbookruns pro Jahr                                   | [REDO-3](https://yt.bi.denbi.de/issue/REDO-3)  | ≥ 21       | 80 % der möglichen PR sind machbar  | 
| Instandhaltung             | Hardwarepflege                          | Anteil Server mit aktivem Wartungsvertrag (WV)- Compute                   | Zabbix                              | 50%      | Erfahrungswert ²                                 |
| Instandhaltung             | Hardwarepflege                          | Anteil Server mit aktivem Wartungsvertrag (WV) - Storage                  | Zabbix                              | 66%      | 3-fach Redundanz  ³                              |
| Instandhaltung             | Hardwarepflege                          | Anteil Server mit aktivem Wartungsvertrag (WV) - Zentrale Server          | Zabbix                              | 66%      | min. 3-fach Redundanz ⁴                          |
| ISMS-Koordination          | Regelmäßigkeit der Managementreviews    | Anzahl der Managementreviews pro Jahr                                     | [REDO-11](https://yt.bi.denbi.de/issue/REDO-11)| ≥2         | vierteljährlich angesetzt           |
| ISMS-Risikomanagement A    | Regelmäßigkeit der Risiko-Reviews       | Anzahl der Risiko-Reviews pro Jahr                                        | [REDO-26](https://yt.bi.denbi.de/issue/REDO-26)| 1          | Risiken werden jährlich reviewed    |
| ISMS-Risikomanagement B    | Asset Risk Reduction Factor             | Verhältnis der mitigierten Risiken zur Gesamtanzahl der Risiken           | Asset Risk Reduction Factor (Eramba) | < 0.8 |  |
| ~~ISMS~~                   | Reviewumfang der ISMS-Dokumente         | Anteil der geprüften Dokumente am Gesamtumfang der zu prüfenden Dokumente | Risikomanagementsystem (Eramba)     | -        |            |  |  
| ~~Risikomanagement~~       | Bewertung akzeptierter Risiken          | Ältestes Bewertungsdatum eines explizit akzeptierten Risikos              | Risikomanagementsystem (Eramba)     | -        |            |
| ~~Schadsoftware~~          | Malwareschutz                           | Anteil der Geräte mit Malwareschutz                                       | Monitoring (Wazuh)                  | -        |            |
| ~~Endnutzerverfügbarkeit~~ | Operabilität der Cloud (API)            | Tage pro Jahr                                                             | HTTP Monitoring (Zabbix): Dashboard | 100%     |            |
| ~~Endnutzerverfügbarkeit~~ | Konnektivität der Cloud (Laufende VMs)  | Tage pro Jahr                                                             | HTTP Monitoring (Zabbix): VM        | 100%     |            |

Der Messzeitraum umfasst für alle Metriken immer ein Jahr mit Ausnahme der Schwachstellen und dem
Asset Risk Reduction Factor (Momentaufnahme) 

Die Metriken zum ISMS bezüglich der Reviews und der Bewertung von Risiken sowie zur Schadsoftware
werden nach dem Beschluss vom [ManagementReview vom 25.05.2022](https://yt.bi.denbi.de/issue/P-126) 
nicht mehr berücksichtigt. Die Messwerte zu den Metriken waren von dem Zeitraum (Mai 2021 bis Mai 2022)
über das letzte Jahr hinweg konstant und bieten keinen (Mehr-)Wert bei der Beurteilung der ISMS 
Wirksamkeit.

- ² mit 50% der Compute können erfahrungsgemäß die grundlegenden Ansprüche unsere Kunden bedient werden
- ³ min. 2 der 3 gespeicherten Kopien eines Objekts sollte auf Hardware mit Wartung gespeichert werden
- ⁴ min. 2 der 3 Controller bzw. 4 der 6 Netzwerk-Controller sollten Wartung haben

## Messbarkeit der Informationssicherheitsziele

Die folgende Zuordnung der Informationssicherheitsziele zu den KPIs erleichert die Einschätzung
ob die Informationssicherheitsziele erreicht wurden.

| Ziel                                                                                                | Maßnahme durch KPI messbar                        |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Wir schützen Informationen der de.NBI Cloud Bielefeld gegen Offenlegung, Verfälschung und Verlust.  | alle                                              |
| Wir streben eine ausreichende Verfügbarkeit an.                                                     | Instandhaltung/Wartungsverträge, Patch-Management | 
| Wir prüfen den Schutzbedarf der Informationen in unserem Tätigkeitsfeld und leiten daraus konkrete Schutzmaßnahmen ab. | Asset Risk Reduction Factor    |
| Wir halten unsere Informationssysteme auf einem aktuellen und sicheren Stand.                       | Patch-Management,  CVE-Management                 |
| Wir überprüfen regelmäßig die Wirksamkeit von Schutzmaßnahmen.                                      | Schwachstellen-Management                         |
| Wir melden Informationssicherheitsvorfälle.                                                         | Reaktionszeit auf Sicherheitsvorfälle             |
| Wir sensibilisieren unsere Mitarbeiter für IT-Sicherheit.                                           | Kompetenzmatrix / Schulungsplan                   |

## Messpunkte

| Datum      |  Fortbildungen | Sicherheitsvorfälle   |  Schwachstellen A |  Schwachstellen B |  Notfallmanagement |  Patchmanagement |  WV Compute |  WV Storage | WV Zentrale Server | ISMS-Koordination | ISMS-Risikomanagement A | ISMS-Risikomanagement B |
|------------|---------------:|-----------------------|------------------:|------------------:|-------------------:|-----------------:|------------:|------------:|-------------------:|------------------:|------------------------:|------------------------:|
| 05.10.2021 |              7 | 0,67 Tage             |                 - |                   |                    |                6 |        100% |        100% |               100% |                 2 |                       1 |                         |
| 09.12.2021 |              5 | 0,67 Tage             |                22 |                   |                    |                6 |        100% |        100% |               100% |                 3 |                       1 |                         |
| 04.02.2022 |            6,3 | 1,25 Tage             |                17 |                   |                    |                6 |        100% |        100% |               100% |                 4 |                       1 |                         |
| 24.03.2022 |              6 | 1 Tag                 |                12 |                   |                    |                7 |        100% |        100% |               100% |                 5 |                       1 |                         |
| 25.05.2022 |            3,6 | 1,5 Tage              |                 8 |                   |                    |                9 |        100% |        100% |               100% |                 6 |                       1 |                         |
| 18.07.2022 |            4,4 | 2,5 Tage (2 Vorfälle) |                 2 |                   |                    |                9 |        100% |        100% |               100% |                 5 |                       1 |                         |
| 23.09.2022 |            3,1 | 4 Tage (1 Vorfall)    |                 0 |                   |                    |           **10** |        100% |        100% |               100% |                 5 |                       1 |                         |
| 16.11.2022 |            3,1 | 4 Tage (1 Vorfall)    |                 0 |                   |                    |           **12** |        100% |        100% |               100% |                 5 |                       1 |                         |
| 28.02.2023 |              3 | 0 Tage (1 Vorfall)    |                 0 |                   |                    |           **16** |         75% |     **59%** |             **0%** |                 5 |                       1 |                         |
| 01.06.2023 |            3,4 | 2 Tage (2 Vorfälle)   |                 6 |                   |                    |           **15** |         75% |     **59%** |            **38%** |                 3 |                       1 |                         |
| 05.03.2024 |            2,5 | 5 Tage (5 Vorfälle)   |                 0 |               365 |                  1 |           **10** |         75% |         77% |            **62%** |                 3 |                       1 |                         |
| 08.04.2025 |            2,8 | 5 Tage (5 Vorfälle)   |                 0 |               365 |                  1 |               23 |         69% |        100% |               100% |                 2 |                       1 |                         |
| 08.07.2025 |            2,4 | 5 Tage (5 Vorfälle)   |                 0 |               365 |                  1 |               21 |         74% |        100% |               100% |                 2 |                       1 |                         |
| 30.10.2025 |            2,1 | 4 Tage (3 Vorfälle)   |                 0 |               365 |                  1 |               21 |     **40%** |         91% |               100% |                 2 |                       1 |                         |
| 05.01.2025 |            2,1 | 1,5 Tage (5 Vorfälle) |                 0 |               365 |                  1 |               22 |     **40%** |         91% |               100% |                 3 |                       1 |                         |
| 21.04.2026 |       **1,75** | 1,5 Tage (8 Vorfälle) |                 0 |           **363** |                  1 |               22 |     **40%** |         91% |               100% |                 3 |                       1 |                    0,6  |
| 06.07.2026 |       **1,75** | 2 Tage (17 Vorfälle)  |                 0 |           **363** |                  1 |               24 |     **40%** |         91% |               100% |                 3 |                       1 |                   0,59  |
| 16.10.2026 |       **1,75** | 5 Tage (19 Vorfälle)  |                 0 |           **363** |                  1 |               25 |     **40%** |         91% |               100% |                 4 |                       1 |                   0,61  |
