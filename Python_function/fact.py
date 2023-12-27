from math import factorial,sqrt

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

n=int(input("Enter the number"))
if n==0 or n==1:
    print(f"factorial of given {n} is {1}")
else:
    result=factorial(n)
    print(f"factorial of given {n} is {result}")

print("*"*20)
print(sqrt(16))
print(factorial(5))
