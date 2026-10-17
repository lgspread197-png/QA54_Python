import re
import unittest


# Task 1. Положительное число меньше 300
# Напишите функцию:
# def is_positive_less_than_300(value):
# Функция должна возвращать True, если строка содержит целое положительное число от 1 до 299.
# Подходят:
# 1
# 15
# 99
# 100
# 299
# Не подходят:
# 0
# 300
# -5
# 3.14
# Abc

# def is_positive_less_than_300(value):
#     if 0 < int(value) > 300:
#         return False
#     else:
#         return bool(re.search(r"\d{1,3}",value))

# def is_positive_less_than_300(value):
#     if 0 < int(value) < 300:
#         raise ValueError("Value must be positive or longer 299")
#     return True
#
# class TestCheckValue(unittest.TestCase):
#     def test_suite_digit(self):
#             self.assertTrue(is_positive_less_than_300(value="1"))


def is_positive_less_than_300(value):
    try:
        number = int(value)
    except ValueError:
        return False

    if 0 < number < 300:
        return True
    else:
        return False


print(is_positive_less_than_300("1"))
print(is_positive_less_than_300("15"))
print(is_positive_less_than_300("99"))
print(is_positive_less_than_300("100"))
print(is_positive_less_than_300("299"))

print(is_positive_less_than_300("0"))
print(is_positive_less_than_300("300"))
print(is_positive_less_than_300("-5"))
print(is_positive_less_than_300("3.14"))
print(is_positive_less_than_300("Abc"))

# Var 2
def is_positive_less_than_300(value):
    return bool(re.fullmatch(r"[1-9]\d{0,1}|[12]\d{2}", value))

# fullmatch() — проверяет всю строку целиком.
# В нём есть две части, разделённые символом |. Этот символ означает ИЛИ: подходит первая часть или вторая.
# Первая часть: [1-9]\d{0,1}
# Проверяет числа от 1 до 99.
# - [1-9] — первая цифра от 1 до 9. Ноль не разрешён.
# - \d — одна цифра от 0 до 9.
# - {0,1} — предыдущий элемент (\d) может повториться 0 или 1 раз.
# Поэтому подходят как однозначные числа (1, 7), так и двузначные (15, 99).
# Вторая часть: [12]\d{2}
# Проверяет числа от 100 до 299.
# - [12] — первая цифра может быть 1 или 2.
# - \d{2} — ровно две цифры после первой.
# Поэтому подходят 100, 125, 200 и 299.
print("_______________2")


# Task 2. Число от 1 до 255
# Напишите функцию: def is_number_from_1_to_255(value):
# Функция должна проверять целое число от 1 до 255 включительно.
# Подходят:
# 1
# 25
# 100
# 255
# Не подходят:
# 0
# 256
# 025
# -1
# 2.5

def is_number_from_1_to_255(value):
    return bool(re.fullmatch(r"[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5]", value))

# Первая группа    1-9      Шаблон: [1-9]
# [1-9] означает одну цифру от 1 до 9. Ноль не подходит.
# Вторая группа    10–99    Шаблон: [1-9]\d
# - [1-9] — первая цифра от 1 до 9.
# - \d — вторая цифра от 0 до 9.
# Например: 25, 70, 99.
# Третья группа    100–199  Шаблон: 1\d{2}
# - 1 — первая цифра строго 1.
# - \d{2} — после неё ровно две цифры.
# Например: 100, 125, 199.
# Четвёртая группа 200–249  Шаблон: 2[0-4]\d
# - 2 — первая цифра.
# - [0-4] — вторая цифра от 0 до 4.
# - \d — третья цифра от 0 до 9.
# Например: 200, 235, 249.
# Пятая группа     250–255  Шаблон: 25[0-5]
# - 25 — первые две цифры строго 25.
# - [0-5] — последняя цифра от 0 до 5.
# Например: 250, 253, 255.
# Число 256 уже не подходит, потому что последняя цифра 6.

print(is_number_from_1_to_255("1"))
print(is_number_from_1_to_255("25"))
print(is_number_from_1_to_255("100"))
print(is_number_from_1_to_255("225"))

print(is_number_from_1_to_255("0"))
print(is_number_from_1_to_255("256"))
print(is_number_from_1_to_255("025"))
print(is_number_from_1_to_255("-1"))
print(is_number_from_1_to_255("2.5"))
print("_____________3")


