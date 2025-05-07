#!/bin/bash

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# فقط اگر فایل اصلی وجود ندارد، از فایل نمونه کپی کن
if [ ! -f inventory.local.yml ]; then
  cp inventory.yml inventory.local.yml
  echo "✔️  Created inventory.local.yml from template"
else
  echo "⚠️  inventory.local.yml already exists. Skipping."
fi

if [ ! -f inventory-server.local.yml ]; then
  cp inventory-server.yml inventory-server.local.yml
  echo "✔️  Created inventory-server.local.yml from template"
else
  echo "⚠️  inventory-server.local.yml already exists. Skipping."
fi

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تنظیم DNS برای Shecan و پیکربندی systemd-resolved
echo "🔅  Setting DNS for Shecan and configuring systemd-resolved"
sudo sed -i 's/^#DNS=.*/DNS=185.51.200.2 185.51.200.3/' /etc/systemd/resolved.conf
sudo sed -i 's/^#FallbackDNS=.*/FallbackDNS=8.8.8.8 1.1.1.1/' /etc/systemd/resolved.conf

# ریستارت کردن سرویس systemd-resolved
echo "🔅  Restarting systemd-resolved service"
sudo systemctl restart systemd-resolved

# ایجاد لینک سمبلیک برای resolv.conf
echo "🔅  Creating symbolic link for /etc/resolv.conf"
sudo ln -sf /run/systemd/resolve/resolv.conf /etc/resolv.conf

# تست DNS با استفاده از دستور dig
echo "🔅  Testing DNS with dig"
dig shecan.ir

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# نصب ابزارهای ضروری
echo "🛠️  Installing essential packages"
sudo apt install -y python3-apt cron git gzip tar curl python3-pip mysql-client postgresql-client

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 🚀 تشخیص نسخه پایتون نصب شده
echo "🐍  Detecting Python version"
python_version=$(python3 --version | awk '{print $2}' | cut -d'.' -f1,2)
echo "Detected Python version: $python_version"

# 🚀 دانلود get-pip.py متناسب با نسخه پایتون
echo "🐍  Downloading get-pip.py for Python $python_version"
curl -O https://bootstrap.pypa.io/pip/$python_version/get-pip.py

# نصب pip برای Python
echo "📦  Installing pip for Python $python_version"
sudo python3 get-pip.py
/usr/local/bin/pip3 --version

# 🔗 ایجاد symlink برای pip3
echo "🔗  Creating symlink for pip3"
sudo ln -sf /usr/local/bin/pip3 /usr/bin/pip3
pip3 --version

# اضافه کردن /usr/local/bin به PATH
echo "🔧  Adding /usr/local/bin to PATH"
export PATH=$PATH:/usr/local/bin

# حذف نسخه‌های قدیمی Ansible
echo "🤖  Removing old versions of Ansible (if needed)"
sudo apt remove ansible -y
sudo pip3 uninstall ansible -y

# نصب Ansible از طریق pip3
echo "🤖  Installing Ansible via pip3"
sudo pip3 install ansible

# نصب ansible-lint
echo "🧹  Installing ansible-lint"
sudo apt install ansible-lint -y

# بررسی نسخه‌های نصب شده
echo "📦  Checking installed versions"
ansible --version
ansible-lint --version

# نصب کالکشن community.docker
echo "🐳  Installing community.docker collection"
sudo ansible-galaxy collection install community.docker

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# بررسی اینکه آیا Docker نصب شده یا نه
echo "🐋  Checking if Docker is installed"
docker_check=$(docker --version 2>/dev/null)
if [ $? -eq 0 ]; then
  echo "✔️  Docker is already installed: $docker_check"
