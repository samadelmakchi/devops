FROM selenium/node-chrome:4.19.1

USER root

# نصب Brave با روش جدید (مطابق با تغییرات رسمی)
RUN apt-get update && \
    apt-get install -y curl gnupg apt-transport-https && \
    curl -fsSL https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg | gpg --dearmor -o /usr/share/keyrings/brave-browser-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" > /etc/apt/sources.list.d/brave-browser-release.list && \
    apt-get update && \
    apt-get install -y brave-browser && \
    rm -rf /var/lib/apt/lists/*

USER seluser
