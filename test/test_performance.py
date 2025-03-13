from locust import HttpUser, task, between

class PerformanceTest(HttpUser):
    # زمان صبر بین هر درخواست، برای شبیه‌سازی رفتار کاربران واقعی
    wait_time = between(1, 3)  # هر کاربر بین 1 تا 3 ثانیه بین درخواست‌ها صبر می‌کند

    @task
    def get_home_page(self):
        """تست عملکرد با درخواست به صفحه اصلی"""
        response = self.client.get("/")
        if response.status_code == 200:
            print("Homepage loaded successfully.")
        else:
            print(f"Failed to load homepage, status code: {response.status_code}")

    @task
    def get_api_data(self):
        """تست عملکرد با درخواست به API داده‌ها"""
        response = self.client.get("/api/data")
        if response.status_code == 200:
            print("API data fetched successfully.")
        else:
            print(f"Failed to fetch API data, status code: {response.status_code}")

    @task
    def post_form(self):
        """تست عملکرد با ارسال داده به فرم (POST)"""
        payload = {"username": "test_user", "password": "test_password"}
        response = self.client.post("/login", json=payload)
        if response.status_code == 200:
            print("Login form submitted successfully.")
        else:
            print(f"Failed to submit login form, status code: {response.status_code}")

            
# هدف از تست عملکرد، بررسی زمان پاسخ‌دهی و توانایی سیستم برای مدیریت تعداد درخواست‌ها است. این تست بر روی زمان‌های پاسخ‌دهی و کارایی کلی سرور تمرکز دارد.

# wait_time = between(1, 3): این خط تنظیم می‌کند که هر کاربر شبیه‌سازی شده بین 1 تا 3 ثانیه بین درخواست‌ها صبر کند. این رفتار واقعی کاربران را شبیه‌سازی می‌کند و بار سنگین مداوم ایجاد نمی‌کند.

# get_home_page: این متد به صفحه اصلی (homepage) درخواست می‌فرستد تا زمان پاسخگویی صفحه اصلی را اندازه‌گیری کند.

# get_api_data: این متد برای ارسال درخواست به API داده‌ها و بررسی زمان پاسخ استفاده می‌شود.

# post_form: این متد یک درخواست POST به مسیر /login ارسال می‌کند تا رفتار سیستم در هنگام ارسال فرم و انجام عملیات ورود تست شود.