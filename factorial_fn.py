def factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result

num=int(input("enter a number to find factorial:"))
print("factorial of given number:",factorial(num))
