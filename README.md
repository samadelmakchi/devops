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

### 🦊 افزودن کلید SSH به حساب GitLab / Github
برای دسترسی آسان و امن به مخازن GitLab، لطفاً کلید عمومی (Public Key) خود را به حساب کاربری‌تان اضافه نمایید. برای این کار مراحل زیر را دنبال کنید:
1. وارد حساب کاربری خود در GitLab / Github شوید.
2. به صفحه `https://github.com/settings/ssh/new` / `https://gitlab.com/-/user_settings/ssh_keys` مراجعه کنید:
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

### 🧪 انجام تست های اتوماتیک

```bash
source ~/ansible-venv/bin/activate
ansible-playbook -i inventory.local.yml playbook-test.yml --ask-become-pass
```

---

### 🌐 راهنمای اختصاص ساب‌دامین به سرویس‌ها

#### **روش اول: استفاده از پنل DirectAdmin**
1. به پنل **DirectAdmin** وارد شوید.
2. به بخش **DNS Management** مراجعه کنید.
3. روی گزینه **Add Record** کلیک کنید.
4. فیلدهای موردنظر را به‌صورت زیر تکمیل کنید:
   - **Record Type**: A
   - **Name**: نام ساب‌دامین (مانند `calibri`)
   - **Value**: آدرس IP سرور مقصد
5. تغییرات را ذخیره کنید.

#### **روش دوم: استفاده از Cloudflare**
1. به حساب کاربری خود در **Cloudflare** وارد شوید.
2. از لیست دامنه‌ها، دامنه موردنظر را انتخاب کنید.
3. از منوی بالای صفحه، به بخش **DNS** بروید.
4. روی دکمه **+ Add record** کلیک کنید.
5. تنظیمات زیر را اعمال کنید:
   - **Type**: A
   - **Name**: نام ساب‌دامین (برای مثال: `calibri`)
   - **IPv4 address**: آدرس IP سرور مقصد
   - **Proxy status**:
     - برای استفاده از قابلیت‌های امنیتی و بهینه‌سازی Cloudflare، گزینه **Proxied** را انتخاب کنید.
     - برای هدایت مستقیم ترافیک به سرور بدون واسطه Cloudflare، گزینه **DNS only** را انتخاب کنید.
6. روی دکمه **Save** کلیک کنید تا رکورد ذخیره شود.

---

### 🔆 سرویس های مشتریان

📜 Gateway (8061 - ...)

📜 Portal Backend (7061 - ...)

📜 Portal Frontend (6061 - ...)

---

### 💢 ابزارهای دواپس

🛣️ Traefik (80) (user: admin - pass: admin)

📊 Splunk (8580)

🔥 Prometheus (9090)

📈 Grafana (9091)

⏰ Uptime Kuma (9092)

♻️ Jenkins (4441)

🐳 Portainer (4100) (set user and pass)

🌐 Nginx (4101)

🐰 RabbitMQ (4102)

📬 Apprise (4103)

✉️ Mailserver (4104)

🗄️ phpMyAdmin (9281)

🐘 pgAdmin (9282)

