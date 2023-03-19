from whatsapp_api_client_python import API


def sendMessage(auth):
    API.GreenApi(auth["idInstance"], auth["apiTokenInstance"]).sending.sendMessage(str(auth["recipient"]) + '@c.us', auth["message"])
    return

def sendFile(auth):
    return

def sendLink(auth):
    API.GreenApi(auth["idInstance"], auth["apiTokenInstance"]).sending.sendMessage(str(auth["recipient"]) + '@c.us',auth["link"])
    return

def sendContact(auth):
    API.GreenApi(auth["idInstance"], auth["apiTokenInstance"]).sending.sendContact(str(auth["recipient"]) + '@c.us',auth["sendContact"])
    return




'''
#####6.1. Управление аккаунтомPOST /setName - Изменить имя пользователя. Пример запроса: {"user_name": "new_name"}. Пример ответа: {"status": "OK", "user_name": "new_name"}
#####POST /setStatus - Изменить статус пользователя. Пример запроса: {"user_status": "CRM ready"}. Пример ответа: {"status": "OK", "user_status": "CRM ready"}
6.2. Отправка и приём сообщений
POST /sendMessage - Отправка сообщения в новый или существующий чат. Пример запроса: {"contact": "79261234567", "from": “manager”, "message": "Hello!", "auth": "auth_key"}. Пример ответа: {"status": "sent"}
хз как POST /sendFile - Отправка файла в новый или существующий чат. Нужна проработка отправки бинарных данных.
хз как POST /sendPTT - Отправка PTT-аудио(иконка с микрофоном) в новый или существующий чат. Нужна проработка отправки бинарных данных.
хз как POST /sendLink - Отправка ссылки в новый или существующий чат. Нужна проработка отправки этого формата данных.
хз как POST /sendContact - Отправка контакта или списка контактов в новый или существующий чат. Нужна проработка отправки этого формата данных.
POST /sendLocation - Отправка локации в новый или существующий чат. Нужна проработка отправки этого формата данных.
POST /sendVCard - Отправка vCard в новый или существующий чат. Нужна проработка отправки этого формата данных.
POST /sendButtons - Отправка сообщения с кнопками в новый или существующий чат. Нужна проработка отправки этого формата данных.
POST /forwardMessage - Пересылка сообщения в новый или существующий чат. Нужна проработка отправки этого формата данных.
POST /messages - Получить список сообщений отсортированных по времени в порядке убывания. Пример запроса: {"dialog": "79261234567"} Пример ответа: {"messages": [{"message_timestamp":123456789, "message_body": "Hello", "message_creator": "79267281964", "message_id": "1234567890"}]}
POST /deleteMessage - Удаляет сообщение из WhatsApp. Пример запроса: {"message_id"}. Пример ответа: {"status": "OK"}'''
