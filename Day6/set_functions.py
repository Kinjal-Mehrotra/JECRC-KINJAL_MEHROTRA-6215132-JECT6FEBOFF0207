'''
add
remove
discard
pop
clear
unique
union
intersection
difference
symmetric difference
'''
s1={1,2, True, False, 0,3+9j}

value=2
s1.add(value)
s1.add(100)
print(s1)
#we can only add immutable data types in set

s1.remove(3+9j)
print(s1)
# s1.remove(100) - if we try to remove an element that doesnt exist , it will throw an error 

s1.discard(1)
s1.discard(200) #doesnt throw an error if value doesnt exist

print(s1)

#pop randomly pops out the value
s1.pop()
print(s1)

s2={1,2,3}
s3={2,3,4}

s4=s2.union(s3,s1)
print(s4)

s5=s2.intersection(s3) #returns common elements
print(s5)

s6=s2.union({1,2,3},{4,6,5},{7,6,7})
print(s6)

s7=s2.difference(s3) #return uncommon elements from the set 1
print(s7)

s8=s2.symmetric_difference(s3)  #gives unique elements of each set
print(s8)

s1.clear()
print(s1)

