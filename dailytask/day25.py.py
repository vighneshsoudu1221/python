### 1. Elements Common in Exactly 2 Sets
#Write a Python program to find the elements that are present in *exactly 2 out of 3 sets*.
#Input:
"""A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {5, 6, 7, 8, 9}
Output:
{3, 4, 6, 7}"""
"""
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {5, 6, 7, 8, 9}
output = set()
for i in A|B|C:
    count=0
    if i in A:
        count=count+1
    if i in B:
        count=count+1
    if i in C:
        count=count+1
    if count == 2:
        output.add(i)
print(output)
 """   
### 2. Unique Elements After Removing Common Elements
#Write a Python program to find all elements that are present in *only one of the three sets*.
#Input:
"""A = {1, 2, 3, 4, 5}
B = {3, 4, 6, 7}
C = {4, 7, 8, 9}
Output:
{1, 2, 5, 6, 8, 9}"""
"""A = {1, 2, 3, 4, 5}
B = {3, 4, 6, 7}
C = {4, 7, 8, 9}
out=[]
for i in A|B|C:
    count=0
    if i in A:
        count=count+1
    if i in B:
        count=count+1
    if i in C:
        count=count+1
    if count==1:
        out.append(i)
print(set(out))
"""

### 3. Write a Python program to check whether the intersection of two sets forms a sequence of consecutive numbers.
"""Input:
A = {2, 3, 4, 5, 8}
B = {1, 2, 3, 4, 5}
Output:
Consecutive
Explanation:
Find the common elements and check whether they form consecutive numbers."""

"""A = {2, 3, 4, 5, 8}
B = {1, 2, 3, 4, 5}
common =sorted(A&B)
for i in range(len(common)-1):
    count=0
    if common[i+1]==common[i]+1:
        count=count+1
if count==len(common)-1:
    print("consecutive")
else:
    print("not consecutive")
"""
### 4. Course Eligibility
#Three sets represent students enrolled in Python, Java, and SQL courses.
#Find the students who are enrolled in both Python and Java but not SQL.
#Input:
"""Python = {1, 2, 3, 4, 5, 6}
Java = {3, 4, 5, 7, 8}
SQL = {4, 5, 8, 9}
Output:
{3}"""
"""python = {1, 2, 3, 4, 5, 6}
java = {3, 4, 5, 7, 8}
sql = {4, 5, 8, 9}
output=set()
for i in python&java:
    for j in sql:
        if i not in sql:
            output.add(i)
print(output)

 """       
### 5. Find Exclusive Groups
"""Three sets represent employees trained in Python, Java, and SQL.
Find:
* Employees trained in *Python and Java but not SQL*
* Employees trained in *Java and SQL but not Python*
* Employees trained in *Python and SQL but not Java*
* Employees trained in *all three*
Input:
Python = {1, 2, 3, 4, 5, 6}
Java = {3, 4, 5, 7, 8}
SQL = {4, 5, 8, 9}
Output:
Python & Java only = {3}
Java & SQL only = {8}
Python & SQL only = set()
All three = {4, 5}"""
python = {1,2,3,4,5,6}
java = {3,4,5,7,8}
sql = {4,5,8,9}
outp=set()
outj=set()
outs=set()
for i in python&java:
    for j in sql:
        if i not in sql:
            outp.add(i)
for i in java&sql:
    for j in python:
        if i not in python:
            outj.add(i)
for i in sql&python:
    for j in java:
        if i not in java:
            outs.add(i)
       
print("python and java",outp)
print("java & sql*",outj)
print("python & sql only =",outs)
print("all three =",python&sql&java)
    







    



