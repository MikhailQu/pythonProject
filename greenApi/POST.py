from whatsapp_api_client_python import API
auth = {"id_instanse":"1101799607","apiTokenInstanse":"056a7216d44740f696c3fd46a73711e6b695827c1cde46ce99", "contact": "79100767686" }
#chatId=(auth['contact']+'@c.us'),
greenAPI = API.GreenApi(auth["id_instanse"],auth["apiTokenInstanse"] )


def sendMessage(resipient, messege, auth): # contact: ф:'79207401234', messege - текст сообщения, auth - данные авторизации ф:{"id_instanse":"0000","apiTokenInstanse":"0000"}
    API.GreenApi(auth["id_instanse"], auth["apiTokenInstanse"]).sending.sendMessage(resipient+'@c.us', messege)
    print("cooбщение отправлено")

sendMessage('79100767686', '*ВАУ-ВАУ-ВАУУУУУ!!!!*', auth)








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
