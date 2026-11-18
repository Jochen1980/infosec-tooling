# IT-Verfahren &ndash; de.NBI Cloud Portal und SimpleVM

[[_TOC_]]

_IT-Verfahren sind im Rahmen der IT-Sicherheit in folgenden
Punkten zu dokumentieren:_

- _Zweck des IT-Verfahrens, Zielsetzung,_
- _Beschreibung der Arbeitsabläufe_
- _Schutzbedarfsfeststellung mit einer Bewertung auf Grundlage der in
  der Vorlage dargestellten Bewertungstabelle_
- _Durchführung einer Risikoanalyse in Abhängigkeit vom Ergebnis der
  Schutzbedarfsanalyse Beschreibung der Rollen; ggf. in Form eines
  Berechtigungskonzepts_
- _Festlegung von Vertretungsregelungen, insbesondere im
  Administrationsbereich Zugriffsrechte_
- _Organisation, Verantwortlichkeit und Durchführung der Datensicherung
  Notfallregelungen_
- _Ggf. Wartungsvereinbarungen_

_Für den Fall, dass personenbezogene Daten verarbeitet werden, ist in
Abstimmung mit der oder dem Datenschutzbeauftragten eine Vorabkontrolle
nach dem Datenschutzgesetz des Landes Nordrhein- Westfalen (DSG NRW)
durchzuführen.
Ferner ist zu klären, inwieweit bei der Einführung eines IT-Verfahrens
personalvertretungsrechtliche Regelungen zu berücksichtigen sind.
Es dürfen ausschließlich dokumentierte Verfahren in einen
Produktivbetrieb/Regelbetrieb überführt werden. Das Verfahren ist
produktiv, wenn die Gruppe der Nutzenden uneingeschränkten Zugriff auf
das Verfahren hat. Die IT-Beauftragten sind verantwortlich für die
Initiierung der Erstellung und Pflege der Dokumentation der IT-Verfahren
ihrer Organisationseinheit. Die IT-Verfahrensverantwortlichen sind
verantwortlich für die Umsetzung. Die Zuständigen für
Systemadministration und Applikationsbetreuung sind zur Mitarbeit
verpflichtet. Fragen zur Art und Umfang der Dokumentation sowie zu den
IT-Verfahren sind an den oder die IT-Sicherheitsbeauftrage/n zu richten._

Übersicht der IT-Arbeitsabläufe für SimpleVM

| Verfahren | Verantwortlich | Beschreibung | einmalig | jährlich | monatlich | wöchentlich | täglich |
| --------- | -------------- | ------------ | -------- | -------- | --------- | ----------- | ------- |
| SVM-IT-1  | ADM            | Prozesse     |          | Prüfung  |           |             |         |

