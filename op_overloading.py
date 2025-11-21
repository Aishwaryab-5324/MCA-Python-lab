class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def area(self):
        return self.__length*self.__width
    def __lt__(self,other):
        return self.area()<other.area()

l1=float(input("enter length of rectangle 1:"))
w1=float(input("enter width of rectangle 1:"))
r1=Rectangle(l1,w1)

l2=float(input("enter length of rectangle 2:"))
w2=float(input("enter width of rectangle 2:"))
r2=Rectangle(l2,w2)

if r1<r2:
    print("rectangle 1 has smaller area than rectangle 2")
else:
    print("rectangle 1 has greater or equal area than recangle 2")
