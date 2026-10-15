import re

text = "The status is passed"
result = re.search("passed",text)
print(result)
print(result.group())
print()
# метод re.search ищет во всей строке (если с маленькой слово - то ищет с маленькой)
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

print(re.search("^Test","Test is start"))
print(re.search("^Test","Start is test"))
# ^ Start of the string (start of each line with re.MULTILINE)
# $ End of the string (end of each line with re.MULTILINE)
print(re.search("Test$","Start is Test"))
print(re.search("Test$","Test is start"))
print("____________")

print(re.search("gr[ae]y","grey"))
print(re.search("gr[ae]y","groy"))
print(re.search("gr[ae]y","greey"))
# [] A set of characters, e.g. [abc]; or a range, e.g. [a-c]
print()

print(re.search("[a-z]","Kristina"))
print(re.search("[0-9]","Order #34"))
print(re.search("[A-Z]","kristina"))
print(re.search("[A-Za-z]","kristina"))
print("_______")

# [^ ] Negation of a set — any character except the ones listed
# ^0-9 ищи любой символ от 0 до 9, кроме
print(re.search("[^0-9]","123456a"))
print(re.search("[^0-9]","123456"))
print(re.search("[^0-9]","123.45.6"))
print()

# \d    A digit, equivalent to [0-9]
print(re.search("\d","Order #34"))
# \w    A word character, equivalent to [a-zA-Z0-9_]
print(re.search("\w","!!!Kristina"))
# \s    Whitespace, equivalent to [ \t\n\r\f\v]
print(re.search("\s","Kristina QA 54"))
# \s подменяет любой пробельный символ.
# К пробельным символам относятся:
# Обычный пробел ( )
# Знак табуляции (\t)
# Перевод строки (\n)
# Возврат каретки (\r)
# Вертикальная табуляция и другие подобные символы.
# если не срабатывает то ставь по 2 \\
print(re.search("\\s","Kristina QA 54"))
print("______")

print(re.search(r"\d","Order #34"))
print(re.search(r"\w","!!!Kristina"))
print(re.search(r"\s","Kristina QA 54"))
print()

# *  +  ?     Zero-or-more / one-or-more / zero-or-one times (greedy — matches as much as possible)
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
print("______")

# {m}  Exactly m times
print(re.search(r"\d{3}","13"))
print(re.search(r"\d{3}","1566638"))
print()

# {m,n}   From m to n times (greedy); add ? after for non-greedy: {m,n}?
print(re.search(r"\d{2,4}","123456"))
# print(re.search(r"\d{2,4}","1"))   падает
print(re.search(r"\d{3,4}","323"))

