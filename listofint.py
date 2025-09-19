nums= list(map(int,input("enter integers seperated by space:").split()))
result=[num if num<=100 else "over" for num in nums]
print(result)
