'''

Abstraction - hiding the internal implementation and showing only functionality to the end user

abstract method - if method/function consists only of declaration not definition then it wil be called as abstract method

abstract class - if a class consist of atleast one abstract method, it will be considered as abstract class 

concrete class - if a class doesn't have an abstract method ,then it is known as concrete class

abc:module
ABC:abstract base class

abstract class cannot be instantiated without implementing the abstract methods


'''
from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


class SBI_ATM(ATM): #concrete class
    # you can only add those methods that have been declared in ATM class
    def generate_pin(self):
        print("It is used to generate ATM pin")

    def forget_pin(self):
        print("It is used to forget ATM pin")

    def check_balance(self):
        print("It is used to check balance")

    def withdraw(self):
        print("It is used to withdraw money")

    def deposit(self):
        print("It is used to deposit money")



obj=SBI_ATM()
obj.generate_pin()
obj.forget_pin()
obj.check_balance()
obj.withdraw()
obj.deposit()