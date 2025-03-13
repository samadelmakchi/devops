import requests

# تست ادغام دو ماژول (مثال: سفارش و پرداخت)
def test_order_and_payment_integration():
    order_data = {"item": "book", "quantity": 2}
    order_response = requests.post("http://localhost:8000/api/order", json=order_data)
    assert order_response.status_code == 200, "Order creation failed"
    order_id = order_response.json().get("order_id")

    payment_data = {"order_id": order_id, "amount": 50}
    payment_response = requests.post("http://localhost:8000/api/payment", json=payment_data)
    assert payment_response.status_code == 200, "Payment processing failed"
    assert payment_response.json().get("status") == "success", "Payment not successful"

