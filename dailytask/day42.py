
#1 Create a BankAccount class with a private variable balance. Create methods: deposit(amount)
#withdraw(amount) displaybalance()
"""
class BankAccount:
    def __init__(self,b,d,w):
        self.__balance=b
        self.deposit=d
        self.withdraw=w
    def deposite(self):
        print("diposit amount:",self.deposit)
        self.__balance=self.__balance+self.deposit
    def withdraws(self):
        print("withdraw anmount:",self.withdraw)
        self.__balance=self.__balance-self.withdraw
    def display(self):
        print("balance amount:",self.__balance)
ob=BankAccount(2000,500,200)
ob.deposite()
ob.withdraws()
ob.display()
"""

#2 Create an Employee class with a private variable salary.
#Create: setsalary(salary) getsalary() The salary should be changed only through setsalary().
"""
class Employee:
    def __init__(self,s):
        self.__salary=s
    def getsalary(self):
        self.salary
    def setsalary(self):
        self.__salary=800
        print(self.__salary)
ob=Employee(500)
ob.setsalary()"""
#3 Create a User class with private variables username and password. Create a method: login(username, password)
#The method should print Login Successful only when both username and password match.
"""
class User:
    def __init__(self,u,p):
        self.__user=u
        self.__password=p
    def login(self,ul,pl):
        self.userl=ul
        self.pssl=pl
        if self.userl==self.__user and self.pssl==self.__password:
            print("login Successful")
        else:
            print("pass or user unmacth")
ob=User("vikky",12345)
ob.login("vikky",12345)
"""
#4 Create a Temperature class with a private variable temperature. Create: settemperature(value) gettemperature()
class Temperature:
    def __init__(slef,t):
        

