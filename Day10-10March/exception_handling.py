#Exception handling
'''
exception - unauthroized event 
flow of the execution of the program will be stopped
after that it will never execute the further code

keywords used in exception handling 
1. try - inside try block we will put the problem statement (the block of code due to which we might get an error)

2. else - its an alternative of try block , if we find out any error inside try block, interpreter will move forward towards else block 
if code is correct , it will give output 
if code is incorrect, it will give error 

3. except - its an important block , if we face any error inside else block also, it will be handled by except block
we put actual solution(resolution for error prone code) for the error 

4. finally - after getting error or after resolution forcefully if we want to execute any particular block of code , we use finally block 

pink/purple- exception
red - error
purple - warning

'''

# Exception handling approaches:
# 1. Specific exception handling
# 2. Generic exception handling
# 3. Default exception handling

'''Specific exception handling - if u know about the error / exception , if we know what kind of exception we might get
try:
    problem statement
except errorname:
    solution code 
'''

n1,n2=int(input("Enter number 1: ")),int(input("Enter number 2: "))
try:
    result=n1/n2
    print(result)
except ZeroDivisionError:
    print("please do not write 0 as second number ")

print("Code after try except 01")
print("Code after try except 02")


try:
    a,b,c=1,2
    print(a,b,c)
except ValueError:
    print("For performing MVC< number of variables should be equal to number of values !!!! Not enough values to unpack")

# try:
#     print(a,b,c)
# except NameError:
#     print("Identifiers are not there in the memory")


'''
Generic exception handling - in this u dont have to mention the speicifc class name , we can just use the parent class name called "Exception"
drawback - using "Exception" class name , it can't handle keyboard interruptions

'''
try:
    print(a,b,c)
except Exception:
    print("Identifiers are not there in the memory")


'''This will still give an error'''
# import time 
# try:
#     while True:
#         print(time.time())
# except Exception:
#     print("Loop got stopped")

import time 
try:
    while True:
        print(time.time())
except KeyboardInterrupt:
    print("Loop got stopped")



#default exception handling - don't need to add anything, we can handle all types of error except of syntaxerror 

import time 
try:
    while True:
        print(time.time())
except :
    print("Loop got stopped")



'''

raise --> it is a keyword, which help us to throw an error in between a program.

Exception Creation,

1. Custom Exception (raise)
2. user defined Exception (raise)
3. Assertion Exception (assert)

'''

'''
Custom Exception:
    1. we use pre built exception class according to our requirement.

    raise ValueError('message')

    ValueEorror: message`   
'''

# num = 17

# if num >= 18:
#     print('Eligible for Voting & Driving')

# else:
#     raise NameError('Age should be greater than or equal to 18!')


'''
-- User-defined Exception

    1. It is a type of exception in which we can create our own exception classess based upon our own requiement. we can also provide name to those classess based upon our own requirement. we can also provide name to those classess according the user cases
'''

class MyException(Exception):
    print("This is exception class")

# raise MyException('This is my exception class!!!')

n1 , n2 = 18 , 0

if n2==0:
    raise MyException
else:
    print(n1/n2)


'''

Assertion Exception (assert)
-- Assertion exception can be created by using one keyword called "assert"

assert <condition>, print(ERROR)
print(output)

'''

s = input('Enter a String:')

assert s == s[::-1], 'Given String is not a palindrome!'
print(f'Given String {s} is a palindrome!')

