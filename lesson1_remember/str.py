s = "cat"
s = s.upper()
print(s)

s1 = 'Hello'
s2 = ("He"
      "llo")
s3 = """Line one
     Line two"""
print(s1)
print(s2)
print(s3)

print(s1,s2,s3)
print(s1,s2,s3,sep="\n")

#len()
s = "Hello my group!"
print(len(s))
print(s[0])
print(s[4])
print(s[-1])
print(s[14])
#print(s[140]) Error

s1 = "P y t h o n"
#len()1 2 3 4 5 6
#ind  0 1 2 3 4 5 -> index of last element = len()-1 or -1
print("__________________")

#slicing срезы  -> my_string[start:end:step]
print(s1[2:4])
text = "automation"
       #0123456789
print(text[2:6])
print(text[:4])  #from start to ind 4 exclusive
print(text[4:])  #from ind 4 to end string
print(text[:])   # all string
print(text[::2])  # every 2 symbol
print(text[::-1])  # reverse
print(text[5:100]) # no mistake

print("__________________")
name = "Mariia"
last_name = "Ivanova"
age =  25
print(name+ " " +last_name + "-" +str(age))
print(f"Hi my name is {name} and my last name is {last_name} and i'm {age}")

print("__________________")
#metods:
#upper()/lower()
raw = " Automation QA "
print(raw.upper())
print(raw.lower())

#strip()
print(raw.strip())
print(raw.strip().upper())

#split()\join()
cvs_line = "Login:Cart,Checkout,Mama,Papa"
parts = cvs_line.split(",") #['Login:Cart', 'Checkout', 'Mama', 'Papa']
print(parts)
print(" - ".join(parts))

print("__________________")
#replace()
msg = "Test failed:element not found"
print(msg.replace("failed","passed"))

#find() and index()
#find() -->-1, if substring is not found
#index()--> ValueError if substring is not found

s = "banana"
print(s.find("na"))
print(s.index("na"))

print(s.find("xyz"))  #-->-1
#print(s.index("xyz")) --> ValueError

#count()
print(s.count("na"))
