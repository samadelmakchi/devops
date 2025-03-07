#!/bin/bash

# این اسکریپت برای گرفتن بکاپ از ولوم‌ها و ذخیره آن در پوشه خاص مشتری است.

# مسیر بکاپ
BACKUP_DIR="/opt/backup/{{ inventory_hostname }}/$(date +'%Y-%m-%d')"
mkdir -p $BACKUP_DIR  # ایجاد پوشه برای بکاپ

# گرفتن لیست از ولوم‌ها
VOLUMES=$(docker volume ls -q)

# فایل گزارش
BACKUP_LOG="$BACKUP_DIR/backup_log.txt"
echo "Backup started at $(date)" >> $BACKUP_LOG

# بکاپ از هر ولوم
for VOLUME in $VOLUMES; do
  docker run --rm -v $VOLUME:/volume -v $BACKUP_DIR:/backup alpine \
    tar czf /backup/$VOLUME.tar.gz -C /volume .  # فشرده‌سازی و ذخیره بکاپ
  echo "Backup for $VOLUME completed at $(date)" >> $BACKUP_LOG
done

echo "Backup completed at $(date)" >> $BACKUP_LOG
