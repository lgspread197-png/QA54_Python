# with open("user.json","r",encoding="utf-8") as file:
#     print(file.read()) # FileNotFoundError: [Errno 2] No such file or directory: 'user.json'
# Ошибка FileNotFoundError означает, что Python не нашёл файл user.json по указанному пути
# и Ты открываешь файл в режиме "r" — это режим чтения! В этом режиме Python ожидает, что файл уже существует

# print("Hello World")
# result = 10/0
# print(result)
# print("Bye World")

# вышла ошибка
# Hello World
# Traceback (most recent call last):
#   File "C:\Project54\lesson6\exeptions.py", line 5, in <module>
#     result = 10/0
#              ~~^~
# ZeroDivisionError: division by zero

# def div_int(a,b):
#     return a/b
# print("start program")
# result =div_int(10,0)
# print(result)
# print("end program")

# вышла ошибка
# start program
# Traceback (most recent call last):
#   File "C:\Project54\lesson6\exeptions.py", line 22, in <module>
#     result =div_int(10,0)
#   File "C:\Project54\lesson6\exeptions.py", line 20, in div_int
#     return a/b
#            ~^~
# ZeroDivisionError: division by zero

#try/except
print("Hello World")
try:
    result = 10/0
    print(result)
except Exception as e:  # в объекте е лежит исключение
    print("An error occurred: ",e)
print("BY")

# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print("Result: ",result)
# except ValueError:
#     print("Error: Please enter a valid number")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")

def is_number(text):
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False
print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Kris"))
print(is_number(None))

print("_________")


try:
    value = int("39")
except ValueError:
    print("An error occurred: ")
else:
    print("An error occurred: ",value)
finally:
    print("End of try")

print()
try:
    value = int("%%%")
except ValueError:
    print("An error occurred: ")
else:
    print("An error occurred: ", value)
finally:
    print("End of try")

