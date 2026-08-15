
#1. Write a Python program to insert the reverse of every two-digit number immediately after it in the same list.
#Input:[12, 8, 45, 123, 67]
#Output:[12, 21, 8, 45, 54, 123, 67, 76]
"""x=[12,8,45,123,67]
y=[]
for i in x:
    y.append(i)
    if i>9 and i<=99:
        rev = int(str(i)[::-1])
        y.append(rev)
print(y)
        
"""

#2. Write a Python program to move all the zeros to the end of the list while maintaining the relative order of the non-zero elements.
#Input:[0, 5, 0, 8, 3, 0, 2, 1]
#Output:[5, 8, 3, 2, 1, 0, 0, 0]
"""x=[0,5,0,8,3,0,2,1]
for i in x:
    if i==0:
        x.remove(i)
        x.append(i)
print(x)
"""

#3. Write a Python program using slicing to swap the first and last three elements of the given list.
#Input:[10, 20, 30, 40, 50, 60, 70, 80, 90]
#Output:[70, 80, 90, 40, 50, 60, 10, 20, 30]
"""x=[10,20,30,40,50,60,70,80,90]

res=x[-3::1]+x[-6:-3:1]+x[:4:]
print(res)
"""

#4. Write a Python program using slicing to divide the given list into four equal parts and print each part separately. 
#Input:[10, 20, 30, 40, 50, 60, 70, 80]
#Output:
"""
[10, 20]
[30, 40]
[50, 60]
[70, 80]
"""
"""x=[10,20,30,40,50,60,70,80]
d=len(x)//4
print(x[0:d])
print(x[d:2*d])
print(x[2*d:3*d])
print(x[3*d:len(x)])

"""

#5. Write a Python program using slicing to reverse only the middle four elements of the given list.
#Input:[10, 20, 30, 40, 50, 60, 70, 80]
#Output:[10, 20, 60, 50, 40, 30, 70, 80]
"""x=[10,20,30,40,50,60,70,80]
res=x[:3:]+x[-3:-6:-1]+x[2:3:]+x[6::]
print(res)
"""

#6. Write a Python program using List Comprehension to create a new list containing the square of each number
#that is divisible by 3 but not divisible by 2.
#Input:[3, 6, 9, 12, 15, 18, 21, 24]
#Output:[9, 81, 225, 441]
"""x=[3,6,9,12,15,18,21,24]
y=[i**2 for i in x if i%3==0]
print(y)
"""

#7. Write a Python program using List Comprehension to replace every negative number with 0 while keeping all other elements unchanged.
#Input:[-5, 12, -8, 20, 0, -3, 15]
#Output:
[0, 12, 0, 20, 0, 0, 15]







    
