#oops concepts demonstration

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Memory of self in add is ",id(self))
        return(self.a+self.b)
    def sub(self):
        print("Memory of self in sub is ",id(self))
        return self.a-self.b
    def mul(self):
        print("Memory of self in mul is ",id(self))
        return self.a*self.b
    def div(self):
        print("Memory of self in mul is ",id(self))
        return self.a/self.b
    def power(self):
        print("Memory of self in power is ",id(self))
        return self.a**self.b
# syntax to create object
# object_name=classname()

c=calculator(5,5)
# print(calculator.__dict__)
print("SUM=",c.add())
print("SUB=",c.sub())
print("MUL=",c.mul())
print("DIV=",c.div())
print("POWER=",c.power())
