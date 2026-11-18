# Richtlinie für mobile Geräte

| |                                               |
|-----|-----------------------------------------------|
| Version: | 2.1                                           |
| Version vom: | 20.02.2024                                    |
| Erstellt durch: | Alex Walender, Viktor Rudko, Jan Krüger       |
| Genehmigt am: | 06.03.2024 (alu), 12.03.2024 (as)             |
| durch: | Alexander Sczyrba (as), Stefan Albaum (alu)   |

# ChangeLog

- 2.1 vom 20.02.2024 : Anweisung zur Webfilterung
- 2.0 vom 07.02.2024 : Anpassung an die neue Norm
- 1.1 vom 26.04.2021 : Links in Referenzen korrigiert
- 1.0 vom 12.04.2021 : Text aus dem ITBS M 2.31 in eine Richtlinie überführt und etwas erweitert.

# Zweck, Anwendungsbereich und Anwender

Die Nutzung von mobilen IT-Geräten stellt ein nicht unerhebliches Risiko für die Daten und
die IT-Infrastruktur dar.

**Der Zugriff auf die Cloud-Infrastruktur ist aus diesem Grund ausschließlich über Dienstgeräte
(Notebooks, ThinClients) gestattet.**

Der Zugang zur Cloud über einen Jump Host ist durch eine zeitbasierte Zwei-Faktor-Authentisierung
(TOTP) abgesichert. Dieses Verfahren setzt den Einsatz von Hardware Tokens (wird gestellt) oder dem
Google Authenticator bzw. einer vergleichbaren Anwendung (auf dem privaten Smartphone des Mitarbeiters)
voraus. (Bei Verwendung eines privaten Smartphones empfiehlt sich die Einrichtung eines separaten
Nutzerprofils für den Einsatz geschäftlicher Anwendungen.)

Der Anwendungsbereich dieser Richtlinie umfasst die de.NBI Cloud Bielefeld. Die Anwender sind alle
Mitarbeiter von ADM und BRF die ein mobiles Endgerät zur Verfügung gestellt bekommen.

# Referenzen

- [Richtlinie für Arbeitsumgebung und Bildschirmsperren](Arbeitsumgebung_und_Bildschirmsperren.md)
- IT-Sicherheitsrichtlinie zur Handhabung von IT-Sicherheitsvorfällen
  ([PDF](UniBi/IT-Sicherheitsrichtlinie_Handhabung_IT-Sicherheitsvorfaelle_final.pdf))

# Anforderungen

1. Alle mobilen Dienstgeräte sind inventarisiert und einem Mitarbeiter zuordenbar.
1. Die Nutzung der Dienstgeräte ist nur den jeweils zugeordneten Mitarbeitern gestattet
1. Die Verwaltung und Wartung liegt in der Hand des Nutzers. Es gibt keine Vorgaben
   bezüglich des zu verwendenden Betriebssystems (Linux, OSX oder Windows) oder der
   installierten Software. Die Mitarbeiter sind nach ITBS angehalten, dass ein aktuelles
   und vom Hersteller mit Sicherheitsupdates versorgtes Betriebssystem eingesetzt wird.
1. Der Festspeicher sowie etwaige Backup-Medien sind durch ein sicheres Passwort
   zu verschlüsseln.
1. Backups der mobilen Dienstgeräte sind regelmäßig durchzuführen. 
   Dabei sind die Backups in sicheren Umgebungen, wie etwa auf verschlüsselten Wechseldatenträgern zu speichern.  
1. Es ist ein Auto-Logout bzw. eine Bildschirmsperre bei Inaktivität einzurichten.
1. Notebooks dürfen nur während des Arbeitstages in den Standby-Modus bzw. in den Ruhezustand versetzt
   werden. Spätestens bei Arbeitsende ist das Gerät vollständig auszuschalten, um die
   Wirksamkeit der Festplattenverschlüsselung sicherzustellen. Ausnahme: Speicherung
   des Ruhezustandabbilds auf einer verschlüsselten Partition.
1. Alle privaten Schlüssel, welche die Cloud betreffen und die auf dem mobilen
   Gerät gespeichert sind, sind mit einem Passwortschutz zu versehen.
1. Unabhängig vom Betriebssystem muss regelmäßig ein Virenscanner eingesetzt werden.
1. Die Geräte sind stets sicher aufzubewahren und niemals unbeaufsichtigt Dritten zugänglich
   zu machen. Auf Dienstreisen sind die Geräte nach Möglichkeit im Hotelsafe wegzuschließen.
1. Die Geräte müssen in Übereinstimmung mit den Sicherheits- und Schutzvorschriften des
   Herstellers verwendet werden.
1. Im öffentlichen Raum ist die Nutzung von Blickschutzfiltern erforderlich.
1. Der Nutzer ist für die Sicherung der auf dem Gerät befindlichen (persönlichen) Daten selbst
   verantwortlich.
1. Der Nutzer darf keine Raubkopien oder illegale Inhalte auf dem mobilen Gerät speichern.
1. Der Nutzer darf nur diejenigen Unternehmensdaten auf das mobile Gerät laden,
   welche für seine Rolle in der de.NBI Cloud Bielefeld relevant sind.
1. Abhanden gekommene oder gestohlene Geräte müssen umgehend gemeldet werden.
1. Vermutet ein Nutzer, dass über ein mobiles Gerät ein unbefugter Zugriff auf Daten der de.NBI Cloud
   Bielefeld erfolgt ist, ist dieses als IT-Sicherheitsvorfall zu werten und entsprechend zu behandeln.
1. Die oben genannten Anforderungen müssen regelmäßig überprüft werden.

## Webfilterung

Um den Zugriff auf potentiell böswillige Webseiten zu verhindern sind alle Mitarbeiter dazu
aufgefordert einen Webbrowser mit entsprechender Filterfunktionalität auszuwählen.
Moderne Browser greifen auf die Arbeit der [Anti-Phishing Working Group](apwg.org) zu
und beziehen dadurch aktuelle Listen zu bösartigen IP-Adressen.

Folgende Browser mitsamt Konfigurationsvorgaben sind hierfür geeignet:

- Mozilla Firefox
  - Inkludiert in der Standardkonfiguration
  - [Informationen zur Webfilterung](https://support.mozilla.org/en-US/kb/how-does-phishing-and-malware-protection-work)
- Chromium Engine (Google Chrome, Vivaldi, Brave, Edge usw.)
  - Inkludiert in der Standardkonfiguration
  - [Informationen zu Webfilterung](https://support.google.com/chrome/answer/99020?hl=de&co=GENIE.Platform%3DDesktop)
- Apple Safari
  - Muss explizit konfiguriert werden!
  - [Siehe Anleitung](https://www.apple.com/de/legal/privacy/data/de/safari/)

Die Nutzung von Browser ohne integrierte Filterfunktion sind untersagt.

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen und weisen die Mitarbeiter
gegebenenfalls auf Defizite hin.**
