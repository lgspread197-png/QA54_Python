# with open("user.json","r",encoding="utf-8") as file:
#     print(file.read()) # FileNotFoundError: [Errno 2] No such file or directory: 'user.json'
# Ошибка FileNotFoundError означает, что Python не нашёл файл user.json по указанному пути
# и Ты открываешь файл в режиме "r" — это режим чтения! В этом режиме Python ожидает, что файл уже существует

print("Hello World")
result = 10/0
print(result)
print("Bye World")

# вышла ошибка
# Hello World
# Traceback (most recent call last):
#   File "C:\Project54\lesson5_1\exeptions.py", line 5, in <module>
#     result = 10/0
#              ~~^~
# ZeroDivisionError: division by zero