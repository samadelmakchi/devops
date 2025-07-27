FROM selenium/node-base:4.19.1-20240506

USER root

# نصب Chromium و وابستگی‌ها
RUN apt-get update && \
    apt-get install -y chromium-browser chromium-driver && \
    ln -s /usr/bin/chromium-browser /usr/bin/chromium && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER seluser

