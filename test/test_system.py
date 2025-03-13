import requests

def test_system_endpoints():
    endpoints = [
        "http://localhost:8000/api/users",
        "http://localhost:8000/api/products",
        "http://localhost:8000/api/orders"
    ]

    for endpoint in endpoints:
        response = requests.get(endpoint)
        assert response.status_code == 200, f"System endpoint {endpoint} failed"

