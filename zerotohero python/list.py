#1. Reverse a list in Python ?
"""x=[1,2,3,4,4,5,6,6]
res=[]
for i in x[::-1]:
    res.append(i)
print(res) """
"""x=[12,34,3,42,2,33,5,6]
s=0
end=len(x)-1
while s<end:
    x[s],x[end]=x[end],x[s]
    s=s+1
    end=end-1
print(x)"""


#2. Remove duplicates from a list in Python ?
"""x=[1,2,3,4,4,5,6,6]
out=set(x)
print(list(out))"""
#3. Find the maximum and minimum elements in a list ?
"""x=[4,2,3,1,4,5,67]
big=x[0]
small=x[0]
for i in range(0,len(x)):
    if x[i] > big:
        big=x[i]
    else:
        if x[i]<small:
            small=x[i]
print(big)
print(small)
"""
#4. Sort a list in ascending and descending order ?
"""x=[12,34,3,42,2,33,5,6]
x.sort()
print(x)"""

#6. Find the index of a specific element in a list ?

"""x=[12,34,3,42,2,33,5,6]
target=int(input("enter the target"))
for i in range(0,len(x)):
    if x[i]==target:
        print(i)"""
#7. Count the occurrences of an element in a list ?
"""x=[12,34,3,42,2,33,5,12,6,3,6,3]
traget=int(input("enter the occurrences target"))
count=0
for i in x:
    if i==traget:
        count=count+1
print(count)"""

#8 Merge two lists in Python ?
"""x=[12,34,3,42,2,33,5,6]
y=[12,34,3,42,2,33,5,6]
print(x+y)
"""
#9. Find the sum of all elements in a list ?
"""x=[12,3,45,6,7,78,8]
s=0
for i in x:
    s=s+i
print(s)"""
#10. Remove an element from a list by its value ?  
"""x=[12,3,45,6,7,78,8]
remove=int(input("enter the element"))
if remove in x:
    x.remove(remove)
print(x)"""


#11. Slice a list to get specific elements ?
"""x=[12,3,4,5,5,65]
res=x[:-1:]
r=x[:1]
e=x[4::-1]
print(res)
print(r)
print(e)"""
#12. Find the length (number of elements) of a list ?
"""x=[1,2,3,4,5,6,1,2,3,4]
count=0
for i  in x:
    count=count+1
print(count)"""
#13. Add an element to the end of a list ?
"""x=[1,2,3,4,5,6,4,7,7]
x.append(10)
print(x)
"""
#14. Iterate through a list using a for loop ?
"""x=[1,23,4,5,6,7,89,]
for i in x:
    print(i)
"""
#15. Insert an element at a specific position in a list ?
"""x=[1,2,3,2,4,5,6,7,89,0]
index=int(input("enter the index:"))
st=int(input("enter element"))
x.insert(index,st)
print(x)"""
#16. Extend a list with elements from another iterable ?
"""x=[1,2,3,4,5]
x.extend([5,60])
print(x)"""
#17. Clear all elements from a list ?
"""x=[1,3,2,4,5,5,6]
x.clear()
print(x)"""
#18. Create a copy of a list ?
"""x=[1,2,3,4,5,6,7]
y=x
x.append(8)
print(y)"""
#19. Reverse a list in-place (modify the original list) ?
"""x=[1,2,3,45,6,7,4]
s=0
e=len(x)-1
while s<e:
    x[s],x[e]=x[e],x[s]
    s=s+1
    e=e-1
print(x)"""

#20. Find the index of the first occurrence of an element from a specific position ?
"""x=[1,2,3,4,5,6,7,8,9,0,4,5,6,7,6,7,8,8,9]
target=int(input("enter the target"))
start=0
for i in range(0,len(x)):
    if x[i]==target:
        start=i
        break
print(start)"""

#21. Remove and return the last element from a list ? 
x=[12,344,68,578,3456,45,]
a=x.pop()
print(a)
print(x)



