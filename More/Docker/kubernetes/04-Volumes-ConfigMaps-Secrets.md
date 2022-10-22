**Topics**

- Volumes
  - PersitentVolume + PersitentVolumeClaim
  - Kötetek csatolása kontérekhez
- ConfigMaps
- Secrets
  - Mount Secrets as Volume

# Volumes

## PersistentVolume and PersistentVolumeClaim

References

- StorageClass - https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/storage-class-v1/
- PersistentVolume - https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-v1/
- PersistentVolumeClaim- https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/

Documentation - https://kubernetes.io/docs/concepts/storage/persistent-volumes/

> Managing storage is a distinct problem from managing compute instances. The PersistentVolume subsystem provides an API
> for users and administrators that abstracts details of how storage is provided from how it is consumed. To do this, we
> introduce two new API resources: PersistentVolume and PersistentVolumeClaim.
>
> A *PersistentVolume* (PV) is a piece of storage in the cluster that has been provisioned by an administrator or
> dynamically provisioned using [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/). It is a
> resource in the cluster just like a node is a cluster resource. PVs are volume plugins like Volumes, but have a
> lifecycle independent of any individual Pod that uses the PV. This API object captures the details of the implementation
> of the storage, be that NFS, iSCSI, or a cloud-provider-specific storage system.
>
> A *PersistentVolumeClaim* (PVC) is a request for storage by a user. It is similar to a Pod. Pods consume node
> resources and PVCs consume PV resources. Pods can request specific levels of resources (CPU and Memory). Claims can
> request specific size and access modes (e.g., they can be mounted ReadWriteOnce, ReadOnlyMany or ReadWriteMany,
> see [AccessModes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes)).
>
> While PersistentVolumeClaims allow a user to consume abstract storage resources, it is common that users need
> PersistentVolumes with varying properties, such as performance, for different problems. Cluster administrators need to
> be able to offer a variety of PersistentVolumes that differ in more ways than size and access modes, without exposing
> users to the details of how those volumes are implemented. For these needs, there is the *StorageClass* resource.
>
> *--kubernetes.io--*

**Hozzunk létre egy tároló osztályt**
Ilyenekből tudunk majd allokálni példányokat ahol szükséges

`storage-class.yaml`

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard    					    # Tetszőleges nevet adhatunk meg itt 
provisioner: kubernetes.io/aws-ebs			 # AWS Elastic Block Storage
parameters: # https://kubernetes.io/docs/concepts/storage/persistent-volumes/
  type: gp2								   # General Purpose SSD
reclaimPolicy: Delete # https://kubernetes.io/docs/concepts/storage/storage-classes/#reclaim-policy
allowVolumeExpansion: true                    # Ennek a kapcsolónak a segítségével növelhető lesz a kötet mérete. Fontos: csak növelhető
volumeBindingMode: WaitForFirstConsumer       # A provisioning addig nem történik meg, amíg valaki nem "igényli" a kötetet 
```

**Ellenőrzés/Aktiválás**

```bash
kubectl get strorageclass
kubectl get sc
kubectl apply -f storage-class.yaml
kubectl get sc
```

**Hozzunk létre egy "kötet-igénylést"**
Ezzel lényegében be tudjuk profilozni, a tárhelyeket amiket szeretnénk használni.

`pvc.yaml`

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-wait 			   # Tetszőleges nevet adhatunk meg itt 
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi			   # A claim-ben határozzuk meg, hogy a kötet méretét is
  storageClassName: standard    # Az előzőleg megadott StorageClass nevét kell itt megadni
```

```bash
kubectl get persistentvolumeclaim
kubectl get pvc
kubectl apply -f pvc.yaml
kubectl get pvc
```

## Stateful deployment

Használjuk fel és egészítsük ki hozzá a `deployment-w-sidecar.yaml` példánkat

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: store-db-w-volumes
spec:
  selector:
    matchLabels:
      app: db					# Ennek meg kell egyeznie (1)
  template:
    metadata:
      labels:
        app: db					# Ennek meg kell egyeznie (1)
    spec:
      volumes:
        - name: db-data 		 # Ennek meg kell egyeznie (2)
          persistentVolumeClaim:
            claimName: pvc-wait   # Itt az előzőleg létrehozott pvc nevét kell megadnunk
      containers:
        - name: postgres
          image: postgres
          volumeMounts:
            - mountPath: /var/lib/postgresql/data
              name: db-data 	 # Ennek meg kell egyeznie (2)
              subPath: ./postgres-data # A köteten ebbe a mappába fogja rakni az adatokat              
          env:
            - name: POSTGRES_PASSWORD
              value: "root"
            - name: POSTGRES_USER
              value: "postgres"
          ports:
            - name: postgres-port
              containerPort: 5432
        - name: adminer
          image: adminer
          ports:
            - name: adminer-port
              containerPort: 8080

