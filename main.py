# 1. Создайте 3 dictionary c ключами: login, email, age, phone_number.
# Добавьте их в лист и запишите его в JSON файл.
# После чего выгрузите все данные из JSON, добавьте к каждой dictionary ключ language и снова запишите в JSON.

import json

with open('test.json', 'r') as file:
    data = json.load(file)
print(data)


