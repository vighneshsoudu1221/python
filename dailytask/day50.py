#Write a function check_number(n) to print all the even numbers from 1 to n without using the % operator.
#Input: n = 48 Output: 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48
"""
n=int(input("enter the number:"))
for i in range(2,n+2,2):
    print(i,end=" ")
    
"""

#Given three sets, write a function find_common(s1, s2, s3) to display all elements that are present in at
#least two of the three sets.
#Input: s1 = {10, 20, 30, 40, 50} s2 = {20, 30, 60, 70} s3 = {30, 40, 80, 90} Output: 20 30 40
"""s1 = {10, 20, 30, 40, 50}
s2 = {20, 30, 60, 70}
s3 = {30, 40, 80, 90}
def display(s1,s2,s3):
    res=s1&s2 | s1&s3 | s2&s3 
    for i in res:
        print(i)
display(s1,s2,s3)"""
