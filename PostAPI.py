import requests

header = {

   'Accept' : 'text/plain',
   'Content-Type' : 'application/json'

}

requests_payload = {

     "id": 151,
     "title": "Atul Testing",
     "dueDate": "2025-08-21T07:27:44.923Z",
     "completed": True
}

response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", headers=header, json=requests_payload)

print(response.status_code)
print(response.json())

data = response.json()
print(data['title'])

assert response.status_code == 200
assert data['id'] == 151

