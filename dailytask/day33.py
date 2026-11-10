
#1 Write a Python function to find the maximum sum of any two consecutive elements in a list and return the elements that produce the maximum sum.
#Input: [4, 7, 2, 9, 5, 12, 3]
#Output: [5, 12]
"""x=[4,7,2,9,5,12,3]
def fun(x):
    p=[]
    su=0#14
    for i in range(0,len(x)-1):
        s=x[i]+x[i+1]
        if s>su:
            su=s
            p=[]
            p.extend((x[i],x[i+1]))#4,7
    return p   
print(fun(x))           
            
"""
#2 Write a Python function to remove consecutive duplicate characters from a string while keeping the first occurrence of each consecutive group.
#Input: "aaabbccdaaee"
#Output: "abcdae"
"""x="aaabbccdaaee"
def fun(x):
    out=" "
    for i in range(0,len(x)-1):
        if x[i]!=x[i+1]:
            out=out+x[i]
    else:
        out=out+x[i]
    return out
print(fun(x))"""

#3 Given a tuple of numbers, find the smallest positive number that is missing from the tuple.
#Input: (3, 4, -1, 1, 2, 6)
#Output: 5    
"""x=(2,4,-1,1,2,6,8,9)
st=""
for i in range(1,len(x)):
    if i not in x:
        st=st+str(i)
        break
print(st)"""
#4 Write a Python program using a nested function and nonlocal to create a counter.
#The counter should start with the given value and increase by the corresponding values in the list.
#Input: start = 5 values = [3, 7, 2, 8]
#Output: 8 15 17 25        
x=[3,7,2,8]
def fun(x):
    y=5
    def add():
        nonlocal y
        for i in x:
            y=y+i
            return y
    re=add()
    return re
res=fun(x)
print(res)        
