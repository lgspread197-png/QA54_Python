# 1. Напишите функцию:
# get_product(products, index)
# Функция должна возвращать товар из списка по переданному индексу.
# Если такого индекса нет, вернуть:
# Product index is out of range
# Примеры:
# products = ["coffee", "tea", "milk"]
# print(get_product(products, 0))
# # coffee
# print(get_product(products, 7))
# # Product index is out of range
# Обработайте IndexError.

def get_product(products, index):
    try:
        return products[index]
    except IndexError:
        return "Product index is out of range"


products = ["coffee", "tea", "milk"]

print(get_product(products, 0))
print(get_product(products, 13))
print(get_product(products, -1))
print()


# 2. Напишите функцию:
# get_settings_value(settings, key)
# Функция должна возвращать значение из словаря по ключу.
# Если ключ отсутствует, вернуть:
# Setting was not found
# Примеры:
# settings = {
# "language": "English",
# "theme": "dark"
# }
# print(get_settings_value(settings, "theme"))
# # dark
# print(get_settings_value(settings, "font"))
# # Setting was not found
# Обработайте KeyError.

def get_settings_value(settings, key):
    try:
        return settings[key]
    except KeyError:
        return "Setting was not found"

settings = {"language": "English","theme": "dark"}
print(get_settings_value(settings, "theme"))
print(get_settings_value(settings, "font"))
print()


# 3. Напишите функцию:
# calculate_total_price(price, quantity)
# Функция получает два значения, преобразует их в числа и возвращает результат умножения.
# Обработайте отдельно:
# ValueError, если значение невозможно преобразовать в число.
# TypeError, если передан неподходящий тип данных.
# Примеры:
# print(calculate_total_price("12.5", "4"))
# # 50.0
# print(calculate_total_price("coffee", "4"))
# # Value must be a number
# print(calculate_total_price(None, 4))
# # Invalid data type
# Не используйте один общий except Exception.

def calculate_total_price(price, quantity):
    try:
        price = float(price)
        quantity = float(quantity)
        return price * quantity
    except ValueError:
        return "Value must be a number"
    except TypeError:
        return "Invalid data type"

print(calculate_total_price("12.5", "4"))
print(calculate_total_price("coffee", "4"))
print(calculate_total_price({"coffe"}, "4"))
print(calculate_total_price(None, 4))
print()


# 4. Напишите функцию:
# def read_temperature():
# Функция должна:
# Запросить у пользователя температуру с помощью input().
# Преобразовать значение в float.
# Если преобразование прошло успешно, вывести:
# Temperature was entered successfully
# Если пользователь ввёл неправильное значение, вывести:
# Invalid temperature
# Независимо от результата всегда вывести:
# Program finished

def read_temperature():
    try:
        temperature = float(input("Enter temperature: "))
        print("Temperature was entered successfully")
    except ValueError:
        print("Invalid temperature")
    finally:
        print("Program finished")


read_temperature()
print()


# 5. Напишите функцию:
# def validate_discount(discount):
# Требования:
# если скидка меньше 0, выбросить:
# ValueError("Discount cannot be negative")
# если скидка больше 100, выбросить:
# ValueError("Discount cannot be greater than 100")

def validate_discount(discount):
    if type(discount) not in (int, float):
        raise TypeError("Invalid discount type")
    if discount < 0:
        raise ValueError("Discount cannot be negative")
    if discount > 100:
        raise ValueError("Discount cannot be greater than 100")
    print("Discount is valid")

validate_discount(50)
validate_discount(0)
# validate_discount(-5)
# validate_discount(150)