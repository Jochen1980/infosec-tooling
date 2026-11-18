# Prozesse

[[_TOC_]]

## Governance und Compliance-Management

```mermaid
flowchart TB

    Leit[Leitung] -->|delegiert an| Pers[Personal]
    Leit --> |gibt Richtung vor,\ngenehmigt Änderungen,\nprüft Einhaltung| ISMS
    Pers -->|pflegt| ISMS
    subgraph ISMS
        Proz[Prozesse]
        Richtl[Richtlinien]
    end
    ArbAb{Arbeitsabläufe}
    Pers -->|erstattet Bericht| Leit
    Pers -->|führt aus| ArbAb
    ISMS -.-> |steuert| ArbAb
    ISMS -.-> |stützt| Einhaltung
    subgraph Einhaltung
        GeltRe([Geltendes Recht])
        BestUNI([Bestimmungen Uni Bielefeld])
        BestFZJ([Bestimmungen FZ Jülich])
    end
```

## Risikomanagement

```mermaid
flowchart TB
    classDef gelb fill:#E9C73F
    A[Assets] --> B[Risikoidentifikation]
    B -->|Assets sind\nrisikobehaftet| A
    B -->|jährliches Brainstorming| B
    B --> C[Risikoanalyse / Bewertung]
    C --> D[Kommunikation mit \nManagement / Verantwortlichen]
    D --> C
    D -->|Aufnahme ins Eramba| E[Risikokatalog]
    E -->|jährliche Reviews| E
    E --> F[Risikobehandlung]
    F --> G([Mitigate]):::gelb
    F --> H([Accept]):::gelb
    F --> J([Avoid]):::gelb
    F --> K([Transfer]):::gelb
    L[IT-Verfahren] --> G
    L -->|jährliche \nReviews| L
    M[Policies] --> G
    M -->|jährliche \nReviews| M
```

## Schwachstellenmanagement

```mermaid
flowchart TB
    CVE[CVE-Scan] -->|meldet| SysVul
    Vuln["Vulnerability-Scanner (GVM)"] -->|meldet| VMVul
    VirS[Virenscanner]
    VMVul([VM-Schwachstellen])
    SysVul([System-Schwachstellen])
    VMVul -.-> Mail
    SysVul -.-> YouTrack
    VirS -->|meldet| Inf([Infektionen])
    Inf -.-> Zabbix

    subgraph Alerting-Systeme
        Mail[Mails]
        YouTrack[YouTrack]
        Zabbix[Zabbix]
    end

    Pers[Personal] -.-> |sichtet regelmäßig| Alerting-Systeme
    Alerting-Systeme --> |benachrichtigt| Pers
    Pers -->|benachrichtigt| Nutz[Nutzer]
    Pers --> Inc[Incident-Management]
    Pers <--> |Kompetenzen| ThrInt([Threat Intelligence])
```

## Sensibilisierung und Kompetenzaufbau

```mermaid
flowchart TB
    classDef gelb fill:#E9C73F
    classDef pink fill:#DF81B4
    classDef zentral stroke-width:5px
    A[Kompetenzen]:::zentral --> B[Weitergabe an \nInteressierte]
    A --> C[Verbesserung der \nInformationssicherheit]
    D[Teilnahme an Schulungen \nund Fortbildungen] --> A
    A -->|Kompetenz \nnotwendig| E[Analyse /\n Protokollierung /\n Bearbeitung] -->|fördert \nKompetenz| A
    F[Datenbeschaffung] --> E
    G[Externe Quellen] --> F
    H[Interne Quellen] --> F
    J([BSI-Reports]):::pink --> G
    K([Heise-Security]):::pink --> G
    L([DFN-Cert]):::pink --> G
    R([OWASP]):::pink --> G
    M(["Vulnerability-Scanner (GVM)"]):::gelb --> H
    N([ClamAV]):::gelb --> H
    O([Zabbix]):::gelb --> H
    P([CVE-Scan]):::gelb --> H
    T([Kolla-Logs]):::gelb --> H
```

## Incident-Management

```mermaid
flowchart TB
    A["Vulnerability-Scanner (GVM)"] --> B[Meldung einer Schwachstelle]
    C[Kunde] --> B
    D[DFN] --> B
    B --> E[Eintragung ins Ticketsystem]
    E --> F[Risikoprüfung und Evaluation]
    F --> G[Fortführung der Meldekette]
    F --> H[Sofortmaßnahmen zur \nGefahrenabwehr]
    E -->|Kontinuierliche\nPflege| E
    H --> I[Ableitung von Verbesserungspotenzialen]
```

