#1. Write a Python program to find the difference between the largest and smallest elements in a given list.
#Input:[18, 7, 25, 12, 30]
#Output:23
"""num=[18,7,25,12,30]
small =num[0]
big=num[-1]
for i in num:
    if big>i:
        big=i
    elif small<i:
        small=i
out=small-big
print(out)
        
"""

#2. Write a Python program to create a new list containing only the numbers whose sum of factors is a Perfect Square.
#Input:[1, 3, 22, 66, 70, 81, 94]
#Output:[1, 3, 22, 66, 70, 81, 94]
"""num = [1,3,22,66,70,81,94]

out=[]
for i in num:
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s=s+j
    r=int(s**0.5)
    if r*r==s:
        out.append(i)
print(out)"""

#3. Write a Python program to create a new list containing only the numbers for which the difference between the
#number and its reverse is divisible by 9.
#Input:[12, 15, 23, 41, 56]
#Output:[12, 15, 23, 41, 56]
"""num=[12,15,23,41,56]
a=[]
for i in num:
    bkp=i
    rev=0
    while i>0:
        d=i%10
        rev=rev*10+d
        i=i//10
    s=rev-bkp

    if s%9==0:
        a.append(bkp)
print(a)

"""
#4. Write a Python program to print the list excluding the first and last elements using slicing.
#Input:[10, 20, 30, 40, 50, 60, 70]
#Output:[20, 30, 40, 50, 60]
"""num=[10,20,30,40,50,60,70]
res=num[1:-1:1]
print(res)
"""

#5. Write a Python program to print the list in reverse order using slicing.
#Input:[10, 20, 30, 40, 50, 60]
#Output:[60, 50, 40, 30, 20, 10]
"""num=[10,20,30,40,50,60]
res=num[::-1]
print(res)"""

#6. Write a Python program to print every second element of the given list using slicing.
#Input:[10, 20, 30, 40, 50, 60, 70, 80]
#Output:[10, 30, 50, 70]
"""num=[10,20,30,40,50,60,70,80]
res=num[::2]
print(res)"""

#7. Write a Python program to print the list from the 3rd element to the 6th element using slicing.
#Input:[10, 20, 30, 40, 50, 60, 70, 80]
#Output:[30, 40, 50, 60]
num=[10,20,30,40,50,60,70,80]
res=num[2:6:1]
print(res)

