# Sensibilisierungsmaßnahmen

## Auslegen von präparierten USB-Sticks

| Durchgeführt am | Durchgeführt von | --- | Sicherheitsrelevante Ereignisse              | Anzahl dieser Ereignisse |
| --------------- | ---------------- | --- | -------------------------------------------- | ------------------------ |
|                 |                  |     | Zurückgegebene USB-Sticks / Kontaktaufnahmen |                          |

### Vorgehen

Es werden USB-Sticks formatiert und auf diese werden im folgenden eine HTML-Datei mit einem eingebauten Redirect
zur Informationsseite zu [Sicherheitsmaßnahmen](https://cloud.denbi.de/it-security)
sowie eine README-Datei aufgespielt.
In der README-Datei ist beschrieben, dass das Einstecken von unbekannten Datenträger in Laptops und/oder
Computer ein schwerwiegendes Sicherheitsproblem darstellt, und das der Verantwortliche,
welcher die Maßnahme durchführt unverzüglich zu kontaktieren ist.
Dieser führt Statistik darüber, wie viele Personen Ihn aufgrund dieses Fehlers kontaktiert haben.
Gefundene USB-Sticks oder Datenträger sind ansonsten an den ITB des IBG-5 zu übergeben.
Zur Ende der Maßnahme wird der ITB, abgefragt wie viele USB-Sticks dort abgegeben wurden.
Über dieses Vorgehen wurden die Mitarbeitenden im Zuge des Jour-Fixe des IBG-5 + CMG am 07.04.2025 informiert.
Im Zuge dessen wurde den Mitarbeitenden auch der zu diesem Zeitpunkt vorliegende 
Stand der Informationsseite zu Sicherheitsmaßnahmen präsentiert.

## Honeypot-Netzwerke

| Durchgeführt am | Durchgeführt von | --- | Sicherheitsrelevante Ereignisse  | Anzahl dieser Ereignisse |
| --------------- | ---------------- | --- | -------------------------------- | ------------------------ |
|                 |                  |     | Kontaktaufnahmen nach Verbindung |                          |

### Vorgehen

In Absprache mit dem BITS werden WLAN-Access Points in den Arbeitsbereichen der Mitarbeitenden zeitweise abgestellt.
Zeitgleich wird ein Honeypot-Netzwerk mit der SSID `eduroam` gestartet. Das Netzwerk ist ungesichert und
nach Verbindung mit dem Netzwerk wird eine HTML-Seite aufgerufen, welche dazu aufruft,
sich umgehend mit der für die Maßnahme verantwortlichen Person in Verbindung zu setzen.
Die Anzahl der Kontaktaufnahmen wird protokolliert.

Analog kann auch der Einfachheit wegen, ein dem `eduroam` nicht ähnliches Netz parallel zum Normalbetrieb gestartet werden.

#### Aufsetzen des Honeypots mithilfe eines Raspberry Pi

1. Installation des `hostapd`-Pakets auf Ihrem Raspberry Pi:

`sudo apt-get install hostapd`

2. Konfiguration der `/etc/hostapd/hostapd.conf` für Einrichtung eines WLAN-Zugangspunktes

```
interface=wlan0
driver=nl80211
ssid=eduroam
channel=1
wmm_enabled=0
```

3. Installation eines Web-Servers, beispielsweise `lighttpd`:

`sudo apt-get install lighttpd`

4. Konfiguration von `lighttpd`:

```
server.modules = (
    "mod_cgi",
)

server.document-root = "/var/www/html"
server.port = 80

$HTTP["url"] =~ "^/" {
    url.redirect-code = 302
    url.redirect = ("/index.html")
}
```

5. Anlegen des entsprechenden Document-Root-Ordners:

`sudo mkdir -p /var/www/html`

6. Anlegen einer `index.html` mit entsprechendem Inhalt, beispielsweise:

```
<!DOCTYPE html>
<html>
<head>
    <title>Sicherheitsvorfall</title>
</head>
<body>
    <h1>Sie benutzen eine nicht sichere WLAN-Verbindung!</h1>
    <p>Kontaktieren Sie bitte umgehend xy!</p>
</body>
</html>
```

7. Starten des Service

`sudo service hostapd start`
