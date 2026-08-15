#2. Write a Python program to print the numbers from 1 to 100 that are prime numbers.
#Output: 2, 3, 5, 7, 11, ..., 97
"""s=2
while s<=100:
    num=s
    i=2
    while i<=num//2:
        if num%i==0:
            break
        i=i+1
    else:
        print(num)
    s=s+1
"""
#1. Write a Python program to count the number of even digits in a given number.
#Input: 4827316
#Output: 4
"""num=4827316
count=0
while num>0:
    digit=num%10

    if digit%2==0:
        count=count+1

    num=num//10
print(count)
"""
#3. Write a Python program to reverse the digits of a given number.
#Input: 3742
#Output: 2473
num=3742
while num>0:
    digit=num%10
    print(digit,end="")
    num=num//10


"""
#fibonnaci series
num=int(input("enter the number"))


"""


