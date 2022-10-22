## AWS Setup

Szükségünk lesz egy AWS fiókra illetve a CLI tool-jukra, hogy terminálból tudjuk kezelni a cloud infrastruktúránkat.

### AWS CLI

[AWS Docs - Install](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

Több féle képpen is megoldható a jogosultság/ hozzáférés kezelése.

- **Root/Admin user**

- **IAM Account**

    - Programmatic access

    - Policy config

      ```json
      {
        "Version": "2022-07-15",
        "Statement": [
          {
            "Effect": "Allow",
            "Principal": {
              "Service": "eks.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
          }
        ]
      }
      ```

    - Download token

Ha megvan a token, az alábbi parancs segítségével tudjuk beállítani a terminál hozzáférést

```bash
aws configure
```

### Eksctl![Gophers: E, K, S, C, T, & L](02-Setup.assets/eksctl.png)

Külön tool, dedikáltan az EKS clusterünk kezelésére

https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html

#### Windows

Ha még nincs choco: [Install Choco](https://chocolatey.org/install)

  ```bash
  choco install -y eksctl 
  ```

#### Linux

  ```bash
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
  ```

## Kubectl

CLI tool, REST Api-n keresztülkommunikálhatunk a Control Plane-el

https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md

Telepítés
- Windows: Docker Desktopnak a része, viszont a Docker settingsben engedélyezni kell a Kubernetest
- [Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

Tesztelés:
- `kubectl version`

Contexts

- A `kubectl`-ben úgynevezett contexteket tudunk használni, hogy el tudjuk szeparálni a különböző clusterjeinket.
    - `~/.kube/config` fájlban találhatóak ezek a beállítások
        - clusters
        - users
        - context = cluster + user
- Docker Desktop
    - Windows (Mac?) - Tálcán jobb klikk -> kubernetes -> majd itt egyszerűen tudunk váltogatni a különböző contextek
      között

## Helm

Ezt keveset fogjuk használni. Segítségével egyszerűen tudunk fehúzni különböző K8-as alkalmazásokat.

https://helm.sh/

## Egyéb hasznos toolok

[Reddit post](https://www.reddit.com/r/kubernetes/comments/xauuxk/what_are_some_useful_kubernetes_tools_you_can/)

- https://k9scli.io/
- https://github.com/alexellis/arkade
- https://monokle.kubeshop.io/
