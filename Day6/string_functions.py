'''THere are two types of inbuilt functions 
1. utility functions
2. function for particular data type
'''

'''
Inbuilt functions
1. lower
2. uppper
3. capitalize
4. title
5. strip
6. lstrip
7. rstrip
8. replace
9. index
10. split
11. join
12. startswith
13. endswith
14. isdigit
15. isalpha
16. islower
17. isupper
'''
s="Python"
print(s.lower())

upper_case=s.upper()
print(upper_case)

#to know more about the method 
help(str.capitalize) 

print('pYTHON is great'.capitalize())

print('pYTHON is great'.title())

#strip methods
str1="   Python Is a great language     ---"

print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
print(str1.rstrip('-'))


#replace function
help(str.replace)
str="Good morning, have a Good day"
print(str.replace('G','g',1))

#index function
print(str.index('e'))
#gives an error if substring is not present 

print(str.find('z'))
print(str.find('m'))
#returns -1 if index is not found

list1=str.split()
print(list1)
str2="I-LOVE-PYTHON-PROGRAMMING-LANGUAGE"
list3=str2.split('-')
print(list3)

#join function
print(' * '.join(list3))

print("1.",str2.startswith('i'))
print("2.",str2.startswith('I'))
print("3.",str2.endswith('*'))
print("4.",str2.islower())
print("5.","HHH".isupper())
print("6.","Hello world".isalpha())
num="6565656"
print("7.",num.isdigit())
print("8.","ABc".isupper())

