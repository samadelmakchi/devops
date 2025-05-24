# DevOps

### 🔽 دانلود فایل ها
``` bash
git clone https://github.com/samadelmakchi/devops.git
```
---

### ⚙️ نصب و کانفیگ سرور
``` bash
cd devops

bash -x setup.sh
```
---

### 🦊 افزودن کلید SSH به حساب GitLab
برای دسترسی آسان و امن به مخازن GitLab، لطفاً کلید عمومی (Public Key) خود را به حساب کاربری‌تان اضافه نمایید. برای این کار مراحل زیر را دنبال کنید:
1. وارد حساب کاربری خود در GitLab شوید.
2. به صفحه `https://gitlab.com/-/user_settings/ssh_keys` مراجعه کنید:
3. فایل کلید عمومی شما با نام `id_rsa.pub` به‌صورت خودکار توسط اسکریپت `setup.sh` ایجاد شده و در پوشه اصلی پروژه قرار دارد.
4. محتوای این فایل را کپی کرده و در قسمت `Key` وارد نمایید.
5. یک عنوان دلخواه در قسمت `Title` وارد کنید (مثلاً: "DevOps").
6. در پایان، روی گزینه `Add key` کلیک کنید.

---

### 🤖 نصب ابزارهای دواپس
لطفاً قبل از اجرای فرآیند نصب، فایل تنظیمات `inventory-server.local.yml` را در پوشه اصلی باز کرده و مطابق نیازهای خود، تغییرات لازم را در آن اعمال کنید.

```bash
source ~/ansible-venv/bin/activate
ansible-playbook -i inventory-server.local.yml playbook-server.yml --ask-become-pass
```

---

### 📦 نصب پروژه های مشتریان
لطفاً فایل `inventory.local.yml` را باز کرده و اطلاعات مربوط به مشتریان را در آن وارد نمایید.

```bash
source ~/ansible-venv/bin/activate
ansible-playbook -i inventory.local.yml playbook.yml --ask-become-pass
```

---

### 🔆 سرویس های مشتریان
📜 Gateway (10101 - ...)

📜 Portal Backend (10201 - ...)

📜 Portal Frontend (10301 - ...)

---

### 💢 ابزارهای دواپس

### Server
- 🛠️ Traefik (80) (user: admin - pass: admin)
- 🛠️ Bind9 (5353)

### Logs Management
- 📑 Dozzle (8580)
- 📑 Fluentd (8581)
- 📑 Kibana (8582)
- 📑 Elasticsearch (-)
- 📑 Logstash (-)
- 📑 Beats (-)

### Monitoring
- 🖥️ Prometheus (9090)
- 🖥️ Zabbix (9091)
- 🖥️ Grafana (9092)
- 🖥️ Splunk (9093)
- 🖥️ Uptime Kuma (9094)

### CICD
- ♻️ Gitlab (3001)
- ♻️ Gitea (3002)
- ♻️ Jenkins (3003)
- ♻️ Nexus (3004)
- ♻️ SonarQube (3005)
- ♻️ Selenium (3006 - Chrome: 3007 - Firefox: 3008)

### Tools
- 📔 Nginx (3972)
<br><br>
- 📕 Apprise (4013)
- 📕 Mailserver (?)
<br><br>
- 📗 Portainer (4100) (set user and pass)
- 📗 Rancher (4101)
<br><br>
- 📙 Shortcut (5231)
- 📙 Mattermost (5232)
- 📙 Focalboard (5233)
- 📙 Nextcloud (5234)
- 📙 Nextcloud Office (5235)
- 📙 n8n (5236)
<br><br>
- 📒 RabbitMQ (6074)
- 📒 Ceph (6075)
<br><br>
- 📘 Wordpress (7087)
- 📘 Joomla (7088)
- 📘 Draw.io (7089)
<br><br>
- 📓 DrawDB (9280)
- 📓 phpMyAdmin (9281)
- 📓 pgAdmin (9282)
- 📓 AdminMongo (9283)
- 📓 RedisInsight (9284)
- 📓 SQLiteWeb (9285)