else
  echo "⚠️  Docker not found. Installing Docker..."

  # شناسایی نسخه اوبونتو و معماری
  echo "🛠️  Checking Ubuntu version and architecture"
  CODENAME=$(lsb_release -cs)
  VERSION=$(lsb_release -rs)
  ARCHITECTURE=$(dpkg --print-architecture)
  echo "$CODENAME $VERSION $ARCHITECTURE"

  # دانلود فایل‌های Docker
  echo "🐋  Downloading Docker .deb files if not already downloaded"
  DOWNLOAD_DIR="docker"
  mkdir -p "$DOWNLOAD_DIR"

  BASE_URL="https://download.docker.com/linux/ubuntu/dists/$CODENAME/pool/stable/$ARCHITECTURE"
  FILES=(
    "containerd.io_1.7.27-1_${ARCHITECTURE}.deb"
    "docker-ce_28.1.1-1~ubuntu.${VERSION}~${CODENAME}_${ARCHITECTURE}.deb"
    "docker-ce-cli_28.1.1-1~ubuntu.${VERSION}~${CODENAME}_${ARCHITECTURE}.deb"
    "docker-buildx-plugin_0.23.0-1~ubuntu.${VERSION}~${CODENAME}_${ARCHITECTURE}.deb"
    "docker-compose-plugin_2.35.1-1~ubuntu.${VERSION}~${CODENAME}_${ARCHITECTURE}.deb"
  )

  for FILE in "${FILES[@]}"; do
    if [ ! -f "$DOWNLOAD_DIR/$FILE" ]; then
      wget -O "$DOWNLOAD_DIR/$FILE" "$BASE_URL/$FILE"
    fi
  done

  # نصب Docker از فایل‌های دانلود شده
  echo "🐋  Installing Docker packages"
  sudo dpkg -i $DOWNLOAD_DIR/*.deb

  # رفع مشکلات احتمالی وابستگی‌ها
  echo "🐋  Fixing dependencies"
  sudo apt install -f -y

  # شروع و فعال‌سازی سرویس Docker
  echo "🐋  Starting Docker service"
  sudo systemctl start docker
  sudo systemctl enable docker
fi

# چک کردن نسخه داکر
echo "🐋  Checking Docker version"
docker_version=$(docker --version)
echo "🐋 Docker version: $docker_version"

# چک کردن نسخه داکر کامپوز
echo "🐋  Checking Docker Compose version"
docker_compose_version=$(docker compose version)
echo "🐋  Docker Compose version: $docker_compose_version"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# چک کنید آیا ماژول docker در پایتون نصب شده است
echo "🐍  Checking if Python Docker module is installed"
docker_module_status=$(python3 -c "import docker" >/dev/null 2>&1 && echo OK || echo FAIL)
if [ "$docker_module_status" != "OK" ]; then
  echo "⚠️  Python Docker module not found. Installing it..."
  sudo pip3 install docker
else
  echo "✔️  Python Docker module is already installed"
fi

# نصب docker-compose اگر نصب نباشد
echo "🐍  Checking if Docker Compose is installed"
docker_compose_installed=$(pip3 show docker-compose)
if [ -z "$docker_compose_installed" ]; then
  echo "⚠️  Docker Compose not found. Installing it..."
  sudo pip3 install docker-compose
else
  echo "✔️  Docker Compose is already installed"
fi

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ساخت پوشه /etc/docker
echo "🐳  Creating /etc/docker folder"
sudo mkdir -p /etc/docker

# تنظیم ArvanCloud Mirror در فایل daemon.json
echo "🐳  Setting up ArvanCloud Mirror in daemon.json"
sudo bash -c 'echo "{
  \"insecure-registries\" : [\"https://docker.arvancloud.ir\"],
  \"registry-mirrors\": [\"https://docker.arvancloud.ir\"]
}" > /etc/docker/daemon.json'

# خروج از لاگین Docker
echo "🐳  Logging out of Docker"
docker logout

# ریستارت سرویس Docker
echo "🐳  Restarting Docker service"
sudo systemctl restart docker

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ایجاد کلید SSH (با جایگزینی در صورت وجود)
echo "🔑  Generating SSH key"
rm -f "$PWD/id_rsa" "$PWD/id_rsa.pub"  # حذف کلیدهای قبلی اگر وجود داشته باشند
ssh-keygen -t rsa -b 4096 -f "$PWD/id_rsa" -N "" && echo "✔️  SSH key generated at $PWD/id_rsa"

# کپی کلید SSH به مسیر پروژه (با جایگزینی در صورت وجود)
echo "🔑  Copying SSH key to project directory"
cp -f "$PWD/id_rsa" /path/to/your/project/directory/

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "✅  Script execution completed!"
