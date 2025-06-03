FROM selenium/node-chrome:4.19.1

USER root

# نصب Opera از آدرس مستقیم
RUN apt-get update && \
    apt-get install -y wget gnupg2 software-properties-common && \
    wget -qO- https://deb.opera.com/archive.key | apt-key add - && \
    add-apt-repository "deb https://deb.opera.com/opera-stable/ stable non-free" && \
    apt-get update && \
    apt-get install -y opera-stable && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER seluser

