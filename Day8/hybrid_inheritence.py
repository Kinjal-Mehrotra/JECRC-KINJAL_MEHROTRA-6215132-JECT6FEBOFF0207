#Hybrid inheritence - type of inheritence that is a mixture of other inheritence types

class A:
    a=30

class B(A):
    b=40

class C(A):
    c=50

class D(B):
    d=90

class E(C):
    e=100

class F(D,E):
    pass

obj1=C()
print(obj1.a)

obj2=E()
print(obj2.e)
print(obj2.c)

obj3=F()
print(obj3.d)
print(obj3.e)
