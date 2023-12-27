num=int(input("Enter number"))
temp=num
rev=0
while num>0:
    digit = num%10
    rev=rev*10+digit
    num=num//10
print(f"The original number {temp} \n The reversed number is {rev}")
if temp==rev:
    print(f"The number is palyndrome {temp}={rev}")
else:
    print(f"The number is not a palyndrome {temp}={rev}")

