#dumps()- pyton ->json str
# он из !объекта пайтон! превращает в файл именно в !формат строки!
#loads() - json str -> pyton object str  (или из dict в dict) !строка обратно в Python!
# наоборот
#dump()save Pyton object  > file.json (file) !записать в файл!
#load() Чтение файла file.json ->> Pyton (file)  !прочитать из файла!

import json

user = {"username":"kristina","age":25,"is_admin":True}  # словарь, хочу превратить в json str строку
json_str = json.dumps(user)
# Функция json.dumps() преобразует объект Python в строку в формате JSON.
print(json_str)
print(type(json_str))

user = json.loads(json_str)
# json.loads(json_str) — преобразует JSON-строку в объект Python. (в данный момент обратно в словарь)
print()
print(user)
print(type(user))
print(user["username"])
# user["username"] — получает значение по ключу "username".

# Сохраняем настройки в файл config.json
# Это обычный Python-словарь с настройками приложения или API-тестов.
test_config = {
    "url": "http://127.0.0.1:8000",
    "username": "kristina",
    "password": "Aa123456!",
    "timeout": 20
}

with open("config.json","w",encoding="utf-8") as file:
    json.dump(test_config,file,indent=4,ensure_ascii=False)
# Записывает словарь в файл в формате JSON. test_config - словарь, записывает непосредственно в file !
# indent=4   - Делает JSON более читаемым, добавляя отступы в 4 пробела
# ensure_ascii=False  - Позволяет сохранять символы других языков, например кириллицу,
# без преобразования в \u....


with open("config.json","r",encoding="utf-8") as file:
    config = json.load(file)
    # json.load(file) — читает JSON и преобразует его в Python-словарь.
    print(config)   # выводит весь словарь.
    print(config["url"])  # получает адрес из словаря
    print(config["username"])

#Advansed
# 3) Save a profile to a JSON file
# Напишите функцию save_profile(name, age, city)
# Функция должна создать файл profile.json со следующим содержимым:
# save_profile("Maria", 30, "Haifa")
# Ожидаемое содержимое файла profile.json:
# {
#     "name": "Maria",
#     "age": 30,
#     "city": "Haifa"
# }
# Use a dictionary and json.dump().json

def save_profile(name,age,city):
    profile = {
        "name":name,
        "age": age,
        "city":city
    }
    with open("profile.json","w",encoding="utf-8") as file:
        json.dump(profile,file,indent=2)

# profile	Словарь, который нужно сохранить
# file	Файл, куда записываем данные
# indent=4	Данные записываются в строку и делается отступы в 4 пробела для удобного чтения

save_profile("Kris","39","Rishon")
# Эта строка запускает функцию. Она создаёт словарь, открывает файл и сохраняет в него данные.

# Не путай json.dump() и json.dumps():
# - json.dump(user, file) — записывает JSON в файл.
# - json.dumps(user) — преобразует данные в JSON-строку и возвращает её.
# - json.load(file)	Читает JSON из файла и преобразует его в Python-объект

# json — стандартный модуль Python для работы с JSON-файлами.
# JSON — это текстовый формат хранения данных.
# Он похож на словарь Python, но имеет собственный формат записи.

# file.read()	Читает содержимое файла как строку (str).
# json.load(file)	Читает JSON и преобразует его в объект Python (dict, list и другие типы).
# json.loads(text) — преобразует JSON из строки в объект Python.
# Запомни: load — файл, loads — строка.