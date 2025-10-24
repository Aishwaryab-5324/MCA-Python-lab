rect1=lambda l,b:l*b
l=int(input("enter the value of l:"))
b=int(input("enter the value of b:"))
print("area of rectangle is",rect1(l,b))

square=lambda s:s*s
s=int(input("enter the value of s:"))
print("area of square is",square(s))

triangle=lambda b,h:(b*h)/2
b=int(input("enter the value of breadth:"))
h=int(input("enter the value of height:"))
print("area of triangle is",triangle(b,h))
