# Auditprogramm 

Alle Teile des ISMS müssen mindestens einmal jährlich in _Audits_
darauf überprüft werden, ob sie den Anforderungen der de.NBI Cloud Bielefeld an ein
ISMS gerecht werden. Das Ergebnis eines Audits muss in jedem Fall dokumentiert werden. 
Die aus einem Audit hervorgehenden Lücken bzw. Abweichungen gegenüber der Norm 
sind in einem Ticket abzulegen und in Absprache einer zu bearbeitenden Person 
zuzuordnen.

## Interne Audits durch Mitarbeiter

Das gesamte ISMS wird regelmäßig (mindestens jährlich) durch die Mitarbeiter
der de.NBI Cloud Bielefeld auditiert. Dabei ist nach der
[RASCI Matrix](../organisation.md#rasci-matrix-der-aufgabenverteilung-und-verantwortlichkeiten) darauf zu achten, 
das es nicht zu Interessenskonflikten kommt.

**Beispiel:**

Die IT-Verfahren zur Installation des Cloud-Frameworks OpenStack sollen auditiert werden.

| IT-Verfahren | Aufgabe              | `jk` | `aw` | `ch` | `vr` | `an` | `bf` | `tk` | `rn` | `ro` | `sa` | `as` |
|-------------:|----------------------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|          ... |                      |      |      |      |      |      |      |      |      |      |      |      | 
|      IT-4.10 | Installation         |  `R` |  `S` |  `S` |  `I` |  `I` | `I`  |  `I` | `I`  |      |  `I` |  `A` |
|          ... |                      |      |      |      |      |      |      |      |      |      |      |      | 

Nach der RASCI Matrix ist `jk` verantwortlich für das Verfahren und wird dabei durch
`aw` und `ch` unterstützt. Alle anderen Mitarbeiter der Gruppe BRF sind über das
Verfahren nur informiert. Idealerweise sollte das Verfahren also von Mitarbeitern der
Gruppe BRF geprüft werden. 

_In der Praxis hat sich allerdings schnell herausgestellt, dass diese Vorgehensweise
in vielen Fällen nicht zielführend ist, da entweder nicht die Expertise vorhanden ist, das
jeweilige Verfahren in angemessener Zeit zu überprüfen, oder vor allem beim Managementteil des
ISMS kein unabhängiges Audit möglich ist._

Interne Audits durch Mitarbeiter werden vollständig über die Risikomanagement- und 
Auditsoftware [Eramba](https://risks.bi.denbi.de) abgedeckt. Eramba unterstützt Audits
für interne Controls (linkes Menü: _Controls Catalogue_ -> _Internal Controls_) sowie
Richtlinien/Arbeitsanweisungen (linkes Menü: _Controls Catalogue_ -> _Security Policies_)
und bietet vielseitige Möglichkeiten, diese nach unterschiedlichen 
Kriterien zu filtern. Der jeweils angegebene geplante Audit-Termin(_Planned Start_) ist als 
letztmöglicher Termin für ein Review zu verstehen. Ein Audit darf auch schon eher erfolgen.

### Prozess zur Begutachtung eines Controls sowie einer Richtlinie/Arbeitsanweisung

1. Wechsel in den Audit-Modus (Menü oben: _Audits_)
1. Auswahl des zu begutachtenden Controls (Menüicon: _Complete Missing Audit_)
1. Die Felder _Audit Result_, _Audit Conclusion_, _Audit Start_ und _Audit End_ müssen 
   ausgefüllt werden. Die _Audit Methodology_ sollte dem tatsächlichen Vorgehen entsprechen
   und muss gegebenenfalls angepasst werden. In die _Audit Conclusion_ sollte man bei Änderungen
   am Control das dazugehörige Ticket verlinken. In das Feld _Audit Owner_ sollte, falls hier
   eine Gruppe voreingetragen ist, zusätzlich auch die Person eingetragen werden, die das Audit 
   durchführt. Unter _evidence_ lassen zusätzliche Dokumente an das Review anhängen.

## Interne Audits durch Externe

Aufgrund der eingeschränkten Anzahl an Mitarbeitern in den Arbeitsgruppen ADM bzw. BRF sind
Unparteilichkeit und Objektivität mangels vollständiger Rollentrennung nicht
immer garantiert. Vor allem der Managementteil des ISMS (ISO 27001 4-10) muss daher zusätzlich
durch einen externen Auditor mindestens jährlich überprüft werden. Hierfür ist nach Absprache 
ein Mitarbeiter aus einem der anderen de.NBI Standorte vorgesehen.

## Zeitplan

| Datum            | Themen                                                                                                | Auditor | Protokoll (Tickets)                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------|---------|---------------------------------------------------------------------------------------------------|
| 17.-18.06.2020   | Vollständiges Test-Assessment nach ISO 27001                                                          | `dz`    | [GAP-Analyse](https://docs.cebitec.uni-bielefeld.de/f/1982374), [Tickets](https://yt.bi.denbi.de) |
| 26.01.2021       | Prüfung der Lücken aus dem Test-Assessment (Management)                                               | `dz`    | [Tickets](https://yt.bi.denbi.de)                                                                 |
| 29.-31.03.2021   | Risikomanagement                                                                                      | `mg`    | [CER-54](https://yt.bi.denbi.de/issue/CER-54)                                                     |
| 28.04.2021       | Audit zur Zertifizierung nach ISO 27001 (Stufe 1)                                                     | `hb`    | siehe Stufe 2                                                                                     |
| 20.05.2021       | Prüfung der Lücken aus dem Test-Assessment (Anhang A)                                                 | `dz`    | [CER-215](https://yt.bi.denbi.de/issue/CER-215), [Tickets](https://yt.bi.denbi.de)                |
| 30.05-02.06.2021 | Audit zur Zertifizierung nach ISO 27001 (Stufe 2)                                                     | `hb`    | [Bericht](anlagen/reports/2021/Auditbericht%20DQS%202021.pdf), [CER-241](https://yt.bi.denbi.de/issue/CER-241) [CER-250](https://yt.bi.denbi.de/issue/CER-250)   | 
| 5.05.2022        | ISO 27001 Managementprozesse: 4 - 10, Nebenabweichungen und Empfehlungen aus dem Zertifizierungsaudit | `ff`    | [Bericht](anlagen/reports/2022/Auditbericht%20FF%202022.pdf), [Tickets](https://yt.bi.denbi.de)   | 
| 01.06.2022       | 1. Überwachungsaudit nach ISO 27001                                                                   | `hb`    | [Bericht](anlagen/reports/2022/Auditbericht%20DQS%202022.pdf)                                        |
| März 2023        | ISO 27001 Managementprozesse, Risikomanagement, Abweichungen aus dem 1. Überwachungsaudit             | `ff`    | [CER-320](https://yt.bi.denbi.de/issue/CER-320)                                                   | 
| Juni 2023        | 2. Überwachungsaudit nach ISO 27001                                                                   | `hb`    | [Bericht](anlagen/reports/2023/Auditbericht%20DQS%202023.pdf)                                        
| 08.03.2024       | Changemanagement + Controls                                                                           | `dz`    | [Bericht](anlagen/reports/2024/Auditbericht%20Optiqum%202024.pdf) [Tickets](https://yt.bi.denbi.de/issues/CER?q=tag:%20%7BInt.%20Audit%202024%7D%20) |
| 1.3, 15.-16. März 2024| Audit zur Rezertifizierung nach ISO 27001:2022 (Stufe 2)                                         | `hb`    | [Bericht](anlagen/reports/2024/Auditbericht%20DQS%202024.pdf), [Tickets](https://yt.bi.denbi.de/issues/CER?q=tag:%20%7BAudit%20M%C3%A4rz%202024%7D%20%2)  |
| 25.-26.03.2025   | ISO 27001:2022 vollständiges internes Audit des ISMS                                                  | `dz`    | [Bericht](anlagen/reports/2025/Auditbericht%20Optiqum%202025.pdf), [Tickets](https://yt.bi.denbi.de/issues/CER?q=tag:%20%7BInt.%20Audit%202025%7D)  |
| 8.3, 14.-15.4.2025 | 1. Überwachungsaudit nach ISO 27001:2022                                                            | `hb`    | [Bericht](anlagen/reports/2025/Auditbericht%20DQS%202025.pdf)  |
| 11.-13.03.2026   | ISO 27001:2022 internes Audit des ISMS                                                                | `ff`, `nm` | [Bericht](./anlagen/reports/2026/Bericht_internes_Audit_Bielefeld2026.pdf) | 
| 30.06/01.07.2026 | 2. Überwachungsaudit nach ISO 27001:2022                                                              | `hb`    | [Bericht](./anlagen/reports/2026/31601202%20-%20de.NBI%20-%20Deutsches%20Netzwerk%20für%20Bioinformatik-Infrastruktur%20am%20Standort%20Bielefeld%20-%20REPORT%20-%202026-07-01%20-%20ISMS22.pdf) |

Für die inhaltliche Planung der internen Audits ist zudem die
[Themenmatrix](audits-intern-themenmatrix.md) maßgebend.

Personenkürzel:

- `dz`: David Zinzius, Optiqum Unternehmensberatung
- `mg`: Marcus Giese, TÜV Süd
- `hb`: Holger Burfeind, DQS
- `ff`: Frank Förster, de.NBI Cloud Gießen
- `nm`: Nils Mittler, de.NBI Cloud Gießen

