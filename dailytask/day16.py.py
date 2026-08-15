#1. Write a Python program to find the largest element in a given list.
#Input:
#[12, 45, 7, 89, 23]
#Output:
#89
"""x=[12,45,7,89,23]
res=max(x)
print(res)
"""
#2. Write a Python program to print all the elements present at even indices of a given list.
#Input:
#[10, 20, 30, 40, 50, 60, 70]
#Output:
#[10, 30, 50, 70]
"""
x=[10,20,30,40,50,60,70]
for i in range(len(x)):
    if i%2==0:
        print(x[i],end=",")

"""


#3. Write a Python program to find the sum of all elements in a given list.
#Input:
#[5, 10, 15, 20]
#Output:50
"""
x=[5,10,15,20]
s=0
for i in x:
    s=s+i
print(s)
"""
#4. Write a Python program to create a new list containing only the numbers whose sum of factors is a Prime Number.
#Input:[9, 16, 20, 25]
#Output:[9, 16, 25]

x=[9, 16, 20, 25]
for i in x:
    s=0
    d=i%10
    s=s+d
    i=i//10
count=0
if s%2==0:
    count=count+1
    if count>2:











#5. Write a Python program to create a new list containing only the numbers for which the sum of the number
#and its reverse is a Palindrome Number.
#Input:[12, 15, 19, 23, 28]
#Output:[12, 15, 23]








