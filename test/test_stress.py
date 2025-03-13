from locust import HttpUser, task, constant_pacing

class StressTest(HttpUser):
    # ارسال درخواست‌ها بدون توقف (با یک تاخیر ثابت)
    wait_time = constant_pacing(1)  # کاربران هر 1 ثانیه یک درخواست ارسال می‌کنند

    @task
    def get_home_page(self):
        """تست فشار با درخواست به صفحه اصلی"""
        response = self.client.get("/")
        if response.status_code == 200:
            print("Homepage loaded successfully.")
        else:
            print(f"Failed to load homepage, status code: {response.status_code}")

    @task
    def get_api_data(self):
        """تست فشار با درخواست به API داده‌ها"""
        response = self.client.get("/api/data")
        if response.status_code == 200:
            print("API data fetched successfully.")
        else:
            print(f"Failed to fetch API data, status code: {response.status_code}")

    @task
    def post_form(self):
        """تست فشار با ارسال درخواست POST به فرم ورود"""
        payload = {"username": "stress_user", "password": "stress_password"}
        response = self.client.post("/login", json=payload)
        if response.status_code == 200:
            print("Login form submitted successfully.")
        else:
            print(f"Failed to submit login form, status code: {response.status_code}")


# تست فشار برای بررسی میزان تحمل سیستم در برابر بارهای سنگین و فراتر از ظرفیت معمول استفاده می‌شود. هدف این تست بررسی نقطه‌ی شکست سیستم است.

# wait_time = constant_pacing(1): کاربران شبیه‌سازی شده هر 1 ثانیه یک درخواست ارسال می‌کنند. در تست فشار، هدف این است که بار بسیار سنگین و بدون توقف روی سیستم اعمال شود تا سیستم به نقطه شکست برسد.

# get_home_page: درخواست به صفحه اصلی ارسال می‌شود تا بررسی شود که تحت بار زیاد، آیا سیستم می‌تواند به درخواست‌ها پاسخ دهد.

# get_api_data: درخواست برای گرفتن داده‌ها از API انجام می‌شود تا توانایی سیستم در پاسخگویی به درخواست‌های API بررسی شود.

# post_form: درخواست POST به مسیر ورود ارسال می‌شود تا رفتار سیستم در زمان ارسال فرم‌ها تحت بار شدید ارزیابی شود.
