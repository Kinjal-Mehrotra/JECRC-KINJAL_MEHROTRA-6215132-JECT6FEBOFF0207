'''
Polymorphism 
Using the same name or operator to perform two or more different operation operations.

In, Python if we want to perform method overloading then it will act as method overriding in other programming languages, based on number of arguments, the respective method block will get executed. But in python it will never happen (as then same name the memory address will get overridden )

Method Overriding is a phenomenon of overriding the prev method’s address with the latest one 

Is it possible to perform Method overloading normally no, but we can implement it using monkey patching 

'''

class Temp:

    def sum(self, a, b):
        print(a+b)
    
    add_two_nums = sum

    # monkey patching : It is the process of storing the prev methods address inside a variable before overriding the method area address using that var, we can access the prev method memory address.
    
    def sum(self, a, b, c):
        print(a+b+c)

obj = Temp()
# obj.sum(10,20)
obj.add_two_nums(10,20)
obj.sum(10,20,30)