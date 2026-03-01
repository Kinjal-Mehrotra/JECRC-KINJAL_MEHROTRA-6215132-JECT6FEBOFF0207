#given a list of integers nums and an integer target , return indices of the two numbers such that they add up to the target , you may assume that each input would have exactly one solution , and you may not use the same element twice, you can return in any order
def Twosum(list1,target):
    length=len(list1)
    for i in range(0,length):
        for j in range(i+1,length):
            if list1[i]+list1[j]==target:
                return ((i,j))

val=Twosum([1,2,5],4)
print(val)