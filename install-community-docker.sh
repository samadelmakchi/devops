#!/bin/bash

# نصب مجموعه مورد نیاز
ansible-galaxy collection install community.docker

# اجرای پلی‌بوک اصلی
ansible-playbook playbook-server.yml -i inventory-server.yml
