#1. Write a Python program to check whether a given number is a Palindrome using a while loop.
#Input: 1221
#Output: Palindrome
"""num =int(input("enter a number"))
s=num
reverse=0
while num>0:
    d=num%10
    reverse=reverse*10+d
    num=num//10
if reverse==s:
    print("palidram")"""

#2. Write a Python program to repeatedly find the sum of the digits of a given number using a while loop until a single-digit number is obtained.
#Input: 4589
#Output: 8
"""num=int(input("enter a number:"))
while True:
    s=0
    while num>0:
        d=num%10
        s=s+d
        num=num//10
    if s>9:
        num=s
    else:
        print(s)
        break
"""
#4. Write a Python program to print the Fibonacci series up to n terms using a while loop.
#Input: 8
#Output:
#0 1 1 2 3 5 8 13
"""a=0
b=1
print(a,b,end="")
i=1
while i<=8:
    c=a+b
    print(c,end="")
    a=b
    b=c
  
    i=i+1
    
"""
#5. Write a Python program to check whether a given number is a Neon Number using a while loop.
#Input: 9
#Output: Neon Number

#Explanation:
#9² = 81
#8 + 1 = 9
#Since the sum of the digits of the square is equal to the original number, print Neon Number.
"""
num=int(input("enter a number"))
s=num*num
d=0
while s>0:
    digit=s%10
    d=digit+d
    s=s//10
if d==num:
    print("Neon number")
else:
    print("not neon number")

"""
#3. Write a Python program to check whether a given number is an Armstrong Number using a while loop.
#Input: 153
#Output: Armstrong Number
num=int(input("enter a number"))
bkp=num
s=0
d_count=0
while num>0:
    num=num//10
    d_count=d_count+1
    while num>0:
        d=num%10
        s=s+d**d_count
        num=num//10

if s==bkp:
    print("Amstrong")
else:
    print("not amstrong")

