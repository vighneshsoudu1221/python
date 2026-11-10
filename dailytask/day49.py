
#Given a list of integers, display the elements whose indexes are both prime numbers and Fibonacci numbers.
#Input: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] Output: 20 30 50
"""
x=[10,20,30,40,50,60,70,80,90,100]
for i in range(len(x)):
    if i<2:
        continue
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    a=0
    b=1
    fibonacci= False
    while a<=i:
        if a == i:
            fibonacci=True
            break
        a,b=b,a+b
    if prime and fibonacci:
        print(x[i])
"""
#Write a function max_after_removal(n, digit) that removes one occurrence of the given digit from the number
#and returns the maximum possible number.If the digit occurs multiple times, try removing it from each
#occurrence and find which removal produces the largest number.
#Input:
#n = 154325
#digit = 5
#Possible numbers:
#14325   # remove the first 5
#15432   # remove the second 5
#Output:
#15432
n=154325

lang=0
def max(n):
    x=n[1:2:]+n[2:]
    lang=x
    r=n[1:5:]
    if int(lang) > int(r):
        print(lang)
    else:
        print(r)
max(n)
