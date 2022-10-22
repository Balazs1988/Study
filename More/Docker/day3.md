Networking - basics
===================

Alapvetően az összes konténerünk egy belső bridge alá kerül be. Ami biztosítani fog saját IP címet mindegyiknek.

- `docker network ls`
    - létező docker hálózatok listázása

- `docker network inspect <network-name>`
    - részletes információk a hálózatról
    - `docker network inspect bridge`
        - láthatjuk, ha fut jelenleg bármilyen konténer, az alapértelmezetten ebbe a hálózatba fog bekerülni, ami automatikusan kioszt neki egy IP címet

Hálózat típusok
---------------

### bridge - single-host networking

Egyszerű ***bridge*** segítségével lehetőségünk van kommunikációra a konténterek között.

- Linuxon és Windowson egyaránt működik.

- Lényegében egy virtual switch-et hoz létre

- Az alapértelmezett hálózat is ilyen típusú amibe kerülnek a konténerjeink.

- A single-host annyit jelent, hogy nincs rá mód hogy 2 ilyen hálózat kommunikálni tudjon egymással, erre vannak speciálisabb típusok

- Érdekesség, hogy minden ilyen hálózat, alapból tartalmaz egy DNS-resolvert ami a konténerünk nevét fel tudja oldani annak IP címére. Fontos, hogy ehhez használjuk a **--name**
  kapcsolót a konténerekhez

> `docker network create -d bridge my-network`
>
> `docker run -d --name my-app1 --network my-network magyarattila90/my-java-app:0.1`
>
>`docker run -d --name my-app2 --network my-network magyarattila90/my-java-app:0.1`
>
> `docker exec -it my-app1 bash`
>
> `:/# ping my-app2`


Docker Compose
==============

A Docker Compose segítségével egyszerűen indíthatunk, előre definiált konténereket.

Pontosabban, itt egy kicsit változik a meghatározás, innentől a futó konténerekre ***service***-ként vagy ***szolgáltatásként*** fogunk hivatkozni.

Ennek a meghatározásához, egy ***docker-compose.yaml*** fájlt fogunk létrehozni, és szerkeszteni.

About  YAML:
------------

