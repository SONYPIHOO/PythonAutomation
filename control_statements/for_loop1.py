#nested loop and branching
print("Nested loops")
n=int(input("Enter Number"))
for i in range(1,n+1):
    for j in range(1,n-i):
        print(chr(64+j),end=" ")
    print()