```

`db-w-storage.yaml`

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: db-w-storage
  labels:
    name: test
---
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: standard    					    # Tetszőleges nevet adhatunk meg itt 
  namespace: db-w-storage
provisioner: kubernetes.io/aws-ebs			 # AWS Elastic Block Storage
parameters: # https://kubernetes.io/docs/concepts/storage/persistent-volumes/
  type: gp2								   # General Purpose SSD
reclaimPolicy: Delete # https://kubernetes.io/docs/concepts/storage/storage-classes/#reclaim-policy
allowVolumeExpansion: true                    # Ennek a kapcsolónak a segítségével növelhető lesz a kötet mérete. Fontos: csak növelhető
volumeBindingMode: WaitForFirstConsumer       # A provisioning addig nem történik meg, amíg valaki nem "igényli" a kötetet 
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-wait 			   # Tetszőleges nevet adhatunk meg itt 
  namespace: db-w-storage
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi			   # A claim-ben határozzuk meg, hogy a kötet méretét is
  storageClassName: standard    # Az előzőleg megadott StorageClass nevét kell itt megadni
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: store-db-w-volumes
  namespace: db-w-storage
spec:
  selector:
    matchLabels:
      app: db					# Ennek meg kell egyeznie (1)
  template:
    metadata:
      labels:
        app: db					# Ennek meg kell egyeznie (1)
    spec:
      volumes:
        - name: db-data 		 # Ennek meg kell egyeznie (2)
          persistentVolumeClaim:
            claimName: pvc-wait   # Itt az előzőleg létrehozott pvc nevét kell megadnunk
      containers:
        - name: postgres
          image: postgres
          volumeMounts:
            - mountPath: /var/lib/postgresql/data
              name: db-data 	 # Ennek meg kell egyeznie (2)
              subPath: ./postgres-data # A köteten ebbe a mappába fogja rakni az adatokat              
          env:
            - name: POSTGRES_PASSWORD
              value: "root"
            - name: POSTGRES_USER
              value: "postgres"
          ports:
            - name: postgres-port
              containerPort: 5432
        - name: adminer
          image: adminer
          ports:
            - name: adminer-port
              containerPort: 8080
```

## Read / See Also

https://kubernetes.io/docs/concepts/storage/persistent-volumes/

# ConfigMaps

Reference - https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/config-map-v1/
Documentation - https://kubernetes.io/docs/concepts/configuration/configmap/

`.postgres-env`

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=root
```



```bash
kubectl create configmap postgres-config --from-env-file .\.postgres-env
```

--vagy--

```
kubectl create configmap postgres-config --from-literal=POSTGRES_USER=postgres --from-literal=POSTGRES_PASSWORD=root
```

--vagy--

`postgres-with-env.yaml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: postgres-config							# Ennek meg kell egyeznie (1)
data:
  POSTGRES_PASSWORD: postgres 				 # Fontos, hogy a kulcs neve az legyen, amilyen környezeti változót majd vár a konténer
  POSTGRES_USER: root				 		
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: store-db-w-volume
spec:
  selector:
    matchLabels:
      app: postgres-db							# Ennek meg kell egyeznie (2)
  template:
    metadata:
      labels:
        app: postgres-db						# Ennek meg kell egyeznie (2)
    spec:
      volumes:
        - name: db-data							# Ennek meg kell egyeznie (3)
          persistentVolumeClaim:
            claimName: pvc-wait
      containers:
        - image: postgres
          name: postgres
          volumeMounts:
            - name: db-data						   # Ennek meg kell egyeznie (3)
              mountPath: /var/lib/postgresql/data	 # A postgres ebbe a mappába menti a db adatokat
              subPath: ./postgres-data				# A köteten ebbe a mappába fogja rakni az adatokat
          envFrom:
            - configMapRef:
                name: postgres-config 				# Ennek meg kell egyeznie (1)
          ports:
            - name: postgres-port
              containerPort: 5432
        - name: adminer
          image: adminer
          ports:
            - name: adminer-port
              containerPort: 8080				# Ennek meg kell egyeznie (4)
---
apiVersion: v1
kind: Service
metadata:
  name: postgre-service
spec:
  type: LoadBalancer
  selector:
    app: postgres-db							# Ennek meg kell egyeznie (2)
  ports:
    - name: adminer-service-port
      port: 9000
      targetPort: 8080							# Ennek meg kell egyeznie (4)

