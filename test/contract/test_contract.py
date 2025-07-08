from pact import Consumer, Provider
import pytest
import requests

pact = Consumer("Client").has_pact_with(Provider("API"), pact_file_write_mode="merge")

@pytest.mark.pact
def test_api_contract():
    pact.given("A user exists with ID 1").upon_receiving("A request for user data").with_request(
        method="GET", path="/users/1"
    ).will_respond_with(
        status=200,
        body={"id": 1, "name": "Test User"}
    )

    with pact:
        response = requests.get(pact.uri + "/users/1")
        assert response.status_code == 200
        assert response.json() == {"id": 1, "name": "Test User"}