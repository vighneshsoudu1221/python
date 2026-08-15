
#1.Write a Python program to print all elements that are greater than both of their adjacent elements.
#Input:[5, 18, 10, 25, 15, 30, 20]
#Output:18 25 30
"""x=[5,18,10,25,15,30,20]
for i in range(len(x)-1):
    if x[i]<x[i+1] and x[i+1]>x[i+2]:
        print(x[i+1],end=" ")"""

#2.Write a Python program to print all elements in a list that are equal to the sum of all previous elements.
#Input:[2, 3, 5, 10, 20, 21]
#Output:5 10 20
"""Explanation:
5 = 2 + 3
10 = 2 + 3 + 5
20 = 2 + 3 + 5 + 10"""
"""x=[2,3,5,10,20,21]
s=0
for i in x:
    if s==i:
        print(i,end=" ")
    s=s+i
"""
#3.Write a Python program to split a list into groups of 3 elements using slicing and print only the groups
#whose sum is greater than 50.
#Input:[10, 20, 30, 5, 10, 15, 25, 20, 15]
#Output:
#[10, 20, 30]
#[25, 20, 15]
"""num=[10,20,30,5,10,15,25,20,15]
res=sum.num[:3:1]
second=sum.num[3:7:1]
third=sum.num[7::]
if res==50:
    print(res)
elif second==50:
    print(second)
else:
    print(third)"""
#4.Write a Python program using List Comprehension to create a new list containing the square of all even numbers.
#Input:[2, 3, 4, 5, 6, 7]
#Output:[4, 16, 36]
"""num=[2,3,4,5,6,7]
x=[ i**2 for i in num if i%2==0 ]
print(x)"""

#5.Write a Python program using List Comprehension to create a new list containing the squares
#of the numbers that are divisible by 5.
#Input:[5, 8, 10, 12, 15, 18, 20]
#Output:[25, 100, 225, 400]
"""num=[5,8,10,12,15,18,20]
y=[i**2 for i in num if i%5==0]
print(y)  
"""

#6.Write a Python program using List Comprehension to create a new list containing only the perfect square numbers from the given list.
#Input:[4, 7, 9, 10, 16, 18, 25]
#Output:[4, 9, 16, 25]
"""num=[4,7,9,10,16,18,25]
y=[ i for i in num if (i**0.5)**2==i]
print(y)

"""
#7.Write a Python program using List Comprehension to create a new list containing the cubes of all odd numbers.
#Input:[2, 3, 4, 5, 6, 7]
#Output:[27, 125, 343]
"""num =[2,3,4,5,6,7]
y=[i**3 for i in num if i%2!=0]
print(y)"""


