import requests

def test_recovery_after_failure():
    # شبیه‌سازی یک خرابی
    requests.post("http://localhost:8000/api/trigger_failure")

    # بازیابی سیستم
    recovery_response = requests.post("http://localhost:8000/api/recover")
    assert recovery_response.status_code == 200, "Recovery failed"
    assert recovery_response.json()["status"] == "recovered", "System did not recover successfully"

