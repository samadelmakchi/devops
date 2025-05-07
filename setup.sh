#!/bin/bash

# فقط اگر فایل اصلی وجود ندارد، از فایل نمونه کپی کن
if [ ! -f inventory.yml ]; then
  cp inventory.yml.tmp inventory.yml
  echo "✔️  Created inventory.yml from template"
else
  echo "⚠️  inventory.yml already exists. Skipping."
fi

if [ ! -f inventory-server.yml ]; then
  cp inventory-server.yml.tmp inventory-server.yml
  echo "✔️  Created inventory-server.yml from template"
else
  echo "⚠️  inventory-server.yml already exists. Skipping."
fi
