# Richtlinie zur Authentifizierung

|                   |                                             |
|-------------------|---------------------------------------------|
| Version:          | 0.1                                         |
| Version vom:      | 12.01.2024                                  |
| Erstellt durch:   | Jan Krüger                                  |
| Genehmigt am:     | 06.03.2024 (alu), 12.03.2024 (as)           |
| durch:            | Alexander Sczyrba (as), Stefan Albaum (alu) |

# ChangeLog

- Version 0.1 vom 12.01.2024: initialer Entwurf

# Zweck, Anwendungsbereich und Anwender

Die vorliegende Richtlinie gilt für alle Informationssysteme, Anwendungen,
Netzwerke und Ressourcen, die von unserer Organisation betrieben, unterstützt
oder genutzt werden und wurde entwickelt, 
um die Sicherheit unserer Informationssysteme zu stärken, indem 
klare und effektive Standards für die Verwaltung und Nutzung von 
Authentifizierungsmethoden festgelegt werden. Das Hauptziel besteht darin, 
sicherzustellen, dass nur autorisierte Benutzer auf unsere Systeme, 
Anwendungen und Ressourcen zugreifen können 

Diese Richtlinie dient als Leitfaden für alle Mitarbeiter, Auftragnehmer, 
und Dritte, die auf unsere Informationstechnologie-Ressourcen zugreifen 
oder diese nutzen.

# Referenzen

- ISO 27001/27002 A5.17
- [Richtlinie für das Identitätsmanagement](Richtlinie_Identitaetsmanagement.md)
- [Richtlinie zur Erteilung von Zugangsrechten](Richtlinie_Zugangsrechte.md)
- [Gebrauch von kryptographischen Maßnahmen](Gebrauch_von_kryptographischen_Maßnahmen.md)

# Authentifizierung

Neben einem sicheren Passwort (siehe Gebrauch von Passwörtern) können alternativ
oder auch zusätzlich die folgenden Verfahren zur Authentifikation verwendet werden.

- **Single Sign On** (SSO)
- **Public Key Infrastructure** (PKI)
- **Time-based One-Time Password** (TOTP) 
- Fast Identity Online (FIDO)
- Smartcards und Token
- Biometrische Authentifizierung

Die hervorgehobenen Verfahren werden aktiv genutzt und werden im folgenden
detaillierter erläutert.

Besonders schützenwerte Bereiche sollten durch eine mehrstufige Authentifizierung,
die Kombination von zwei oder mehreren Authentifizierungsmethoden, abgesichert 
werden.

## Gebrauch von Passwörtern

Werden in einem IT-System Passwörter zur Authentisierung gebraucht, so ist die
Sicherheit der Zugangs- und Zugriffsrechteverwaltung des Systems entscheidend
davon abhängig, dass das Passwort richtig benutzt wird. Sofern technisch möglich
sollten durch die IT folgende Randbedingungen eingehalten werden:

- Die Wahl von Trivialpasswörtern ("QWERTZAS", "123456") oder Passwörtern mit
  weniger als 10 Zeichen ist nicht zulässig.
- Benutzer sollten für unterschiedliche Services auch stets
  verschiedene Passwörter verwenden und dürfen diese nicht weitergeben.
- Benutzer müssen ihr eigenes Passwort jederzeit ändern können.
- Bei der Authentisierung in vernetzten Systemen dürfen Passwörter nicht
  unverschlüsselt übertragen werden.
- Bei der Eingabe sollte das Passwort nicht im Klartext auf dem Bildschirm
  einsehbar sein.
- Die Passwörter sollten im System zugriffssicher gespeichert werden,
  beispielsweise durch den Einsatz einer Einwegverschlüsselung.
- Eine Zurücksetzung des Passwortes durch die Administration sollte ausschließlich
  mit einem Initialkennwort erfolgen, das die empfangende Person bei der ersten
  Anmeldung zwingend ändern muss.
- Bei der Zurücksetzung eines Passwortes ist ein ausreichend sicheres Verfahren
  zur Verifikation der Identität der Benutzerinnen und Benutzer und zur Übermittlung
  des neuen initialen Kennwortes zu verwenden.
- Ein Passwort wird geändert, sobald es kompromitiert sind oder ein Hinweis darauf 
  vorliegt.

Auf die Einhaltung der Regeln ist insbesondere zu achten, wenn das System diese
nicht erzwingt.

## Gebrauch von alternativen Authentifizierungsmethoden

### Single Sign On (SSO)

SSO kann als eine Methode für die Authentifizierung von Benutzern verwendet werden. 
Der Benutzer authentifiziert sich einmalig gegenüber einem vertrauenswürdigen
Identitätsprovider und erhält so Zugriff auf das System. Der Identitätsprovider sollte
eine vergleichbare Richtlinie zur Authentifizierung nutzen.
SSO kann mit mehrstufiger Authentifizierung kombiniert werden, um zusätzliche 
Sicherheitsebenen bereitzustellen. Benutzer können neben dem SSO-Passwort
eine zusätzliche Authentifizierungsmethode verwenden, wie zum Beispiel TOTP, SMS-Codes,
biometrische Daten oder Token.

### Public Key Infrastructure (PKI)

SSH-Public-Key-Verfahren für den Zugriff auf Systeme über SSH (Secure Shell) kann als eine 
Form von Public Key Infrastructure (PKI) betrachtet werden. Das Verfahren verwendet 
asymmetrische Kryptografie, bei der der öffentliche Schlüssel auf dem Server verfügbar ist, 
während der private Schlüssel nur beim Benutzer verbleibt. Dies ermöglicht eine sichere 
Authentifizierung, ohne dass Passwörter über das Netzwerk übertragen werden müssen.

Der Umgang mit kryptographischen Schlüsseln ist in der Richtlinie zum 
[Gebrauch von kryptographischen Maßnahmen](Gebrauch_von_kryptographischen_Maßnahmen.md)
definiert.

### Gebrauch von TOTP (Time-based One-Time Passwords)

TOTP (Time-based One-Time Password) ist ein Algorithmus für die Erzeugung von 
Einmalpasswörtern (OTP), der in der Zwei-Faktor-Authentifizierung (2FA) verwendet wird.

TOTP wird oft in Kombination mit einer speziellen Authentifizierungs-App auf einem 
mobilen Gerät verwendet. Diese Apps, wie zum Beispiel Google Authenticator oder 
Authy, implementieren den TOTP-Algorithmus und generieren die Einmalpasswörter für
die Verwendung bei der Anmeldung.

Die Verwendung von TOTP in der Zwei-Faktor-Authentifizierung erhöht die Sicherheit, 
da ein Angreifer beispielsweise nicht nur das Passwort kennen müsste (1. Faktor), 
sondern auch im Besitz des physischen Geräts (z. B. des Smartphones mit der 
Authentifizierungs-App) sein müsste, um sich erfolgreich zu authentifizieren.

## Nutzerverantwortung

Die Nutzer eines Authentifizierungsystem müssen über den korrekten Umgang mit den
zur Anwendung kommenden Methoden informiert werden.

**Die Vorgesetzten haben die Einhaltung der Richtlinie sicherzustellen
und weisen die Mitarbeiter ggf. auf Defizite hin.**
