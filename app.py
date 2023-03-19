from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from greenApi import GET
import json

app: Flask = Flask(__name__)
api = Api()

@app.route("/")
def page_index():
    return "страничка для теста API"

def extrainLoginData():
    parser = reqparse.RequestParser()
    parser.add_argument("apiTokenInstanse", type=str)
    parser.add_argument("id_instanse", type=int)
    parser.add_argument("contact", type=int)
    argum = parser.parse_args()
    id_instanse = argum['id_instanse']
    apiTokenInstanse = argum["apiTokenInstanse"]
    contact = argum["contact"]
    login = {"id_instanse": str(id_instanse), "apiTokenInstanse": apiTokenInstanse, "contact": contact}
    return login


class Account(Resource):

    def get(self, request):
        if request == "ok":
            return jsonify("request:ok___")


        if request == "status":

            status = GET.status(extrainLoginData())
            if status['message'] == "Аккаунт не авторизован":
                qr = GET.qr_code64(extrainLoginData())
                return jsonify("request:status___", status, qr)
            else:
                return jsonify("request:status___", status['message'])


        if request == "me":
            me = GET.me(extrainLoginData())
            return jsonify("request:me___", me)

        if request == "qr":
            qr = GET.qr_code64(extrainLoginData())
            return jsonify("request:qr___", qr)


        if request == "logout" and GET.status(extrainLoginData())['message'] != "Аккаунт авторизован":
            return jsonify("Аккаунт не авторизован или находится в сервисном режиме")
        else:
            logout = GET.logout(extrainLoginData())
            return jsonify("выхожу из аккаунта", logout)

api.add_resource(Account, '/app/account/<string:request>')
api.init_app(app)

class Messenger(Resource):

    def post(self, request):
        return


api.add_resource(Messenger, '/app/messenger/<string:request>')
api.init_app(app)





if __name__ == "__main__":
    app.run(debug=True)
