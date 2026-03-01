#WAP to find out the maximum number 

l=[10,2.2,5,"Hello",[100,2000],99.0]
st=0
length=len(l)-1
max=float('-inf')
while(st<=length):
    if(type(l[st]) in [int,float]):
        if max<l[st]:
            max=l[st]
    st+=1
print(max)