Die in der Tabelle verwendeten Personenkürzel und Rollen
sind in [Organisation](organisation.md#gesamtverantwortlichkeit)
beschrieben.

# SVM-IT-1 Deployment 

## General information on deployments

Deployments should be carried out securely in accordance with the guidelines specified in the ISMS.
This includes strict adherence to the "four-eyes-principle" and other measures to prevent disruptions,
such as failures due to misconfigurations or data leaks. 
The only exceptions to deployment without applying the dual control principle are the
implementation/execution of necessary emergency changes to avert damage to the de.NBI Cloud and
SimpleVM as well as its users. If no other employee of the respective scope is present, for example
due to illness, a person from the ADM group must be called in to carry out the deployment.
If also no one from the ADM group is present, members of the PRT scope are also permitted to carry
out emergency changes on their own. In such a case, both groups must be **informed immediately**.

All deployments have to be carried out by connecting to a dedicated deployment instance. All members
of the PRT-group, as well as a selected scope of members of the ADM-group have access to that deployment
machine.

## 1.1 Cloud Portal

The [de.NBI Cloud Portal](https://cloud.denbi.de) and its components are based on a docker compose stack,
running on a dedicated virtual machine, that is operated at the de.NBI Cloud site in Bielefeld. The
corresponding, central repository, that holds both the configuration-templates and compose-files as
well es the scripts that need to be executed for the deployment are located at
the [Cloud Portal repository](https://github.com/deNBI/cloud-portal).

1. Check for backups
    Check the sources, which hold the rotated backups for the databases to have a current backup. 
    E.g. for the Portal, connect to the virtul machine that hosts the production environment of the
    cloud portal.
    ```
    ssh management-production
    cd /vol/persistent/backup/portal/backup
    ls -latrh
    ```
    It will show the latest backup-files created for the backend-database of the portal. The file size
    indicates of the backup was successful.
    ```
    -rw-r--r-- 1 root   root   322M Jan 20 16:01 cloud_db-26-01-20-1600.dump.gz
    ```
    Independent of a successfully created backup being present, always create a manual backup of all
    relevant databases, which then can be used to run a rollback, if any problems occur during the
    deployment.

2. Connect to the deployment instance
    One can connect to the deployment instance via ssh. A configuration that can be added to the local
    ssh-config as well as an corresponding instruction are located at the `portal-organisation`-repository.
    This allows to simply connect the VM as follows:
    ```ssh deployment_instance```

3. Checkout current state of cloud-portal repository
    ```
    cd ~/repositories/cloud-portal
    git checkout master
    git pull
    ```
    **Note**: If another branch has to be used, because certain changes, like hotfixes have to be applied,
    the checkout command can vary.

4. Update `.env` and `.secrets` files
    The `.env` and `.secrets`-files hold all variables that are needed for the configuration of the
    cloud-portal stack.
    The values stored on the CeBiTec volume disk are considered to be the ground truth.
    Therefore one can either connect to the CeBiTec volume using `ssh` again. One needs to utilize
    the user-account one has at the CeBiTec to connect to `porta`:
    `ssh <USERNAME>@porta.cebitec.uni-bielefeld.de`
    Both files are located at `/prj/denbi_cloud_portal/deployment/management`.
    One needs to adjust the values, that need a change in comparison to the currently running setup.
    All changes to be carried out shall be described in a [Release] within the cloud-portal-repository.
    This holds a summary of tags of the components that will be upgraded and information on variables
    to be changed.
    One does update the tag of the components, e.g. of the API-container:
    ```CLOUD_API_TAG=0.1.0-example```
    After the changes are carried out, a second look on the changed variables has to be carried out.
    Now one can transfer the files to the deployment-instance, e.g. via `scp`.
    When running the command from the deployment instance, one runs the following command from the
    `cloud-portal`-directory:
    ```scp -r <USERNAME>@porta.cebitec.uni-bielefeld.de:/prj/denbi_cloud_portal/deployment/management/. .```
    After the files have been transfered, one shall have another check if the variable changes have been
    correct.
    One can utilize `cat` and `grep`, to check for the corresponding tags.
    ```
    ubuntu@deploymentinstance:~/repositories/cloud-portal$ cat .env | grep -i "TAG"
    CLOUD_API_TAG=0.1.0-example
    ...
    ```
    When all checked variables correspond the the expected values, one can proceed.

    An overview of all variables and secrets to set can be found in the main
    [README of the cloud-portal-repository](https://github.com/deNBI/cloud-portal).

5. If changes to the playbook have been made, check the adjusted steps again
    Ensure, that the newly added or adjusted playbook-tasks have been tested, e.g. on the staging
    environment. Double check with your colleagues, what possible consequences the corresponding
    adjustments in the playbook can have on the production enviroment.
    The playbook executed is located within the cloud-portal repository: `cloud-portal/plays/misc/redis/redis.site.yml`.
6. Check at the container-image-registry for tags to be built
    The cloud-api-container, for example, is one of the components that is based on images, which are 
    mashed together using code that has been developed in-house.
    Therefore, one needs to check whether an image with the tag stated in the environment file for the
    corresponding container has been successfully uploaded to the container image registry currently in
    use. Currently, we use [quay.io](https://quay.io/organization/denbicloud).
    For example for the api-images the following link can be used: 
    [https://quay.io/repository/denbicloud/cloud-api?tab=tags](https://quay.io/repository/denbicloud/cloud-api?tab=tags)
    to see all images with the corresponding tags that have been built sucessfully. One wants to ensure,
    that the tag stated in the environment-file is present here.

7. Execution of the deployment script
    The actual deployment can be triggered by running the `run.sh`-bash-script: `./run.sh` or `bash run.sh`.
    It will utilize the `inventory.production`-file that holds the connection information the the host,
    which is acutally running the production environment.
    It runs the already stated ansible-playbook. One needs to ensure that the playbook-run is executed
    successfully.
    - 7.1. If any problems occur during the deployment, the team needs to decide weither some immediate
      changes can fix the issues that occur or a rollback to the previous version of the stack needs to 
      be carried out.
8. Check for basic functionality of the updated stack
    Visit the [landing-page](cloud.denbi.de) and the cloud-portal. Login in the latter and check if basic
    functionalities work as expected after the deployment.
    This includes the listing of cloud-applications and the opening of the form for new applications.
9. Clean-up the files within the repository to avoid data leaks
    To prevent critical data, such as highly sensitive information from the `.secrets` file, from being
    read by third parties in the event of malicious access to the deployment instance, it is necessary
    to delete the `.env` and `.secrets` files from the machine after the deployment has been successfully
    completed.
    ```
    rm .env
    rm .secrets
    ```
## 1.2 SimpleVM

The [de.NBI SimpleVM Portal](https://simplevm.denbi.de) and its components are based on a docker compose
stack, running on a dedicated virtual machine, that is operated at the de.NBI Cloud site in Bielefeld.
The corresponding, central repository, that holds both the configuration-templates and compose-files as
well es the scripts that need to be executed for the deployment are located at the
[SimpleVM Portal repository](https://github.com/deNBI/simplevm-portal).

### 1.2.1 Basic-Stack

The steps for deploying the basic stack can be carried out in the same way as for the cloud portal. Only
the following differences need to be taken into account.

1. One connects to the SimpleVM production environment by using the following ssh-command: `ssh simplevm-production`.
     The backups are located at `/vol/persistent/backup/portal`.

3. The repository to checkout is `simplevm-portal`.
4. The environment files at the CeBiTec-Volume are located at another directory.
    After adjustment, they can be copied as follows:
    ```scp -r <USERNAME>@porta.cebitec.uni-bielefeld.de:/prj/denbi_cloud_portal/deployment/simplevm/. .```

    An overview of the variables and secrets can be found in the main
    [README of the cloud-portal-repository](https://github.com/deNBI/simplevm-portal).

5. The playbook is located in the root of the `simplevm-portal`-directory: `site.yml`
7. The deployment script can be executed by running the `run_prod.sh`.
8. One checks the basic functionality of the SimpleVM-portal. This includes the listing, starting and
   stopping of virtual machines.

### 1.2.2 SimpleVM Clients and Web-Gateways at corresponding locations

The deployment of SimpleVM-Clients are also carried out by utilizing the dedicated deployment instance. 
There is an dedicated script that performs analogous steps for each corresponding cloud location, that
configures the Clients and the [SimpleVM-Webgateway/FORC](https://github.com/deNBI/simpleVMWebGateway)
to be utilized by SimpleVM. 

1. Relevant files
    1.1  The environment files needed for deployment are located on the CeBiTec-volume and need to be
    copied to the deployment instance and adjusted before copying. The path on the CeBiTec volume is
    `/prj/denbi_cloud_portal/deployment/client`.
    E.g. for the Bielefeld cloud location, within that directory there is an `.env.bi`-file that holds
    the corresponding environment variables for the Client to be deployed at that specific cloud-location.
    One can use the following table tofor informations on the environment 

    | VARIABLE                | INFORMATION |  
    | :---------------------- | :---------------------------------------------------------------------------------------------------------- |
    | CLOUD_PORTAL_CLIENT_TAG | The tag of the image to be utilized from the container registry for the client container                    |
    | BIBIGRID_TAG            | The tag of the image to be utilized for the cluster orchestration component                                 |
    | FORC_API_KEY            | The API key to be utilized, so the Web-Gateway configuration can be adjusted from the client                |
    | METADATA_SERVER_TOKEN | The token to be utilized to read data from the SimpleVM metadata server running at the corresponding location |
    | METADATA_WRITE_TOKEN    | The corresponding token to write data to the server                                                         |
    | CLIENT_PORT             | Defines at which port of the machine to be deployed the Client will be available for requests               |
    | OS_PROJECT_ID           | Defines the ID of the project in OpenStack that serves as the pool project for SimpleVM                     |
    | OS_AUTH_URL             | The URL to be used for authentication with OpenStack at the correspoding cloud-location                     |
    | OS_USERNAME             | The user that is utlized as the service-user for the project at that cloud location                         |
    | OS_PASSWORD             | the corresponding passworfd for the user                                                                    |
    | OS_USER_DOMAIN          | If the cloud location has multiple domains, one can specify the domain to be used here                      |
    | OS_PROJECT_DOMAIN_ID    | analogous as for the domain                                                                                 |
    | OS_REGION_NAME          | Specifying the region name                                                                                  |
    | APPLICATION_CREDENTIAL_ID | **Important**: Alternative to the *OS_* variables, allows to authenticate with the OpenStack API          |
    | APPLICATION_CRENDENTIAL_SECRET | Corresponding secret fo the ID given                                                                 |
    | FILEBEAT_TAG            | Tag of the filebeat version to use for monitoring that client installation                                  |
    | ELASTIC_USER            | The username for the elastic-stack to be utilized to send logs and monitoring data                          |
    | ELASTIC_PASSWORD        | Corresponding password for the user of the service                                                          |
    | LOG_FILE_HANDLER_ACTIVATED | Activation flag for the log-file handling of the elastic-stack                                           |
    | LOG_LEVEL               | Setting the log level to be written to the log-files, e.g. "INFO"                                           |
    | LOG_FILE                | The path to the log-file                                                                                    |
    | LOG_BACKUP_COUNT        | Number of backup files to be kept on rotation                                                               |
    | LOG_MAX_BYTES           | The amout of bytes to be written into a single log-file before rotation                                     |
    | HOST                    | Domain/Adress of of the machine                                                                             |
    | REGION                  | The Region name of the installation                                                                         |

    1.2 The same path as the environment path holds server and client certificates that are urilized for
    the communication with the client running on the site to be deployed.
    These are `CA.location.pem` and `server.location.pem`-files.

    1.3 The same path holds a `clouds.location.yml`, which has configuration information to utilize
    [BiBiGrid](https://github.com/BiBiServ/bibigrid), which is used to orchestrate Clusters within
    cloud environments.

    | CONFIGURATION                                   | INFORMATION                                                            |
    |-------------------------------------------------|------------------------------------------------------------------------|
    | openstack.auth.auth_url | Analogous for previously described `.env`-files: URL for the OpenStack authentication          |
    | openstack.auth.authentication_credential_id     | Analogous for previously described `.env`-files                        |
    | openstack.auth.authentication_credential_secret | Analogous for previously described `.env`-files                        |
    | openstack.region_name                           | Region name of the cloud location                                      |
    | openstack.interface                             | Set to public, when endpoints are utilized that are publicly available |
    | openstack.identity_api_version                  | Identity API version to use, e.g. *3*                                  |
    | openstack.auth_type                             | The type of authentication method to use, e.g. *v3applicationcredential* |

    1.4 The path `/prj/denbi_cloud_portal/deployment/forc` holds data for the configuration of the
    SimpleVM-Webgateway/FORC. It is named according to the following pattern: `.env.forc.<location>`.

    | VARIABLE                                | INFORMATION                                               |
    |-----------------------------------------|-----------------------------------------------------------|
    | FORC_\<LOCATION\>_PRODUCTION_SECRET_KEY | Secret key to authorize actions                           |
    | FORC_\<LOCATION\>_PRODUCTION_API_KEY    | API key to authorize actions                              | 
    | FORC_OIDC_CLIENT_ID                     | ID of the corresponding client, utilizing the Web-Gateway |
    | FORC_OIDC_CLIENT_SECRET                 | Secret of the corresponding client                        |

    1.5 The `simplevm-portal`-repository holds configurations for the clients at the
    following path: `config/client/production/<location>/<location>.yml` These hold additional
    configuration information listed below, e.g. for the cloud location in Bielefeld: 

    | VARIABLE                               | INFORMATION                                                                 |
    |----------------------------------------|-----------------------------------------------------------------------------|
    | redis.host                             | Hostname or IP address of the Redis server.                                 |
    | redis.port                             | Port number on which the Redis server is listening.                         |
    | redis.password                         | Password for authenticating with the Redis server.                          |
    | logger.level                           | Log level (e.g., DEBUG, INFO, WARNING, ERROR) to control verbosity.         |
    | logger.file                            | File path where log messages will be written.                               |
    | logger.file_backup_count               | Number of backup log files to keep before overwriting old ones.             |
    | logger.max_bytes                       | Maximum size in bytes for each log file before a new one is created.        |
    | server.threads                         | Number of threads for handling incoming requests on the server.             |
    | server.host                            | Hostname or IP address where the server will listen for incoming connections.|
    | server.port                            | Port number on which the server will listen for incoming connections.       |
    | server.certfile                        | Path to the SSL certificate file for secure (HTTPS) communication.          |
    | server.ca_certs_path                   | Path to the CA certificates used for verifying client certificates.         |
    | server.use_ssl                         | Boolean indicating whether to use SSL/TLS encryption for server communications.|
    | openstack.gateway_ip                   | IP address of the SSH-gateway urlized to allow access to instances.         |
    | openstack.internal_gateway_ip          | Internal IP address of the SSH-Gateway                                      |
    | openstack.use_gateway                  | Boolean indicating whether to use the gateway                               |
    | openstack.network                      | Network name or ID used for creating VMs on OpenStack.                      |
    | openstack.gateway_security_group_id    | Security group ID associated with the gateway in OpenStack.                 |
    | openstack.forc_security_group_id       | Security group ID associated with the FORC web-gateway                      |
    | openstack.availability_zone            | Availability zone for deploying VMs on OpenStack.                           |
    | openstack.ssh_port_calculation         | Formula to calculate SSH port numbers for instances based on IP address.    |
    | openstack.udp_port_calculation         | Formula to calculate the SSH port numbers for instances, analogous but for UDP protocol |

    1.6 The same repository holds the configiration for the
    [SimpleVM-Metadata-Server](https://github.com/deNBI/simplevm-metadata-server/blob/main/.env.in). More
    information on the variables to set can be found in the corresponding linked repository.
    The file `config/client/compose/metadata_server.yml` is used to setup the corresponding server for
    propagation of information to virtual machines on the same instance as the client.

2. Pulling repository and copying files. Within the `simplevm-portal` repository-path on the deployment instance,
   one pulls the branch to use for deployment (mostly this is the `main`-branch) and copies all relevant files from the CeBiTec-volume: 
   `scp -r <USERNAME>@porta.cebitec.uni-bielefeld.de:/prj/denbi_cloud_portal/deployment/client/. simplevm-client/`

1. Exection of the script
   For a specific cloud location, one can then run the ansible-playbook, that will the client:
   `bash deploy/production/<LOCATION>/client/deploy_<LOCATION>_client.sh`
 
   E.g. for Bielefeld the executed script looks something like this:

```~shell
#!/bin/bash

# Define constants for relative paths and file names
ROOT_DIR_RELATIVE_PATH="../../../../"

# Get the directory path of the script
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
ROOT_DIR=${SCRIPT_DIR}/${ROOT_DIR_RELATIVE_PATH}

# Construct paths to inventory file and playbook file
INVENTORY_FILEPATH="${ROOT_DIR}config/client/production/bielefeld/inventory.prod.bielefeld"
PLAYBOOK_FILEPATH="${ROOT_DIR}site.client.yml"
CONFIG_FILEPATH="${ROOT_DIR}config/client/production/bielefeld/bielefeld.yml"

ansible-playbook -v -i "${INVENTORY_FILEPATH}" --tags "client, bibigrid, metadata_server" \
                 --extra-vars "client_server_pem=${ROOT_DIR}simplevm-client/server-bielefeld.pem \
                               client_config=${CONFIG_FILEPATH} \
                               bibigrid_clouds_yml=${ROOT_DIR}simplevm-client/clouds.bielefeld.yml \
                               env_file=${ROOT_DIR}simplevm-client/.env.bi \
                               client_ca_pem=${ROOT_DIR}simplevm-client/CA.bielefeld.pem" 
                 ${PLAYBOOK_FILEPATH}

```

It deploys the client with the enabled cluster-feature (BiBiGrid).

4. Execution of scripts for FORC/SimpleVM-Web-Gateway deployment.

   The scripts for the cloud locations can also be easily executed with the following commands:
   `bash deploy/production/<LOCATION>/forc/deploy_forc_<LOCATION>.sh`.

   E.g. for Bielefeld the executed script looks like this:

```~shell
#!/bin/bash

# Define constants for relative paths and file names
ROOT_DIR_RELATIVE_PATH="../../../../config"
INVENTORY_FILE_NAME="inventory.forc.production.bielefeld"
PLAYBOOK_FILE_NAME="forc.production.bielefeld.yml"

# Get the directory path of the script
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

# Construct paths to inventory file and playbook file
INVENTORY_FILEPATH="${SCRIPT_DIR}/${ROOT_DIR_RELATIVE_PATH}/forc/production/bielefeld/${INVENTORY_FILE_NAME}"
PLAYBOOK_FILEPATH="${SCRIPT_DIR}/${ROOT_DIR_RELATIVE_PATH}/forc/production/bielefeld/${PLAYBOOK_FILE_NAME}"

export $(xargs < .env.forc.bielefeld)
ansible-galaxy install -r ${SCRIPT_DIR}/${ROOT_DIR_RELATIVE_PATH}/forc/requirements.yml --force

ansible-playbook -i  "${INVENTORY_FILEPATH}" \
                     --extra-vars "FORC_SECRET_KEY=${FORC_BIELEFELD_PRODUCTION_SECRET_KEY} \
                                   FORC_API_KEY=${FORC_BIELEFELD_PRODUCTION_API_KEY} \
                                   FORC_OIDC_CLIENT_ID=${FORC_OIDC_CLIENT_ID} \
                                   FORC_OIDC_CLIENT_SECRET=${FORC_OIDC_CLIENT_SECRET}" 
                     "${PLAYBOOK_FILEPATH}"
```