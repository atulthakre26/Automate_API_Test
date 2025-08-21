import pytest
import requests

def test_getrequest_validation():
    head = {
        'Content-Type' : 'application/json'
    }

    response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=head)

    print(response.status_code)
    print(response.json())

    assert response.status_code == 200

