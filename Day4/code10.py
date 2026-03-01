user_input = ('Hello','Hi',20,40.2,9.6j,[1,2],'PYTHON','JECRC',(1,2,3))
new_coll = {}

for i in user_input:
    if type(i) in [tuple,str,set]:
        l=len(i)
        if l%2==0:
            new_coll[i]=i[0]+i[-1]
        else:
            mid=i[l//2]
            new_coll[i]=mid

print(new_coll)















# for i in user_input:

#     if(type(i) in [str,tuple,set]):
#         l = len(i)
#         if(l%2==0):
#             new_coll[i] = i[0]+i[l-1] 
#         else:
#             new_coll[i] = i[l//2]

# print(new_coll)