words=input("enter words seperated by spaces:").split()
longest=max(len(word) for word in words)
print("length of the longest word is:",longest)
