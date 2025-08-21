import requests

para = {
    'page' : 1,
    'per_page' : 10
}

response = requests.get("https://gorest.co.in/public/v2/users", params= para)

print(response.status_code)
print(response.json())

assert response.status_code == 200