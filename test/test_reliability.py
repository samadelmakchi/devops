import requests

def test_service_reliability():
    for _ in range(1000):  # تست ۱۰۰۰ درخواست متوالی
        response = requests.get("http://localhost:8000/api/status")
        assert response.status_code == 200, "Service reliability test failed"

