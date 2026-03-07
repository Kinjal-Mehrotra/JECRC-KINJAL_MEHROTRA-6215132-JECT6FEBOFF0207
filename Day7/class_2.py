#constructor - __init__ (magic method to initialize state of an object)

'''
self stores memory address of the object
self points towards the object - for example self points to tata
class class_name:
    properties

    def __init__(self,arg1,arg2,...,argn):
        self.arg1=arg1
        self.arg2=arg2
        self.arg3=arg3
        .
        .
        .
        self.argn=argn

'''

class Car:
    #below variables are known as Properties/states/members
    wheelers=4
    engine='Petrol'
    base_speed='40kmph'
    max_speed='120kmph'
    gears=4

    def __init__(self,air_bags,security,base_budget,no_of_variants,total_sale):
        self.air_bags=air_bags
        self.security=security  
        self.base_budget=base_budget
        self.no_of_variants=no_of_variants
        self.total_sale=total_sale

    #adding functionality
    def display_properties(self):
        print({

            'wheelers':self.wheelers,
            'engine':self.engine,
            'base_speed': self.base_speed,
            'max_speed' : self.max_speed,
            'gears': self.gears,
            'air_bags':self.air_bags,
            'security':self.security,
            'base_budget': self.base_budget,
            'varient' : self.no_of_variants,
            'total_sale': self.total_sale
            })
        
    def update_base_speed(self,new_base_speed):
        self.base_speed=new_base_speed
        print(f"New base speed: {self.base_speed}")

    def update_max_speed(self,new_max_speed):
        self.max_speed=new_max_speed
        print(f"New max speed: {self.max_speed}")

    @classmethod
    def update_gears(cls,new_gears):
        cls.gears=new_gears
        print(f'No of gears: {cls.gears}')

#using a constructor , we used less line of codes to create object properties
tata=Car(True,'Level 5','2L',12,100000)
tata.update_gears(5)
print("Tata Properties before updation")
tata.display_properties()
print("Tata properties after updation")
tata.update_base_speed('60kmph')
tata.update_max_speed('140kmph')
tata.display_properties()



mahindra=Car(True,'Level 4','4L',20,250000)
# tata=Car()
# tata.engine=['Petrol','Diesel','EV'] #modifications done with respect to an object
# tata.air_bags=True
# tata.no_of_airbags=4
# tata.base_budget='2L'
# tata.no_of_variants=12
#to add 5 more properties , we have written 5 line of code, which is very time consuming and is prone to error