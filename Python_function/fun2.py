def cal(a,b):
    sum=a+b
    diff=abs(a-b)
    mul=a*b
    div=a/b
    print("Sum=",sum)
    print("Sub=",diff)
    print("mul=",mul)
    print("div=",div)
    return sum,diff,mul,div

sum,diff,mul,div=cal(20,50)
print(sum)
print(diff)
print(div)
