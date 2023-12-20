num=234
temp=num
rev=0
while num>0:
    digit = num%10
    rev=digit+rev*10
    num=num/10

print(rev)
