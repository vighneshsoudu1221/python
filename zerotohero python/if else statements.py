#1.Write a Python program that checks if a given year is a leap year.
"""year = int(input("enter the year"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not leap year")
"""
#2.Write a Python program that checks if a given character is a vowel or a consonant.
"""num = input("enter a character")
if num in "aeiouAEIOU":
    print("vowels")
else:
    print("consonant")
"""
#3.Write a Python program that checks if a given year is a century year (ending in '00').
"""year=int(input("enter the year"))
if year%100==0:
    print("century")
else:
    print("not century")
    """
#4.Write a Python program that checks if a person is eligible to vote based on their age.
"""age = int(input("please enter your age :"))

if age>=18:
    print("you are elgible to vote")
else:
    print("sorry you are not elgible to vote")
"""
#5. Write a Python program that checks if a number is positive or non-positive (including  zero).
"""num = int(input("enter a number:"))
if num>=0:
    print("positive")
else:
    print("negative")
   """
#6.Write a Python program that compares two numbers and prints the largest one.
"""num1=int(input("enter a number :"))
num2=int(input("enter a number :"))

if num1>num2:
    print("largest one is : ",num1)
else:
    print("largest one is :",num2)
"""
#7. Write a Python program that checks if a given character is a letter or not
"""letter = input("Enter a character: ")

if ('a' <= letter <= 'z') or ('A' <= letter <= 'Z'):
    print("It is a letter")
else:
    print("It is not a letter")"""

#8Write a Python program that finds and prints the smallest of three numbers without using inbuilt methods.
"""num1 = int(input("enter a number :"))
num2 = int(input("enter a number :"))
num3 = int(input("enter a number :"))
if num1<num2:
    print("smallest is num1:",num1)
if num2<num3:
    print("smallest is num2:",num2)
else:
    print("smallest is num3:", num3)"""

#9.Write a Python program to check if a given string is a palindrome.  
"""text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")"""
#10. Write a Python program that finds and prints the largest of four numbers.
"""num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))
num3 = int(input("enter a number:"))
num4 = int(input("enter a number:"))
if num1>num2 and num1 > num3 and num1>num4:
    print("num1 is largest in four")
if num2>num3 and num2>num4:
    print("num2 is largest :")
if num3>num4:
    print("num3 is largest :")
else:
    print("num4 is largest :")"""

#11 Write a Python program that checks if a number is a multiple of 7 or not.
"""num = int(input("enter a number :"))
if num%7==0:
    print("divisble")
else:
    print("not disible")"""

#12 Write a Python program that calculates and prints the absolute value of a given number  if input is -5 convert into 5

num = int(input("enter a number"))
if num<0:
    print(num*-1)
else:
    print(num)









