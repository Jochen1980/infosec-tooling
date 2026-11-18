# Richtlinie zum Gebrauch von kryptographischen Maßnahmen in der de.NBI Cloud Bielefeld

|                 |                                             |
|-----------------|---------------------------------------------|
| Version:        | 1.1                                         |
| Version vom:    | 30.01.2024                                  |
| Erstellt durch: | Jan Krüger, Christian Henke, Alex Walender  |
| Genehmigt am:   | 06.03.2024 (alu), 12.03.2024 (as)           |
| durch:          | Alexander Sczyrba (as), Stefan Albaum (alu) |

# ChangeLog

- Version 1.1 vom 30.01.2024
- Version 1.0 vom 14.11.2023
- Version 0.2 vom 20.05.2022
- Version 0.1 vom 09.12.2020
- Version 0.0.1-WIP vom 08.12.2020: Work in Progress

# Zweck, Geltungsbereich und Anwender

## Zweck

Die de.NBI Cloud Bielefeld ist in hohem Maße auf den angemessenen und wirksamen
Gebrauch von Kryptographie zum Schutz der Vertraulichkeit, Authentizität und
Integrität von Informationen angewiesen.
Die Richtlinie beschreibt den Gebrauch von kryptographischen Maßnahmen und gilt für
den kompletten Anwendungsbereich des Informationssicherheits-Management-Systems (ISMS)
der de.NBI Cloud Bielefeld.

## Anwender

Die Mitarbeiter von ADM und BRF sowie die Cloud-Nutzer (sofern betroffen)
stimmen den Regelungen der Richtlinie zum Gebrauch von kryptographischen
Maßnahmen zu und beachten diese beim Umgang mit der Cloud.

## Geltungsbereich

Diese Richtlinie gilt verbindlich für alle Mitarbeiter von ADM und BRF im Rahmen
ihrer dienstlichen Tätigkeiten.

# Verschlüsselungsverfahren

Je nach Anwendungsszenario kommen sowohl symmetrische als auch asymmetrische
Verschlüsselungsverfahren zum Einsatz.

Als Referenz für die in diesem Dokument
benannten Verschlüsselungsverfahren wird die technische Richtlinie
[Kryptographische Verfahren: Empfehlungen und Schlüssellängen](richtlinien/BSI/BSI-TR-02102.pdf)
des BSI herangezogen.

## Symmetrische Verschlüsselungsverfahren

Symmetrische Verschlüsselungsverfahren dienen der Gewährleistung der Vertraulichkeit
von Daten, die zum Beispiel über ein öffentliches Netz ausgetauscht werden oder zur
Verschlüsselung von lokalen Festplatten. Der aktuelle Standard für ein symmetrisches
Verschlüsselungsverfahren ist der _Advanced Encryption Standard (AES)_.
Die de.NBI Cloud Bielefeld folgt den vom BSI empfohlenen Schlüssellängen zur Verwendung
in neuen kryptographischen Systemen.

| Verfahren | Schlüssellänge (Bit) |
|-----------|----------------------|
| AES-128   | 128                  |
| AES-192   | 192                  |
| AES-256   | 256                  |

## Asymmetrische Verschlüsselungsverfahren

Asymmetrische Verschlüsselungsverfahren werden u. a. aufgrund des höheren Rechenaufwands im
Vergleich zu symmetrischen Standardverfahren in der Praxis meist lediglich zur
Übertragung symmetrischer Schlüssel eingesetzt.

| Verfahren | Schlüssellänge (Bit) |
|-----------|----------------------|
| RSA       | 3072                 |
| ECIES     | 256                  |

Die angegebenen Schlüssellängen für RSA und ECIES gelten für den Einsatz bis
Ende des Jahres 2022. RSA Schlüssel, die über das Jahr 2022 hinaus eingesetzt werden,
müssen eine Mindestlänge von 3072 Bit haben. ECIES steht stellvertretend für
vergleichbare kryptographische Verfahren auf der Basis von elliptischen Kurven
(ECDH, ECDSA und ED25519).

# Schlüsselgenerierung und -verwaltung

1. Der Schlüssel wird ausschließlich vom Nutzer selbst erstellt (z.B. per `ssh-keygen`).

2. Es muss ein als sicher geltendes Verfahren bei der Erzeugung ausgewählt werden. Als sicher geltende
   Verfahren sind RSA (mindestens 2048 Bit noch bis Ende 2023, mindestens 3072 Bit ab Januar 2024),
   ECDSA und ED25519 (Stand Nov 2023). Die als sicher geltenden Verfahren sind dem aktuellen
   Stand der Technik anzupassen.

3. Der Schlüssel sollte mit einer als sicher geltenden Passphrase (min. 10 Zeichen bestehend
   aus Klein-/Großbuchstaben, Zahlen sowie Sonderzeichen) gesichert sein.

4. Der private Schlüssel muss sicher aufbewahrt werden, z.B. auf einem verschlüsselten
   Speichermedium und darf keinem Dritten zugänglich gemacht werden.

5. Sobald das zur Erzeugung eines Schlüssels verwendete Verfahren als unsicher gilt, muss dieser
   ausgetauscht werden.

6. Neue PGP-Schlüssel sind am Tag der Erzeugung in der
   [Aufstellung der Kryptografischen Schlüssel](../aufstellungen/schluessel.md)
   zu registrieren. Diese Einträge sind nach Möglichkeit mit einem signierten Commit
   mittels eines vorangegangenen Schlüssels zu protokollieren und somit prüfbar zu machen.

# Widerrufen von Schlüsseln / Meldeweg

Muss ein Schlüssel widerrufen werden, z.B. weil der private Schlüssel kompromittiert ist, so ist
folgender Prozess einzuhalten.

1. Die folgenden Personen davon in Kenntnis setzen
    1. Mitarbeiter und Gruppenleiter von ADM
    1. Mitarbeiter und Gruppenleiter von BRF
    1. ggf. IT-Sicherheitsbeauftragter/Datenschutzbeauftragte

1. Feststellen, ob ein Schaden entstanden ist und ob ggf. ein IT-Sicherheitsvorfall in Folge
   des kompromittierten Schlüssels vorliegt. Ist ein IT-Sicherheitsvorfall entstanden, ist
   der IT-Sicherheitsbeauftragte zu informieren.
   → [IT-Sicherheitsrichtlinie zur Handhabung von IT-Sicherheitsvorfällen
   ](richtlinien/UniBi/IT-Sicherheitsrichtlinie_Handhabung_IT-Sicherheitsvorfaelle_final.pdf )

1. Widerruf des Schlüssels

_Hinweis: Das Widerrufen von Schlüsseln ist in eigenen IT-Verfahren
([IT-11.1](../it-verfahren.md#it-111-administrative-accounts-der-denbi-cloud), [IT-11.3](../it-verfahren.md#it-113-cebitec-accounts))
für den jeweiligen Anwendungszweck beschrieben._

# Verantwortlichkeiten

Die Leiter von ADM und BRF sind verantwortlich dafür, dass die Richtlinie zum Gebrauch
von kryptographischen Maßnahmen Anwendung findet.
