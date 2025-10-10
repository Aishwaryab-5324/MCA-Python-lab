str1=input("enter a word:")
length=len(str1)
if length>2:
    if str1[-3:]=='ing':
        str1+='ly'
    else:
        str1+='ing'
print("new string:",str1)
