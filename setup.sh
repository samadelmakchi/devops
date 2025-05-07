#!/bin/bash

# فقط اگر فایل اصلی وجود ندارد، از فایل نمونه کپی کن
if [ ! -f inventory.local.yml ]; then
  cp inventory.yml inventory.local.yml
  echo "✔️  Created inventory.local.yml from template"
else
  echo "⚠️  inventory.local.yml already exists. Skipping."
fi

if [ ! -f inventory-server.local.yml ]; then
  cp inventory-server.yml inventory-server.local.yml
  echo "✔️  Created inventory-server.local.yml from template"
else
  echo "⚠️  inventory-server.local.yml already exists. Skipping."
fi
