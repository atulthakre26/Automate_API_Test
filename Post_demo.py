import requests

headers = {
    "Content-Type": "application/json"
}

payload = {
    "name": "Atul Thakre",
    "job": "Software Developer"
}

response = requests.post("https://reqres.in/api/users", headers= headers, json=payload)

print(response.status_code)
print(response.text)
