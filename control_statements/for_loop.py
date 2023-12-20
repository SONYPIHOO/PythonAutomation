# for and while loop demonstration

ls = [4,5,6,'Vishal',True]
t = (4,5,6,'Vishal',True)
d={1:"Vishal",2:"Adhya",3:"Pranjali",4:"Kavya"}
s={1,2,3,4,5,5,6,6}
fs=frozenset({1,4,5,6,7,7,7,8})

#syntax for
#for value in iterativedata:
#   statements

for i in ls:
    ind=ls.index(i)
    print(f"In tuple {t} The value of {i} present {ind} index")
print("*"*50)
for j in t:
    ind=t.index(j)
    print(f"The value of {j} present {ind} index")

table = ['prifile','email','phone','transaction']
print("*"*50)
for tb in table:
    print(f"select count(*) from {tb}")

print("*"*50)
for key, values in d.items():
    print(f"Dictionary {d}, The key is {key} and value is value")

print("*"*50)
print("the set is",s)
for k in s:
    print(f"Set {s}, The value is {k}")

for i in range(1,10):
    print(i)

print("*********EVEN NUMBERs**********")
for i in range(1,10):
    if i%2==1:
        print(i)
