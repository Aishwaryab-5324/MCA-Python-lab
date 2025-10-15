def sumofdigit(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    print("sum of digits of number:",sum)

a=int(input("enter a number:"))
sumofdigit(a)
