import requests

# تست بررسی دسترسی به صفحه اصلی
def test_homepage_is_accessible():
    response = requests.get("http://localhost:8000")  # آدرس پایه وب‌سایت یا سرویس شما
    assert response.status_code == 200, "Homepage is not accessible"

# تست بررسی دسترسی به صفحه ورود
def test_login_page_is_accessible():
    response = requests.get("http://localhost:8000/login")  # آدرس صفحه ورود
    assert response.status_code == 200, "Login page is not accessible"

# تست بررسی عملکرد یک API
def test_api_health_check():
    response = requests.get("http://localhost:8000/api/health")  # آدرس API چک سلامت
    assert response.status_code == 200, "API health check failed"
    assert response.json()["status"] == "ok", "API is not healthy"

# تست عملکرد پایگاه داده (تست سریع)
def test_database_connection():
    # فرض کنید یک نقطه endpoint برای بررسی اتصال به دیتابیس دارید
    response = requests.get("http://localhost:8000/api/db_check")
    assert response.status_code == 200, "Database connection failed"
    assert response.json()["db_status"] == "connected", "Database is not connected"

# تست بررسی عملکرد لاگین (سمت سرور)
def test_login_functionality():
    data = {"username": "test_user", "password": "test_password"}
    response = requests.post("http://localhost:8000/login", json=data)
    assert response.status_code == 200, "Login failed"
    assert "token" in response.json(), "Login token not found"

# تست ساده برای بررسی بخش مدیریت
def test_admin_panel_access():
    response = requests.get("http://localhost:8000/admin")
    assert response.status_code == 302, "Admin panel not redirecting for unauthenticated users"


