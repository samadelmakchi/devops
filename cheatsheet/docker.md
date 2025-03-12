# Docker

این راهنما شامل دستورات کاربردی Docker برای کار با کانتینرها، ایمیج‌ها، شبکه‌ها و Volumeها است.

### ۱. دستورات عمومی و اطلاعاتی
| فرمان | توضیحات |
|-------|---------|
| `docker --version` | نمایش نسخه نصب شده‌ی Docker |
| `docker info` | نمایش اطلاعات کلی Docker از جمله تعداد کانتینرها، ایمیج‌ها و شبکه‌ها |
| `docker help` | مشاهده لیست دستورات Docker و راهنمای هر یک از دستورات |

### ۲. مدیریت ایمیج‌ها (Images)
| فرمان | توضیحات |
|-------|---------|
| `docker images` یا `docker image ls` | نمایش لیست تمامی ایمیج‌های ذخیره‌شده در سیستم |
| `docker pull <image-name>` | دانلود یک ایمیج از Docker Hub |
| `docker push <image-name>` | آپلود یک ایمیج به Docker Hub (نیاز به ورود به حساب Docker دارد) |
| `docker rmi <image-name>` | حذف یک ایمیج از سیستم |
| `docker build -t <image-name> .` | ساخت یک ایمیج از داکرفایل (Dockerfile) موجود در دایرکتوری جاری |
| `docker tag <image-id> <new-image-name>` | اضافه کردن یک تگ (برچسب) جدید به یک ایمیج |
| `docker save -o <file-name.tar> <image-name>` | ذخیره ایمیج به عنوان یک فایل .tar برای انتقال به سیستم دیگر |
| `docker load -i <file-name.tar>` | بارگذاری ایمیج از فایل .tar در سیستم |

### ۳. مدیریت کانتینرها (Containers)
| فرمان | توضیحات |
|-------|---------|
| `docker ps` یا `docker container ls` | نمایش لیست کانتینرهای در حال اجرا |
| `docker ps -a` یا `docker container ls -a` | نمایش لیست همه کانتینرها (در حال اجرا و متوقف‌شده) |
| `docker run <image-name>` | اجرای یک کانتینر جدید از یک ایمیج |
| `docker run -d <image-name>` | اجرای کانتینر به صورت پس‌زمینه‌ای (Detached) |
| `docker run -it <image-name> /bin/bash` | اجرای کانتینر به همراه دسترسی به شل برای وارد کردن دستورات |
| `docker start <container-id>` | شروع به کار یک کانتینر متوقف‌شده |
| `docker stop <container-id>` | متوقف کردن یک کانتینر در حال اجرا |
| `docker restart <container-id>` | راه‌اندازی مجدد یک کانتینر |
| `docker kill <container-id>` | خاتمه دادن فوری به اجرای کانتینر |
| `docker rm <container-id>` | حذف یک کانتینر متوقف‌شده |
| `docker exec -it <container-id> /bin/bash` | ورود به شل یک کانتینر در حال اجرا برای وارد کردن دستورات |
| `docker logs <container-id>` | مشاهده لاگ‌های یک کانتینر |
| `docker inspect <container-id>` | نمایش جزئیات کامل یک کانتینر در قالب JSON |

اجرای یک کانتینر در پس‌زمینه و اتصال به پورت‌های مشخص
```bash
docker run -d -p 8080:80 nginx
```

برای اجرای کانتینر با دسترسی به محیط تعاملی
```bash
docker run -it ubuntu /bin/bash
```

### YAML ۴. مدیریت شبکه‌ها (Networks)

Docker امکان ایجاد و مدیریت شبکه‌ها را برای کانتینرها فراهم می‌کند تا بتوانند با یکدیگر ارتباط برقرار کنند.

| فرمان | توضیحات |
|-------|---------|
| `docker network ls` | نمایش لیست شبکه‌های Docker |
| `docker network create <network-name>` | ایجاد یک شبکه جدید |
| `docker network rm <network-name>` | حذف یک شبکه مشخص |
| `docker network connect <network-name> <container-name>` | اتصال یک کانتینر به یک شبکه خاص |
| `docker network disconnect <network-name> <container-name>` | جدا کردن کانتینر از یک شبکه خاص |

