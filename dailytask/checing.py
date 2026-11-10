class Student:
    def __init__(self,n,m):
        self.name=n
        self.marks=m
        print(self.name,self.marks)
    def info(s):
        print(s.name,s.marks)
ob=Student("vignesh",39)
ob.info()
