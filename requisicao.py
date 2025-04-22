import requests

dados = {
    "a": 10,
    "b": 20
}

response = requests.post("http://127.0.0.1:8000/soma", json=dados)

print(response.status_code)
print(response.json())

