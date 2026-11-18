# Strombedarf

Aufstellung des Strombedarfs der de.NBI Cloud Bielefeld basierend auf einer Kombination
aus Messung und Schätzung bzw. auf Angaben aus den Leistungsverzeichnissen der Lieferanten.

## OpenStack

| Lieferung | Besitzer | Anzahl in Betrieb | Name                             | HE | ∑ HE    | typ W | ∑ typ W | max W | ∑ max W | Quelle für Strombedarf |
|-----------|----------|------------------:|----------------------------------|---:|--------:|------:|--------:|------:|--------:|------------------------|
| 2018      | UniBi    |                   |                                  |    |         |       |         |       |         |                        |
|           |          |           3 von 4 | DELL Poweredge R740 GPU/T4       |  2 |    8    |   300 |     900 |   575 |    1725 | Messung                |
|           |          |                 5 | DELL Poweredge R740 GPU/P100     |  2 |   10    |   400 |    2000 |  1000 |    5000 | Messung                |
| 2019      | UniBi    |                   |                                  |    |         |       |         |       |         |                        |
|           |          |                10 | DELTA Tyan GPU/V100              |  2 |   20    |   400 |    4000 |  1000 |   10000 | Schätzung              |
|           |          |         37 von 38 | DELTA SuMi AMD                   |  2 |   76    |   150 |    5550 |   400 |   14800 | Schätzung              |
| 2020      | UniBi    |                   |                                  |    |         |       |         |       |         |                        |
|           |          |                 4 | RaidMedia SuMi Highmem           |  2 |    8    |   400 |    1600 |   750 |    3000 | Messung/Leistungsverzeichnis   |
|           |          |                15 | RaidMedia SuMi GPU/T4            |  1 |   30    |   150 |    2250 |   490 |    7350 | Messung/Leistungsverzeichnis   |
|           |          |            49 von 50 | RaidMedia SuMi                |  1 |   50    |   120 |    1680 |   300 |   1400 | Messung/Leistungsverzeichnis   |
| 2021      | UniBi    |                   |                                  |    |         |       |         |       |         |                        |
|           |          |                28 | DELL Poweredge  R7525 Largescale |  2 |   56    |   520 |   14560 |  1050 |   29400 | Messung/Leistungsverzeichnis   |
|           |          |                 4 | DELL Poweredge  R7525 Highmem    |  2 |    8    |   570 |    2280 |  1200 |    4800 | Messung/Leistungsverzeichnis   |
|           |          |                10 | DELL Poweredge R7525 GPU/A100    |  2 |   20    |   650 |    6500 |  1000 |   10000 | Messung/Leistungsverzeichnis   |
|           |          |           8 von 9 | DELL Poweredge R7515             |  2 |   16    |   250 |    2000 |   450 |    3600 | Messung/Leistungsverzeichnis   |
| 2023      | FZJ      |                   |                                  |    |         |       |         |       |         |                        |
|           |          |                 3 | DELTA23 SuMi Controller (FZJ)    |  2 |    6    |   150 |     450 |   330 |     990 | Messung/Leistungsverzeichnis   |
|           |          |                 2 | DELTA23 SuMi Service (FZJ)       |  2 |    4    |   120 |     240 |   250 |     500 | Messung/Leistungsverzeichnis   |
|           |          |                 6 | DELTA23 GPU A40   (FZJ)          |  4 |   24    |   400 |    2400 |  1800 |   10800 | Messung/Leistungsverzeichnis   |
| 2024      | FZJ      |                   |                                  |    |         |       |         |       |         |                        |
|           |          |                12 | DELTA24 GP   (FZJ)               |  2 |   24    |   140 |    1680 |   400 |    4800 | Messung/Leistungsverzeichnis   |
|           |          |                 4 | DELTA24 GPU L4   (FZJ)           |  4 |   16    |   640 |    2560 |  1500 |    6000 | Messung/Leistungsverzeichnis   |
|           |          |                 1 | DELTA24 GPU H100   (FZJ)         |  4 |    4    |   750 |    2500 |   750 |    2500 | Messung/Leistungsverzeichnis   |
| **SUMME** |          |           **204** |                                  |    | **379** |       |**53.120** |     | **129965** |                    |

Die Summen für idle/typ bzw. max sind lediglich als grobe Schätzwerte zu sehen,
da eine direkte Messung nicht flächendeckend möglich ist.

## Ceph

| Lieferung  | Besitzer | Anzahl in Betrieb | Name             | HE |    ∑ HE |typ W | ∑ typ W | max W | ∑ max W | Quelle für Strombedarf |
|------------|----------|------------------:|------------------|----|--------:|-----:|--------:|------:|--------:|------------------------|
| 2020       | UniBi    |                 4 | DELTA20 SuMi     |  4 |      16 |  360 |    1440 |   600 |    2400 | Leistungsverzeichnis   |
| 2021       | UniBi    |                20 | MemorySolutions  |  4 |      80 |  360 |    7200 |   600 |   12000 | Leistungsverzeichnis   |
| 2023       | FZJ      |                 8 | DELTA23 SuMi     |  4 |      32 |  360 |    2880 |   600 |    4800 | Messung/Leistungsverzeichnis   |
| 2023       | FZJ      |                 6 | DELTA23 SuMi SSD |  2 |      12 |  220 |    1320 |   480 |    2280 | Messung/Leistungsverzeichnis   |
| 2024       | FZJ      |                 9 | DELTA24 SuMi     |  4 |      36 |  560 |    5040 |   780 |    7020 | Messung/Leistungsverzeichnis   |
| **Gesamt** |          |            **47** |                  |    | **176** |      | **17.880** |    |**28.500** |                              |

Die Summen für typ bzw. max sind lediglich als Schätzwerte zu sehen,
da eine direkte Messung nicht flächendeckend möglich ist.
