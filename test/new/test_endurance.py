from locust import HttpUser, task, constant_pacing

class EnduranceTest(HttpUser):
    # کاربران هر 5 ثانیه یک درخواست ارسال می‌کنند
    wait_time = constant_pacing(5)

    @task
    def get_home_page(self):
        """تست استقامت با درخواست به صفحه اصلی"""
        response = self.client.get("/")
        if response.status_code == 200:
            print("Homepage loaded successfully.")
        else:
            print(f"Failed to load homepage, status code: {response.status_code}")

    @task
    def get_api_data(self):
        """تست استقامت با درخواست به API داده‌ها"""
        response = self.client.get("/api/data")
        if response.status_code == 200:
            print("API data fetched successfully.")
        else:
            print(f"Failed to fetch API data, status code: {response.status_code}")

    @task
    def post_data(self):
        """تست استقامت با ارسال درخواست POST به API"""
        payload = {"name": "Locust", "type": "EnduranceTest"}
        response = self.client.post("/api/submit", json=payload)
        if response.status_code == 200:
            print("Data posted successfully.")
        else:
            print(f"Failed to post data, status code: {response.status_code}")


# تست استقامت با هدف بررسی عملکرد سیستم در مدت زمان طولانی انجام می‌شود. این تست نشان می‌دهد که آیا سیستم تحت بارهای مداوم و طولانی به درستی عمل می‌کند یا خیر.

# wait_time = constant_pacing(5): این مشخص می‌کند که هر کاربر شبیه‌سازی‌شده هر 5 ثانیه یک درخواست ارسال می‌کند. در تست استقامت، هدف این است که با بار ثابت در مدت طولانی، پایایی سیستم بررسی شود.

# get_home_page: این متد برای تست بارگذاری صفحه اصلی استفاده می‌شود.

# get_api_data: این متد برای ارسال درخواست به یک API و دریافت داده‌ها استفاده می‌شود.

# post_data: این متد یک درخواست POST برای ارسال داده‌ها به API ارسال می‌کند.
