# 1. Syntax ERROR
# 2. Runtime Error
#print(test)#name error
a=int(input("Enter a value"))
b=int(input("Enter b value"))
try:
    print(f"sum={a+b}")
    print(f"sub={a-b}")
    print(f"Mul={a*b}")
    print(f"div={a/b}")#dividion error
except:
    print("Enter the integer value for a and b and value of b is greater than 0")
for i in range(1,10):
    print(f"square of {i} = {i*i}")

ls=[1,2,3]
print(ls[100])#index error