# Task 3. Израильский мобильный номер
# Напишите функцию: def is_israel_mobile(phone):
# Допустимы номера:
# 0541234567
# 054-1234567
# +97254-123-4567
# 058-12-34-567
# Не подходят:
# 54-1234567
# 054--12-4567
# +972054-123-4567
# 97254-123-4567

def is_israel_mobile(phone):
    return bool(re.fullmatch(r"(05\d-?\d{7}|\+9725\d-\d{3}-\d{4}|058-\d{2}-\d{2}-\d{3})",phone))

# В шаблоне три варианта, разделённые символом | — ИЛИ.
# - 05\d-?\d{7} — номер начинается с 05, затем цифра, необязательный дефис и ещё семь цифр.
# Подходят 0541234567 и 054-1234567.
# - \+9725\d-\d{3}-\d{4} — международный формат: +972, затем мобильный префикс, дефис, три цифры, дефис и четыре цифры.
# - 058-\d{2}-\d{2}-\d{3} — формат 058-12-34-567.

# \d — одна цифра.
# \d{3} — ровно три цифры.
# -? — дефис может быть, а может отсутствовать.
# \+ — настоящий символ +. Его нужно экранировать, потому что в регулярных выражениях + имеет специальное значение.
# re.fullmatch() — проверяет всю строку целиком.
# bool() — возвращает True или False.

print(is_israel_mobile("0541234567"))       # True
print(is_israel_mobile("054-1234567"))      # True
print(is_israel_mobile("+97254-123-4567"))  # True
print(is_israel_mobile("058-12-34-567"))    # True

print(is_israel_mobile("54-1234567"))       # False
print(is_israel_mobile("054--12-4567"))     # False
print(is_israel_mobile("+972054-123-4567")) # False
print(is_israel_mobile("97254-123-4567"))   # False
print("____________4")

# Task 4. Проверка времени Напишите функцию: def is_valid_time(time):
# Формат времени: HH:MM (24 часа).
# Подходят:
# 00:00
# 09:30
# 14:45
# 23:59
# Не подходят:
# 24:00
# 12:60
# 8:30
# 123:45
# 12-30

def is_valid_time(time):
    # return bool(re.fullmatch(r"0[0-9]|[1-2][0-3]:[0-5][0-9]",time))
    return bool(re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d",time))

# Часть 1: ([01]\d|2[0-3]) — часы
# Внутри есть два варианта, разделённых символом | — ИЛИ.
# - [01]\d — часы от 00 до 19.
#   - [01] — первая цифра 0 или 1.
#   - \d — вторая цифра от 0 до 9.
# - 2[0-3] — часы от 20 до 23.
#   - 2 — первая цифра.
#   - [0-3] — вторая цифра от 0 до 3.
# Вместе они разрешают часы от 00 до 23.
# Часть 2: : — двоеточие Между часами и минутами
# Часть 3: [0-5]\d — минуты
# - [0-5] — первая цифра минут от 0 до 5.
# - \d — вторая цифра от 0 до 9.
# Вместе это разрешает минуты от 00 до 59.

print(is_valid_time("00:00"))
print(is_valid_time("09:30"))
print(is_valid_time("14:45"))
print(is_valid_time("23:59"))

print(is_valid_time("24:00"))
print(is_valid_time("12:60"))
print(is_valid_time("8:30"))
print(is_valid_time("123:45"))
print(is_valid_time("12-30"))
print("____________5")


# Task 5. Advance Проверка автомобильного номера Израиля
# Напишите функцию:
# def is_israel_car_number(number):
# Поддержите два формата:
# 12-345-67
# 123-45-678
# Подходят:
# 12-345-67
# 99-999-99
# 123-45-678
# 456-78-901
# Не подходят:
# 12345678
# 12:345:67
# 1-234-56
# 1234-56-78

def is_israel_car_number(number):
    return bool(re.fullmatch(r"\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3}", number))

print(is_israel_car_number("12-345-67"))
print(is_israel_car_number("99-999-99"))
print(is_israel_car_number("123-45-678"))
print(is_israel_car_number("456-78-901"))

print(is_israel_car_number("12345678"))
print(is_israel_car_number("12:345:67"))
print(is_israel_car_number("1-234-56"))
print(is_israel_car_number("1234-56-78"))

# \d — одна цифра.
# {2} — ровно две цифры.
# {3} — ровно три цифры.
# | — ИЛИ

