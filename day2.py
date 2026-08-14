""" #not sholud used for taking an opposite result use

num = int(input("enter anumber:"))

if not (num%3==0 or num%5==0):
    print("odd")
else:
    print("even")
    
"""

#fizz buzz game 3%= fizz 5%= buzz 3% and 5% = fizz value not divisible buzz invalid
"""
num = int(input("enter a number:"))
if num%3==0  and num%5==0:
    print(" fizz buzz")
elif num%3==0:
    print("fizz")
elif num%5==0:
    print("buzz")
else:
    print("invalid")

"""
# biggest in given two numbers
"""num1 = int(input("enter a number :"))
num2 = int(input("enter a number :"))

if num1>num2:
    print("num1 big")
else:
    print("num2 big")
"""

# leap year or not year%4==0  and year % 100!=0 leap year , year %400 leap year , not leap year
"""year = int(input("enter a year:"))

if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not leap year")
    
"""

# discount amount
"""amount = int(input("enter the amount:"))
membership = input("do you have membership (yes/no):")
copun = input(" do you have copun (yes/no):")
if amount>1000:
   amount=amount-amount*0.10
if membership == "yes":
   amount=amount-amount*0.05
if copun == "yes":
   amount=amount-amount*0.05
else:
   print(" no discount")
   
print(" amount:",amount)
"""

   

    
