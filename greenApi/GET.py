from whatsapp_api_client_python import API
import json

loginData = dict(id_instanse="1101799607", apiTokenInstanse="056a7216d44740f696c3fd46a73711e6b695827c1cde46ce99",
                 contact="79100767686")
loginData['contact'] = (loginData['contact'] + '@c.us')
greenAPI = API.GreenApi(loginData["id_instanse"], loginData["apiTokenInstanse"])


def status(loginData):
    res =greenAPI.account.getStateInstance()
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
    if greenAPI.account.getStateInstance().data[
        'stateInstance'] == "notAuthorized":
        qr_code64 = API.GreenApi(loginData["id_instanse"], loginData["apiTokenInstanse"]).account.qr()
        # print("qr:", qr_code64.data)
        return (qr_code64.data)
    else:
        reply = {"message": "to get a QR code, log out of your account or contact the administrator"}
        print(reply)
        return json.dumps(reply)


def logout(loginData):
    res = greenAPI.account.logout()
    res.data['message'] = "выход из аккаунта"
    print(res.data)
    return (res.data)


def me(loginData):
    chatId = (str(loginData['contact']) + '@c.us')
    print(chatId)

    if greenAPI.account.getStateInstance().data['stateInstance'] == "authorized":
        print("ok")
        res = API.GreenApi(loginData["id_instanse"], loginData["apiTokenInstanse"]).serviceMethods.getContactInfo(
            chatId=chatId)
        res.data['message'] = "инфо о профиле"
        print(res.data)
        return res.data
    else:
        reply = {"message": " данные не доступны. Войдите в учетную запись или свяжитесь с администратором"}
        print(reply)
        return json.dumps(reply)
