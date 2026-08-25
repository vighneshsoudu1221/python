#1.Write a Python program to find the first row containing the maximum number of even elements.
#Input:x = [[11, 24, 7, 18],[10, 15, 22, 9],[8, 12, 14, 5],[20, 3, 6, 11]]
#Output:[8, 12, 14, 5]
#Even Count: 3
"""x = [[11, 24, 7, 18],[10, 15, 22, 9],[8, 12, 14, 5],[20, 3, 6, 11]]
y=[]
z=[]
for i in range(0,len(x)-1):
    if x[i][i]%2==0:
        d=x[i]
        for c in x[i]:
            if c%2==0:
               z.append(c)
print(x[i])
count=0
for d in z:
    count=count+1
print(count)
"""
#2.Write a Python program to find all elements that appear exactly once in the entire nested list,
#while maintaining their original order.
#Input:x = [[10, 20, 30],[20, 40, 50],[30, 60, 70]]
#Output:[10, 40, 50, 60, 70] 
"""x = [[10, 20, 30],[20, 40, 50],[30, 60, 70]]
def unique(x):
    d={}
    out=[]
    for i in x:
        for j in i:
             if j in d:
                 d[j]=d[j]+1
             else:
                 d[j]=1
    for i in d:
        if d[i]==1:
            out.append(i)
    return out
res=unique(x)
print(res)
    """
#3.Write a Python program to find the row having the maximum difference between its largest and smallest elements.
#Input:x = [[10, 25, 18],[5, 40, 12],[30, 35, 20],[8, 50, 15]]
#Output:[8, 50, 15]
#Difference: 42
"""x = [[10, 25, 18],[5, 40, 12],[30, 35, 20],[8, 50, 15]]
out=[]
high=0
for i in x:
    res=max(i)-min(i)
    if res>high:
        high=res
        out.clear()
        out.extend(i)
print(out)
print(high)"""
#4.Write a Python program to reverse only those tuples whose sum of elements is odd.
#Input:x = ((1, 2, 3),(4, 5, 2),(7, 8, 9),(10, 11, 12))
#Output:((1, 2, 3), (2, 5, 4), (7, 8, 9), (12, 11, 10))
"""x = ((1, 2, 3),(4, 5, 2),(7, 8, 9),(10, 11, 12))
out=[]
for i in x:
    s=0
    for j in i:
        s=s+j
    if s%2==0:
        out.append(i)
    else:
        r=list(i)
        a=r[::-1]
        out.append(tuple(a))
print(tuple(out))
"""
#5.Write a Python program to find the student who has the highest total marks from a nested dictionary.
"""Input:
students = {"Ravi": {"Math": 85, "Science": 78, "English": 90}, 
                     "Priya": {"Math": 92, "Science": 88, "English": 84},
                     "Arjun": {"Math": 76, "Science": 95, "English": 89}}
Output:
Student: Priya
Total Marks: 264"""
"""
marks = {"Ravi": {"Math": 85, "Science": 78, "English": 90}, 
                     "Priya": {"Math": 92, "Science": 88, "English": 84},
                     "Arjun": {"Math": 76, "Science": 95, "English": 89}}
greatest=0
student=""
for k in marks:
    total=0
    for i in marks[k]:
        total=total+marks[k][i]
    if total>greatest:
        greatest=total
        student=k
print("student",student)
print("total marks:",greatest)

"""
#6.Write a function that returns True if a number is a Perfect Number, otherwise returns False.
"""Input:
n = 28
Output:
True"""
def perfect(n):
    s=0
    d=1
    while d<=n//2:
        if n%d==0:
            s=s+d
        d=d+1
        
    if s == n:
        return True
    else:
        return False
n=int(input("enter the number"))
print(perfect(n))




    
    
