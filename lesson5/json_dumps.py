#dumps()- pyton ->json str
# он из объекта пайтом превращает в ф формат  именно в строку
#loads() - json -> pyton object str
# наоборот
#dump()save Pyton object- > file.json (file)
#load() file.json ->> Pyton (file)

import json

user = {"username":"kristina","age":25,"is_admin":True}  # словарь, хочу превратить в json str строку
json_str = json.dumps(user)
print(json_str)
print(type(json_str))

user = json.loads(json_str)
print()
print(user)
print(type(user))
print(user["username"])

test_config = {
    "url": "http://127.0.0.1:8000",
    "username": "kristina",
    "password": "Aa123456!",
    "timeout": 20
}

with open("config.json","w",encoding="utf-8") as file:
    json.dump(test_config,file,indent=4,ensure_ascii=False)

with open("config.json","r",encoding="utf-8") as file:
    config = json.load(file)
    print(config)
    print(config["url"])
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
save_profile("Kris","39","Rishon")

