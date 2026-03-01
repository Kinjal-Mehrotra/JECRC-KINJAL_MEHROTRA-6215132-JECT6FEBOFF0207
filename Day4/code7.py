#wap to achieve desired output for the below given output
#Hello123@ --> hELLO123@

string=input("Enter a string: ")
l=len(string)-1
st=0
result=''

while(st<=l):
    
    char=string[st]
    val=ord(char)
    if 'A'<=char<='Z':
        ch=chr(val+32)
    elif 'a'<=char<='z':
        ch=chr(val-32)
    else:
        ch=char
    result+=ch
    st+=1

print(result)