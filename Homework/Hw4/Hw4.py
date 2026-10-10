import csv
import os
import json
from pathlib import Path


# 1. Save a book list
# Напишите функцию save_books(books).
# Функция принимает список строк и создаёт файл books.txt, в который сохраняет названия книг.
# Каждая книга должна быть записана с новой строки.
# Пример:
# books = [
#  	"Harry Potter",
#  	"The Hobbit",
#  	"1984",
#  	"The Little Prince"
#  ]
#  save_books(books)
# После выполнения программы файл books.txt должен выглядеть так:
# Harry Potter
#  The Hobbit
#  1984
#  The Little Prince
# Используйте:
# •       with open(...)
# •       режим "w"
# •       цикл for

# Task 1
def save_books(books):
    if books is None or type(books) is not list:
        print("books is not list")
        return None
    with open("books.txt","w",encoding="utf-8") as file:
        for book in books:
            file.write(f'{book}\n')
            # file.write(book + "\n")
    # print("File saved:", os.path.abspath("books.txt"))
    # os.getcwd() возвращает (показывает) путь к текущей рабочей папке.

books = [
 	"Harry Potter",
 	"The Hobbit",
 	"1984",
 	"The Little Prince"
 ]
save_books(books)
save_books(True)
# save_books([])
save_books(3)

print("____")

# Task 2
# 2. Read data from a CSV file
# Создайте файл products.csv со следующим содержимым:
# product,price
#  Coffee,25
#  Tea,18
#  Chocolate,12
# Напишите функцию:
# read_products(filename)
# Функция должна прочитать данные из файла и вывести информацию в следующем формате:
# Product: Coffee (25)
#  Product: Tea (18)
#  Product: Chocolate (12)
# Используйте:
# csv.DictReader()


with open("products.csv","w",encoding="utf-8",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["product","price"])
    writer.writerow(["Coffee", 25])
    writer.writerow(["Tea", 18])
    writer.writerow(["Chocolate", 12])

def read_products(filename):

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Product: {row['product']} ({row['price']})")


read_products("products.csv")

# Task 3. Save user information to a JSON file
# Напишите функцию:
# save_user(username, email, country)
# Функция должна создать файл user.json и сохранить в него информацию о пользователе.
# Пример вызова:
# save_user("anna21", "anna@example.com", "Israel")
# Ожидаемое содержимое файла user.json:
# {
#  	"username": "anna21",
#  	"email": "anna@example.com",
#  	"country": "Israel"
#  }
# Используйте:
# •       словарь dict
# •       json.dump()


def save_user(username, email, country):
    user = {
        "username": username,
        "email": email,
        "country": country
    }

    with open("user.json", "w", encoding="utf-8") as file:
        json.dump(user, file, indent=4)

# user	Словарь, который нужно сохранить
# file	Файл, куда записываем данные
# indent=4	Данные записываются в строку и делается отступы в 4 пробела для удобного чтения

save_user("anna21", "anna@example.com", "Israel")

# Не путай json.dump() и json.dumps():
# - json.dump(user, file) — записывает JSON в файл.
# - json.dumps(user) — преобразует данные в JSON-строку и возвращает её.
# - json.load(file)	Читает JSON из файла и преобразует его в Python-объект

print("____")

# Task 4. Advanced ★
# Напишите функцию:
# create_logs_folder()
# Функция должна:
# 1.     Создать папку logs.
# 2.     Создать внутри неё файл app.txt.
# 3.     Записать в файл строку:
# Application started successfully!
# Используйте:
# •       pathlib.Path
# •       mkdir()
# •       with open(...)
# General Requirements
# •       Используйте encoding='utf-8' при работе с текстовыми файлами.
# •       Проверьте работу каждой функции на примерах из задания.
# •       Используйте названия функций, указанные в задании.
# •       Код должен быть читаемым и аккуратно оформленным.
# •       После выполнения программы проверьте содержимое созданных файлов.

from pathlib import Path


def create_logs_folder():
    folder = Path("logs")
    # Создаём объект пути к папке logs Пока сама папка ещё не создана.
    folder.mkdir(exist_ok=True)
    # mkdir() — создаёт папку.
    # exist_ok=True — позволяет выполнить код, даже если папка logs уже существует.
    # Без этого параметра может возникнуть ошибка FileExistsError.

    file_path = folder / "app.txt"
    # Оператор / здесь соединяет путь к папке и имя файла. Получаем путь logs/app.txt

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Application started successfully!")

# open() — открывает файл.
# "w" — режим записи. Если файл уже существует, его содержимое будет перезаписано.
# encoding="utf-8" — кодировка файла.
# with — автоматически закрывает файл после завершения работы с ним.
# Записываем указанную строку в файл

create_logs_folder()