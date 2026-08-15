"""i=1
while i<=100:
    print(i)
    i=i**2
"""
"""i =2
while i<=100:
    print(i)
    i=i**2
"""
"""
i=0
while i<=3 and i%2==0:
    print(i)
    i=i+1
"""
"""i=0
while i<=3 or i%2==0:
    print(i)
    i=i+1
    """

"""# factor /divisor of a give number
num=int(input("enter a number:"))
d =1
while d<=num:
    if num%d==0:
        print(d)
    d=d+1"""

"""
num =int(input("enter a number "))
count=0
i=1
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count == 2:
    print("prime")
else:
    print("not prime")
"""
"""# print first 100 even numbers
a=1
cnt = 0
while cnt <=100:# <=100
        if a%2==0:#2%=0
            cnt = cnt +1
            print(a)
        
        a=a+1
    """

num = int(input("enter a number"))
d=2
while d<=num//2:
    if num%d==0:
        print("")
    d=d+1
else:
    print("prime")
