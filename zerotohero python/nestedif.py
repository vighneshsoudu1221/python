#1.Given x = 10 and y = 5, write a Python program to determine if x is greater than y. 
#If x is greater than y,check if it's also greater than 15 and print appropriate 
#messages accordingly.  
"""x=10
y=5
if x>y:
    if x>15:
        print(" x is greatest")
    else:
        print("x is small")
"""
#2. Write a Python program that takes a grade as input and prints the corresponding 
#letter grade. If the grade is less than 70, also print "You failed."
"""grade=int(input("enter a number"))
if grade>70:
    if grade>=90 and grade<=100:
        print("A")
    if grade>=80 and grade<90:
        print("B")
else:
    print("you are failed")
"""
#3. Write a Python program to check if a person is eligible for a credit card based on 
#their age and income.If the person is underage, print "You are underage." If they 
#are of age but have an income below $30,000, print "Your income is too low for a 
#credit card."
"""age = int(input("enter your age "))
if age>18:
    income=int(input("enter your income"))
    if income>30000:
        print("you can get the cradit card")
    else:
        print("your income is low")
else:
    print("you are underage")"""
#4.Write a Python program to determine if a given number num is even or odd. If it's 
#even, check if it's greater than 10 and print appropriate messages.  
"""num = int(input("enter a number"))
if num%2==0:
    if num>10:
        print("message")
    else:
        print("not greater")

else:
    print("odd number")
"""
#5. Write a Python program that calculates the ticket price for a theme park based on 
#age and height. If a person isunder 12 years old and under 4 feet tall, their ticket 
#price is $10. If they are under 12 but 4 feet tall or taller,their ticket price is $15. 
#For individuals 12 and older who are 4 feet tall or taller, the ticket price is $20.  
"""age=int(input("enter how many years are you"))
feet=int(input("enter your feet"))
if age<12:
    if age<12 and feet<4:
        print("ticket price is 10$")
    else:
        print("ticket price is 15$")

else:
    if age>=12 or feet>=4:
        print("ticket price is 20$")
"""

#6.Write a Python program for user authentication. Ask the user to enter their 
#username and password. If both theusername and password are correct, print 
#"Access granted." If the username is correct but the password is incorrect,print 
#"Incorrect password." If the username is incorrect, print "Invalid username."  
"""use="venorx_650"
pss="@vighnesh@"
user=input("enter your user name:")
password=input("enter your password:")
if user==use and password==pss:
    print("access granted")
else:
    if user==use:
        if password==pss:
            print("correct")
        else:
            print("incorrect password")
    else:
        print("incorrect user")

"""
#7. Write a Python program for ordering food. Ask the user to select a type of food 
#(e.g., "Burger" or "Pizza").If they choose "Burger," ask if they want fries. If they 
#choose "Pizza," ask if they want extra cheese. Print their order with the additional items if chosen.  
"""

user=input(" choose what type of food you want:(burger/pizza)")
if user=="burger":
    print("fries")
if user=="pizza": 
    print("pizza")
"""

#8. Write a Python program that takes an integer as input and checks if it's positive, negative, or zero. If it'
#s positive,check if it's even or odd. Print the appropriate messages.  
"""num=int(input("enter the number"))
if num>0:
    if num%2==0:
        print("positive even")
    else:
        print("positive odd")
else:
    if num%2==0:
        print("negative even")
    else:
        print("negative odd")"""
#9. Write a Python program that asks for a user's age and whether they have a driver's 
#license. If the user is 18 or older andhas a driver's license, print "You are eligible 
#to drive." Otherwise, print "You are not eligible to drive."  
"""age=int(input("enter your age:"))
if age>=18:
    liecense=input("enter if you have driving liecense (yes/no)")
    if liecense=="yes":
        print("you are eligible to drive")
    else:
        print("you are not eligible to drive")
else:
    print("you are not eligible to drive")
"""



















