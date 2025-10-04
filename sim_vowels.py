vowel=['a','e','i','o','u','A','E','I','O','U']
s=input("enter a string :")
count=0
for i in range(len(s)):
    if s[i] in vowel:
        count+=1
print("the number of vowels is",count)