```

```bash
kubectl apply -f postgres-with-env.yaml
```

# Secrets

> **Uses for Secrets**
>
> There are three main ways for a Pod to use a Secret:
>
> - As [files](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod) in a [volume](https://kubernetes.io/docs/concepts/storage/volumes/) mounted on one or more of its containers.
> - As [container environment variable](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-environment-variables)
> - By the [kubelet when pulling images](https://kubernetes.io/docs/concepts/configuration/secret/#using-imagepullsecrets) for the Pod.
> 
> ### Alternatives to Secrets
> 
> Rather than using a Secret to protect confidential data, you can pick from alternatives.
> 
>Here are some of your options:
> 
>- If your cloud-native component needs to authenticate to another application that you know is running within the same
>   Kubernetes cluster, you can use a [ServiceAccount](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens) and its tokens to identify your client.
>- There are third-party tools that you can run, either within or outside your cluster, that provide secrets management. For example, a service that Pods access over HTTPS, that reveals a secret if the client correctly authenticates (for example, with a ServiceAccount token).
> - For authentication, you can implement a custom signer for X.509 certificates, and use [CertificateSigningRequests](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/) to let that custom signer issue certificates to Pods that need them.
>- You can use a [device plugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) to expose node-local encryption hardware to a specific Pod. For example, you can schedule trusted Pods onto nodes that provide a Trusted Platform Module, configured out-of-band.
> 
> You can also combine two or more of those options, including the option to use Secret objects themselves.
> 
> *--kubernetes.io--*

`secret.yaml`

```yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: mysecret
data:
  username: YWRtaW4=                     # Fontos, ezek az értékek itt base64 encodinggal vannak letárolva
  password: MWYyZDFlMmU2N2Rm             # Viszont ezt egyszerűen vissza tudjuk alakítani: https://www.base64decode.org/ 
```

```bash
kubectl apply -f .\secret.yaml
kubectl get secrets
```

## Mounting secrets - Why?

Lehetőségünk van meghajtóként felcsatolni ezeket a Secreteket ( egyébként a ConfigMap-eket is ).

Felmerülhet a kérdés, hogy mégis miért lehet erre szükségünk. Például azért, hogy valamilyen tanúsítványt tudjunk
eltárolni, amit ezután fel tud használni az alkalmazásunk.

**Ez csak egy példa, production környezetben a HTTPS-t nem így oldjuk meg a frontendünk elé. Erről később!**

```shell
# Windows
mkdir C:\Dev\certs
cd "C:\Program Files\Git\usr\bin\"
./openssl.exe req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out C:/Dev/certs/cert -keyout C:/Dev/certs/cert.key

#Unix 
openssl req -new -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out cert -keyout cert.key
```

`nginx-w-cert.yml`

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-conf
data:
  nginx.conf: |
    user nginx;
    worker_processes  1;
    events {
      worker_connections  10240;
    }
    http {
      server {
          listen                80;
          listen                443 ssl;
          root                  /usr/share/nginx/html;
          server_name           localhost;
          ssl_certificate       /etc/ssl/cert;
          ssl_certificate_key   /etc/ssl/cert.key;
          ssl_protocols         TLSv1 TLSv1.1 TLSv1.2;
      }
    }
---
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: mysecret
data:
  cert.key: LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1...value omitted...JVkFURSBLRVktLS0tLQo=
  cert: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUZ...value omitted...USUZJQ0FURS0tLS0tCg==
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-w-https
  namespace: default
spec:
  selector:
    matchLabels:
      app: nginx-w-https
  template:
    metadata:
      labels:
        app: nginx-w-https
    spec:
      volumes:
        - name: secret-cert
          secret:
            secretName: mysecret     # Ugyanaz kell legyen mint a létrehozott secret neve
            optional: false 		# default setting; "mysecret" must exist
        - name: nginx-conf
          configMap:
            name: nginx-conf
            items:
              - key: nginx.conf
                path: nginx.conf
      containers:
        - image: nginx
          name: nginx-w-https
          volumeMounts:
            - name: secret-cert
              mountPath: "/etc/ssl"
              readOnly: true
            - name: nginx-conf
              mountPath: /etc/nginx/nginx.conf
              subPath: nginx.conf
              readOnly: true
          ports:
            - name: http-nginx
              containerPort: 80
            - name: https-nginx
              containerPort: 443

---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: LoadBalancer
  selector:
    app: nginx-w-https
  ports:
    - name: http-ngnx-svc
      port: 80
      targetPort: 80
    - name: https-ngnx-svc
      port: 443
      targetPort: 443

```

```bash
kubectl apply -f .\nginx-w-cert.yml
kubectl get pods
kubectl exec -it nginx-w-https-<some-id> -- /bin/bash # Ne felejtsük el módosítani az id-t!

ls -l /etc/ssl/ # Ezt már a konténer belsejéből kell kiadnunk, látni fogjuk, hogy felcsatolódtak a secret kulcs-érték párjai fájlokként
```

## ImagePullCreds

https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/

