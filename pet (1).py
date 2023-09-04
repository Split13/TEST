import requests
import random
Names = ['Sharik', 'Boo', 'Candy']

id = "0"
url = 'https://petstore.swagger.io/v2/pet'
response = requests.post("https://petstore.swagger.io/v2/pet", json = {
    "id": 0,
    "category": {
    "id": 0,
    "name": Names[random.randint(0,2)]
  },
    "name": "doggie",
    "photoUrls": [
    "string"
  ],
    "tags": [
     {
      "id": 0,
      "name": "string"
     }
  ],
  "status": "available"
}

)

assert response.status_code == 200, "Код ответа не 200"
id = response.json()['id']
print(id)


response = requests.get("https://petstore.swagger.io/v2/pet/" + str(id))
assert response.status_code == 200, "Код ответа не 200"
print(response.json())


response = requests.delete("https://petstore.swagger.io/v2/pet/" + str(id))
assert response.status_code == 200, "Код ответа не 200"





id = "0"
url = 'https://petstore.swagger.io/v2/pet'
response = requests.post("https://petstore.swagger.io/v2/pet353", json = {
    "id": 0,
    "category": {
    "id": 0,
    "name": Names[random.randint(0,2)]
  },
    "name": "doggie",
    "photoUrls": [
    "string"
  ],
    "tags": [
     {
      "id": 0,
      "name": "string"
     }
  ],
  "status": "available"
}

)

try:
 if response.status_code == 200:
    id = response.json()['id']
    print(response.status_code)
 else:
    print("Ошибка Post: Код ответа не 200")
except AssertionError as e:
    print("Ошибка Post: Код ответа не 200")


response = requests.get("https://petstore.swagger.io/v2/pet/" + str(id))
try:
 if response.status_code == 200:
    id = response.json()['id']
    print(response.status_code)
 else:
    print("Ошибка Get: Код ответа не 200")
except AssertionError as e:
    print("Ошибка Post: Код ответа не 200")




response = requests.delete("https://petstore.swagger.io/v2/pet45/" + str(id))
try:
 if response.status_code == 200:
    id = response.json()['id']
    print(response.status_code)
 else:
    print("Ошибка Delete: Код ответа не 200")
except AssertionError as e:
    print("Ошибка Post: Код ответа не 200")