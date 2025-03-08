#!/bin/bash

# انتخاب نسخه اوبونتو و معماری مناسب
echo "لطفا نسخه اوبونتو خود را از لیست انتخاب کنید:"
echo "| نسخه اوبونتو |       نام کد     |"
echo "|--------------|------------------|"
echo "| 20.04        | Focal Fossa      |"
echo "| 18.04        | Bionic Beaver    |"
echo "| 16.04        | Xenial Xerus     |"
echo "| 22.04        | Jammy Jellyfish  |"
echo "| 21.10        | Impish Indri     |"
echo "| 19.10        | Eoan Ermine      |"
echo "| 17.10        | Artful Aardvark  |"
echo "| 15.04        | Vivid Vervet     |"
echo "| 14.04        | Trusty Tahr      |"
echo "| 12.04        | Precise Pangolin |"
echo ""
echo "لطفا نام کد نسخه اوبونتو خود را وارد کنید (مثال: focal, bionic, xenial و ...):"
read UBUNTU_VERSION

# انتخاب معماری مناسب
echo "لطفا معماری سیستم خود را وارد کنید (مثال: amd64, armhf, arm64, s390x):"
read ARCHITECTURE

# به پوشه هدف بروید
cd /home/install/docker/

# نسخه و معماری را برای دانلود فایل‌ها تنظیم کنید
VERSION="latest_version"  # به جای "latest_version" نسخه مورد نظر را وارد کنید

# دانلود فایل‌های .deb از Docker
wget https://download.docker.com/linux/ubuntu/dists/$UBUNTU_VERSION/pool/stable/$ARCHITECTURE/containerd.io_${VERSION}_$ARCHITECTURE.deb
wget https://download.docker.com/linux/ubuntu/dists/$UBUNTU_VERSION/pool/stable/$ARCHITECTURE/docker-ce_${VERSION}_$ARCHITECTURE.deb
wget https://download.docker.com/linux/ubuntu/dists/$UBUNTU_VERSION/pool/stable/$ARCHITECTURE/docker-ce-cli_${VERSION}_$ARCHITECTURE.deb
wget https://download.docker.com/linux/ubuntu/dists/$UBUNTU_VERSION/pool/stable/$ARCHITECTURE/docker-buildx-plugin_${VERSION}_$ARCHITECTURE.deb
wget https://download.docker.com/linux/ubuntu/dists/$UBUNTU_VERSION/pool/stable/$ARCHITECTURE/docker-compose-plugin_${VERSION}_$ARCHITECTURE.deb

# نصب فایل‌های .deb دانلود شده
sudo dpkg -i containerd.io_${VERSION}_$ARCHITECTURE.deb
sudo dpkg -i docker-ce_${VERSION}_$ARCHITECTURE.deb
sudo dpkg -i docker-ce-cli_${VERSION}_$ARCHITECTURE.deb
sudo dpkg -i docker-buildx-plugin_${VERSION}_$ARCHITECTURE.deb
sudo dpkg -i docker-compose-plugin_${VERSION}_$ARCHITECTURE.deb

# رفع مشکلات وابستگی‌ها
sudo apt-get install -f

# شروع Docker
sudo systemctl start docker

# فعال‌سازی خودکار Docker در هنگام بوت
sudo systemctl enable docker

# بررسی نصب Docker
docker --version

# نصب Docker Compose
docker compose version

