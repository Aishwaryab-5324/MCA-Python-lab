class Rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        print("area of the rectangle with length",self.length,"and breath",self.breadth,"is ",a)
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print("primeter of rectangle with length",self.length,"and breadth",self.breadth,"is ",p)

#main program
l=int(input("enter length of rectangle:"))
b=int(input("enter breadth of rectangle:"))
obj1=Rectangle()
obj1.getdata(l,b)
obj1.area()
obj1.perimeter()
    
