
# Docker Compose 

Docker Compose ابزاری است برای تعریف و مدیریت چند کانتینر Docker که می‌توانند به صورت همزمان اجرا شوند. این ابزار به شما اجازه می‌دهد که با استفاده از یک فایل YAML، پیکربندی و تنظیمات کانتینرها، شبکه‌ها و ولوم‌ها را مدیریت کنید.

### ۱. نصب Docker Compose

بررسی نسخه نصب شده:
```bash
docker-compose --version
```

نصب Docker Compose (در سیستم‌های لینوکس):
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### ۲. فایل `docker-compose.yml`

در Docker Compose از فایل YAML برای پیکربندی استفاده می‌شود. این فایل می‌تواند شامل سرویس‌ها، شبکه‌ها و ولوم‌ها باشد.

ساختار یک فایل `docker-compose.yml`:

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "8080:80"
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: example
```

### ۳. دستورات اصلی Docker Compose

| فرمان | توضیحات |
|-------|---------|
| `docker-compose up` | راه‌اندازی سرویس‌ها و کانتینرها از فایل `docker-compose.yml` |
| `docker-compose up -d` | راه‌اندازی سرویس‌ها در پس‌زمینه (detached mode) |
| `docker-compose down` | متوقف کردن سرویس‌ها و حذف کانتینرها، شبکه‌ها و ولوم‌ها |
| `docker-compose ps` | نمایش وضعیت کانتینرهای در حال اجرا |
| `docker-compose logs` | مشاهده لاگ‌های سرویس‌ها |
| `docker-compose logs -f` | مشاهده لاگ‌ها به صورت زنده |
| `docker-compose build` | ساخت یا بازسازی ایمیج‌ها برای سرویس‌ها |
| `docker-compose restart` | راه‌اندازی مجدد سرویس‌ها |
| `docker-compose stop` | توقف سرویس‌ها بدون حذف کانتینرها |
| `docker-compose start` | راه‌اندازی مجدد سرویس‌های متوقف شده |
| `docker-compose exec <service> <command>` | اجرای فرمان داخل کانتینر یک سرویس (مثلاً برای ورود به کانتینر) |
| `docker-compose run <service> <command>` | اجرای فرمان در یک کانتینر موقت برای سرویس |
| `docker-compose pull` | دریافت ایمیج‌ها از Docker Hub |
| `docker-compose push` | ارسال ایمیج‌ها به Docker Registry |

مثال‌ها:

راه‌اندازی سرویس‌ها در پس‌زمینه:
```bash
docker-compose up -d
```

مشاهده لاگ‌های یک سرویس:
```bash
docker-compose logs -f web
```

متوقف کردن و حذف سرویس‌ها:
```bash
docker-compose down
```

### ۴. مدیریت سرویس‌ها و شبکه‌ها

اضافه کردن یا حذف سرویس‌ها:   
برای افزودن سرویس جدید به فایل `docker-compose.yml` و سپس بازسازی و راه‌اندازی آن:

```bash
docker-compose up -d
```

برای حذف سرویس‌ها:

```bash
docker-compose down
```

پیکربندی شبکه‌ها:
در فایل `docker-compose.yml` می‌توانید شبکه‌ها را برای ارتباط میان سرویس‌ها تعریف کنید.

```yaml
version: '3'
services:
  web:
    image: nginx
    networks:
      - front-end
  db:
    image: postgres
    networks:
      - back-end
networks:
  front-end:
  back-end:
```

### ۵. Volume‌ها و ذخیره‌سازی داده‌ها

در Docker Compose می‌توانید از Volume‌ها برای ذخیره دائمی داده‌ها استفاده کنید.

```yaml
version: '3'
services:
  db:
    image: postgres
    volumes:
      - db-data:/var/lib/postgresql/data
volumes:
  db-data:
```

برای حذف Volume‌ها:

```bash
docker-compose down -v
```

### ۶. محیط‌های مختلف (Environments)

می‌توانید متغیرهای محیطی (environment variables) را در فایل `docker-compose.yml` یا در فایل `.env` برای پیکربندی سرویس‌ها استفاده کنید.

استفاده از متغیرهای محیطی در فایل `docker-compose.yml`:

```yaml
version: '3'
services:
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
```

استفاده از فایل `.env`:
در فایل `.env` مقادیر متغیرهای محیطی را تعریف کنید:

```env
POSTGRES_PASSWORD=mysecretpassword
```

### ۷. Docker Compose و چندین محیط

برای استفاده از چندین فایل Compose برای محیط‌های مختلف (مثلاً توسعه، تولید):

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up
```

### ۸. دستورات مفید دیگر

مشاهده وضعیت سرویس‌ها:
```bash
docker-compose ps
```

کپی کردن فایل‌ها به کانتینر:
```bash
docker-compose exec <service> cp /path/to/file /path/in/container
```

وارد شدن به کانتینر یک سرویس:
```bash
docker-compose exec <service> /bin/bash
```

اجرای دستورات در کانتینر یک سرویس:
```bash
docker-compose exec <service> <command>
```

حذف کانتینرهای متوقف شده:
```bash
docker-compose rm
```

### ۹. مثال کامل فایل `docker-compose.yml`

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - front-end
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - back-end
networks:
  front-end:
  back-end:
volumes:
  db-data:
```

### ۱۰. راه‌اندازی چندین کانتینر با یک فرمان

برای راه‌اندازی چندین سرویس به همراه شبکه‌ها و Volume‌ها در یک فایل Compose، فقط کافیست از دستور زیر استفاده کنید:

```bash
docker-compose up -d
```
