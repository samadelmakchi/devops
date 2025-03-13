from locust import HttpUser, task, between

class LoadTest(HttpUser):
    # کاربران هر 1 تا 5 ثانیه یک درخواست ارسال می‌کنند
    wait_time = between(1, 5)  # زمان انتظار بین درخواست‌های کاربر

    @task
    def get_home_page(self):
        """تست بارگذاری صفحه اصلی"""
        response = self.client.get("/")
        if response.status_code == 200:
            print("Homepage loaded successfully.")
        else:
            print(f"Failed to load homepage, status code: {response.status_code}")

    @task
    def get_api_data(self):
        """تست بارگذاری API داده‌ها"""
        response = self.client.get("/api/data")
        if response.status_code == 200:
            print("API data fetched successfully.")
        else:
            print(f"Failed to fetch API data, status code: {response.status_code}")

    @task
    def post_login(self):
        """تست بارگذاری فرم ورود (POST)"""
        payload = {"username": "test_user", "password": "test_password"}
        response = self.client.post("/login", json=payload)
        if response.status_code == 200:
            print("Login form submitted successfully.")
        else:
            print(f"Failed to submit login form, status code: {response.status_code}")

# در تست بار، عملکرد سیستم در بارهای معین (مثلاً تعداد مشخصی از کاربران) ارزیابی می‌شود. این تست به ما کمک می‌کند بفهمیم که سیستم در چه مقدار بار به درستی عمل می‌کند.

# wait_time = between(1, 5): هر کاربر شبیه‌سازی شده به صورت تصادفی بین 1 تا 5 ثانیه بین درخواست‌ها صبر می‌کند. این رفتار کمک می‌کند بار به طور مستمر و طبیعی روی سیستم اعمال شود.

# get_home_page: این متد برای تست بارگذاری صفحه اصلی و ارزیابی سرعت پاسخگویی استفاده می‌شود.

# get_api_data: این متد به یک API درخواست ارسال می‌کند تا بررسی شود که سیستم تحت بار قادر به پاسخگویی به درخواست‌ها است یا خیر.

# post_login: این متد یک درخواست POST برای فرم ورود به سیستم ارسال می‌کند تا عملکرد سیستم در ارسال فرم‌ها تست شود.
