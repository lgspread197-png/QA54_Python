import re


def has_digits(password):
    return bool(re.search(r"\d",password))
# re.search() — ищет совпадение с шаблоном в строке.
# r"\d" — регулярное выражение, которое означает одну цифру от 0 до 9.
# password — строка, в которой ищем цифру
# bool() преобразует результат в обычное логическое значение True или False.

print(has_digits("dr123456"))
print(has_digits("qwerty"))
print(has_digits("-1"))  # Есть цифра 1. Символ - не мешает поиску → True

