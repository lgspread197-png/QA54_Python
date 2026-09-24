def print_configuration(**kwargs):
    print(type(kwargs),kwargs)

print_configuration(browser="safari",headless=True,timeout=10)
print(print_configuration())

def create_user3(**data):
    return data

user = create_user3(name="Kristina", role="Student")
print(user)

#user = create_user3("name":"Kris") неверно
print()

def for_example(a,b=15,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

for_example(2,name="Alex")