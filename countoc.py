names=input("enter first names seperated by space:").split()
count_a=sum(name.lower().count('a')for name in names)
print("otal occurence o 'a':",count_a)
