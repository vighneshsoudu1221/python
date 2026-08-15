#1. Write a Python program to find all indices where a given element occurs in a list.
#Input:[10, 20, 30, 20, 40, 20]
#Target = 20
#Output:[1, 3, 5]
"""num=[10,20,30,20,40,20]
traget=int(input("enter the targeted"))
for i in range(0,len(num)):
    if num[i] == traget:
        print(i,end=" ")
"""
#2. Write a Python program to find all the missing numbers in a list.
#Input:[1, 2, 4, 6, 7, 9]
#Output:[3, 5, 8]
"""num = [1,2,4,6,7,9]
for i in range(1,10):
    if i not in num:
        print(i,end=" ")
"""
#3. Write a Python program to find the last occurrence of a target element in a list.
#Input:[2, 4, 4, 4, 6, 8, 10]
#Target = 4
#Output:3
"""num=[2,4,4,4,6,8,10]
target = int(input("enter the target "))
count=0
for i in range(len(num)):
    if num[i] == target:
        count=count+1
print(count)"""

#4. Write a Python function to return a new list containing only the elements whose indices are Fibonacci numbers.
#Input:[10, 20, 30, 40, 50, 60, 70, 80, 90]
#Output:[10, 20, 30, 40, 60, 90]
"""num = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = 0
b = 1
result = []
while a<len(num):
    if a not in result:
        result.append(num[a])
    c=a+b
    b=a
    a=c
print(result)"""


#5. Write a Python program to print all elements in a list that are equal to the product of all previous elements.
#Input:[2, 3, 6, 36, 5]
#Output:6 36
#Explanation:
#6 = 2 × 3
#36 = 2 × 3 × 6
"""num=[2,3,6,36,5]
s=1
for i in num:
    if s==i:
        print(i)
    s=i*s
 """
#6. Write a Python program to split a list into groups of 3 elements using slicing and print only the groups in which every element is greater than 10.
#Input:[12, 15, 18, 5, 20, 25, 30, 35, 40]
#Output:
#[12, 15, 18]
#[30, 35, 40]
#Explanation:
#Split the list into groups of 3 elements and print only those groups where every element is greater than 10.
num=[12,15,18,5,20,25,30,35,40]
for i in range(0,len(num),3):
    group = num[i:i+3]
    for x in group:
        if x<10:
            break
        else:
            print(group)
            break

    