## Business-Continuity-Management

```mermaid
flowchart TB
    classDef alrm stroke-width:5px, fill:#DF9581;
    classDef gelb fill:#E9C73F
    SIT[Situationsabfrage]
    NORMB[Normalbetrieb]
    CHANGEMBT[Change-Management]
    SIT -->|Monitoring sauber| NORMB
    SIT -->|Störung| CHANGEMBT
    SIT -->|Notfall / Krise| BCM
    BCM:::alrm
    BCMUBI[BCM Uni Bielfeld] -.-> |beeinflusst| BCM
    BCM --> |umfasst| KK[Kriesenkommunikation]
    BCM --> AKT{Aktionen}
    BCM --> |Recovery| WAP[Wiederanlaufplan]
    BACK[Backups]:::gelb -.->|sind Teil von|WAP
    BESCH[Beschaffung]:::gelb -.->|ist Teil von|WAP
    UEBDR[Übung Desaster Recovery] -->|jährliche Ausführung| WAP
    AKT-->|wenn notwendig| NOTAS
    AKT -->|wenn notwendig| NOTAEND[Notfall-Änderung]
    UEBNA[Übung Notfall-Abschaltung] -->|jährliche Ausführung| NOTAS[Notfall-Abschaltung]
```

## Change-Management

```mermaid
flowchart TB
    A[Änderungsbedarf] --> C[Dokumentation als Ticket]
    B[Projekt] --> C
    C -->|4-Augen-Prinzip| D[Änderungen im Playbook]
    D --> E[Test auf Entwicklungssystemen]
    E -->|4-Augen-Prinzip| F[Veränderung der Produktionssysteme]
    G[Regelmäßige Playbook-Runs] -.-> E
    G -.-> F
    E -->|bei Bedarf| D
```

## Projekt-Management

```mermaid
flowchart TB
  A[Idee] -->  |Diskussion | Z[Brainstorming]
  Z --> | Anpassung| A
  A --> B[Ticket]
  A --> C[BA/MA<br>Studentenprojekt]
  C --> B
  B --> | Lastenheft<br>Festlegen der Verantwortlichkeiten<br>ggf. Informieren der Leitung | D[Projekt]
  D <-.-> X[SubTickets]
  D <--> | regelmässig| E((Meeting))
  D <--> |4-Augen Prinzip|F[Abnahme]
  D <--> |Informationssicherheit|F
  F -->|ChangeManagement| G[ Produktion]
```

## Nutzerinteraktion

```mermaid
flowchart TB
    A[Nutzer] -->|stellen Anfragen| P
    P[Personal] -->|betreut| A
    P -.->|bei Änderungsbedarf| E[Eintrag im Ticketsystem]
    P -->|veranstaltet| F[Schulungen]
    A -->|nehmen teil an| F
    P -->|kündigt an| G[Veränderungen]
    G -.->|haben Auswirkungen auf| A
    P -->|dokumentiert im| W[Wiki]
    W -->|instruiert| A
```

## Technischer Betrieb

```mermaid
flowchart TB
    A -->|bei Bedarf| B[Beschaffung]
    A -->|bei Defekt| C[Austausch]
    subgraph Produktivsystem
        A[Hardware]
        D[Software]
    end
    E[Nutzer] -->|nutzen| Produktivsystem
    F[Dokumentation]
    B --> F
    C --> F
    G[Änderungen]-->|unter Berücksichtigung\nChange-Management| D
    G --> F
```

## Wiederkehrende Aufgaben

```mermaid
graph LR;
    Approaching_due_date[Approaching due date]
    Scheduled
    Closed
    
    Scheduled --> Approaching_due_date
    Scheduled --> Due
    Scheduled --> Closed
    Approaching_due_date --> Due
    Due --> Overdue
    Due --> In_progress[In progress]
    Overdue --> In_progress
    Due --> Skipped
    Overdue --> Skipped
    In_progress --> Skipped
    In_progress --> To_be_reviewed[To be reviewed]
    To_be_reviewed --> Reviewed
    Reviewed --> Scheduled
    Reviewed --> Closed
    Skipped --> Reviewed
    Skipped --> Closed
    Closed --> Scheduled
```
