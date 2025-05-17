
# Kubernetes


### 🛠 مقدمه

Kubernetes (یا K8s) یک سیستم متن‌باز برای اورکستریشن کانتینرهاست که توسط Google طراحی شده و اکنون توسط CNCF نگهداری می‌شود. این ابزار به شما اجازه می‌دهد تا اپلیکیشن‌های کانتینری‌شده را در مقیاس اجرا و مدیریت کنید.

---

### 🧱 اجزای اصلی (Core Components)

| جزء | توضیح |
|-----|-------|
| **Pod** | کوچکترین واحد اجرایی که شامل یک یا چند کانتینر است |
| **Node** | ماشین فیزیکی یا مجازی که Podها روی آن اجرا می‌شوند |
| **Cluster** | مجموعه‌ای از Nodeها |
| **Deployment** | مدیریت نسخه‌ها و انتشار Podها |
| **Service** | دسترسی پایدار به مجموعه‌ای از Podها |
| **Ingress** | کنترل دسترسی HTTP به سرویس‌ها |
| **ConfigMap & Secret** | مدیریت پیکربندی‌ها و اطلاعات حساس |
| **Volume & PVC** | ذخیره‌سازی پایدار داده‌ها |

---

### ⚙ نصب و راه‌اندازی

#### با `minikube` (برای لوکال)
```bash
minikube start
kubectl get nodes
```

#### با `kind` (Kubernetes in Docker)
```bash
kind create cluster
kubectl cluster-info
```

---

### 🔧 دستورات پایه `kubectl`

```bash
kubectl get pods                   # نمایش همه Podها
kubectl get svc                    # نمایش سرویس‌ها
kubectl get nodes                  # نمایش Nodeها
kubectl describe pod <name>        # جزییات کامل یک Pod
kubectl logs <pod>                 # مشاهده لاگ‌های Pod
kubectl exec -it <pod> -- bash     # ورود به Pod
kubectl apply -f <file.yaml>       # اعمال کانفیگ YAML
kubectl delete -f <file.yaml>      # حذف منابع
kubectl rollout restart deploy/<name>  # ریستارت Deployment
```

---

### 📝 منابع YAML نمونه

### Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
          ports:
            - containerPort: 80
```

### Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  type: ClusterIP
  ports:
    - port: 80
      targetPort: 80
```

### Ingress
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
spec:
  rules:
    - host: myapp.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: nginx-service
                port:
                  number: 80
```

---

### 🧪 فضای Namespaces

```bash
kubectl get ns
kubectl create ns my-namespace
kubectl apply -f myfile.yaml -n my-namespace
```

---

### 🔐 Secret & ConfigMap

#### Secret
```bash
kubectl create secret generic db-secret --from-literal=password=SuperSecret
```

#### ConfigMap
```bash
kubectl create configmap app-config --from-literal=mode=production
```

---

### 💾 Persistent Storage

#### PVC (PersistentVolumeClaim)
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

---

### 🚦 Liveness & Readiness

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
```

---

### ☁ Helm (Package Manager)

#### نصب:
```bash
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
```

#### استفاده:
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-release bitnami/nginx
```

---

### 📊 مانیتورینگ و لاگ‌ها

- ابزارها:
  - Prometheus + Grafana
  - Loki + Grafana
  - Fluentd / Filebeat
  - K9s
  - Lens (GUI)

---

### 🔐 RBAC (دسترسی)

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "watch", "list"]
```

---

### 🔧 نکات حرفه‌ای

- همیشه منابع را با `kubectl apply` مدیریت کنید نه `create`
- از `helm` برای اپلیکیشن‌های پیچیده استفاده کنید
- از Health Checks برای افزایش پایداری استفاده کنید
- Namespaceها را برای جداسازی محیط‌ها (dev/stage/prod) استفاده کنید
