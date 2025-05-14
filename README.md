# DevOps

### ⚙️ نصب و کانفیگ سرور
این مخزن شامل تنظیمات دواپس برای پروژه‌های شما است. لطفاً پیش از اجرای هر پلی بوک، مراحل راه‌اندازی زیر را انجام دهید.
``` bash
git clone --depth=1 https://github.com/samadelmakchi/devops.git

cd devops

./setup.sh
```

### 🤖 اجرای پلی بوک های آنسیبل

اجرای پلی بوک آنسیبل و کانفیگ سرور
```bash
sudo ansible-playbook -i inventory-server.local.yml playbook-server.yml
```

اجرای پلی بوک آنسیبل و نصب سرویس ها برای مشتریان
```bash
sudo ansible-playbook -i inventory.local.yml playbook.yml
```

---

### 🦊 ساخت Token برای اتصال به GitLab
جهت دریافت توکن در گیت لب به مسیر زیر بروید
```
GitLab >> Preferences >> Access tokens >> Add new token
```
و توکن بدست امده را در فایل inventory.yml و در متغیر gitlab_token بنویسید

---

### 🔆 سرویس های مشتریان
📜 Gateway (10101 - ...)

📜 Portal Backend (10201 - ...)

📜 Portal Frontend (10301 - ...)

---

### ✳️ ابزارهای نصب شده

Server
- ⚙️ Traefik (80) (user: admin - pass: admin)
- ⚙️ Portainer (9000) (set user and pass)
- ⚙️ Bind9 (5353)
- ⚙️ Mailu (?)
- ⚙️ Rancher (8085)

Logs Management
- 📑 Elasticsearch (-)
- 📑 Logstash (-)
- 📑 Beats (-)
- 📑 Fluentd (9880)
- 📑 Kibana (5601)
- 📑 Dozzle (8080)

Monitoring
- 🖥️ Prometheus (9090)
- 🖥️ Zabbix (8082)
- 🖥️ Grafana (3000)
- 🖥️ Splunk (8000)
- 🖥️ Uptime Kuma (3001)

CICD
- ♻️ Gitlab (?)
- ♻️ Jenkins (8081)
- ♻️ Nexus (8084)
- ♻️ SonarQube (9001)
- ♻️ Selenium (4444 - Chrome: 5900 - Firefox: 5901)

Develop
- ✳️ Apprise (8073)
- ✳️ Nginx (8081)
- ✳️ RabbitMQ (15672)
- ✳️ Ceph (?)

Tools
- 🛠️ phpMyAdmin (8083)
- 🛠️ Shortcut (5231)
- 🛠️ Draw.io (8089)
- 🛠️ DrawDB (3500)
- 🛠️ Joomla (8083)
- 🛠️ Wordpress (8082)

---

[✔️ راهنماهای مورد نیاز برای مهندسین دواپس](cheatsheet/README.md)  
