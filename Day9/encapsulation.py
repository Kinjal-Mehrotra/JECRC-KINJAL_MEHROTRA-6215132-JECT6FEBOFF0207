'''
Encapsulation:

1. It is used to provide security to the data (data here means variables/properties/methods present inside class)

How to provide security to data ?
To provide security to data we have to use access specifier
1. Public
2. Private
3. Protected (Soft barrier using _)

Access specifier - it describes who can access the class members

'''
#example for public access specifier 
class Temp:
    a,b,*c,d='HELLO'

    def greeting(self):
        print('GOOF AFTERNOON USER: ')

# obj=Temp()

class C2(Temp):
    pass

class Temp2:
    
    _a=10 #private member
    _b='I LOVE PYTHON' #protected member - soft barrier


obj2=Temp2()
print(obj2._a)
print(obj2._b)

#class with private members
class Temp3:
    __a=100
    __string_1="Private member string of class Temp3"
    
    def __status(self):
        print("Class name is Temp3")

obj3=Temp3()
# print(obj2.__a) - will throw an error as it is private member
# print(obj3.__status())

'''
ways of accessing private members:
1. By using syntax
2. by using get and set method
3. by using @property decorator (setter)
'''
#1. By using syntax
'''
(by using which u r accessing)._(by which class u r accessing)__(mention the property/method name)
objname/classname._CN__prop_name/__method_name  (Accessing)

objname/classname._CN__member_name = new_val (modify) 
'''
print("Printing private members of class Temp 3")
print(obj3._Temp3__a)
print(obj3._Temp3__string_1)

print("Modifying private members of class Temp 3")
obj3._Temp3__a='0123456789'
print(obj3._Temp3__a)

def new_method():
    print("Modified the orignal private method of class Temp3")

obj3._Temp3__status=new_method
obj3._Temp3__status()

#2. using set and get methods
print("Using set and get methods:")
class Temp4:
    __a=1000
    def __status(self):
        print('class name is Temp4')
    def get(self):
        print(self.__a)
    def set(self,new_val):
        self.__a=new_val

obj4=Temp4()
obj4.get()
obj4.set(1500)
obj4.get()

#3. using property decorator
print("Using property decorator:")
class Temp5:
    __a=2000
    @property
    def decorator(self):
        print(self.__a)
    @decorator.setter
    def set(self, new_val):
        self.__a=new_val

obj5=Temp5()
obj5.decorator
obj5.set=2000000
obj5.decorator