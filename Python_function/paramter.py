#calling a function pos, keyword, default argument

def sum(a,b):
    print("Value of a is ",a)
    print("Value of b is ",b)
    print(f"sum of {a} and {b} is {a+b}")

sum(10,20)#positional arguments
print("_"*20)
sum(b=20,a=10)#keyword arguments
print("_"*20)
sum(10,b=200)
print("_"*20)

def welcome(marks,name='Vishal'):#default arguments
    print("Welcome "+name+" Marks "+str(marks))

welcome(64)

