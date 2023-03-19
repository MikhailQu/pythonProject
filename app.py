from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from greenApi import GET, POST
import json
import os
from pathlib import Path

app: Flask = Flask(__name__)
api = Api()


@app.route("/")
def page_index():
    return "страничка для теста API"


def extrainData():
    parser = reqparse.RequestParser()
    parser.add_argument("apiTokenInstance", type=str)
    parser.add_argument("idInstance", type=str)
    parser.add_argument("contact", type=int)
    parser.add_argument("recipient", type=int)
    parser.add_argument("message", type=str)
    parser.add_argument("file", type=str)
    arg = parser.parse_args()
    id_instance = arg['idInstance']
    apiTokenInstance = arg["apiTokenInstance"]
    contact = arg["contact"]
    recipient = arg["recipient"]
    message = arg["message"]
    file = arg["file"]
    login = {"idInstance": str(id_instance),
             "apiTokenInstance": apiTokenInstance,
             "contact": contact,
             "recipient": recipient,
             "message": message,
             "file": file
             }
    return login


class Account(Resource):

    def get(self, request):
        if request == "ok":
            return jsonify({"Account": "request:ok___"})

        if request == "status":

            status = GET.status(extrainData())
            if status['message'] == "Аккаунт не авторизован":
                qr = GET.qr_code64(extrainData())
                return jsonify("request:status___", status, qr)
            else:
                return jsonify("request:status___", status['message'])

        if request == "me":
            me = GET.me(extrainData())
            return jsonify("request:me___", me)

        if request == "qr":
            qr = GET.qr_code64(extrainData())
            return jsonify("request:qr___", qr)

        if request == "logout":
            if GET.status(extrainData())['message'] != "Аккаунт авторизован":
                return jsonify("Аккаунт не авторизован или находится в сервисном режиме")
            else:
                logout = GET.logout(extrainData())
                return jsonify("выхожу из аккаунта", logout)

        else:
            return jsonify("Используйте /help для получения списка доступных запросов")


class Messenger(Resource):

    def post(self, request):
        if request == "ok":
            return jsonify({"Messenger": "request:ok___"})


        if request == "sendMessage" :
            if extrainData()['recipient'] is not None \
            and extrainData()["contact"] is not None:
                Message = POST.sendMessage(extrainData())
                a= str(extrainData()['message']), "send to ", str(extrainData()['recipient'])
                return json.dumps({"message": a[0:5]})
            else:
                return json.dumps({"message": "sendMessage(recipient, message, auth) - неверный аргумент  "})

        if request == "sendFile":
            return extrainData()['file']


api.add_resource(Account, "/app/account/<string:request>")
api.add_resource(Messenger, '/app/messenger/<string:request>')
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
