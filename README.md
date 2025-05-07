# DevOps

### ⚙️ مراحل راه‌اندازی (Setup)
این مخزن شامل تنظیمات دواپس برای پروژه‌های شما است. لطفاً پیش از اجرای هر پلی بوک، مراحل راه‌اندازی زیر را انجام دهید.
``` bash
git clone --depth=1 https://github.com/samadelmakchi/devops.git

cd devops

chmod +x setup.sh

./setup.sh
```


### 🤖 نصب و کانفیگ سرور

نصب آنسیبل
```bash
# Remove old versions of Ansible (if needed)
sudo apt remove ansible -y

# Install Ansible via apt
sudo apt update
sudo apt install ansible -y

# Install Ansible (recommended)
sudo pip3 install ansible -y

# Install ansible-lint
sudo apt install ansible-lint -y

# Install the required packages
sudo ansible-galaxy collection install community.docker

# Check installed versions
ansible --version
ansible-lint --version
```

اجرای پلی بوک آنسیبل و کانفیگ سرور
```bash
sudo ansible-playbook -i inventory-server.local.yml playbook-server.yml
```

اجرای پلی بوک آنسیبل و نصب سرویس ها برای مشتریان
```bash
sudo ansible-playbook -i inventory.local.yml playbook.yml
```

---

### ✴️ ساخت کلید عمومی و خصوصی SSH (id_rsa/id_rsa.pub)
#### ساخت کلید SSH
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
- -t rsa: نوع کلید را RSA تعیین می‌کند.
- -b 4096: اندازه کلید را 4096 بیت می‌سازد (امن‌تر از 2048).
- -C "your_email@example.com": یک توضیح یا تگ به کلید اضافه می‌کند (اختیاری).

#### پاسخ به سوالات در طول فرآیند:  
اینجا مسیر ذخیره‌سازی را می‌پرسه. اگه همون پیش‌فرض .ssh/id_rsa خوبه، فقط Enter بزن.
```
Enter file in which to save the key (/home/youruser/.ssh/id_rsa):
```
اگه خواستی کلیدت رمز داشته باشه، اینجا وارد کن. در غیر این صورت Enter بزن تا بدون رمز ساخته بشه.
```
Enter passphrase (empty for no passphrase):
```
#### نتیجه:
بعد از انجام مراحل بالا، دو فایل ساخته می‌شه:
```
~/.ssh/id_rsa → کلید خصوصی (محرمانه، فقط در اختیار شما)

~/.ssh/id_rsa.pub → کلید عمومی (قابل اشتراک‌گذاری با سرورها)
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
- ⚙️ Portainer (9000)
- ⚙️ Bind9 (-)
- ⚙️ Mailu (?)
- ⚙️ Rancher (?)

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
- ✳️ Nginx (?)
- ✳️ RabbitMQ (15672)
- ✳️ Ceph (?)

Tools
- 🛠️ phpMyAdmin (8083)
- 🛠️ Shortcut (5231)
- 🛠️ Draw.io (8089)
- 🛠️ DrawDB (3500)

---

[✔️ راهنماهای مورد نیاز برای مهندسین دواپس](cheatsheet/README.md)  
