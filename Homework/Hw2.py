#Task 1. Shopping cart
#var1
def clean_cart(cart):
    while "sold out" in cart:
        cart.remove("sold out")
    return cart

print(clean_cart(["milk", "sold out", "bread", "sold out", "coffee"]))
# ["milk", "bread", "coffee"]

#var2
def clean_cart2(cart,elem_del):
    while elem_del in cart:
        cart.remove(elem_del)
    return cart

print(clean_cart2(["milk", "sold out", "bread", "sold out", "coffee"],"sold out"))
# ["milk", "bread", "coffee"]
print(clean_cart2(["milk", "sold out", "bread", "sold out", "coffee"],"test"))
print()

#var3
def clean_cart2(cart,elem_del="sold out"):
    while elem_del in cart:
        cart.remove(elem_del)
    return cart

print(clean_cart2(["milk", "sold out", "bread", "sold out", "coffee"]))
# ["milk", "bread", "coffee"]
print()

#Task 2. Temperature report
def temperature_report(temperatures):
    result = []
    for i in temperatures:
        if i>25:
            result.append(i)
    return result

print(temperature_report([21, 28, 19, 31, 25, 27]))
# [28, 31, 27]

#Task 3. Fix negative balances
def fix_balances(balances):
    result = []
    for i in balances:
        if i<=0:
            result.append(0)
        if i>0:
            result.append(i)
    return result

print(fix_balances([120, -30, 50, -5, 0, 200]))
# [120, 0, 50, 0, 0, 200]
print()

#Task 4. Remove duplicates without set
def unique_items(items):
    result = []
    for i in items:
        if i not in result:
            result.append(i)
    return result

print(unique_items(["red", "blue", "red", "green", "blue"]))
# ["red", "blue", "green"]
print()

#Task 5. ADVANCED •Longest word
def longest_word(words):
    result = words[0]
    for i in words:
        if len(i)>len(result):
            result = i
    return result

print(longest_word(["cat", "elephant", "python", "coffee"]))
# "elephant"

