#1.write a python program to print all disarium numbers between 1 and n using a for loop
#input:100
#output:1 2 3 4 5 6 7 8 9 89
"""nu=int(input("enter a number:"))
count=0
for i in range(1,nu+1):
    count=0
    tmp=i

    while tmp>0:
        count=count+1
        tmp=tmp//10

    tmp=i
    total=0
    while tmp>0:
        d=tmp%10
        total=total+(d**count)
        count=count-1
        tmp=tmp//10

    if total==i:
        print(i,end="")

"""
#2 write a python program to print all harshad(niven) numbers between 1 and N using a for loop
#input:30
#output:1 2 3 4 5 6 7 8 9 10 12 18 20 21 24 27 30
"""num = int(input("enter the number"))#30
for i in range(1,num+1):#1to30
    tmp=i#2
    s=0
    while tmp>0:#2>0
        d=tmp%10#2%10=2
        s=s+d#0+2=2
        tmp=tmp//10
    if i%s==0:
        print(i,end=' ')#1,
"""

#3 write a python program to print the folling pattern using for loop
#input:5
#output
"""
15 14 13 12 11
10 9 8 7 6
6 5 4
3 2
1"""
#4
rows = int(input("enter a number"))
for row_no in range(1,rows+1):
    print(" "*(rows-row_no),end="")
    for i in range(row_no,0,-1):
        print(chr(i),end=" ")
    print()



