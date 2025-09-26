num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
num3=float(input("enter the third number:"))
if(num1>num2)and(num2>num3):
    large=num1
elif(num2>num1)and(num2>num3):
    large=num2
else:
    large=num3
print("the largest number is",large)
