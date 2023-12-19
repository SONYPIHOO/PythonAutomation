#if conditional statement
#if condition syntax if condition: code

name='Vishal'
class1="Auto"
if name=='Vishal':
    print("Hello",name)
    print("Hoe R u?")

#elif condition --
#if condition:
#   stat1
#else:
#   stat2

name=input("Enter the name")
print("The type of name is",type(name))
print("Name=",name)
if name=='Vishal':
    print("Hello",name)
    print("Hoe R u?")
else:
    print("Hello guest",name)

#if-elif-else condition
#if condition:
#   statments
#elif condition:
#   statements
#else:
#   statements
name=input("Entwr the name")
print("The type of name",type(name))
print("Name=",name)
if name=='Vishal':
    print("Hello ",name)
elif name=='kavya':
    print("Hello ",name)
elif name=='sony':
    print("Hello",name)
else:
    print("Hello guest")
