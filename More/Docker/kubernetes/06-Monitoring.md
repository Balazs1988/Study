**Topics**

- Monitoring service felhúzása K8 alá
  - Prometheus és Grafana

# Monitoring

## Kubernetes Metrics Server

Ha még nem tettük meg, akkor telepítsük a metrics-servert a clusterünkbe

https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

### Prometheus

https://prometheus-community.github.io/helm-charts/
https://docs.aws.amazon.com/eks/latest/userguide/prometheus.html

```bash
kubectl create namespace prometheus

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm upgrade -i prometheus prometheus-community/prometheus --namespace prometheus --set alertmanager.persistentVolume.storageClass="gp2",server.persistentVolume.storageClass="gp2"
```

Ha `Error: failed to download "prometheus-community/prometheus"` hibát kapunk, lehet hogy updpatelni kell a helmet:

```bash
helm repo update
```

**Ellenőrzés**

```bash
kubectl get all -o wide -n prometheus
```

### Grafana

https://grafana.com/docs/grafana/next/setup-grafana/installation/kubernetes/

`grafana.yaml`

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: grafana
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: grafana-pvc
  namespace: grafana
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: grafana
  namespace: grafana
  labels:
    app: grafana
spec:
  selector:
    matchLabels:
      app: grafana
  template:
    metadata:
      labels:
        app: grafana
    spec:
      securityContext:
        fsGroup: 472
        supplementalGroups:
          - 0
      containers:
        - name: grafana
          image: grafana/grafana:7.5.2
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 3000
              name: http-grafana
              protocol: TCP
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /robots.txt
              port: 3000
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 30
            successThreshold: 1
            timeoutSeconds: 2
          livenessProbe:
            failureThreshold: 3
            initialDelaySeconds: 30
            periodSeconds: 10
            successThreshold: 1
            tcpSocket:
              port: 3000
            timeoutSeconds: 1
          resources:
            requests:
              cpu: 250m
              memory: 750Mi # Attól függően, hogy mekkora node-jaink vannak, ezt lehet állítgatni kell, 250Mi-vel még simán fut
          volumeMounts:
            - mountPath: /var/lib/grafana
              name: grafana-pv
      volumes:
        - name: grafana-pv
          persistentVolumeClaim:
            claimName: grafana-pvc
---
apiVersion: v1
kind: Service
metadata:
  name: grafana
  namespace: grafana
spec:
  type: LoadBalancer
  ports:
    - port: 80
      protocol: TCP
      targetPort: http-grafana
  selector:
    app: grafana
  sessionAffinity: None
```

```bash
kubectl apply -f grafana.yaml
```



Majd böngészőben nyissuk meg a public IP-jét a grafana load-balancer-nek.

- Grafana default account: `admin `+ `admin`
- Bal oldalt configuration -> Datasources -> Add Datasource -> Prometheus
  URL: `CLUSTER IP OF PROMETHEUS-SERVER`
  Access: `Server`
  Save & Test
- Ezután baloldalt `Dashboards` - > `Manage `-> `Import `-> `https://grafana.com/grafana/dashboards/10092`
  De más egyéb dashboardokat is behúzhatunk, próábljuk ki ezeket: https://grafana.com/grafana/dashboards/