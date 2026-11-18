# Zugänge zu den manuell gepflegten OpenStack Domänen

Neben der de.NBI Domäne existieren drei weitere Domäne (DSI, CeBiTec, Default). Das Identitätsmanagement
für diese Domänen erfolgt manuell über die entsprechende OpenStack Komponente. Die Liste der Zugänge wird
in regelmässigen Abständen (monatlich) durch [REDO-12](https://yt.bi.denbi.de/issue/REDO-12/Prufung-der-Zugangsberechtigungen)
überprüft.

Die Projekte der einzelnen Domänen lassen sich mit Hilfe der OpenStack API/CLI listen:

```Shell
\$ openstack project list --domain (default|cebitec|dsi)
```

Die Mitglieder lassen sich ebenfalls über die API oder einfacher über das Skript `list_project_membership.py` ermitteln:

```Shell
\$ python list_project_membership.py  --project  SparkHit
+----------------------------------+----------------------------------+-----------+
|                id                |               name               |           |
| 7f317ceb66e34a8e9abff3bdeebea22f | huanglr                          | sparkhit  |
+----------------------------------+----------------------------------+-----------+
```

## DSI Domäne

DSI (Data Science Infrastructure) ist ein Kooperationsprojekt um zukünftig zumindestens die
Entwicklung einer Cloud Infrastruktur gemeinsam mit der Universität Bielefeld voran zu treiben.
Der Prototyp wird vom ADM betrieben, die Nutzer kommen aus dem Umfeld der Universität Bielefeld.

| Projekt | Beschreibung | Datum |  Laufzeit | Nutzer | Verantwortlicher |
| --- | --- | --- | --- | --- | --- |
| dsi-simple-vm | Simple VM Projekt für DSI Prototypen| 09.2023 | 12.2025 | David Weinholz, Viktor Rudko, Peter  Belmann, Alex Walender, Jan Krüger, Christian Henke, Oliver Francke(BITS) | Jan Krüger |
| dsi-simple-vm-stagging | Simple VM Staging Projekt für DSI Prototypen| 09.2023 | 12.2025 | David Weinholz, Viktor Rudko, Peter  Belmann,  Christian Henke, Oliver Francke(BITS) | Jan Krüger |
| dsi-test | Projekt zum Testen der Domänen Funktionalität | 07.2023 | 12.2025 |  Jan Krüger, Alex Walender, Christian Henke, Oliver Francke(BITS), Stefan Albaum (CeBiTec), Martin Flasskamp, Michael Thies, Florian Porrmann (alle TechFak)  |  Jan Krüger |
| LibTec | Testprojekt für LibTec Team der Bibliothek | 02.2024 | 12.2025 | Artur Nold, Vitali Peil, Andreas Graupp| Jan Krüger |
| Techfak-RGB | Testprojekt für die RBG der technischen Fakultät | 01.2025 | 12.2025 | Michael Götting, Christian Hilker |  Jan Krüger |

## CeBiTec Domäne

Vor allem für längerfristig laufende Projekte im CeBiTec betreibt die BRF eine von de.NBI
abgekoppelte Domäne auf derselben Cloud-Infrastruktur. Die Nutzer kommen vornehmlich aus
der BRF, die Forschenden aus dem CeBiTec einzelne vorkonfigurierte Instanzen zur Verfügung
stellen.

| Projekt | Beschreibung | Datum |  Laufzeit | Nutzer | Verantwortlicher |
| --- | --- | --- | --- | --- | --- |
| bibiserv | langfristiger Ersatz der derzeitigen BiBiServ Solaris Zone | 01.2025 | ∞ | Tizian Schulz, Niclas Tawakol, Jan Krüger | Jan Krüger |
| brf | CeBiTec Admin Projekt |  12.2022 |∞ | aharin, Achim Neuman, Björn Fischer, Torsten Kasch, Volker Tölle, Rainer Orth  | Stefan Albaum |
| brf-kube | K8S |  06.2023 |∞ |  Stefan Albaum | Stefan Albaum |
| brf-projects| CeBiTec Projekte |  06.2023 |∞ |  Stefan Albaum | Stefan Albaum |
| brf-services| CeBiTec Services |  06.2023 |∞ |  Stefan Albaum, Björn Fischer | Stefan Albaum |
| brf-test | Test Projekt |  12.2022 |∞ |  Achim Neuman, Björn Fischer, Torsten Kasch, Volker Tölle, Rainer Orth | Stefan Albaum |
| cf-ngs | **CoreFacility** Omics NGS  |   05.2024  |∞ | Antatoli Harin, Stefan Albaum | Stefan Albaum |  
| cf-promet | **CoreFacility** Omics NGS  |  07.2024 |∞ | Stefan Albaum | Stefan Albaum |  
| cf-proteomics-course | **CoreFacility** Omics NGS  |  06.2024 |∞ | Stefan Albaum | Stefan Albaum |  
| cf-virtualmicro |  **CoreFacility** Omics NGS  |   08.2023 |∞ | Antatoli Harin, Stefan Albaum | Stefan Albaum |  
| cf-winvms | **CoreFacility** Omics NGS |   05.2023  | ∞ | Antatoli Harin, Stefan Albaum | Stefan Albaum |  

## Default Domäne

Die Default Domäne beherbergt vor allem Services der Cloud Infrastruktur und der de.NBI Geschäftstelle,
sowie ein paar wenige historisch bedingte Projekte, die nicht mehr aktiv genutzt werden, deren
Forschungsergebnisse aber noch gebraucht werden (als legacy gekennzeichnet).

| Projekt | Beschreibung | Datum | Laufzeit | Nutzer | Verantwortlicher |
| --- | --- | --- | --- | --- | --- |
| admin               | Bootstrap project for initializing the cloud + adminstrative Services  | 03.2017 | ∞ |  [ADM], [BRF], Peter Belmann, Viktor Rudko, David Weinholz, Nils Hoffmann | Jan Krüger |
| admin_dummy         | Empty project with no resources for admin accounts  | 03.2017 | ∞ |  [ADM] | Jan Krüger |
| ansible_dev         | Internal project for the development of Ansible roles | 06.2017 |  legacy |     
| awalende_playground | Experiments like kubernetes, ceph stuff, and other stuff I find interesting  | 03.2021 | ∞ | Alex Walender | Alex Walender |
| BiBiGrid2         | Openstack Projekt zu BiBiGrid2, Entwicklungsumgebung | 11.2021 | ∞ | Xaver Stiensmeier, Jan Krüger |  Jan Krüger |
| bibiserv            | Allgemeines Projekt das in der Projekt Entwicklung eingesetzt wird. | 02.2017 | ∞ | [ADM],  Xaver Stiensmeier, Alexander Sczyrba | Jan Krüger|
| Bielefeld-Services  | project for general services like a registry for docker , a private git, sharelatex, ...| 11.2017 | ∞ |  [ADM] | Jan Krüger |
| biogas              | Analyse von Biogas-Datensätzen aus dem SRA. | 06.2017  | legacy | Christian Henke, Benedeikt Osterholz   | Alexander Sczyrba |
| Cami                |   - Critical Assessment of Metagenome Interpretation| 11.2017 | legacy | Gary Robertson, Peter Belmann, Alexander Sczyrba  | Alexander Sczyrba |
| DataRepositories  | Reines Storageprojekt z.B. für SRA Daten | 08.2018 | ∞ | - | Alexander Sczyrba |
| FZJ-ITS             | FZJ ITS-Ausfallumgebung |  11.2024 |  ∞ | J. Heidbüchel, M.Greune, J. Szilvasi  | Jan Krüger |
| Gobi                | Good Bacteria bioactives in industry (Irena / Alex) | 09.2017 | legacy |  Irena Maus, Christian Henke | Alexander Sczyrba |
| portal-pool         | Project is used for the simple usecase. The portal provides to start a single instance without having an Openstack account. | 08.2017 | ∞ | Peter Belmann, Viktor Rudko, David Weinholz, Nils Hoffmann | Peter Belmann |
| portal-pool-dev     |  Development Umgebung vom portal-pool | 08.2017 | ∞ | Peter Belmann, Viktor Rudko, David Weinholz, Nils Hoffmann | Peter Belmann |
| rally               | Rally benchmarking project | 09.2020| ∞ |  [ADM]  | Jan Krüger |
| service             | Service Project | 03.2017 | ∞ |  [ADM]  | Jan Krüger |
