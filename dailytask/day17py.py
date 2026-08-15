#1. Write a Python program to create a new list containing only the elements that are greater than the average of the given list.
#Input:[10, 20, 30, 40, 50]
#Output:[40, 50]
"""
num=[10, 20, 30,40,50]
for i in num:
    avg=sum(num)/len(num)
    if i>avg:
        print(i)
"""   
#2. Write a Python program to create a new list containing only the numbers whose reverse is divisible by the original number.
#Input:[12, 22, 25, 44, 13]
#Output:[22, 44]
"""
num=[12,22,25,44,13]
reverse=num[1::2]
print(reverse)
"""

#3. Write a Python program to create a new list containing only the numbers whose sum of digits is greater than
#the product of their digits.
#Input:[12, 22, 111, 24, 123]
#Output:[111]
"""num=[12, 22, 111, 24, 123]
for i in num:
    s=0
    d=i%10
    s=s+d
    i=i//10
    if s>i:
        res=num[i]
print(res)
"""
#4. Write a Python program to create a new list containing only the elements that are divisible by the sum of their digits.
#Input:[12, 18, 20, 25, 27, 30]
#Output:[12, 18, 20, 27, 30]
num=[12,18,20,25,27,30]
for i in num:
    s=0
    d=i%10
    s=s+d
    i=i//10
    if s%i==0:
        print(num[i],end=" ")










