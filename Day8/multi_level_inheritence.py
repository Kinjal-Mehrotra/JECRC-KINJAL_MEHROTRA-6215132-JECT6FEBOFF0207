#multi level inheritence/ sequential - it is a type of inheritence in which the properties will be derived from one to another class by considcering more than one level 

class Class_1:
    a='class 1'

class Class_2(Class_1):
    b='class 2'

class Class_3(Class_2):
    c='class 3'

class Class_4(Class_3):
    d='class 4'

class Class_5(Class_4):
    e='class 5'

obj=Class_5()
print(obj.a,obj.b,obj.c,obj.d,obj.e)
