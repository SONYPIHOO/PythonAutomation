#Lambda Functions or anonymus function
#syntax
#lamda arguments : expression

cal=lambda a,b: a+b

print("Lamda output is ",cal(10,20))

largest=lambda a,b: a if a>b else b

print(largest(100,20))

upper=lambda col:col.upper()

print(upper('vishal'))

trim_upper=lambda col:col.strip().upper()
print(trim_upper(' vishal '))
