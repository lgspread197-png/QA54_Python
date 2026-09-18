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
print(clean_cart2(["milk", "sold out", "bread", "sold out", "coffee"],"empty"))
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
    result2 = []
    for i in balances:
        if i<=0:
            result2.append(0)
        if i>0:
            result2.append(i)
    return result2

print(fix_balances([120, -30, 50, -5, 0, 200]))
# [120, 0, 50, 0, 0, 200]
print()

#Task 4. Remove duplicates without set
def unique_items(items):
    result3 = []
    for i in items:
        if i not in result3:
            result3.append(i)
    return result3

print(unique_items(["red", "blue", "red", "green", "blue"]))
# ["red", "blue", "green"]
print()

#Task 5. ADVANCED •Longest word
def longest_word(words):
    result4 = words[0]
    for i in words:
        if len(i)>len(result4):
            result4 = i
    return result4

print(longest_word(["cat", "elephant", "python", "coffee"]))
# "elephant"

