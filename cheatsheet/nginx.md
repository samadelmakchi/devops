
# 🧭 Nginx Cheat Sheet (مرجع کامل)

### 🔧 نصب سریع

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install nginx
```

#### CentOS/RHEL:
```bash
sudo yum install epel-release
sudo yum install nginx
```

#### Docker:
```bash
docker run --name nginx -p 80:80 -v $(pwd)/html:/usr/share/nginx/html:ro -d nginx
```

---

### 📁 ساختار دایرکتوری

| مسیر | کاربرد |
|------|--------|
| `/etc/nginx/nginx.conf` | فایل پیکربندی اصلی |
| `/etc/nginx/sites-available/` | فایل‌های پیکربندی مجزا |
| `/etc/nginx/sites-enabled/` | لینک به فعال‌شده‌ها |
| `/var/www/html/` | مسیر پیش‌فرض محتوای سایت |

---

### 🔄 مدیریت سرویس

```bash
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx
sudo systemctl status nginx
```

---

### 📜 پیکربندی پایه

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    root /var/www/html;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

---

### 🔀 Reverse Proxy

```nginx
server {
    listen 80;
    server_name api.example.com;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

### 🔒 HTTPS با Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com
```

---

### 🔁 Redirect (تغییر مسیر)

#### از http به https:
```nginx
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}
```

#### از www به non-www:
```nginx
server {
    server_name www.example.com;
    return 301 $scheme://example.com$request_uri;
}
```

---

### 🧪 تست پیکربندی

```bash
sudo nginx -t
```

---

### 🔥 Cache Static Files

```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 30d;
    access_log off;
}
```

---

### 📛 خطای سفارشی

```nginx
error_page 404 /custom_404.html;
location = /custom_404.html {
    root /usr/share/nginx/html;
    internal;
}
```

---

### 🔐 محدودیت IP

```nginx
location /admin/ {
    allow 192.168.1.0/24;
    deny all;
}
```

---

### 🔐 Basic Auth

```bash
sudo apt install apache2-utils
htpasswd -c /etc/nginx/.htpasswd admin
```

```nginx
location /secure/ {
    auth_basic "Restricted";
    auth_basic_user_file /etc/nginx/.htpasswd;
}
```

---

### 📜 Logging

```nginx
access_log /var/log/nginx/access.log;
error_log /var/log/nginx/error.log;
```

---

### 🔁 Load Balancing

```nginx
upstream backend {
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
    }
}
```