#### انواع شبکه‌ها در Docker

- **bridge**: شبکه پیش‌فرض برای کانتینرهای روی یک میزبان.
- **host**: استفاده از شبکه میزبان، بدون ایجاد پل برای کانتینر.
- **none**: بدون اتصال شبکه؛ معمولاً برای ایجاد شبکه‌های خصوصی و کنترل شده.

ایجاد شبکه برای کانتینرهای یک سرویس:

```bash
docker network create my-network
```

### ۵. Volumeها برای مدیریت داده‌ها (Volumes)

Volumeها به ما اجازه می‌دهند تا داده‌ها را خارج از کانتینر ذخیره کنیم تا با حذف کانتینر، داده‌ها باقی بمانند.

| فرمان | توضیحات |
|-------|---------|
| `docker volume ls` | نمایش لیست Volumeها |
| `docker volume create <volume-name>` | ایجاد یک Volume جدید |
| `docker volume rm <volume-name>` | حذف یک Volume |
| `docker run -v <volume-name>:/path/in/container <image-name>` | اتصال Volume به یک مسیر خاص در کانتینر |
| `docker inspect <volume-name>` | نمایش اطلاعات Volume مشخص |

اجرای کانتینر و اتصال Volume برای ذخیره دائمی داده‌ها:

```bash
docker run -d -v my-volume:/data nginx
```

### ۶. پاکسازی سیستم

برای مدیریت بهینه منابع، Docker امکان پاکسازی کانتینرها، ایمیج‌ها و شبکه‌های بدون استفاده را فراهم می‌کند.

| فرمان | توضیحات |
|-------|---------|
| `docker system df` | نمایش فضای دیسک استفاده شده توسط Docker |
| `docker system prune` | پاکسازی همه‌ی منابع بدون استفاده (شامل کانتینرهای متوقف‌شده، ایمیج‌ها و شبکه‌های بدون استفاده) |
| `docker image prune` | حذف ایمیج‌های بدون استفاده |
| `docker container prune` | حذف کانتینرهای متوقف‌شده |
| `docker volume prune` | حذف Volumeهای بدون استفاده |
| `docker network prune` | حذف شبکه‌های بدون استفاده |

پاکسازی همه‌ی منابع بدون استفاده:

```bash
docker system prune -a
```

### ۷. سایر دستورات کاربردی و متفرقه

| فرمان | توضیحات |
|-------|---------|
| `docker stats` | نمایش مصرف منابع کانتینرها مانند CPU و حافظه |
| `docker top <container-id>` | نمایش پردازش‌های در حال اجرا در کانتینر |
| `docker rename <old-name> <new-name>` | تغییر نام یک کانتینر |
| `docker pause <container-id>` | متوقف کردن موقت اجرای یک کانتینر |
| `docker unpause <container-id>` | از سرگیری اجرای کانتینر متوقف‌شده |
| `docker commit <container-id> <new-image-name>` | ساخت یک ایمیج جدید از یک کانتینر در حال اجرا |
| `docker cp <container-id>:/path/to/file /host/path` | کپی فایل یا دایرکتوری از کانتینر به سیستم میزبان |
| `docker cp /host/path <container-id>:/path/in/container` | کپی فایل یا دایرکتوری از سیستم میزبان به کانتینر |

### ۸. مدیریت داکرفایل (Dockerfile)

داکرفایل به شما امکان می‌دهد تا ایمیج‌های سفارشی خود را با تنظیمات خاص ایجاد کنید.

مثال داکرفایل

```Dockerfile
# انتخاب ایمیج پایه
FROM ubuntu:latest

# نصب پکیج‌ها
RUN apt-get update && apt-get install -y nginx

# کپی کردن فایل‌ها
COPY . /app

# تنظیم دستور پیش‌فرض
CMD ["nginx", "-g", "daemon off;"]
```

برای ساخت ایمیج از داکرفایل:

```bash
docker build -t my-custom-image .
```
