vowel=['a','e','i','o','u','A','E','I','O','U']
s=input("enter a string :")
vowel_list=[]
for ch in s:
    if ch in vowel:
        vowel_list.append(ch)
print("vowels in the given string are:",vowel_list)
