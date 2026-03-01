#WAP to take a character from the user and convert it into lowercase if its in uppercase or vice-versa

ch=input()
val=ord(ch)

if val>=65 and val<=90:
    ch=chr(val+32)
elif (val>=97 and val<=122):
    ch=chr(val-32)

print(ch)

# if ch.islower():
#     print(ch.upper())
# else:
#     print(ch.lower())
