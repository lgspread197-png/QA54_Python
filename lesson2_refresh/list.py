from lesson2_refresh.hw_1_sol import result

fruits = ["apple","banana","orange"]

print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(len(fruits))
fruits[1] = "cat"
print(fruits)

print()
#добавление - append(), insert(), extend()
fruits.append("kivi") #добавление в конец
print(fruits)
fruits.append(["car","track"]) #добавление в конец
print(fruits)
#extend() добавляет из другой колекции по одному в конец колекции

fruits.extend(["cat","dog"])
print(fruits)

# insert() вставляет не 1 а 2 - индекс и объект
fruits.insert(4,"pear")
print(fruits)

print("_________")
#удаление remove(), pop(), del(), clear()

#remove() - принимает объект - удаляет что-то не важно где находится
#pop() - удаляет элемент под контректным определен индексом, но значение возвращает
#del() - удаляет элемент под контректным определен индексом, но ничего не возвращает
#clear() - удаляет всю коллекуцию

e = ["apple","banana","orange"]
e.remove("banana")
print(e)
print()

f = ["apple","banana","orange"]
popped = f.pop(1)
print(popped)
print(popped,f)
print()

h = ["apple","banana","orange"]
del h[0]
print(h)
print()

k = ["apple","banana","orange"]
k.clear()
print(k)

# поиск и подсчет index(), count(), in (если что-то в коллекции)  not in
m = ["apple","banana","cherry","orange"]
print(m.index("cherry")) #2
print(m.count("banana")) #1
print("apple" in m)  # True
print("kivi" not in m)  # True

print("____________")
# сортировка  sort(), sorted(), reverse()
#sort() - отсортировывает и возвращает пустоту
#sorted() - отсортировывает и возвращает новый отсортированный список
#reverse() - не отсортировывает, а просто переворачивает (если надо отсортировать еще, надо применить 2 метода)
numbers = [3,1,5,2,9,6]
result = numbers.sort()
print(numbers,result)

numbers_2 = [3,1,5,2,9,6]
new_list = sorted(numbers_2)
print(numbers_2,new_list)

numbers_3 = [3,1,5,2,9,6]
numbers_3.reverse()
print(numbers_3)
print()

numbers_4 = [3,1,5,2,9,6]
print(sorted(numbers_4,reverse=True))
print(numbers_4)
# мы отсортировали и развернули

print("____________")
#перебор
items = ["apple","banana","orange"]

for item in items:
    print(item)

print()

for i in range(len(items)):
    print(i,items[i])

print()

numbers_5 = [-2,3,-1,5,0,-9]
result = []
for n in numbers_5:
    if n >0:
        result.append(n)
print(result)

#то же самое, но коротко
result2 = [n for n in numbers_5 if n>0]
print(result2)
