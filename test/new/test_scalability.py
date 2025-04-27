from locust import HttpUser, task, between, constant_pacing

class ScalabilityTest(HttpUser):
    # زمان انتظار بین درخواست‌های کاربران، که می‌تواند متغیر یا ثابت باشد
    wait_time = constant_pacing(1)  # هر کاربر هر 1 ثانیه یک درخواست ارسال می‌کند

    @task
    def test_add(self):
        """ارسال درخواست به /api/add"""
        response = self.client.get("/api/add", params={"a": 10, "b": 20})
        if response.status_code == 200:
            print("Response (Add):", response.json())

    @task
    def test_subtract(self):
        """ارسال درخواست به /api/subtract"""
        response = self.client.get("/api/subtract", params={"a": 30, "b": 10})
        if response.status_code == 200:
            print("Response (Subtract):", response.json())

    # شبیه‌سازی تعداد کاربران در حالت افزایش تدریجی
    @task
    def load_increasing_users(self):
        """افزایش تدریجی تعداد کاربران برای تست مقیاس‌پذیری"""
        for i in range(1, 1001, 100):
            print(f"Testing with {i} users")


# تست مقیاس‌پذیری با هدف ارزیابی اینکه چگونه سیستم با افزایش تدریجی تعداد کاربران یا درخواست‌ها سازگار می‌شود، انجام می‌شود. در این تست، تعداد کاربران به تدریج افزایش می‌یابد.

# HttpUser: این کلاس کاربران را شبیه‌سازی می‌کند که درخواست‌های HTTP به سرور ارسال می‌کنند.

# wait_time = constant_pacing(1): در اینجا زمان صبر بین درخواست‌ها ثابت و یک ثانیه است، به طوری که هر کاربر هر 1 ثانیه یک درخواست ارسال می‌کند. می‌توانید آن را تغییر دهید یا از between استفاده کنید تا زمان انتظار متغیر باشد.

# test_add و test_subtract: هر کدام وظیفه ارسال درخواست GET به یک endpoint مشخص را دارند.

# load_increasing_users: این متد کاربران شبیه‌سازی‌شده را به تدریج افزایش می‌دهد تا مشاهده شود سیستم چگونه با افزایش تعداد کاربران سازگار می‌شود. این متد صرفاً برای نمایش یک الگو از کاربران افزایش‌یافته است.
