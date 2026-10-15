import re

print(re.search(r"@","test@gmail.com"))
print(re.search(r"[\w.]","test@gmail.com"))
print(re.search(r"\w.+@","test@gmail.com"))
print(re.search(r"[\w.]+@[\w]+","test@gmail.com"))