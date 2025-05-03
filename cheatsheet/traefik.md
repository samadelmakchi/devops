
# 🧭 Traefik Cheat Sheet

### 📦 Docker Labels Examples

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.myapp.rule=Host(`example.com`)"
  - "traefik.http.routers.myapp.entrypoints=websecure"
  - "traefik.http.routers.myapp.tls.certresolver=myresolver"
  - "traefik.http.services.myapp.loadbalancer.server.port=80"
```

### 🛣 EntryPoints

```yaml
entryPoints:
  web:
    address: ":80"
  websecure:
    address: ":443"
```

### 🔐 TLS & Let's Encrypt

```yaml
certificatesResolvers:
  myresolver:
    acme:
      email: your@email.com
      storage: acme.json
      httpChallenge:
        entryPoint: web
```

### 🐳 docker-compose.yml Sample

```yaml
version: "3"

services:
  traefik:
    image: traefik:v2.10
    command:
      - "--api.dashboard=true"
      - "--providers.docker=true"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.myresolver.acme.httpchallenge.entrypoint=web"
      - "--certificatesresolvers.myresolver.acme.email=your@email.com"
      - "--certificatesresolvers.myresolver.acme.storage=acme.json"
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080" # Dashboard
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
      - "./acme.json:/acme.json"
    networks:
      - traefik_reverse_proxy

networks:
  traefik_reverse_proxy:
    external: true
```

## 📊 Dashboard Access

```text
http://localhost:8080/dashboard/
```

### ⚙ Middlewares

Redirect HTTP to HTTPS:
```yaml
labels:
  - "traefik.http.middlewares.redirect-to-https.redirectscheme.scheme=https"
  - "traefik.http.routers.myapp.middlewares=redirect-to-https"
```

Basic Auth:
```yaml
labels:
  - "traefik.http.middlewares.auth.basicauth.users=user:$(openssl passwd -apr1 yourpassword)"
  - "traefik.http.routers.myapp.middlewares=auth"
```

Rate Limit:
```yaml
labels:
  - "traefik.http.middlewares.ratelimit.ratelimit.average=100"
  - "traefik.http.middlewares.ratelimit.ratelimit.burst=50"
```

### 🔧 Static vs Dynamic Configuration

| نوع | فایل | قابل استفاده در |
|-----|------|------------------|
| Static | traefik.yml | زمان استارت |
| Dynamic | labels یا فایل جدا | در زمان اجرا |

---

### 🧪 Debug Tips

فعال‌سازی لاگ‌ها:
```yaml
log:
  level: DEBUG
```

بررسی روترها:
```
traefik http routers
```

بررسی لاگ‌ها در Docker:
```
docker logs traefik
```
