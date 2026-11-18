# de.NBI Cloud Bielefeld Infrastruktur für externe Berater

*Dieses Dokument sollte einem externen Berater/Partner als ToDo-Liste vorgelegt werden.*

Die Cloud-Infrastruktur ist ausschließlich aus dem CeBiTec-Netz über einen
gesonderten Jumphost zu erreichen. In das CeBiTec-Netz kann man sich über
ein SSH-Portal oder via RDP einloggen. Dafür ist ein CeBiTec-Account
notwendig (-> Erstellung eines CeBiTec-Accounts).
Auf dem Jumphost können sich die dafür berechtigten Nutzer mittels
Zwei-Faktor-Authentisierung (SSH-Public-Key  + TOTP) einloggen (-> Cloud Jumphost)
und haben von diesem aus Zugriff auf alle Cloud Infrastruktur Hosts.

## Erstellung eines CeBiTec-Accounts

Zur Erstellung eines CeBiTec-Accounts sind folgende Schritte notwendig:

* [ ] Über das [Webformular](https://www.cebitec.uni-bielefeld.de/account)
    einen Account beantragen. Als Gruppe "opstconsult" (Openstack Consulting
    Partner) auswählen.
* [ ] Bestätigen der Identität (via Ausweis/Video-Meeting)

Sobald die Identität bestätigt und der Account aktiviert ist, kann man sich
via ssh oder RDP im CeBiTec einloggen:

* **SSH** -> `porta.cebitec.uni-bielefeld.de`
* **RDP** (via [Cendio ThinLinc Client](https://www.cebitec.uni-bielefeld.de/intranet/de/computer-systeme/unix/thinlinc-remote-desktop))->
    `thinlinc.cebitec.uni-bielefeld.de`

## Cloud Jumphost

Die de.NBI Cloud-Infrastruktur ist ausschließlich über einen Jumphost zu erreichen.
Der Zugang zu dem Jumphost (jopstcon) erfolgt mittels SSH-Public-Key-Verfahren in
Kombination mit einem TOTP-Token (zeitbasiertes Einmalpasswort) als zweiten Faktor.

* [ ] Hinterlegen eines öffentlichen SSH-Keys (`~/.ssh/authorized_keys`).
    *Der private Schlüssel muss nach den IT-Sicherheitsrichtlinien der Universität
    Bielefeld und dem der Cloud zugrunde liegenden ISMS erstellt
    und durch eine geeignete Passphrase (oder vergleichbare oder besserer Technik)
    geschützt sein.*
* [ ] Bereitstellen des öffentlichen SSH-Keys
    *Der öffentliche SSH Schlüssel wird auf den Cloud-Infrastruktur-Hosts mittels
    Ansible hinterlegt.*

### Aktivieren von 2FA

* [ ] Ausführen des Google Authenticator auf der Konsole
    (von `porta.cebitec.uni-bielefeld.de`):

```
$ google-authenticator
Do you want authentication tokens to be time-based (y/n)
```

Die Frage mit 'y' beantworten, es werden damit TOTP Tokens erstellt.
Es wird nun ein QR-Code auf der SSH-Konsole angezeigt.

* [ ] Scanne den Code mit einer kompatiblen App auf dem Smartphone.
* [ ] Kopiere und verwahre die unterhalb aufgelisteten Keys sicher. Mit diesen
    Keys kann ein Login ohne OTP durchgeführt werden.
* [ ] Die Datei `~/.google_authenticator` wird von der Applikation auf Wunsch angelegt (default) oder
    muss manuell mit diesen Informationen erzeugt werden.

Der Login auf dem Jumphost (jopstcon) sollte nun via SSH und 2FA funktionieren.

## Cloud-Infrastruktur-Hosts

Vom Jumphost aus kann man sich nun auf den Cloud-Infrastruktur-Hosts (Controller,
Hypervisor, Storage-Knoten, ...) einloggen. Der Zugang zur Entwicklungsumgebung
ist immer möglich, während der Zugang zur Produktionsumgebung bei Bedarf gezielt
für einzelne Hosts freigeschaltet wird.

## Zugang zu OpenStack bzw. OpenStack-Dev

Die Authentisierung erfolgt über Elixir AAI.

* [ ] [Registrieren](https://cloud.denbi.de/wiki/registration/) für einen
    Elixir-Account
* [ ] Login in das [de.NBI Cloud Portal](https://cloud.denbi.de/portal) sollte
    nun möglich sein
* [ ] Namen/Elixir ID bereitstellen

Sobald der Elixir-Account erstellt ist und dieser einem Projekt zugewiesen wird,
ist der Login via OpenStack Horizon möglich.

1. [openstack.cebitec.uni-bielefeld.de](https://openstack.cebitec.uni-bielefeld.de)
1. [openstack-dev.cebitec.uni-bielefeld.de](https://openstack-dev.cebitec.uni-bielefeld.de)

## Zugang zu den nicht öffentlichen de.NBI Cloud GitLab Repositories

* [ ] Name + Email-Adresse bereitstellen

Sobald der Account eingerichtet ist (GitLab ist ein Service der Universitätsbibliothek)
und dieser den entsprechenden de.NBI Cloud Projekten zugeordnet ist, ist der
[Login](https://gitlab.ub.uni-bielefeld.de/) dort möglich.
