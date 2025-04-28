#!/bin/bash

# شناسایی نسخه اوبونتو و معماری
UBUNTU_VERSION=$(lsb_release -cs)
ARCHITECTURE=$(dpkg --print-architecture)

echo "✅ شناسایی شد: نسخه اوبونتو شما '$UBUNTU_VERSION' و معماری '$ARCHITECTURE' است."

DOWNLOAD_DIR="docker"
mkdir -p "$DOWNLOAD_DIR"

FILES=(
    "containerd.io_1.7.27-1_amd64.deb"
    "docker-ce_28.1.1-1~ubuntu.20.04~$UBUNTU_VERSION_$ARCHITECTURE.deb"
    "docker-ce-cli_28.1.1-1~ubuntu.20.04~$UBUNTU_VERSION_$ARCHITECTURE.deb"
    "docker-buildx-plugin_0.23.0-1~ubuntu.20.04~$UBUNTU_VERSION_$ARCHITECTURE.deb"
    "docker-compose-plugin_2.6.0~ubuntu-$UBUNTU_VERSION_$ARCHITECTURE.deb"
)

BASE_URL="https://download.docker.com/linux/ubuntu/dists/$UBUNTU_VERSION/pool/stable/$ARCHITECTURE"

for FILE in "${FILES[@]}"; do
    if [ ! -f "$DOWNLOAD_DIR/$FILE" ]; then
        echo "🔽 در حال دانلود $FILE ..."
        wget -O "$DOWNLOAD_DIR/$FILE" "$BASE_URL/$FILE"
    else
        echo "✅ $FILE قبلاً دانلود شده، رد شد."
    fi
done

sudo dpkg -i "$DOWNLOAD_DIR/"*.deb

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
