# 🧪 SonarQube 

### ⚙ نصب با Docker

```bash
docker run -d --name sonarqube   -p 9000:9000   sonarqube:lts
```

### 📦 نصب با docker-compose.yml

```yaml
version: '3'

services:
  sonarqube:
    image: sonarqube:lts
    ports:
      - "9000:9000"
    environment:
      - SONAR_JDBC_URL=jdbc:postgresql://db:5432/sonar
      - SONAR_JDBC_USERNAME=sonar
      - SONAR_JDBC_PASSWORD=sonar
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_extensions:/opt/sonarqube/extensions
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=sonar
      - POSTGRES_PASSWORD=sonar
      - POSTGRES_DB=sonar
    volumes:
      - postgresql:/var/lib/postgresql/data

volumes:
  sonarqube_data:
  sonarqube_extensions:
  postgresql:
```

### 🔧 نصب SonarScanner
روی Debian/Ubuntu:
```bash
sudo apt install unzip
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
unzip sonar-scanner-cli-*.zip
sudo mv sonar-scanner-* /opt/sonar-scanner
echo 'export PATH=$PATH:/opt/sonar-scanner/bin' >> ~/.bashrc
source ~/.bashrc
```
بررسی نصب:
```bash
sonar-scanner --version
```
اجرای آنالیز:

```bash
sonar-scanner
```
---

### 🌐 آدرس دسترسی

http://localhost:9000  
یوزر و پسورد پیش‌فرض:  
**Username:** `admin`  
**Password:** `admin`

---

### 🔍 فایل sonar-project.properties

```properties
sonar.projectKey=my_project
sonar.projectName=My Project
sonar.projectVersion=1.0
sonar.sources=src
sonar.language=java
sonar.sourceEncoding=UTF-8
```

---

### ⚙ تنظیمات CI/CD

- GitHub Actions:
```yaml
- name: SonarQube Scan
  uses: sonarsource/sonarcloud-github-action@master
  with:
    args: >
      -Dsonar.projectKey=my_project
      -Dsonar.organization=my_org
      -Dsonar.host.url=https://sonarcloud.io
      -Dsonar.login=${{ secrets.SONAR_TOKEN }}
```
- Gitlab CI:
```yaml
stages:
  - sonar

sonarqube-check:
  image: sonarsource/sonar-scanner-cli:latest
  stage: sonar
  variables:
    SONAR_USER_HOME: "${CI_PROJECT_DIR}/.sonar"  # کش لوکال
    GIT_DEPTH: "0"  # تاریخچه کامل برای آنالیز
  script:
    - sonar-scanner \
        -Dsonar.projectKey=my_project \
        -Dsonar.sources=. \
        -Dsonar.host.url=http://sonarqube:9000 \
        -Dsonar.login=$SONAR_TOKEN
```

- Jenkins + SonarQube Plugin:

پیش‌نیاز:
```
نصب SonarQube Scanner plugin و SonarQube plugin
```
اضافه کردن SonarQube server در:   
```
Manage Jenkins > Configure System > SonarQube servers
```
نمونه فایل Jenkinsfile:
```
pipeline {
  agent any

  tools {
    sonarQube 'SonarScanner' // اسم تعریف‌شده در Jenkins tools
  }

  stages {
    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv('My SonarQube Server') {
          sh 'sonar-scanner \
            -Dsonar.projectKey=my_project \
            -Dsonar.sources=src \
            -Dsonar.host.url=http://sonarqube:9000 \
            -Dsonar.login=${SONAR_TOKEN}'
        }
      }
    }
  }
}

```

---

### 🔒 امنیت

- تغییر رمز عبور پیش فرض پس از ورود اول

- تنظیم دسترسی پروژه‌ها از:
```
Administration > Security > Users/Roles
```

---

### 🧪 دیباگ و لاگ‌ها

مسیر لاگ‌ها در نصب داکری:
```
/opt/sonarqube/logs/
```
بررسی لاگ‌ها:
```bash
docker logs -f sonarqube
```

