#1.Write a Python program to create a new tuple by inserting the index of every element immediately after it.
#Input:(10, 20, 30, 40)
#Output:(10, 0, 20, 1, 30, 2, 40, 3)
#Explanation:Create a new tuple by inserting the index of each element immediately after that element.
"""
num=(10,20,30,40)
x=list(num)
z=[]
for i in range(0,len(num)):
    z.append(x[i])
    z.insert(num[i],i)
    #y=tuple(x)
    r=tuple(z)
print(r)
"""

#2.Write a Python program to create a new tuple by repeating every element according to its position.
#Input:(10, 20, 30, 40)
#Output:(10, 20, 20, 30, 30, 30, 40, 40, 40, 40)
#Explanation:Repeat the element at index 0 once, index 1 twice, index 2 three times, and so on.
"""num=(10,20,30,40)
y=[]
for i in num:
    k=num.index(i)
    j=0
    while j<k:
        y.append(i)
        j=j+1
print(tuple(y))
"""        
#3.Write a Python program to create a new tuple by inserting the sum of digits of every element immediately after that element.
#Input:(12, 35, 101)
#Output:(12, 3, 35, 8, 101, 2)
#Explanation:
#Insert the sum of digits of each element immediately after that element.   
"""num=(12,35,101)
y=[]
s=0
for i in range(0,len(num)):
    y.append(num[i])
    d=num[i]%10
    s=s+d
    d=d//10
    y.append(s)
print(tuple(y))
"""
#4.Write a Python program to create a new tuple containing only those elements that are greater than the average of the tuple.
#Input:(10, 25, 15, 30, 20)
#Output:(25, 30)
#Explanation:
#Average = 20. Create a new tuple containing only the elements greater than the average.
"""x=(10,25,15,30,20)
avg=sum(x)//len(x)
r=[]
for i in x:
    if i>avg:
        r.append(i)
print(tuple(r))
"""
#5.Write a Python program to create a new tuple by replacing every even-index element with its square and every odd-index element with its cube.
#Input:(2, 3, 4, 5, 6)
#Output:(4, 27, 16, 125, 36)
#Explanation:
#* Even index → Square the element.
#* Odd index → Cube the element.
num=(2,3,4,5,6)
y=[]
for i in range(0,len(num)):
    if i%2==0:
        x=num[i]*2
        
        y.append(x)
    else:
        x=num[i]**3
        
        y.append(x)

print(tuple(y))

        
    
    





