# это способ написать малую часто одноразовую функцию (простые и короткие формулы), пример
def double(x):
    return x*2

double_lambda = lambda x:x*2   #здесь: означает return
double_lambda2 = lambda x:x*2 if x>0 else -x  # 3

print(double(4))
print(double_lambda(4))
print(double_lambda2(-3))

print("____________")

add = lambda x,y:x+y  # задаем х и у, где return х и у складываем
print(add(3,4))

is_even = lambda p:p%2==0
print(is_even(8))  #True
print(is_even(5))  #False

grades = [90,75,88,63,100,81]
even = list(filter(lambda x:x%2==0,grades))
odd = list(filter(lambda x:x%2!=0,grades))

print("четные оценки ", even)
print("нечетные оценки ", odd)
