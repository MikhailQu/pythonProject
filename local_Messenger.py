from pathlib import Path
import requests
import json
import time

#file = json.loads(open("test.bin","r"))
url = "http://127.0.0.1:5000/app/get/status"
headers = {"Content-Type": "application/json"}
data = {
    "idInstance": "1101799607",
    "apiTokenInstance": "056a7216d44740f696c3fd46a73711e6b695827c1cde46ce99",
    "contact": "79100767686",
    "recipient": "79207559006",
    "message": "this is test message.",
    "file": "file",
    "link": "http://host10999999.pro.host1855377.serv80.hostland.pro/?page_id=5",
    "sendContact": str({"phoneContact": "79001234568", "firstName": "Артем", "middleName": "Петрович", "lastName": "Евпаторийский", "company": "Велосипед"}),

      }
data = json.dumps(data)



res = requests.post("http://127.0.0.1:5000/app/messenger/sendFile", headers=headers, data=data)
time.sleep(0.5)
print(res.json())

res = requests.post("http://127.0.0.1:5000/app/messenger/sendMessage", headers=headers, data=data)
time.sleep(0.5)
print(res.json())

res = requests.post("http://127.0.0.1:5000/app/messenger/sendContact", headers=headers, data=data)
time.sleep(0.5)
print(res.json())

res = requests.post("http://127.0.0.1:5000/app/messenger/sendLink", headers=headers, data=data)
time.sleep(0.5)
print(res.json())

'''
'''