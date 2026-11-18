# On-Boarding und Off-Boarding Prozesse für Mitarbeiter

## On-Boarding

Damit neue Mitarbeitende ihre Arbeit ordnungsgemäß ausführen können, 
müssen verschiedene Voraussetzungen hinsichtlich der Berechtigungen und (Nutzer-)Zugänge erfüllt sein.
Des Weiteren müssen neue Mitarbeitende über Zusammenhänge und Vorgehensweisen aufgeklärt werden.

### Zugänge

Folgende Zugänge und technische Einstellungen werden benötigt,
wobei Details abhängig von Art der Beschäftigung/Aufgaben sind:

- [ ] Universitäts-Account (mindestens Gast-Account über BRF)
  - [ ] Zugriff Element/Matrix-Chat sowie entsprechende Gruppen
  - [ ] Zugriff auf GitLab der Universität mit entsprechenden Repositories 
- [ ] CeBiTec Account
  - [ ] Einrichtung des Accounts
    - [ ] Zuweisung zu Gruppen (automatischer Zugriff zu Shared-Directories im Netzwerk des CeBiTec)
      - [ ] denbi
      - [ ] opstadm und opstconsult
  - [ ] Einrichtung einer Zwei-Faktor-Authentifizierung
  - [ ] Generieren von SSH-Keys für Zugriff auf gesicherte Maschinen
    - [ ] Zugriff auf CeBiTec-Account
    - [ ] Zugriff auf Cloud-Infrastruktur
      - [ ] Weiterreichen des Keys an Administrator (ADM oder BRF)
  - [ ] Einrichtung [VPN-Tunnel](https://github.com/sshuttle/sshuttle)
       in gesichertes Netzwerk (unter Zuhilfenahme des Keys für CeBiTec)
  - [ ] Zugang zu Mailing-Listen (über BRF)
  - [ ] Request-Tracker (über Sebastian Jünemann, IBG-5)
- [ ] OpenStack
  - [ ] Produktionsumgebungen
  - [ ] Testumgebungen
- [ ] Weitere Accounts
  - [ ] YouTrack
  - [ ] Eramba
  - [ ] Zabbix
  - [ ] OpenVas
  - [ ] Ceph-Dashboard
  - [ ] Ara
  - [ ] Gitea
- [ ] Account für LifeScience-AAI
  - [ ] Berechtigungen für Perun.AAI
- [ ] GitHub Account für separate Repositories

### Weitere Vorgänge

- [ ] Ausstellung Token für Zugang in Büro-Räumlichkeiten
- [ ] Zurverfügungstellung von IT-Geräten
- [ ] Sicherheitseinweisung
- [ ] Sichtung ISMS
  - [ ] [Informationssicherheitsleitlinie](../informationssicherheitsleitlinie.md)
  - [ ] [Guidelines](../guidelines.md)
  - [ ] [Regelungen zur Dokumentation](../regelungen-zur-dokumentation.md)
  - [ ] [Richtlinien](../dokumente.md)

> ![](../assets/c.png) `vr` Das Guideline-Dokument muss noch mit entsprechenden Informationen gefüllt werden

## Offboarding

Bei Ausscheiden von Mitarbeitenden aus dem Dienst müssen die Zugänge
zu den entsprechenden Accounts wieder entfernt werden, sowie die Token
für den Zugang zu Räumlichkeiten und die ausgegebenen IT-Geräte eingezogen werden.
Wenn nachvollziehbar bleiben muss, welche Personen welche Schritte vollzogen haben,
beispielsweise durch Logs in Systemen, in denen anhand der Accounts die 
Verantwortlichkeiten einsehbar sind, so ist eine Deaktivierung des Accounts/Zugriffs
einer vollständigen Löschung vorzuziehen.
Werden bestimmte Accounts/Zugriffe (beispielsweise CeBiTec oder OpenStack) für
andere Zwecke als die der Anstellung genutzt, ist eine Anpassung der Rechte notwendig,
statt die Zugriffe komplett zu deaktivieren

### Zugänge

- [ ] Entfernen/Deaktivieren von Accounts und Zugriffen
  - [ ] YouTrack
  - [ ] Eramba
  - [ ] Zabbix
  - [ ] OpenVas
  - [ ] Ceph-Dashboard
  - [ ] Ara
  - [ ] OpenStack
    - [ ] Produktionsumgebungen
    - [ ] Testumgebungen
  - [ ] Zugriff auf GitHub-Repositories
  - [ ] Zugriff auf GitLab-Repositories
  - [ ] Zugriff auf Gitea-Repositories
  - [ ] Berechtigungen in Perun
  - [ ] CeBiTec
    - [ ] Entfernen aus Gruppen
    - [ ] Entfernen aus Request-Tracker
    - [ ] Entfernen des Schlüssels für Zugriff
      - [ ] Auf Cloud-Infrastruktur
      - [ ] Auf CeBiTec-Infrastruktur
    - [ ] Entfernen aus Mailing-Listen
  - [ ] Anpassung der Rechte für Universitäts-Account
  - [ ] Entfernen aus Chat-Gruppen

### Weitere Vorgänge

- [ ] Deaktivierung der Rechte des Schließtokens für Räumlichkeiten
  bzw. Rückgabe des Tokens
- [ ] Rückgabe der dienstlichen IT-Geräte

