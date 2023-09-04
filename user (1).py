import requests

headers = {"W-Token": "Users"}
data = [
    {
    "id": 0,
    "username": "user1",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
    }
  
]
response = requests.post("https://petstore.swagger.io/v2/user/createWithList", json=data, headers=headers)
assert response.status_code == 200, "Response code is not 200"
print(response.json())

response = requests.get("https://petstore.swagger.io/v2/user/user1")
assert response.status_code == 200, "Response code is not 200"
print(response.json())


response = requests.delete("https://petstore.swagger.io/v2/user/user1")
assert response.status_code == 200, "Response code is not 200"






headers = {"W-Token": "Users"}
data = [
        {
        "id": 7999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999990,
        "username": "user1",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
        }
    ]

response = requests.post("https://petstore.swagger.io/v2/user/createWithList", json=data, headers=headers)
try:
 if response.status_code == 200:
    id = response.json()['id']
    print(response.status_code)
 else:
    print("Ошибка Post: Код ответа не 200")
except AssertionError as e:
    print("Ошибка Get: Код ответа не 200")



response = requests.get("https://petstore.swagger.io/v2/user/1user")
try:
 if response.status_code == 200:
    id = response.json()['id']
    print(response.status_code)
 else:
    print("Ошибка Get: Код ответа не 200")
except AssertionError as e:
    print("Ошибка Get: Код ответа не 200")



response = requests.delete("https://petstore.swagger.io/v2/user/us12er")
try:
 if response.status_code == 200:
    id = response.json()['id']
    print(response.status_code)
 else:
    print("Ошибка Delete: Код ответа не 200")
except AssertionError as e:
    print("Ошибка Get: Код ответа не 200")
