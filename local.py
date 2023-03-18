import requests
import json
import time

url = "http://127.0.0.1:5000/app/get/status"
headers = {"Content-Type": "application/json"}
data = {
    "id_instanse": "1101799607",
    "apiTokenInstanse": "056a7216d44740f696c3fd46a73711e6b695827c1cde46ce99",
    "contact": "79100767686"
}
data = json.dumps(data)

res = requests.get("https://jolly-phoenix-915d16.netlify.app/get/me")
time.sleep(0.5)
print(res.json())
'''

res = requests.get("http://127.0.0.1:5000/app/get/qr", headers=headers, data=data)
time.sleep(0.5)
print(res.json())

res = requests.get("http://127.0.0.1:5000/app/get/status", headers=headers, data=data)
time.sleep(0.5)
print(res.json())





res = requests.get("http://127.0.0.1:5000/app/get/logout", headers=headers, data=data)
time.sleep(0.5)
print(res.json())

res = requests.post(url, headers=headers, json=data)
time.sleep(0.5)
print(res.json())

res = requests.get("http://127.0.0.1:5000/app/db/0")
time.sleep(0.5)
print(res.json())
'''