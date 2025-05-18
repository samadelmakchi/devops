
# 🔧 Jenkins Cheat Sheet (مرجع کامل)


### 🧱 مفاهیم اصلی

| مفهوم | توضیح |
|-------|-------|
| **Job / Project** | تعریف وظیفه CI/CD |
| **Build** | اجرای یک Job |
| **Pipeline** | اسکریپت برای اجرای مراحل CI/CD |
| **Node / Agent** | ماشینی که Build روی آن اجرا می‌شود |
| **Executor** | تعداد buildهای هم‌زمان روی یک Node |
| **Plugin** | افزودنی‌هایی برای توسعه قابلیت‌ها |
| **SCM** | سیستم مدیریت سورس مثل Git |

---

### 🚀 نصب Jenkins

#### با Docker
```bash
docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts
```

#### دسترسی اولیه
- آدرس: http://localhost:8080
- رمز عبور اولیه: داخل `/var/jenkins_home/secrets/initialAdminPassword`

---

### 🔐 تنظیمات اولیه

- نصب پلاگین‌ها: Git, Pipeline, Docker, Blue Ocean, ...
- ساخت کاربر Admin
- تنظیم آژنت‌ها (Nodes) اگر نیاز به اجرا در ماشین‌های دیگر دارید

---

### 🛠 Job Types

| نوع Job | کاربرد |
|---------|--------|
| Freestyle | ساده و قابل تنظیم از GUI |
| Pipeline | اسکریپت‌های پیچیده با `Jenkinsfile` |
| Multibranch | برای هر شاخه Git یک Pipeline |
| Folder | دسته‌بندی Jobها |

---

### 🧾 ساخت Jenkinsfile

```groovy
pipeline {
  agent any

  environment {
    STAGE = "development"
  }

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/user/repo.git'
      }
    }

    stage('Build') {
      steps {
        sh 'make build'
      }
    }

    stage('Test') {
      steps {
        sh 'make test'
      }
    }

    stage('Deploy') {
      when {
        branch 'main'
      }
      steps {
        sh './deploy.sh'
      }
    }
  }
}
```

---

### ⚙ اتصال به GitLab / GitHub

- نصب پلاگین Git / GitLab / GitHub
- ساخت Webhook در Git برای URL:
  ```
  http://<jenkins-host>/project/<job-name>
  ```
- تنظیم SSH Key یا Access Token

---

### 🪝 اتصال به Gitea

- نصب پلاگین Gitea
- ساخت Access Token در Gitea
- افزودن Repository با SCM: Gitea (یا Git)
- ایجاد Webhook در Gitea:
  ```
  http://<jenkins>/gitea-webhook/post
  ```

---

### 🔍 پلاگین‌های ضروری

| پلاگین | کاربرد |
|--------|--------|
| Git | اتصال به مخزن |
| Pipeline | استفاده از Jenkinsfile |
| Docker | اجرای job در Docker |
| Blue Ocean | رابط گرافیکی زیباتر |
| GitLab | اتصال GitLab به Jenkins |
| Matrix Authorization | کنترل دسترسی دقیق |

---

### 🪄 دستورات Groovy در Pipeline

```groovy
sh 'echo Hello'
env.BRANCH_NAME
currentBuild.result = 'SUCCESS'
input 'آیا ادامه دهیم؟'
```

---

### 📦 دستورات پرکاربرد CLI

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ list-jobs
java -jar jenkins-cli.jar -s http://localhost:8080/ build my-job
```

---

### 📊 گزارش‌گیری و Notification

- پلاگین Slack / Telegram / Email
- استفاده از `post`:
```groovy
post {
  success {
    slackSend message: "Build موفق بود"
  }
  failure {
    mail to: 'admin@example.com', subject: 'Build شکست خورد'
  }
}
```

---

### 🔐 مدیریت کاربران و دسترسی

- نصب پلاگین Matrix Authorization Strategy
- ساخت Role و تخصیص دسترسی برای View / Build / Configure

---

### 🚀 CI/CD واقعی با Docker

#### مرحله Build و Push:
```groovy
sh 'docker build -t myapp:latest .'
sh 'docker tag myapp:latest registry.local/myapp:latest'
sh 'docker push registry.local/myapp:latest'
```

#### مرحله Deploy:
```groovy
sshagent(['deploy-key']) {
  sh 'ssh user@server "docker pull registry.local/myapp:latest && docker-compose up -d"'
}
```
