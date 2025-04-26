#!/bin/bash

# شناسایی نسخه اوبونتو و معماری
UBUNTU_VERSION=$(lsb_release -cs)
ARCHITECTURE=$(dpkg --print-architecture)

echo "✅ شناسایی شد: نسخه اوبونتو شما '$UBUNTU_VERSION' و معماری '$ARCHITECTURE' است."

if [[ "$UBUNTU_VERSION" == "focal" && "$ARCHITECTURE" == "amd64" ]]; then

    DOWNLOAD_DIR="docker"
    mkdir -p "$DOWNLOAD_DIR"

    FILES=(
        "containerd.io_1.7.27-1_amd64.deb"
        "docker-ce_28.1.1-1~ubuntu.20.04~focal_amd64.deb"
        "docker-ce-cli_28.1.1-1~ubuntu.20.04~focal_amd64.deb"
        "docker-buildx-plugin_0.23.0-1~ubuntu.20.04~focal_amd64.deb"
        "docker-compose-plugin_2.6.0~ubuntu-focal_amd64.deb"
    )

    BASE_URL="https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64"

    for FILE in "${FILES[@]}"; do
        if [ ! -f "$DOWNLOAD_DIR/$FILE" ]; then
            echo "🔽 در حال دانلود $FILE ..."
            wget -O "$DOWNLOAD_DIR/$FILE" "$BASE_URL/$FILE"
        else
            echo "✅ $FILE قبلاً دانلود شده، رد شد."
        fi
    done

    sudo dpkg -i "$DOWNLOAD_DIR/"*.deb

elif [[ "$UBUNTU_VERSION" == "bionic" && "$ARCHITECTURE" == "amd64" ]]; then
    echo "✅ اوبونتو bionic و معماری amd64 شناسایی شد. (کد این قسمت کامل نشده)"
else
    echo "❌ نسخه یا معماری شناسایی شده پشتیبانی نمی‌شود."
    exit 1
fi

# رفع مشکلات احتمالی وابستگی‌ها
sudo apt-get install -f -y

# شروع و فعال سازی Docker
sudo systemctl start docker
sudo systemctl enable docker

# بررسی نسخه‌های نصب شده
docker --version
docker compose version

# تنظیم Docker برای ArvanCloud
echo "⚙️ تنظیم ArvanCloud Mirror برای Docker..."

sudo mkdir -p /etc/docker

sudo tee /etc/docker/daemon.json > /dev/null <<EOF
{
  "insecure-registries" : ["https://docker.arvancloud.ir"],
  "registry-mirrors": ["https://docker.arvancloud.ir"]
}
EOF

docker logout
sudo systemctl restart docker
