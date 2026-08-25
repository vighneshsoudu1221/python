#1.Write a Python program to group all keys having the same value into a list.
#Input:d = {"a": 10,"b": 20,"c": 10,"d": 30,"e": 20,"f": 10}
#Output:{10: ['a', 'c', 'f'],20: ['b', 'e'],30: ['d']}
"""num = {"a": 10,"b": 20,"c": 10,"d": 30,"e": 20,"f": 10}
out={}
for i in num.keys():
    if num[i]in out:
        out[num[i]].append(i)
        
    else:
        out[num[i]]=[i]
print(out)"""


#2.Write a Python program to arrange the dictionary in ascending order of values without using the built-in sorted()
#function.
#Input:
#d = {"A": 45,"B": 12,"C": 78,"D": 30,"E": 56}
#Output:
#{"B": 12,"D": 30,"A": 45,"E": 56,"C": 78}
"""d={"A": 45,"B": 12,"C": 78,"D": 30,"E": 56}
y=list(d.items())
for j in range(0,len(y)-1):
    for i in range(0,len(y)-j-1):
        if y[i][1]>y[i+1][1]:
            y[i],y[i+1]=y[i+1],y[i]
output={k:v for k,v in y}
print(output)
"""

#3.Write a Python program to find all keys whose values are prime numbers.
#Input:d = {"a": 12,"b": 17,"c": 23,"d": 25,"e": 31}
#Output:['b', 'c', 'e']
"""d = {"a": 12,"b": 17,"c": 23,"d": 25,"e": 31}
y=list(d.items())
out=[]
for i in range(0,len(y)):
    count=0
    prime=True
    for k in range(2,y[i][1]//2):
        if y[i][1]%k==0:
            prime=False
    if prime:
        out.append(y[i][0])
print(out)
"""  
#4.Write a Python program to find the row whose sum is maximum in a nested list. If two rows have the same sum,
#consider the first one.
#Input:x = [ [10, 20, 5],[15, 8, 12],[25, 5, 10],[7, 18, 20] ]
#Output:[7, 18, 20]
#Sum: 45
"""x = [ [10, 20, 5],[15, 8, 12],[25, 5, 10],[7, 18, 20] ]
maf_sum=0
out=[]
for i in x:
    total=0
    for j in i:
        total=total+j
    if total>maf_sum:
        maf_sum=total
        out=i
print(out)
print(maf_sum)
"""
#5.Write a Python program to remove duplicate tuples from a nested tuple while maintaining the original order.
#Input:x = ((1, 2),(3, 4),(1, 2),(5, 6),(3, 4),(7, 8))
#Output:((1, 2), (3, 4), (5, 6), (7, 8))
x = ((1, 2),(3, 4),(1, 2),(5, 6),(3, 4),(7, 8))
out=()
for i in x:
    if i not in out:
        out=out+(i,)
print(out)




        





