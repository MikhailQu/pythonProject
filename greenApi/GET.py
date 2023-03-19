from whatsapp_api_client_python import API
import json




def status(loginData):
    res =API.GreenApi(loginData["idInstance"], loginData["apiTokenInstance"]).account.getStateInstance()
    if res.data['stateInstance'] == "authorized":
        res.data['message'] = "Аккаунт авторизован"
        print(res.data)
        return (res.data)

    elif res.data['stateInstance'] == "blocked":
        res.data['message'] = "Аккаунт забанен"
        print(res.data)
        return (res.data)

    elif res.data['stateInstance'] == 'sleepMode':
        res.data['message'] = "Аккаунт ушел в спящий режим. Состояние возможно, когда выключен телефон."
        print(res.data)
        return (res.data)

    elif res.data['stateInstance'] == "starting":
        res.data['message'] = "Аккаунт в процессе запуска (сервисный режим)."
        print(res.data)
        return (res.data)

    elif res.data['stateInstance'] == "notAuthorized":
        res.data['message'] = "Аккаунт не авторизован"
        print(res.data)
        return (res.data)


    else:
        res.data['message'] = "что то не так"
        print(res.data)
        return (res.data)


def qr_code64(loginData):
    if API.GreenApi(loginData["idInstance"], loginData["apiTokenInstance"]).account.getStateInstance().data[
        'stateInstance'] == "notAuthorized":
        qr_code64 = API.GreenApi(loginData["id_instance"], loginData["apiTokenInstance"]).account.qr()
        # print("qr:", qr_code64.data)
        return (qr_code64.data)
    else:
        reply = {"message": "to get a QR code, log out of your account or contact the administrator"}
        print(reply)
        return json.dumps(reply)


def logout(loginData):
    res = API.GreenApi(loginData["idInstance"], loginData["apiTokenInstance"]).account.logout()
    res.data['message'] = "выход из аккаунта"
    print(res.data)
    return (res.data)


def me(loginData):
    chatId = (str(loginData['contact']) + '@c.us')
    print(chatId)

    if API.GreenApi(loginData["idInstance"], loginData["apiTokenInstance"]).account.getStateInstance().data['stateInstance'] == "authorized":
        res = API.GreenApi(loginData["idInstance"], loginData["apiTokenInstance"]).serviceMethods.getContactInfo(chatId=(str(loginData["contact"]) + '@c.us'))
        print("ok")
        res.data['message'] = "инфо о профиле"
        print(res.data)
        return res.data
    else:
        reply = {"message": " данные не доступны. Войдите в учетную запись или свяжитесь с администратором"}
        print(reply)
        return json.dumps(reply)
