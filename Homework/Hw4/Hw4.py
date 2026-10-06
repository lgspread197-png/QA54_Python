import csv


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

books = [
 	"Harry Potter",
 	"The Hobbit",
 	"1984",
 	"The Little Prince"
 ]
save_books(books)
save_books(True)
save_books([])
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
