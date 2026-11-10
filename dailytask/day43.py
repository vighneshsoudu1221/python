#Create a class Employee with attributes name and salary. Create a child class Manager that inherits
#from Employee and adds department. Display all three details using the child object.
#Input: Name: Ravi Salary: 45000 Department: IT Output: Name: Ravi Sala
"""class Employee:
    def __init__(self,n,s):
        self.name=n
        self.salary=s
    def info(self):
        print("Name:",self.name)
        print("Salary:",self.salary,end=" ")
class Manager(Employee):
    
    def __init__(self,n,s,d):
        super().__init__(n,s)
        self.depart=d
    def info(self):
        super().info()
        print("Department:",self.depart)
ob=Manager("vikky",23456789,"cse")
ob.info()"""
#2 Create a parent class Mobile with a method power_on() that prints "Mobile Powered On".
#Create a child class SmartPhone with a method use_app()
#that prints "Using Instagram". Create a SmartPhone object and call both methods. Output: Mobile Powered On Using
"""class Mobile:
    def power_on():
        pass
    def dispaly(self):
        print("mobile powered on",end=" ")
    
class SmartPhone(Mobile):
    def use_app():
        super().power_on()
    def dispaly(self):
        super().dispaly()
        print("Using Instagram")

ob=SmartPhone()
ob.dispaly()
  """  
#Create three classes: Student, Marks, and Result. Student stores the
#student's name. Marks inherits Student and stores marks. Result inherits Marks and displays the name,
#marks, and "Pass" if marks are 40 or above. Input: Name: Anil Marks: 75 Output: Name
"""
class Student:
    def __init__(self,n):
       self.name=n
class Marks(Student):
    def __init__(self,n,m):
        super().__init__(n)
        self.marks=m
        pass
class Result(Marks):
    def __init__(self,n,m):
        super().__init__(n,m)
        if self.marks>40:
            print(f"Name:{self.name} marks:{self.marks} is pass")
        else:
            print("fail")
ob=Result("vikky",56)"""
#Create a parent class Company with a method company_name() that prints "ABC Technologies".
#Create two child classes Developer and Tester, each having their own method to display their role.
#Create objects of both child classes and display the company name
"""class Company:
    def company_name(self):
        print("ABC Techologies")
class Developer(Company):
    def display(self):
        super().company_name()
class Tester(Developer):
    def display(self):
        super().display()
ob=Tester()
ob.display()"""
#Create a parent class Payment with a method pay() that prints "Payment Processing".
#Create a child class UPIPayment that overrides the pay() method and prints "Paid using UPI".
#Create an object of UPIPayment and call pay(). Output: Paid using UPI
"""class Payment:
    def pay(self):
        print("payment processing")
class UPIPayment(Payment):
    def pay(self):
        print("paid using Upi")
oo=UPIPayment()
oo.pay()"""
