import csv
from pathlib import Path


# 1) Напишите функцию save_shopping_list(items).
# Функция принимает список строк и создаёт файл shopping.txt и сохраняет в него список покупок.
# Каждый товар должен быть записан с новой строки. Пример:
# items = [
#     "Milk",
#     "Bread",
#     "Apples",
#     "Coffee"
# ]
# save_shopping_list(items)
# После выполнения программы файл должен выглядеть так:
# Milk
# Bread
# Apples
# Coffee
# Используйте:
# • with open(...)
# • режим "w"
# • цикл for

def save_shopping_list(items):
    with open("shopping_list.txt","w",encoding="utf-8") as file:
        for item in items:
            file.write(item+"\n")
items = [
    "Milk",
    "Bread",
    "Apples",
    "Coffee"
]
save_shopping_list(items)

with open("shopping_list.txt","r",encoding="utf-8") as file:
    print(file.read())

# 2) Read data from a CSV file
# Создайте файл students.csv со следующим содержимым:
# name,age
# Anna,21
# Tom,19
# Kate,22
# Напишите функцию read_students(filename)
# которая выводит информацию в виде
# Student: Anna (21)
# Student: Tom (19)
# Student: Kate (22)
# Use csv.DictReader().

def read_students(filename):
    # мы вручную создали файл students.csv
    with open("students.csv","r",encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student:{row['name']}({row['age']})")
read_students("students.csv")

"""
то же самое
def read_students(filename):
    with open(filename,"r",encoding="utf-8",newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Student:{row['name']}({row['age']})")
read_students("students.csv")
"""


# Напишите функцию create_reports_folder()
# Функция должна:
# Создать папку reports.
# Создать внутри неё файл result.txt.
# Записать в файл строку:
# Homework completed successfully!
# Use pathlib.Path, mkdir() and with open(...).
# General requirements
# • Use encoding='utf-8' when working with text files.
# • Test every function using the examples from the task.

def create_reports_folder():
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    results_file = reports_dir/"result.txt"
    # Оператор / соединяет путь к папке и имя файла (пока еще не создает файл, только путь)
    with open(results_file,"w",encoding="utf-8") as file:
        file.write("Homework completed successfully!")
    # создает файл "result.txt" и записывает в него "Homework completed successfully!"
create_reports_folder()

