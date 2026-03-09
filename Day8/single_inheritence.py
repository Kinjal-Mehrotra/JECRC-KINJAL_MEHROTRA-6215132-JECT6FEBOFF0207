'''
1. Single
2. Multi-level
3. Multiple
4. Hierarchical 
5. Hybrid
'''
#Single Level Inheritence
#single level - we wil have a single parent and child class , also the properties will be derived only one time 

#parent class or super class - the class from which we are going to derive the properties , is known as parent class
class Parent:
    bank_balance="54L"
    def desc(self):
        print('I am a parent class')
    def __init__(self, *members):
        self.members=members

#child class or sub class - the class in which we are going to derive the properties is known as child class
#constructor chaining - calling parent class constructor from inside child class constructor
#method chaining - calling parent class method from inside child class method 

class Child(Parent):
    def __init__(self,child_name,*args):
        super().__init__(args)
        self.child_name=child_name
    def desc_method(self):
        super().desc()
        print("THis is the child class")

print(Child.bank_balance)
Child.desc("hi")

obj=Child('Kinjal','Mom','Dad')
print(obj.child_name)
obj.desc_method()