# Fluentd

**Fluentd** یک پلتفرم منبع باز است که برای جمع‌آوری، پردازش و ارسال لاگ‌ها و داده‌ها از منابع مختلف به مقاصد مختلف طراحی شده است. این ابزار به‌ویژه در محیط‌های توزیع‌شده و کانتینری شده مانند Docker و Kubernetes کاربرد فراوانی دارد. Fluentd از معماری پلاگینی بهره می‌برد که به کاربران امکان می‌دهد تا انواع مختلفی از ورودی‌ها (مثل فایل‌ها، پایگاه داده‌ها، سرویس‌های وب و...) و خروجی‌ها (مثل Elasticsearch، Amazon S3، Google Cloud Storage، و غیره) را پیکربندی کنند. با استفاده از قابلیت‌هایی مانند پردازش داده‌های در حال حرکت، فیلتر کردن، تبدیل و تجزیه و تحلیل داده‌ها، Fluentd به سازمان‌ها کمک می‌کند تا جریان‌های لاگ و داده‌های خود را به شکلی مؤثرتر مدیریت کنند و از آن‌ها در جهت نظارت، هشدار و تجزیه و تحلیل‌های بیشتر استفاده نمایند.

### نحوه استفاده در PHP
```php
$ch = curl_init('http://localhost:24224/myapp.test');
$data = json_encode(['message' => 'Hello from PHP!', 'level' => 'info']);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
curl_exec($ch);
curl_close($ch);
```

### نحوه استفاده در Python
```bash
pip install fluent-logger
```
```python
from fluent import sender, event
logger = sender.FluentSender('myapp')
logger.emit('test', {'message': 'Hello from Python!', 'level': 'info'})
```

### نحوه استفاده در React / Vue
```javascript
fetch('http://localhost:24224/myapp.test', {
  method: 'POST',
  body: JSON.stringify({ message: 'Hello from Frontend!', level: 'info' }),
  headers: { 'Content-Type': 'application/json' }
});
```

## اسکرین شات

در زیر یک تصویر از رابط کاربری Fluentd آورده شده است:

![Screenshot](screenshot.png)

### جهت اجرای Fluentd با استفاده از Docker Compose، دستور زیر را وارد کنید:

```bash
sudo docker compose up -d
```


