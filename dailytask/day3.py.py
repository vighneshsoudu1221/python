
# biggest of three numbers
"""
num1= int(input("enter a number:"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))

if num1>num2 and num1>num3:
    print("num1 is greater one:",num1)
elif num2>num3:
    print("num2 is greater one:",num2)
else:
    print("num3 is greater one",num3)
"""
# grade marks >70=A >60=B <60=c
"""marks=int(input("enter the marks:"))
if marks>=70:
    print("A")
elif marks>=60:
    print("B")
else:
    print("c")
"""

#electricity bill <= 100 =>5rs ,100 to 200= 7rs, 200 to 300 =10rs, >300 = 15
"""units = int(input("enter number of units:"))
if units<=100:
    bill= units*5
elif units<=200:
    bill=100*5+(units-100)*7
elif units<=300:
    bill=100*5+100*7+(units-200)*10
else:bill = 100*5+100*7+100*10+(units-300)*15
print("bill",bill)
"""

# nested if positive even or positive odd and other
"""num = int(input("enter a number:"))
if num>0:
    if num%2==0:
        print("positive even")
    else:
        print("positive odd")
else :
    print("other")
"""

# if given odd chiranjeevi even 2 to 6 balayya even 7 to 15 pawan kalyan even >15 prabhas
num = int(input("enter a number:"))
if num%2!=0:
    print("chiranjeevi")
else:
    if num>=2 and num<=6:
        print("balayya")
    elif num>=7 and num<=15:
        print("pawan kalyan")
    else:
        print("prabhas")
        
