class student:
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displaystudent(self):
        print("Roll No:",self.rollno)
        print("name of student:",self.name)
        print("course:",self.course)
        print("----------------------")

#first student object is created
stud1=student(10,"Jack","MCA")
stud2=student(16,"George","MCA")

#display
stud1.displaystudent()
stud2.displaystudent()
