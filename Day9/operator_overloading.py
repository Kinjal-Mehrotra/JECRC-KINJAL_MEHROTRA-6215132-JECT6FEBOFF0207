'''
operator overloading - its a phenomenon of making the operators to work on user-defined data types by invoking respective magic methods 

magic method/ Dundar - special type of methods in which double underscores will be there at the starting and ending of method's name , 

example - __add__, __sub__,__mul__,__floordiv__, __truediv__, __mod__,

Q> If we don't use operator overloading then what will happen ?
A> FOr using the operators inside user defined data type we have to use operator overloading

Syntax 
    class ClassName:
        def __init__(self,val):
            self.val=val

            def __add__(self, ano_obj):
                return self.val+ano_obj.val

    obj1=ClassName(val1)
    obj2=ClassName(val2)
    obj1+obj2

    #how this looks like in background - obj1.__add__(obj2) = self.val.__add__(obj2.val) = self.val+obj2.val
'''

class MyDT:
    def __init__(self,val):
        self.val=val

    def __add__(self,ano_obj): #method 1
        return MyDT(self.val+ano_obj.val)
    
    def __add__(self,*args): #method 2
        sum=self.val
        for num in args:
            sum+=num.val
        return MyDT(sum)
    
    def __str__(self):
        return str(self.val)
    
    def __sub__(self,ano_obj):
        return self.val-ano_obj.val
    
    def __sub__(self,*args):
        substract=self.val
        for num in args:
            substract+=num.val
        return MyDT(substract)
    
    def __mul__(self,ano_obj):
        return self.val*ano_obj.val
    
    def __mul__(self,*args):
        multiply=self.val
        for num in args:
            multiply*=num.val
        return MyDT(multiply)

    def __floordiv__(self, ano_obj):
        return self.val//ano_obj.val
    
    def __truediv__(self, ano_obj):
        return self.val/ano_obj.val
    
    # def __mod__(self, ano_obj):
    #     return MyDT(self.val%ano_obj.val)
    
    def __mod__(self,*args): #method 2
        mod=self.val
        for num in args:
            mod%=num.val
        return MyDT(mod)
    
    
    # def add(self,*args):
    #     sum=self.val
    #     for num in args:
    #         sum+=num.val
    #     return sum
    
    # def sub(self, *args):
    #     sub=self.val
    #     for num in args:
    #         sub-=num.val
    #     return sub
    
    # def mul(self,*args):
    #     mul=1
    #     for num in args:
    #         mul*=num.val
    #     return mul

print("Result of addition:",MyDT(10)+MyDT(20))
print("Result of addition:",MyDT(15.10)+MyDT(25435.9898))
print("Result of multiple addition:",MyDT(15.10)+MyDT(25435.9898)+MyDT(30))
print("Result of substraction:",MyDT(1003)-MyDT(2055))
print("Result of multiplication:",MyDT(1003)*MyDT(2055))
print("Result of floor division:",MyDT(100)//MyDT(3))
print("Result of true division:",MyDT(36583568)/MyDT(20))
print("Result of modulus:",MyDT(1003)%MyDT(2055))
print("Result of multiple addition:",MyDT(15.10)+MyDT(25435.9898)+MyDT(30)+MyDT(40)+MyDT(100))
print("Result of multiple value multiplication:",MyDT(15.10)*MyDT(25435.9898)*MyDT(30)*MyDT(40)*MyDT(100))
print("Result of multiple value modulus:",MyDT(15.10)%MyDT(25435.9898)%MyDT(2))
# print("Result of multiple value addition:",MyDT.add(MyDT(10),MyDT(20),MyDT(40)))
# print("Result of multiple value substraction:",MyDT.sub(MyDT(10),MyDT(20),MyDT(40)))
# print("Result of multiple value multiplication:",MyDT.mul(MyDT(10),MyDT(20),MyDT(40)))


