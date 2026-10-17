import re


# модуль re в Python для поиска текста с помощью регулярных выражений.
# В QA это полезно, например, для поиска статуса теста passed или failed в логах
text = "The status is passed"
result = re.search("passed",text)  # "passed" — шаблон, который мы ищем; text — строка, в которой выполняется поиск
print(result)
print(result.group()) # Метод .group() возвращает сам найденный текст, без дополнительной информации об объекте
print()
# метод re.search ищет во всей строке первое совпадение с заданным шаблоном (если слово с маленькой буквы - то ищет с маленькой)
#span=(14, 20) это позиция passed в тексте The status is passed

# text = "The status is passed"
# result = re.search("test",text)
# print(result)
# print(result.group())
#
# None
# Traceback (most recent call last):
#   File "C:\Project54\lesson7_1_Regexpression\regexpression.py", line 11, in <module>
#     print(result.group())
#           ^^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'group'

text2 = "passed: test registration"
text3 = "test registration: passed"
print(re.match("passed",text2))
print(re.match("passed",text3))
print()
# метод re.match ищет только в начале строки и строгое соответствие (если с маленькой слово - то ищет с маленькой, до последнего символа)

print(re.match("passed: test registration",text2))
print(re.match("passed: test registration ",text2))
print("___________")

print(re.search("d.g","dog"))
print(re.search("d.g","dig"))
print(re.search("d.g","dg"))
# в слове d.g точка означает любой символ (поэтому dog и dig проходят, а dg не подходит)
print(re.search("d..g","doog"))
print(re.search("d.g","doog"))
print()

# re.search() по умолчанию различает большие и маленькие буквы. Поэтому Test и test — разные варианты.

print(re.search("^Test","Test is start"))
print(re.search("^Test","Start is test"))
# ^ Start of the string (start of each line with re.MULTILINE)
# $ End of the string (end of each line with re.MULTILINE)
print(re.search("Test$","Start is Test"))
print(re.search("Test$","Test is start"))
print("____________1")

print(re.search("gr[ae]y","grey"))
print(re.search("gr[ae]y","groy"))
print(re.search("gr[ae]y","greey"))

# обозначают набор допустимых символов - на этом месте должен стоять один символ из указанного набора
# пример - [ae] — на этом месте должна быть либо a, либо eh -
# [ae] означает ровно один символ: либо a, либо e. Это не означает «несколько букв из набора»
print()
# [] A set of characters, e.g. [abc]; or a range, e.g. [a-c]
# Это означает, что внутри квадратных скобок можно указать отдельные символы или диапазон

print(re.search("[a-z]","Kristina"))
print(re.search("[0-9]","Order #34"))
print(re.search("[A-Z]","kristina"))
print(re.search("[A-Za-z]","kristina"))
print("__________2")

# [^ ] Negation of a set — any character except the ones listed
# [^0-9] означает «любой один первый символ, кроме цифр от 0 до 9
print(re.search("[^0-9]","123456a"))
print(re.search("[^0-9]","123456"))
print(re.search("[^0-9]","123.45.6"))
print()

# \d    A digit, equivalent to [0-9] - означает одну цифру от 0 до 9
print(re.search("\\d","Order #34"))
# \w    A word character, equivalent to [a-zA-Z0-9_] - поиск букв(болш,мал), цифр или подчёркивания
print(re.search("\\w","!!!Kristina"))
# \s    Whitespace, equivalent to [ \t\n\r\f\v] - — поиск любого пробельного символа
print(re.search("\\s","Kristina QA 54"))
# К пробельным символам относятся:
# Обычный пробел ( )
# Знак табуляции (\t)
# Перевод строки (\n)
# Возврат каретки (\r)
# Вертикальная табуляция и другие подобные символы.
# если не срабатывает, то ставь по 2 \\ для дополнительного экранирования
print("__________3")

# Здесь r"\d" означает, что обратный слеш передаётся как есть, без дополнительного экранирования
print(re.search(r"\d","Order #34"))
print(re.search(r"\w","!!!Kristina"))
print(re.search(r"\s","Kristina QA 54"))
print()

# *  +  ?     Zero-or-more / one-or-more / zero-or-one times (greedy — matches as much as possible)
# Они определяют, сколько раз может повторяться символ перед ними
# эти символы относятся к предыдущему символу или элементу шаблона, а не ко всей строке
print(re.search(r"ab*c","ac"))
print(re.search(r"ab*c","abc"))
print(re.search(r"ab*c","abccccc"))
print()

print(re.search(r"ab+c","ac"))
print(re.search(r"ab+c","abc"))
print(re.search(r"ab+c","abccccc"))
print()

print(re.search(r"colou?r","color"))
print(re.search(r"colou?r","colour"))
print(re.search(r"colou?r","colouur"))
print("__________4")

# {m}  Exactly m times
# {m} и {m,n}. Они позволяют указать {m} точное количество повторений или {m,n} допустимый диапазон
print(re.search(r"\d{3}","13"))
print(re.search(r"\d{3}","1566638"))
print()

# {m,n}   From m to n times (greedy); add ? after for non-greedy: {m,n}?
# Дополнительный ? делает квантификатор неголодным (non-greedy): он старается найти минимально возможное совпадение.
print(re.search(r"\d{2,4}","123456"))
# Шаблон \d{2,4} означает:
# - \d — цифра;
# - {2,4} — от двух до четырёх цифр подряд.
# Подходящие варианты: 12, 123, 1234.
# В строке "123456" есть шесть цифр. По умолчанию квантификатор жадный (greedy): он старается найти
# максимально длинное совпадение, которое разрешает шаблон

# print(re.search(r"\d{2,4}","1"))   падает
print(re.search(r"\d{3,4}","323"))

