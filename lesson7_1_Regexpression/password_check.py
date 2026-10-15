import re


def has_digits(password):
    return bool(re.search(r"\d",password))

print(has_digits("dr123456"))
print(has_digits("qwerty"))
print(has_digits("-1"))

