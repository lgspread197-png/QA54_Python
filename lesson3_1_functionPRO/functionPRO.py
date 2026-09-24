def greet(name):
    return f'Hello,{name}!'
result = greet("Kris")

print(result)

#result2 = greet() обязательно нужно ввести аргумент
#print(result2)

def create_user(name,role="user"):
    return {'name':name,'role': role}
print(create_user("Alex"))
print(create_user("Kristina","admin"))
print()

def cal_discount(prise,discount=20):
    return prise - (prise*discount/100)
print(cal_discount(2000))
print(cal_discount(2000,25))

def foo(a=2,b=2):
    return a+b
print(foo(5,3))

# def foo(a=2,b):
#     return a+b
# print(foo(5))

def add_tests(name,resalts=[]):
    resalts.append(name)
    return resalts

print(add_tests("test_registration"))
print(add_tests("test_ligin"))
print()

def add_tests(name,resalts=None):
    if resalts is None:
        resalts = []
    resalts.append(name)
    return resalts

print(add_tests("test_registration"))
print(add_tests("test_ligin"))
print()

def create_user2(username,email,role):
    return f'{username} ({email}) - {role}'

print(create_user2("Kris","test@gm.com","teamLead"))

print(create_user2(role="Project",username="Alex", email="test2@gm.com"))

print(create_user2("Kristina",role="QA",email="qa@gm.com"))
print()

