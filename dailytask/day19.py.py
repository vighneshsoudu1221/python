#1. Write a Python program to print the list starting from the second element up to the second last element, taking every third element using slicing.
#Input:[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#Output:[20, 50, 80]
"""x=[10,20,30,40,50,60,70,80,90,100]
res=x[1:10:3]
print(res)
"""
#2. Write a Python program to print the list from the third last element to the beginning in reverse order using slicing.
#Input:[10, 20, 30, 40, 50, 60, 70, 80]
#Output:[60, 50, 40, 30, 20, 10]
"""x=[10,20,30,40,50,60,70,80]
res=x[-3::-1]
print(res)
"""

#3. Write a Python program to divide the given list into two equal halves and swap the halves using slicing.
#Input:[10, 20, 30, 40, 50, 60, 70, 80]
#Output:[50, 60, 70, 80, 10, 20, 30, 40]
"""
x=[10,20,30,40,50,60,70,80]
res=x[-4::1]
for i in range(0,4):
    res.append(x[i])
print(res)
"""

#4. Write a Python program to reverse only the second half of the given list using slicing.
#Input:[10, 20, 30, 40, 50, 60, 70, 80]
#Output:[10, 20, 30, 40, 80, 70, 60, 50]
"""x=[10,20,30,40,50,60,70,80]
y=x[len(x)//2::]
y=y[::-1]
x=x[:len(x)//2:1]
print(x+y)
"""

#5. Write a Python program to rotate the given list to the right by K positions using slicing.
#Input:
#List: [10, 20, 30, 40, 50, 60, 70, 80]
#K = 3
#Output:
#[60, 70, 80, 10, 20, 30, 40, 50]
"""
x=[10,20,30,40,50,60,70,80]
res=x[-3::1]
for i in range(0,5):
    res.append(x[i])
print(res)

"""

#6. Write a Python program using List Comprehension to create a new list containing the square of all even numbers from the given list.
#Input:[2, 3, 4, 5, 6, 7, 8]
#Output:[4, 16, 36, 64]
"""x=[2,3,4,5,6,7,8]
y=[i**2 for i in x if i%2==0]
print(y)"""

#7. Write a Python program using List Comprehension to create a new list containing only the numbers whose
#last digit is 5.
#Input:[12, 25, 35, 41, 55, 60, 75]
#Output:[25, 35, 55, 75]
x=[12,25,35,41,55,60,75]
y=[i for i in x if i%10==5]
print(y)


