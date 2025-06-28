import subprocess

# تنظیمات ZAP
ZAP_PATH = "/path/to/zap.sh"  # مسیر نصب OWASP ZAP
TARGET_URL = "http://example.com"  # آدرس وبسایتی که قصد دارید تست امنیتی انجام دهید
REPORT_FILE = "zap_baseline_report.html"  # نام فایل گزارش

# پارامترهای اسکن
BASELINE_CMD = [
    ZAP_PATH,
    "-daemon",  # اجرای ZAP به صورت پس‌زمینه
    "-quickurl", TARGET_URL,  # اسکن سریع برای آدرس مشخص‌شده
    "-quickout", REPORT_FILE,  # خروجی فایل گزارش
    "-quickprogress",  # نمایش پیشرفت اسکن
    "-cmd",  # اجرای دستورات به صورت خط فرمان
]

# اجرای دستور baseline scan با استفاده از subprocess
def run_zap_baseline_scan():
    print(f"Starting ZAP baseline scan for {TARGET_URL}...")
    result = subprocess.run(BASELINE_CMD, capture_output=True, text=True)

    # بررسی نتیجه اجرای اسکن
    if result.returncode == 0:
        print("ZAP baseline scan completed successfully!")
    else:
        print("ZAP baseline scan failed!")
        print(f"Error: {result.stderr}")
    
    # چاپ گزارش
    print(f"Report saved to {REPORT_FILE}")

if __name__ == "__main__":
    run_zap_baseline_scan()


# ZAP_PATH: مسیر فایل اجرایی OWASP ZAP را مشخص می‌کند. اگر ZAP در مسیر نصب شده است، باید آن را تنظیم کنید (مثلاً /usr/share/zap/zap.sh).

# TARGET_URL: آدرس هدف وبسایتی است که می‌خواهید تست امنیتی انجام دهید. این می‌تواند آدرس لوکال‌هاست یا آدرس یک وبسایت خارجی باشد.

# REPORT_FILE: نام فایل HTML خروجی که شامل گزارش اسکن است.

# BASELINE_CMD: پارامترهای لازم برای اجرای ZAP به صورت خط فرمان. این پارامترها شامل مواردی است که OWASP ZAP به آن نیاز دارد، از جمله آدرس هدف، نوع اسکن، و نام فایل گزارش.

# subprocess.run(): از این تابع برای اجرای دستور در خط فرمان استفاده می‌شود و نتایج اجرای اسکن را بررسی می‌کند.
