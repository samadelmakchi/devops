FROM selenium/node-chrome:4.19.1

USER root

# نصب Node.js و Electron
RUN apt-get update && apt-get install -y curl gnupg && \
    curl -sL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g electron

ENV SE_BROWSER_NAME=electron
ENV SE_BROWSER_BINARY=/usr/local/bin/electron

USER seluser

