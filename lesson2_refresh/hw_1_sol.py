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
    return filename.lower().endswith(".py")

print(is_python_file("lesson.py"))
print(is_python_file("HOMEWORK.PY"))
print(is_python_file("lesson.Py"))
print(is_python_file("HOMEWORK.pY"))
print(is_python_file("notes.txt"))

print("________________")
#Task4 Replace Words
def fix_message(message):
    return message.replace("bad","good")

message = "bad weather, bad mood"
result = fix_message(message)
print(result)
print(message)

#Task5 Count a Letter
def count_letter(text, letter):
    return text.lower().count(letter.lower())

print(count_letter("Programming", "g"))
print(count_letter("Mississippi", "I"))

print("________________")
#Task6 Create a Short Login
def create_login(first_name, last_name):
    #first_name = first_name.strip().lower()
    #last_name = last_name.strip().lower()
    #return first_name+ "." +last_name
    return f"{first_name.strip().lower()}.{last_name.strip().lower()}"

print(create_login("  Anna ", " SMITH  "))

#Task7_Bonus 1. Split Full Name
def split_name(full_name):
    return full_name.strip().split()

print(split_name("  Anna   Smith  "))

#Task8_Bonus 2. Simple Password Check
#var1
def check_password(password):
    if len(password)<8:
        return False
    if " " in password:
        return False
    if password.isalpha():
        return False
    return True

print(check_password("python123"))
print(check_password("python"))
print(check_password("python 123"))

print()
#var2
def check_password_1(password):
    if len(password)<8:
        return False
    for char in password:
        if char.isspace():  #проверяет побуквенно пробел буква или нет
            return False
        if password.isalpha():
            return False

print(check_password_1("python123"))
print(check_password_1("python"))
print(check_password_1("python 123"))

print()
#var3
def check_password_2(password):
    return len(password)>8 and " " not in password and not password.isalpha()

print(check_password_2("python123"))
print(check_password_2("python"))
print(check_password_2("python 123"))