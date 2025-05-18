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

### 🔆 سرویس های مشتریان
📜 Gateway (10101 - ...)

📜 Portal Backend (10201 - ...)

📜 Portal Frontend (10301 - ...)

---

### 💢 ابزارهای نصب شده

Server
- 🛠️ Traefik (80) (user: admin - pass: admin)
- 🛠️ Bind9 (5353)

Logs Management
- 📑 Dozzle (8580)
- 📑 Fluentd (8581)
- 📑 Kibana (8582)
- 📑 Elasticsearch (-)
- 📑 Logstash (-)
- 📑 Beats (-)

Monitoring
- 🖥️ Prometheus (9090)
- 🖥️ Zabbix (9091)
- 🖥️ Grafana (9092)
- 🖥️ Splunk (9093)
- 🖥️ Uptime Kuma (9094)

CICD
- ♻️ Gitlab (3001)
- ♻️ Gitea (3002)
- ♻️ Jenkins (3003)
- ♻️ Nexus (3004)
- ♻️ SonarQube (3005)
- ♻️ Selenium (3006 - Chrome: 3007 - Firefox: 3008)

Tools
- 📔 Nginx (3972)

- 📕 Apprise (4013)
- 📕 Mailu (?)

- 📗 Portainer (4100) (set user and pass)
- 📗 Rancher (4101)

- 📙 Shortcut (5231)
- 📙 Mattermost (5232)
- 📙 Focalboard (5233)
- 📙 Nextcloud (5234)
- 📙 Nextcloud Office (5235)
- 📙 n8n (5236)

- 📒 RabbitMQ (6074)
- 📒 Ceph (6075)

- 📘 Wordpress (7087)
- 📘 Joomla (7088)
- 📘 Draw.io (7089)

- 📓 DrawDB (9280)
- 📓 phpMyAdmin (9281)
- 📓 pgAdmin (9282)
- 📓 AdminMongo (9283)
- 📓 RedisInsight (9284)
- 📓 SQLiteWeb (9285)

---

[✔️ راهنماهای مورد نیاز برای مهندسین دواپس](cheatsheet/README.md)  
