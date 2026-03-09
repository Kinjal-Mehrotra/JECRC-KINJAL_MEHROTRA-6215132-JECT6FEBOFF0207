'''
lambda 
1. Lambda is a keyword which is used to create anonymous functions
2. For calling the lambda function, we can store the address of lambda inside a variable. By invoking the var_name, we can all the function

'''

#lmabda args:<exp>
result=lambda a,b:a+b
print(result(1,2))
print(result)

(lambda a,b: print(a*b))(int(input("Enter number 1:")),int(input("Enter number 2:")))

#Write to find the sqaure of a number if it is even
num=int(input("Enter a number: "))
if num%2==0:
    print(num*num)

result=lambda num:print(num**2) if num%2==0 else None
result(11)
(lambda num:print(num**2) if num%2==0 else None) (int(input("Enter a number: ")))

#Write a program to find the square of a number if it is even otherwise print cube 
(lambda num:print(num**2) if num%2==0 else print(num**3)) (int(input("Enter a number: ")))

#check whether a number is zero or positive or negative 
num1=int(input("Enter a number to check positive/negative/zero"))
# if num1>0:
#     print("Positive")
# else:
#     if num1<0:
#         print('Negative')
#     else:
#         print('Zero')

result1=lambda num: print('Positive') if num>0 else print('Negative') if num<0 else print('Zero')
result1(num1)


