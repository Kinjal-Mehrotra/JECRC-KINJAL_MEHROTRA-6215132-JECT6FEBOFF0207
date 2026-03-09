#It is a type of inheritence in which properties will be derived from multiple parent class to single child class

class Parent_1:
    a=10
class Parent_2:
    b=20
class Parent_3:
    c=30
class Parent_4:
    d=40

class Child(Parent_1,Parent_2,Parent_3,Parent_4):
    pass

print(Child.a,Child.b,Child.c,Child.d)