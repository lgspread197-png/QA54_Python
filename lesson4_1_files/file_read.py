# Существуют 3 способа читать файлы:

with open("user.txt","w",encoding="utf-8") as file:
    file.write("Kristina\n")
    file.write("Alex\n")

# метод read() - весь файл полностью
with open("user.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(len(content))

# метод readlines() - он возвращает список, где каждая (элемент) строчка это отдельный элемент строки
with open("user.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
# получилось
#     ['Kristina\n', 'Alex\n']
    for line in lines:
        print(line.strip())
# for - для каждой строки в списке строк напечатай  строку line -
# где с учетом регистра \n каждая строка печатается без пробелов - получилось:
# Kristina
# Alex
print("___")

# метод for()
with open("user.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())