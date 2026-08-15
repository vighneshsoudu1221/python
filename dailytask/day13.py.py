#1. Write a Python program to count the frequency of a given digit in a number using a while loop.
#Input:
#Number: 122313221
#Digit: 2
#Output: 4
"""num=int(input("enter a number:"))
count=0
digit=int(input("enter a number"))
while num>0:
    d=num%10
    if digit==d:
        count=count+1
    num=num//10
print(count)"""

#2. Write a Python program to count how many even digits and odd digits are present in a given number using a while loop.
#Input: 4827316
#Output:
#Even digits: 4
#Odd digits: 3
"""
num=int(input("enter a number"))
even_count=0
odd_count=0
while num>0:
    d=num%10
    if d%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    num=num//10
print("even digits:",even_count)
print("odd digits:",odd_count)
"""
#3. Write a Python program to reverse a number and check whether the reversed number is divisible by 11 using a while loop.
#Input: 121
#Output: Divisible by 11
"""num=int(input("enter a number"))
reverse=0
while num>0:
    d=num%10
    reverse=reverse*10+d
    num=num//10
if reverse%11==0:
    print("divisible by 11")"""
#4. Write a Python program to find the sum of all even digits and the sum of all odd digits in a given number using a while loop.
#Input: 4827316
#Output:
#Sum of even digits: 20
#Sum of odd digits: 10
"""num=int(input("enter a number:"))
sum_even=0
sum_odd=0
while num>0:
    d=num%10
    if d%2==0:
        sum_even=sum_even+d
    else:
        sum_odd=sum_odd+d
    num=num//10
print("sum of even digits",sum_even)
print("sum of odd digits",sum_odd)
"""

#5. Write a Python program to count the number of digits that are greater than 5 in a given number using a while loop.
#Input: 58392716
#Output: 4
num=int(input("enter a number:"))
count=0
while num>0:
    d=num%10
    if d>5:
        count=count+1
    num=num//10
print(count)




