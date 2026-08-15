"""pin=7993
d=1
show_menu = False
while d<=3:
    mypin = int(input("enter a number:"))
    if mypin==pin:
       print("vaild")
       show_menu=True
       break
    else:
       print(" pin invalid ")
    d=d+1
 
else:
    print("your acccount is blocked")
if show_menu == True:
    balance = 2000
    while True:
     print("1. deposite")
     print("2. withdraw")
     print("3. checkbalance")
     print("4. exit")

     ch = int(input("choice your opion (1/2/3/4)"))
     if ch == 1:
         amt = int(input("enter your amount"))
         if amt%100==0 or amt%500==0:
             print("sucssesfully deposite")
         else:
             print("denamination check ")
     elif ch == 2:
         amt=int(input("enter our amount"))
         if amt%100==0 or amt%500==0:
             balance= balance-amt
             print("collect your money:")
         else:
             print("check the denamination")
     elif ch == 3:
         print("available balance ",balance)
     elif ch == 4:
         print("thank you for visiting see you again")
         break 
     else:
         print("choice correct opion")
   """

"""# lcd
num1 = int(input("enter a number:"))#78
num2 = int(input("enter a number:"))#65
small=0
d=2
if num1>num2:#78>65
    small=num2#65
else:
    small=num1
while d<=small:
    if num1%d==0 and num2%d==0:
        print(d)
        break
    d=d+1
else:
     print("Not a lcd") 

"""
#gcd
num1 =int(input("enter a number:"))
num2 =int(input("enter a number:"))
small=0
d=2
if num1>num2:
    small=num2
else:
    small=num1
while d<=small:
    if num1%d==0 and num2%d==0:
        if small==d:
            print(d)
            break
    d=d+1
else:
    print("not a gcd")
    
    
    
