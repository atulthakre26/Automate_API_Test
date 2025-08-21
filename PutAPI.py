import requests

header = {
    'Accept' : 'text/plain',
    'Content-Type' : 'application/json'
}

requests_payload = {
  "id": 5,
  "title": "Atul Bhau",
  "dueDate": "2025-08-21T08:14:06.817Z",
  "completed": True
}

response = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/4", headers=header, json=requests_payload)

print(response.status_code)
print(response.json())

assert response.status_code == 200