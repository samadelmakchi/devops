FROM selenium/node-chrome:4.19.1

USER root

# نصب Vivaldi
RUN wget -qO- https://downloads.vivaldi.com/stable/vivaldi-stable_6.7.3329.29-1_amd64.deb > vivaldi.deb && \
    apt-get update && apt-get install -y ./vivaldi.deb && \
    rm vivaldi.deb

ENV SE_BROWSER_NAME=vivaldi
ENV SE_BROWSER_BINARY=/usr/bin/vivaldi

USER seluser

