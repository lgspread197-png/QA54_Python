def login(username,password):
    print(username,password)
    
    
data = ['admin','897654']
login(data[0],data[1])
(login(*data)) # разложи список на отдельные элементы, а я сама найду куда распечатать


user = {
    "username":"admin",
    "password":"897654"
}
login(**user)

user ={
    "username":"admin",
    "password":"897654",
    "remember_me":True    #SyntaxError: invalid syntax
}
login(**user)