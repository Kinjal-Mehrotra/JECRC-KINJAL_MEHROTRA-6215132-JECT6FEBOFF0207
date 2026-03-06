'''
append
insert
extend
pop
remove
clear
sort
reverse
index
count
'''

list1=[1,2,3]
list2=[5,6]
list1.append(100)
print(list1)

list1.insert(0,0)
print(list1)

list1.extend(list2)
print(list1)

list1.pop()
print(list1)

list1.remove(100)
print(list1)

s1={1,2,3}
s2={'a':1,'b':2}
list1.extend(s1)
print(list1)
list1.extend(s2)
print(list1)


# help(list.clear)

# help(list.sort)
list1.pop()
list1.pop()
list1.sort(reverse=False)
print(list1)

list1.sort(reverse=True)
print(list1)

list1.reverse()
print(list1)


print(list1.index(5))
# print(list1.index(100)) - if value doesnt exist , we get ValueError
print(list1.count(3))
print(list1.count(100))

list1.clear()
print(id(list1))
