#Task 1
# Написать функцию print_list_reverse(lst)
# Функция принимает список и выводит этот список в консоль в обратном порядке.
# Если lst равен None, пустой список, или если аргумент не является объектом типа list,
# функция должна вывести: Wrong list
# Пример:  print_list_reverse([1, 2, 3, 4, 5])
# Вывод в консоль:  [5, 4, 3, 2, 1]

def print_list_reverse(lst):
    if lst is None or len(lst) == 0 or type(lst) is not list:
        print("Wrong list")
        return
    else:
        lst.reverse()
        print(lst)


print(print_list_reverse([1, 2, 3, 4, 5]))
print_list_reverse([1, 2, 3, 4, 5])
print(print_list_reverse((1, 2, 3, 4, 5)))
print(print_list_reverse([]))
print(print_list_reverse(None))

print("______________")
#Task 2
# Написать функцию is_valid_point(point)
# Функция принимает кортеж и проверяет, является ли он корректной точкой на плоскости.
# Условия корректной точки:
#  • аргумент должен быть кортежем (tuple), а не списком или другим типом;
#  • кортеж состоит ровно из 2 элементов;
#  • оба элемента являются числами (int или float).
# Если кортеж соответствует всем условиям, функция возвращает True.
# Если аргумент не соответствует условиям, функция возвращает False.
# Если point равен None или является пустым кортежем, функция возвращает None.

# def is_valid_point(point):
#     if point is None or len(point) == 0:
#         return None
#     elif type(point) is not tuple or len(point) != 2:
#         return False
#     elif isinstance(point[0],(int,float)) and isinstance(point[1],(int,float)):
#         return True
#     else:
#         return False

def is_valid_point(point:tuple):
    if point is None or point==():
        return None
    # if not isinstance(point,tuple):
    #     return False
    if type(point) is not tuple:
        return False
    if len(point) != 2:
        return False
    a,b = point
    # if isinstance((a,(int,float)) and isinstance(b,(int,float)):
    if type(a) in (int, float) and type(b) in (int, float):
        return True
    return False


print(is_valid_point((3, 5)))      # True
print(is_valid_point((3, "5")))    # False
print(is_valid_point([3, 5]))      # False
print(is_valid_point((1, 2, 3)))   # False
print(is_valid_point(()))          # None
print(is_valid_point(None))        # None

print("______________")
# Task 3
# Написать функцию print_sublist_reverse(lst, start, finish)
# Функция принимает список, стартовый индекс и финишный индекс.
# Нужно вывести в консоль список, в котором элементы от индекса start до индекса finish включительно
# расположены в обратном порядке, а остальные элементы остаются в обычном порядке.

# def print_sublist_reverse(lst, start, finish):
#     if lst is None or len(lst) == 0 or type(lst) is not list:
#         return "Wrong args"
#     elif type(start) is not int or type(finish) is not int:
#         return "Wrong args"
#     elif start>finish or finish>len(lst):
#         return "Wrong args"
#     else:
#         lst[start:finish+1] = lst[start:finish+1][::-1]
#         return lst

# print(print_sublist_reverse([1, 2, 3, 4], 1, 2))
# print(print_sublist_reverse((None), 1, 2))
# print(print_sublist_reverse([], 1, 2))
# print(print_sublist_reverse((1, 2, 3), 1, 2))
# print(print_sublist_reverse([1, 2, 3], "1", 2))
# print(print_sublist_reverse([1, 2, 3], 1, "2"))
# print(print_sublist_reverse([1, 2, 3], 3, 2))
# print(print_sublist_reverse([1, 2, 3], 1, 4))
# print(print_sublist_reverse([1, 2, 3], False, 4))

def print_sublist_reverse(lst, start, finish):
    if not isinstance(lst,list) or not lst:
        print("Wrong args")
        return
    if type(start) is not int or type(finish) is not int:
        print("Wrong args")
        return
    if not 0<=start<len(lst) or not 0<=finish<len(lst) or start>finish:
        print("Wrong args")
        return

    # result = lst[:start] + lst[finish: start - 1: -1] + lst[finish+1:]
    result = lst[:start] + lst[start:finish+1][::-1] + lst[finish+1:]
    print(result)

print_sublist_reverse([1, 2, 3, 4], 1, 2)
print_sublist_reverse((None), 1, 2)
print_sublist_reverse([], 1, 2)
print_sublist_reverse((1, 2, 3), 1, 2)
print_sublist_reverse([1, 2, 3], "1", 2)
print_sublist_reverse([1, 2, 3], 1, "2")
print_sublist_reverse([1, 2, 3], 3, 2)
print_sublist_reverse([1, 2, 3], 1, 4)
print_sublist_reverse([1, 2, 3], False, 4)


print("______________")
# Task 4 Advanced
# Написать функцию get_students_by_grade(students)
# Функция принимает словарь, где ключ — имя студента, а значение — его оценка.
# Нужно вернуть новый словарь, где ключ — оценка, а значение — список имён студентов, получивших эту оценку.
# Пример:
# get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85})
# Результат:
# {90: ["Alice", "Diana"], 85: ["Bob", "Charlie"]}
# Если students равен None, является пустым словарём или аргумент не является словарём,
# функция должна вернуть пустой словарь: {}

# мое решение
def get_students_by_grade(students):
    if students is None or len(students) == 0 or type(students) is not dict:
        return {}
    new_g_s_b_g = {}
    for key, value in students.items():
        new_g_s_b_g[value] = key
    return new_g_s_b_g


print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))

# !решение чата GPT!  - я сам не придумал, как правильно сохранять !все имена студентов и их оценки!
# def get_students_by_grade(students):
#     if not students:
#         return {}
#
#     new_g_s_b_g = {}
#
#     for key, value in students.items():
#         if value in new_g_s_b_g:
#             new_g_s_b_g[value].append(key)
#         else:
#             new_g_s_b_g[value] = [key]
#
#     return new_g_s_b_g
#
# print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))

def get_students_by_grade(students):
    if not isinstance(students,dict) or not students:
        return {}

    result ={}
    for name,grade in students.items():
        if grade not in result:
            result[grade] = []

        result[grade].append(name)
    return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie": 85}))