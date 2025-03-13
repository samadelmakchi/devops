import requests

def test_database_migration():
    # ارسال درخواست به endpoint برای اجرای مهاجرت دیتابیس
    response = requests.post("http://localhost:8000/api/migrate")
    assert response.status_code == 200, "Migration failed"
    assert response.json()["status"] == "migration successful", "Migration not successful"

