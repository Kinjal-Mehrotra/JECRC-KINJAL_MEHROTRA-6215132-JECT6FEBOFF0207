#Write a program to check whether the username and password is correct or not. If correct print login successfully, if not , do nothing

user={
    'username':'user123',
    'password':'****'
}

uid=input("Enter username: ")
upass=input("Enter password: ")

if(uid==user['username'] and upass==user['password']):
    print("Login successful")
else:
    print("Password or username is incorrect")
print("Program got ended")

#if-else-elif statements
'''
1. if statement 
2. if else
3. elif
4. nested
'''

#if statement block is also called TSB (True statement block)
#else statement block is also called FSB (False statement block)