import requests
import json
import time

url = "http://127.0.0.1:5000/app/get/status"
headers = {"Content-Type": "application/json"}
data = {
    "idInstance": "1101799607",
    "apiTokenInstance": "056a7216d44740f696c3fd46a73711e6b695827c1cde46ce99",
    "contact": "79100767686"
}
data = json.dumps(data)



res = requests.get("http://127.0.0.1:5000/app/account/me", headers=headers, data=data)
time.sleep(0.5)
print(res.json())


res = requests.get("http://127.0.0.1:5000/app/account/status", headers=headers, data=data)
time.sleep(0.5)
print(res.json())

res = requests.get("http://127.0.0.1:5000/app/account/qr", headers=headers, data=data)
time.sleep(0.5)
print(res.json())



'''
res = requests.get("http://127.0.0.1:5000/app/account/logout", headers=headers, data=data)
time.sleep(0.5)
print(res.json())

'''