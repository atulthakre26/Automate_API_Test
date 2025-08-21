import requests

# GET request
head = {
    'Accept': 'application/json'
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/2", headers=head)

print(response.status_code)
print(response.json())
assert response.status_code == 200

# PUT request
headerPut = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

requests_payloadPut = {
    "id": 5,
    "title": "Atul Bhau",
    "dueDate": "2025-08-21T08:14:06.817Z",
    "completed": True
}

response = requests.put(
    "https://fakerestapi.azurewebsites.net/api/v1/Activities/5",  # ✅ specify the ID
    headers=headerPut,
    json=requests_payloadPut
)

print(response.status_code)
print(response.json())

assert response.status_code == 200
