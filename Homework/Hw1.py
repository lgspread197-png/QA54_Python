#Task1 Clean a Name
def clean_name(name):
    return name.strip().title()

print(clean_name("   anna smith   "))
print(clean_name("DAVID COHEN"))

#Task2 Normalize an Email
def normalize_email(email):
    return email.strip().lower()

print(normalize_email("  Anna.Smith@Example.COM  "))

#Task3 Check a File Name
def is_python_file(filename):
    if filename.lower().endswith(".py"):
        return True
    else:
        return False

print(is_python_file("lesson.py"))
print(is_python_file("HOMEWORK.PY"))
print(is_python_file("lesson.Py"))
print(is_python_file("HOMEWORK.pY"))
print(is_python_file("notes.txt"))

#Task4 Replace Words
message = "bad weather, bad mood"
def fix_message(message):
    return message.replace("bad","good")

result = fix_message(message)
print(result)
print(message)

#Task5 Count a Letter
def count_letter(text, letter):
    return text.lower().count("g")

print(count_letter("Programming", "g"))

def count_letter(text, letter):
    return text.upper().count("I")

print(count_letter("Mississippi", "I"))

def count_letter(text, letter):
    return text.lower().count(letter.lower())

print(count_letter("Programming", "g"))
print(count_letter("Mississippi", "I"))

#Task6 Create a Short Login
def create_login(first_name, last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()
    return first_name + "." + last_name

print(create_login("  Anna ", " SMITH  "))

#Bonus 1. Split Full Name
def split_name(full_name):
    return full_name.strip().split()

print(split_name("  Anna   Smith  "))

#Bonus 2. Simple Password Check
def check_password(password):
    password = password.strip()
    if password.isalnum() and len(password)>8:
        return True
    else:
        return False

print(check_password("python123"))
print(check_password("python"))
print(check_password("python 123"))