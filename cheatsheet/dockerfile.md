# Dockerfile Cheat Sheet
این Cheat Sheet به شما کمک می‌کند تا به سرعت با دستورات و تکنیک‌های اساسی Dockerfile آشنا شوید و بتوانید ایمیج‌های Docker سفارشی خود را ایجاد کنید.

### 1. ساختار یک Dockerfile

یک Dockerfile به شما امکان می‌دهد تا یک ایمیج Docker سفارشی بسازید. در ادامه برخی از دستورات مهم Dockerfile را معرفی کرده‌ایم.

### 2. دستورات اصلی Dockerfile

| فرمان       | توضیحات                                                                                         |
|-------------|-------------------------------------------------------------------------------------------------|
| `FROM`      | تعیین پایه برای ساخت ایمیج. معمولاً باید اولین دستور باشد.                                        |
| `RUN`       | اجرای دستور در حین ساخت ایمیج. معمولاً برای نصب پکیج‌ها یا انجام تنظیمات استفاده می‌شود.            |
| `COPY`      | کپی کردن فایل‌ها و دایرکتوری‌ها از میزبان به ایمیج.                                               |
| `ADD`       | مشابه `COPY` با قابلیت‌های اضافی مانند استخراج آرشیوها (مثلاً `.tar` files).                       |
| `WORKDIR`   | تغییر دایرکتوری کاری در داخل کانتینر.                                                           |
| `CMD`       | تعیین دستور پیش‌فرض برای اجرا هنگام راه‌اندازی کانتینر.                                           |
| `ENTRYPOINT`| مشابه `CMD` اما بیشتر برای تعریف دستورات ثابت که نمی‌توان آن‌ها را تغییر داد.                     |
| `EXPOSE`    | اعلام پورت‌هایی که توسط کانتینر استفاده می‌شود.                                                    |
| `ENV`       | تنظیم متغیرهای محیطی.                                                                           |
| `VOLUME`    | ایجاد یک Volume برای ذخیره‌سازی داده‌ها در طول عمر کانتینر.                                       |
| `USER`      | تعیین کاربری که کانتینر باید تحت آن اجرا شود.                                                   |
| `ARG`       | تعیین متغیرهای ساخت (build-time variables).                                                     |
| `LABEL`     | افزودن متا داده به ایمیج (مثلاً برای مدیریت و مستندات).                                           |
| `STOPSIGNAL`| تعیین سیگنال متوقف کننده برای کانتینر.                                                          |

### 3. مثال‌های Dockerfile

#### ۳.۱. انتخاب ایمیج پایه و نصب پکیج‌ها

```Dockerfile
# انتخاب ایمیج پایه
FROM ubuntu:latest

# بروزرسانی و نصب Nginx
RUN apt-get update && apt-get install -y nginx

# کپی کردن فایل‌های پروژه
COPY ./html /usr/share/nginx/html

# راه‌اندازی سرویس Nginx
CMD ["nginx", "-g", "daemon off;"]
```

#### ۳.۲. استفاده از متغیرهای محیطی (Environment Variables)

```Dockerfile
# انتخاب ایمیج پایه
FROM node:14

# تنظیم متغیرهای محیطی
ENV NODE_ENV=production
ENV APP_HOME=/app

# کپی کردن فایل‌ها
COPY . $APP_HOME

# نصب وابستگی‌ها
WORKDIR $APP_HOME
RUN npm install

# اجرای اپلیکیشن
CMD ["npm", "start"]
```

#### ۳.۳. استفاده از `EXPOSE` برای اعلام پورت‌ها

```Dockerfile
# انتخاب ایمیج پایه
FROM node:14

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های پروژه
COPY . /app

# نصب وابستگی‌ها
RUN npm install

# اعلام پورت
EXPOSE 3000

# اجرای اپلیکیشن
CMD ["npm", "start"]
```

#### ۳.۴. ساختن یک ایمیج از Dockerfile

```bash
# ساختن ایمیج از Dockerfile در دایرکتوری جاری
docker build -t my-node-app .
```

#### ۳.۵. استفاده از `ARG` برای متغیرهای ساخت (Build-time variables)

```Dockerfile
# تعیین یک متغیر ساخت
ARG APP_VERSION=1.0

# انتخاب ایمیج پایه
FROM node:14

# استفاده از ARG
RUN echo "Building version ${APP_VERSION}"

# سایر دستورات
COPY . /app
WORKDIR /app
RUN npm install
CMD ["npm", "start"]
```

ساخت ایمیج با تعیین متغیر `APP_VERSION`:

```bash
docker build --build-arg APP_VERSION=2.0 -t my-node-app .
```

#### ۳.۶. استفاده از `ADD` برای کپی و استخراج فایل‌ها

```Dockerfile
# انتخاب ایمیج پایه
FROM ubuntu:latest

# کپی و استخراج فایل‌های آرشیو
ADD my-archive.tar.gz /usr/local/app

# سایر دستورات
CMD ["echo", "Finished extracting archive"]
```

### 4. مدیریت چندین مرحله ساخت (Multi-stage Builds)

در Dockerfile می‌توان از چندین مرحله ساخت (multi-stage builds) استفاده کرد تا ایمیج نهایی به حداقل ممکن برسد.

```Dockerfile
# مرحله اول: ساخت اپلیکیشن
FROM node:14 AS builder
WORKDIR /app
COPY . /app
RUN npm install && npm run build

# مرحله دوم: ساخت ایمیج نهایی
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html

# راه‌اندازی Nginx
CMD ["nginx", "-g", "daemon off;"]
```

### 5. فایل `.dockerignore`

در کنار Dockerfile، می‌توانید از فایل `.dockerignore` برای نادیده گرفتن فایل‌ها و دایرکتوری‌های خاص استفاده کنید تا آن‌ها در هنگام ساخت ایمیج به کانتینر اضافه نشوند.

مثال `.dockerignore`

```text
node_modules/
*.log
*.md
```

### 6. نکات و بهترین شیوه‌ها

- همیشه از آخرین نسخه پایدار ایمیج‌ها استفاده کنید.
- از `WORKDIR` برای تنظیم دایرکتوری کاری به جای استفاده از `RUN cd` استفاده کنید.
- از دستورات `RUN` به صورت معقول استفاده کنید تا از تولید لایه‌های اضافی جلوگیری شود.
- از `COPY` به جای `ADD` استفاده کنید مگر اینکه نیاز به استخراج آرشیو یا دانلود فایل‌ها از اینترنت داشته باشید.
- `CMD` را برای تنظیم دستور پیش‌فرض استفاده کنید و اگر نیاز به تنظیم دستورات دائمی دارید از `ENTRYPOINT` استفاده کنید.


