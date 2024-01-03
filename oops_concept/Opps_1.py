#oops concepts demonstration
#SYNTAX
# class classname:
#     def _init_(self):#constructor method optinal
#         stmt1
#         stmt2
#     def method1(self):#instancemethod(Optional)
#         stmt1
#         stmt2
#     def method(self):#classmethod(Optional)
#         stmt1
#         stmt2
#     def method3():#staticmethod(Optional)
#         stmt1
#         stmt2

class calculator:
    def __init__(self):
        print("Inside Constructor")
        print("ID of self is",id(self))
    def add(self,a,b):
        return(a+b)
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
# syntax to create object
# object_name=classname()

c=calculator()
print(calculator.__dict__)
print("SUM=",c.add(5,5))
print("SUB=",c.sub(5,5))
print("MUL=",c.mul(5,5))
print("DIV=",c.div(5,5))