- [*https://en.wikipedia.org/wiki/YAML*](https://en.wikipedia.org/wiki/YAML)

- [*YAML Syntax*](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)

docker-compose.yaml példakód:
-----------------------------

[*Compose file version 3 reference*](https://docs.docker.com/compose/compose-file)

```dockerfile
version: "3.8"
services:
  java-app:
    image: magyarattila90/my-java-app:0.1
    networks: 
    - java-app-network
    volumes:
    - "java-app-volume:/usr/"
networks:
  java-app-network:
volumes:
  java-app-volume:
```

**Fontos**, hogy az indentálás kritikus a fájlban, hiszen ez alapján ismeri fel a különböző hierarchiákat.

Ez a leírás távolról sem teljeskörű, de jó alapokat ad. Ha további konfigurációra van szükség a hivatalos dokumentációban mindent megtalálunk.

- **version**

    - `version: "3.8"`

    - a docker-compose verziónkat határothatjuk meg

    - [*Compose file version 3 reference | Docker Documentation*](https://docs.docker.com/compose/compose-file/compose-file-v3/#compose-and-docker-compatibility-matrix)

- **services**

    - Ezen belül határozhatjuk meg a különböző konténereink felépítését

    - **[services](https://docs.docker.com/compose/compose-file/compose-file-v3/#service-configuration-reference):**

        - **image** vs **build**

            - **image: magyarattila90/my-java-app:0.1**

                - Megadhatjuk melyik imageből hozzuk létre a konténert...
                  ```
                  version: "3.8"
                  services:
                    java-app:
                      image: magyarattila90/my-java-app:0.1
                  ```

            - **build: ./**

                - ...vagy melyik dockerfile-ból építsük fel azt

                  ```
                  version: "3.8"
                  services:
                    java-app:
                      build: ./
                  ```

                - További konfigurálás:

                  ```
                  version: "3.8"
                  services:
                    java-app:
                      build:
                        context: ./dir
                        dockerfile: Dockerfile-alternate
                  ```

- **networks**

  ```
  version: "3.8"
  services:
    java-app:
      ...
      networks: 
      - java-app-network
  ```

    - Itt adhatjuk meg, hogy melyik hálózatokba rakjuk bele a konténert

- **depends\_on**

  ```
  version: "3.8"
  services:
    java-app:
      ...
      depends_on: 
      - some-other-services-name
  ```

    - Megadhatjuk, hogy mely egyéb konténerektől függ a jelenlegi. Csak akkor fogja elindítani, ha a többi már elindult.
  > **Fontos, hogy ez nem feltétlenül jelenti azt, hogy azok készen is állnak a kommunikációra.**
  >
  > Tehát a konténer már elindult, de a benne futó alkalmazás, még inicializálódik. Klasszikus eset erre például az adatbázisszerverek esete. Ha szükségünk van rá, hogy bevárjuk az inicializálódást is, akkor egy úgynevezett HealthChecket kell implementálnunk.
  >
  > [How to Add a Health Check to Your Docker Container](https://howchoo.com/devops/how-to-add-a-health-check-to-your-docker-container)

- **restart**

  ```
  version: "3.8"
  services:
    java-app:
      ...
      restart: "unless-stopped"
  ```

    - Hasznos lehet, ha például szeretnénk, hogy a konténer a Dockerrel együtt elinduljon ( Nem ez az alapértelmezett működés! )

- **ports**

  ```
  version: "3.8"
  services:
    java-app:
      ...
      ports:
      - "3000"
      - "3000-3005"
      - "8000:8000"
      - "9090-9091:8080-8081"
      - "49100:22"
      - "127.0.0.1:8001:8001"
      - "127.0.0.1:5000-5010:5000-5010"
      - "127.0.0.1::5000"
      - "6060:6060/udp"
      - "12400-12500:1240"
  ```

    - A nyitni kívánt portjaink konfigurációja

- **volumes:**

  ```
  version: "3.8"
  services:
    java-app:
      ...
      volumes:
      - "/home/" 
      - "dbdata:/var/lib/postgresql/data"
      - "/var/run/postgres/postgres.sock:/var/run/postgres/postgres.sock" 
  ```

    - Unnamed mounts, Named mounts, Volume mounts
        - Ezekről bővebben később!

- **[*networks:*](https://docs.docker.com/compose/compose-file/compose-file-v3/#network-configuration-reference)**

  ```
  version: "3.8"
  services:
    ...
  networks:
    java-app-network:
  ```

    - Itt konfigurálhatjuk a különböző hálózatainkat
    - Az esetek többségében megfelel a default értékek használata, ezért elég csak a hálózat nevét megadni.

- [***volumes:***](https://docs.docker.com/compose/compose-file/compose-file-v3/#volume-configuration-reference)

  ```
  version: "3.8"
  services:
    ...
  networks:
    ...
  volumes:
    java-app-volume:
  ```

    - Itt konfigurálhatjuk a különböző köteteinket

    - Hasonlóan a hálózatokhoz, itt is használhatjuk a default értékeket



[//]: # "TODO Secrets példakód"

[*Docker-compose CLI*](https://docs.docker.com/compose/reference/)
------------------------------------------------------------------

- `docker-compose` ÉS `docker compose` egyaránt működik (mint utólag tapasztaltam, ez -egyelőre- csak Windowson igaz) Utóbbi később került bele a Dockerbe.

- `docker-compose build`
    - Ennek a segítségével hozhatjuk létre a service-eket a yaml fájlból

    - `docker-compose build java-app`
        - Ha a parancs végére odaírjuk a szolgáltatás nevét, akkor csak azt fogja újra buildelni

- `docker-compose up`
    - Ennek a parancsnak a segítségével indíthatjuk a létrehozott szolgáltatásokat

    - **-d**
        - a detach kapcsolóra itt is szükségünk lesz, hogy a háttérben indítsuk a konténereket

- `docker-compose down`
    - Leállítja, majd TÖRLI a konténereket

- `docker-compose down --rmi all --volumes`
    - Ez a parancs törli az összes hozzátartozó image-et, illetve kötetet is!

- `docker-compose logs <konténer név>`
    - Megtekinthetjük a futó konténerek logjait

- `docker-compose ps`
    - Listázás

- `docker-compose stop`
    - Leállítja a konténereket

- `docker-compose start`
    - Ezzel a paranccsal elindíthatjuk a leállított konténereket, de nem hozunk létre újakat

- `docker-compose rm`
    - Törli a leállított servicek konténereit.

**A következő egy aktív projekt docker compose fájlja, 2 különböző hálózattal, és 5 szolgáltatással.**

```
version: "3.8"
networks:
  container-fe-network:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.20.0.0/16
  container-be-network:
    driver: bridge
    ipam:
      driver: default
      config:
        - subnet: 172.21.0.0/16
services:

  tomcat-fe:
    build: ./tomcat-fe
    container_name: container-fe-tomcat
    restart: always
    ports:
      - "52010:8080"
      - "52011:8009"
      - "52012:8000"
    environment:
      - PROFILE=dev
      - LOG_CONFIG=container-fe-logback.xml
    volumes:
      - ../volumes/container-fe-tomcat/app_config:/usr/local/tomcat/app_config:ro
      - ../volumes/container-fe-tomcat/logs:/usr/local/tomcat/logs:rw
    networks:
      container-fe-network:
  
  httpd-fe:
    build: ./apache-fe
    container_name: container-fe-httpd
    restart: always
    ports:
      - "52000:8080"
      - "52001:80"
    volumes:
      - ../volumes/container-fe-httpd/vhosts.d:/usr/local/apache2/conf/vhosts.d:ro
      - ../volumes/container-fe-httpd/logs:/usr/local/apache2/logs:rw
    networks:
      container-fe-network:

  postgre:
    build: ./postgre
    container_name: container-be-postgre
    restart: always
    ports:
      - "52121:5432"
    environment:
      - POSTGRES_DB=container-db
      - POSTGRES_USER=container-user
      - POSTGRES_PASSWORD=strong_passw0rd
    volumes:
      - ../volumes/container-be-postgre:/var/lib/postgresql/data:rw
    networks:
      container-be-network:
  
  tomcat-be:
    build: ./tomcat-be
    container_name: container-be-tomcat
    restart: always
    ports:
      - "52110:8080"
      - "52111:8009"
      - "52112:8000"
    environment:
      - PROFILE=dev
      - LOG_CONFIG=container-be-logback.xml
    volumes:
      - ../volumes/container-be-tomcat/app_config:/usr/local/tomcat/app_config:ro
      - ../volumes/container-be-tomcat/logs:/usr/local/tomcat/logs:rw
    networks:
      container-be-network:
  
  httpd-be:
    build: ./apache-be
    container_name: container-be-httpd
    restart: always
    ports:
      - "52100:8080"
      - "52101:80"
    volumes:
      - ../volumes/container-be-httpd/vhosts.d:/usr/local/apache2/conf/vhosts.d:ro
      - ../volumes/container-be-httpd/logs:/usr/local/apache2/logs:rw
    networks:
      container-be-network:
```

See also
--------

[*How to configure HTTPS for an Nginx Docker Container Stackify*](https://stackify.com/how-to-configure-https-for-an-nginx-docker-container/)

## Gyakorló feladatok

1. MySql konténer
    - Keress egy hivatalos base-image-t hozzá
    - A konténer létrehozásánál legyen megadva az alábbi konfigurációk ( Nézd át az image dokumentációját! )
        - Jelszó: test1234
        - Hozzon létre egy adatbázist, "test-db" néven
2. PostgreSql konténer
    - Keress egy hivatalos base-image-t hozzá
    - Forwardold a belső Postgres portot (dokumentáció!) tetszőleges lokális portra.
3. Több konténeres kompozíció

- Hozz létre 2 tetszőleges, de egymástól eltérő Dockerfile-t
    - pl MySql és nGinx
- Mindegyikből határozz meg egy service-t
- Adj hozzá egy harmadik service-t, ez viszont buildelődjön egy hivatalos image alapján
    - pl OpenJDK-11