import requests
import random

id = "0"
url = 'https://petstore.swagger.io/v2/store/order'
response = requests.post("https://petstore.swagger.io/v2/store/order", json = {
            "id": f"{random.randint(1,10)}",
            "petId": 0,
            "quantity": 0,
            "shipDate": "2023-09-01T13:12:52.652Z",
            "status": "placed",
            "complete": "true"

    }

)

assert response.status_code == 200, "Код ответа не 200"
id = response.json()['id']
print(id)


response = requests.get("https://petstore.swagger.io/v2/store/order/" + str(id))
assert response.status_code == 200, "Код ответа не 200"
print(response.json())


response = requests.delete("https://petstore.swagger.io/v2/store/order/" + str(id))                  
assert response.status_code == 200, "Код ответа не 200"







id = "0"
url = 'https://petstore.swagger.io/v2/store/order'
response = requests.post("https://petstore.swagger.io/v2/store/order43", json = {
            "id": f"{random.randint(1,10)}",
            "petId": 0,
            "quantity": 0,
            "shipDate": "2023-09-01T13:12:52.652Z",
            "status": "placed",
            "complete": "true"

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



response = requests.get("https://petstore.swagger.io/v2/store/order/" + str(id))
try:
 if response.status_code == 200:
    id = response.json()['id']
    print(response.status_code)
 else:
    print("Ошибка Get: Код ответа не 200")
except AssertionError as e:
    print("Ошибка Get: Код ответа не 200")



response = requests.delete("https://petstore.swagger.io/v2/store/order/" + str(id))
try:
 if response.status_code == 200:
    id = response.json()['id']
    print(response.status_code)
 else:
    print("Ошибка Delete: Код ответа не 200")
except AssertionError as e:
    print("Ошибка Delete: Код ответа не 200")

