
#1 Create a class Student with the attributes name, roll_no, and marks. Create an object and display all the student details.
#Input: name = "Rahul" roll_no = 101 marks = 85 Output: Name: Rahul Roll No: 101 Marks: 85
"""
class Student:
    def __init__(self,n,r,m):
        self.name=n
        self.rollno=r
        self.marks=m
    def info(self):
        print("Name:",self.name,"Roll No:",self.rollno,"Marks:",self.marks)
obj=Student("Rahul",101,85)
res=obj.info()
"""
#2 Create a class Rectangle with attributes length and breadth. Create an object and calculate and display
#the area and perimeter of the rectangle.
#Input: length = 10 breadth = 5 Output: Area: 50 Perimeter: 30
"""
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def calucate(self):
        print("Area:",self.length*self.breadth,"perimeter:",2*(self.breadth+self.breadth))
ob=Rectangle(10,5)
ob.calucate()
"""
#3 Create a class Employee with attributes name, employee_id, and salary. Create an object and display the
#employee details. Also calculate the salary after adding a ₹5000 bonus.
#Input: name = "Arjun" employee_id = 101 salary = 30000 Output: Name: Arjun Empl
"""class Employee:
    def __init__(self,n,e,s,b):
        self.name=n
        self.employee_id=e
        self.salary=s
        self.bonus=b
    def info(self):
        print("Name:",self.name,"employee_id",self.employee_id,"salary:",self.salary+self.bonus)
ob=Employee("Arjun",101,30000,5000)
ob.info()
"""
#4 Create a class Mobile with attributes brand, model, and price. Create an object and display the mobile details.
#Input: brand = "Samsung" model = "A55" price = 30000 Output: Brand: Samsung Model: A55 Price: 30000
class Mobile:
    def __init__(self,b,m,p):
        self.brand=b
        self.model=m
        self.price=p
    def info(self):
        print("brand:",self.brand,"model:",self.model,"price:",self.price)
ob=Mobile("Samsung","A55",30000)
ob.info()
