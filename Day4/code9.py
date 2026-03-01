# dict={1:11,2:22}

# for key, value in dict.items():
#     print(key,value)

dict={'a':1,'b':2,'c':3,'d':4}
new_dict={}

for index in dict:
    new_dict[dict[index]]=index

print(new_dict)

