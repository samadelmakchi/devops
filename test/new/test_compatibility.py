import requests

def test_browser_compatibility():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get("http://localhost:8000", headers=headers)
    assert response.status_code == 200, "Browser compatibility test failed"

def test_mobile_compatibility():
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X)"
    }
    response = requests.get("http://localhost:8000", headers=headers)
    assert response.status_code == 200, "Mobile compatibility test failed"

