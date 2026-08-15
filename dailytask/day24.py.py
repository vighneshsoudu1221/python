#1. Write a Python program to find all pairs of elements whose sum is equal to the given target.
#Input:(2, 7, 11, 15, 3, 8)
#Target = 10
#Output:[(2, 8), (7, 3)]
"""x=(2,7,11,15,3,8)
target = int(input("enter the target number:"))
y=[]

for i in range(0,len(x)-1):
    if x[i]and x[i+1] == target:
        y.append(x[i])
        y.append(x[i+1])
print(set(y))

"""
#2. Write a Python program to remove all duplicate elements from a tuple while maintaining the original order.
#Input:(10, 20, 10, 30, 20, 40, 30, 50)
#Output:(10, 20, 30, 40, 50)
"""x=(10,20,10,30,20,40,30,50)
res=()
for i in x:
    if i not in res:
        res=res+(i,)
print(res)
"""

#3. Write a Python program to find the longest continuous sequence of the same element in a tuple.
#Input:(1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5)
#Output:4
#Explanation:The number 4 occurs continuously 4 times, which is the longest continuous sequence.
"""x=(1,1,2,2,2,3,3,4,4,4,4,5)
num=int(input("enter the number:"))
seq=0
for i in x:
    if x.count(i)>1:
        squ=seq+1

       """
#4. Write a Python program to split a tuple into two tuples: one containing elements at even indices and another containing elements at odd indices.
#Input:(10, 20, 30, 40, 50, 60, 70, 80)
#Output:Even Index Tuple: (10, 30, 50, 70)
#Odd Index Tuple: (20, 40, 60, 80)        
"""x=(10,20,30,40,50,60,70,80)
even=[]
odd=[]
for i in range(0,len(x)):
    if i%2==0:
        even.append(x[i])
    else:
        odd.append(x[i])
print("Even Index Tuple:",tuple(even))
print("odd Index tuple:",tuple(odd))
        
"""
#5. Write a Python program to check whether a tuple is a palindrome without converting it into a list.
#Input:(10, 20, 30, 20, 10)
#Output:Palindrome
"""x=(10,20,30,20,10)
i=0
j=len(x)-1
count=0
while i<j:
    if i==j:
        count=count+1
    i=i+1
    j=j-1
if count==0:
    print("palindrom")
else:
    print("not palidrom")
"""
#6. Write a Python program to find the common elements between two sets.
#Input:
#Set1 = {10, 20, 30, 40, 50}
#Set2 = {30, 40, 50, 60, 70}
#Output:
#{30, 40, 50}
"""set1={10,20,30,40,50}
set2={30,40,50,60,70}
print(set1 & set2)"""
#7. Write a Python program to find all elements that are present in the first set but not in the second set.
#Input:
#Set1 = {10, 20, 30, 40, 50}
#Set2 = {30, 40, 60, 70}
#Output:{10, 20, 50}
"""set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}
print(set1-set2)"""

