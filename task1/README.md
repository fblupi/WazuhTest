# Instalación de OSSEC

## Manager

Se ha procedido a instalar OSSEC-Wazuh en una máquina ubuntu. Para ello se han instalado los paquetes necesarios:

```
sudo apt-get install gcc make git libc6-dev libssl-dev
```

y, a continuación, se ha clonado la última versión estable del repositorio de GitHub y se ha instalado:

```
cd ~
mkdir ossec_tmp && cd ossec_tmp
git clone -b stable https://github.com/wazuh/wazuh.git ossec-wazuh
cd ossec-wazuh
sudo ./install.sh
```

Se ha elegido la opción correspondiente para instalar el Manager y se ha iniciado tras la instalación con:

```
sudo /var/ossec/bin/ossec-control start
```

## Agente

Se ha procedido a instalar OSSEC-Wazuh en una máquina ubuntu, repitiendo los pasos anteriores hasta la instalación donde se ha escogido la opción de instalar el Agente en lugar del Manager.

Durante la instalación ha preguntado por la dirección del Manager la cual ha sido proporcionada para que automáticamente el instalador lo agregue en el fichero `/var/ossec/etc/ossec.conf`.

Una vez instalado, en el Manager se ha ejecutado la orden:

```
sudo /var/ossec/bin/manage_agents
```

y se ha agregado el nuevo agente proporcionando un nombre y una dirección IP. A continuación se ha obtenido la clave, necesaria para el Agente donde se ha ejecutado

```
sudo /var/ossec/bin/manage_agents
```

y se ha importado la clave que se había obtenido en el Manager.

Por último se ha ejecutado:

```
sudo /var/ossec/bin/ossec-control restart
```

# Problemas encontrados durante el proceso

Durante este proceso no se ha tenido ningún problema, pues siguiendo los pasos proporcionados en la [web de Wazuh](https://documentation.wazuh.com/1.1/wazuh_installation.html) la instalación se realiza fácilmente.

# Diferencias entre OSSEC-Wazuh y OSSEC

OSSEC-Wazuh es un fork de OSSEC que contiene caracterísitcas adicionales como el soporte de logging en JSON así como la inegración con Elasticsearch, Logstash y Kibana. Además cuenta con una API RESTful la cual permite realizar una gestión de OSSEC-Wazuh de forma remota.
