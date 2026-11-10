
#1 Write a generator function that takes anumber and generates its digits from right to left.
#Input: n = 58321
#Output: 1 2 3 8 5
"""n=58321
def display(x):
    while x>0:
        yield x%10
        x=x//10
for i in display(n):
    print(i)"""
#2 Write a generator function that generates the first n Fibonacci numbers.
#Input: n = 7
#Output: 0 1 1 2 3 5 8
"""n=7
def fib(a,b):
    c=0
    yield a
    yield b
    while c<n:
       c=a+b
       yield c
       a=b
       b=c

for i in fib(0,1):
    print(i)
    
"""    
#3 Write a generator function that takes a list and yields an element only when it is different from the
#previously yielded element.
#Input: nums = [1, 1, 2, 2, 2, 3, 1, 1, 4]
#Output: 1 2 3 1 4
"""nums = [1,1,2,2,2,3,1,1,4]
def fun(n):
    for i in range(0,len(n)-1):
        if n[i]==n[i+1]:
            yield n[i]
for i in fun(n):
    print(i)"""
#4 Write a generator function that generates the first n prime numbers.
#Input: n = 8
#Output: 2 3 5 7 11 13 17 19
"""
def prime(n):
    count=0
    num=2
    while count<n:
      is_prime = True
      for i in range(2,num//2+1):
          if num%i==0:
              is_prime=False
              break
      if is_prime:
          yield num
          count=count+1
      num=num+1
n=8
for i in prime(n):
    print(i,end=" ")
"""  
        
#5 Write a Python generator function that takes a compressed string and yields each
#character/group according to its count. Input: a[2]bc[3] Output: a a bc bc bc
def fun(x):
    for i in x:
        if 
