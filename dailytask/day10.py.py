"""num=int(input("enter a number:"))#8654
while True:
    s=0
    while num!=0:
        d=num%10#8654%10=4#865//10=5
        s=s+d#4,
        num=num//10#865
    if s>9:
        num=s
    else:
        print(s)
        break
 """       
#1.A movie theater has 20 seats. Seats with numbers divisible by 5 are reserved. Write a program to display only
#the available seat numbers?
"""num=20
d=1
while d<num:
    if d%5!=0:
        print(d)
    d=d+1"""
#2.A company issues employee IDs from 1001 to 1020. Write a program to count how many employee IDs are even?
"""num=1020
d=1001
count=0
while d<=num:
    if d%2==0:
        count=count+1
        print(d)
    d=d+1
print(count)
"""
#3.A game contains 15 levels. Bonus rewards are given for levels divisible by 3.
#Write a program to display all bonus levels?
"""num=15
d=1
while d<=num:
    if d%3==0:
        print(d)
    d=d+1"""
#4.A library contains books numbered from 1 to 50. Write a program to count how many book numbers are multiples of 7?
#Input:50
#Output:7
"""num=50
d=1
count =0
while d<=num:
    if d%7==0:
        count=count+1
    d=d+1
print(count)"""

#5.Write a program to find the first number greater than 100 that is divisible by both 7 and 9 using a while loop?
#Output:126
"""n=101
while n%7!=0 or n%9!=0:
    n=n+1
print(n)"""

#6 6.Write a program to print all numbers from 1 to n whose square is less than 50?

#Input:20
#Output:1 2 3 4 5 6 7
#Explanation:
#The squares of these numbers are less than 50.
"""
num=int(input("enter a number:"))
d=1
while d<=num:
    if d*d<50:
        print(d)
    d=d+1
"""    
#sum of digits the number
"""num=int(input("enter a number:"))
s=0
while num!=0:
    d=num%10
    s=s+d
    num=num//10
print(s)
"""
#sum digits until singal
"""num=int(input("enter a number"))#153
while True:
    s=0
    while num>0:#153>0 T #15>0 T
        d=num%10#153%10=3 #15%10=5
        s=s+d#0+3 #3+5=8+1=9
        num=num//10#153//10=15//10=1
    if s>9:
        num=s
    else:
        print(s)
        break
"""

#sum of the digits of bigest
"""num=int(input("enter the a number:"))
big=0
while num>0:
    d=num%10
    if d>big:
        big=d
    num=num//10
print(big)"""





