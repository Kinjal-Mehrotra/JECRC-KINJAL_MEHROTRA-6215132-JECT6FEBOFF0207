#get method
d={1:1,2:2,(1,2,3):(1,2,3)}
print(d)
print(d.get(2))

d.pop(2)
print(d)
# d.pop(2) - if key doesnt exist it will throw a keyerror

d.popitem()
print(d)

user={
    'username':'user123',
    'password':'****',
    'location':'IN'
}

# user.popitem()
# user.popitem()
# user.popitem()
# print(user)

user['password']='123'
user.update({'password':'9999'})
print(user)


print(type(user.items()))
print(user.keys())
print(user.values())

