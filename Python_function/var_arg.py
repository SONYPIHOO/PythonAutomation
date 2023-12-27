#variable length argument

def cal(a,b):
    sum=a+b
    diff=abs(a-b)
    mul=a*b
    print("Sum=",sum)
    print("Sub=",diff)
    print("mul=",mul)
    return sum,diff,mul

cal(10,20)

def cal1(*n):#variable length argument
    print(type(n))
    print(n)
    sum=0
    sub=0
    mul=1
    for i in n:
        sum+=i
        sub-=i
        mul*=i
    print(f"Sum of {n} is {sum}")
    print(f"sub of {n} is {sub}")
cal1(10,20,30,40,50,40,200)
