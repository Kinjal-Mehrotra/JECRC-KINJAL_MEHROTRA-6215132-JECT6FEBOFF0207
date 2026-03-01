#Write a program in python to take a character from the user and check whether it is a vowel or consonant or digit or special character

'''
1. take a character from user
2. apply conditions one by one 
3. 
'''
val=input("Enter a character: ")

if val>='a' and val<='z' or val>='A' and val<='Z':
    if val.lower() in 'aeiou':
        print('vowel')
    else:
        print('consonant')
elif val>='0' and val<='9':
    print('digit')
else:
    print('special character')

