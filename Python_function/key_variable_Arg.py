def cal(**args):
    print(type(args))
    print(args)
    print("args.get('name')",args.get("name"))
    sum=0
    for key,value in args.items():
        sum+=value
    print(f"Sum of {args.values()} is {sum}")

cal(a=10,b=20,c=30,d=400,e=50,f=60)

cal(k=100,l=200,m=300,n=400,o=50,f=60)
