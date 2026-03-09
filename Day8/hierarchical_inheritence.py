#It is a type of inheritence in which the properties will be derived from single parent class to multiple child class

class Parent:
    gold='2kg'
    silver='10kg'
    no_of_flats=12


class YoungestBrother(Parent):
    name='Daniel'

class ElderBrother(Parent):
    my_name='Rob'

class Sister(Parent):
    sis_name='Ben'

print(YoungestBrother.gold)
print(ElderBrother.silver)
print(Sister.no)
