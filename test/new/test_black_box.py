import requests

def test_black_box():
    response = requests.get("http://localhost:8000/api/endpoint")
    assert response.status_code == 200, "Endpoint failed"
    assert response.json()["result"] == "expected_result", "Unexpected output in black box test"

