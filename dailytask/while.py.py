#1. Basic Counting: Write a while loop that counts from 1 to 10 and prints each number.  
"""num=0
while num<=10:
    print(num)
    num=num+1
"""
#2. Create a program that asks the user to enter a number, and then use a while loop to count down from that
#number to 1, printing each value.  
"""user=int(input("enter a number:"))
i=2
count=0
while i<user:
    count=count+1
    print(i,end="")
    print(count)
    i=i+1
    
"""

#3. Write a while loop that calculates the sum of even numbers from 1 to 100.
"""num=int(input("enter a number:"))
i=1
count=0
while i<=num:
    if i%2==0:
        count=count+1
        print(i,end="  ")
        print(count)
    i=i+1
"""
#4. Create a simple number guessing game using a while loop. Generate a random
"""import random
fix=random.randint(1,9)
i=1
while True:
    while i<=3:
        guess=int(input("enter a number"))
        if fix==guess:
            print("you are won the game")
            break
        elif guess>fix:
            print("you are bit bigg")
        elif guess<fix:
            print("you are bit small")

        i=i+1
    else:
        print("your loss the game")
    ch=input("enter if want play again say (yes/no)")
    if ch=="no":
     break
print("game over")
  """      
#5. Use a while loop to calculate the factorial of a given number.
"""num=int(input("enter a number:"))
f=1
while num>=1:
    f=f*num
    num=num-1
print(f)
    """

#6. Write a while loop that prints all even numbers between 1 and 50.
"""num=int(input("enter a number"))
i=1
count=0
while i<=num:
    if i%2==0:
        count=count+1
        print(i,end="->")
        print(count)
    i=i+1

"""
#7. Create a program that calculates the sum of the digits of a given integer using a while loop.  
"""num=int(input("enter the digits:"))
s=0
while num>0:
    d=num%10
    s=s+d
    num=num//10
print(s)
"""
#8. Generate a multiplication table for a given number using a while loop.
"""num = int(input("enter a number"))
s=1
i=1
while i<=10:
    print(num*s)
    s=s+1
    i=i+1
"""

#9. Write a program to find all the factors of a given number using a while loop.  
"""num=int(input("enter a number"))
d=1
while d<=num:
    if num%d==0:
        print(d)
    d=d+1
"""
#10. Implement a program to reverse a given number using a while loop.
"""num=int(input("enter a number:"))
reverse=0
while num>0:
    d=num%10
    reverse=reverse*10+d
    num=num//10
print(reverse)"""

#11. Create a program that prompts the user to enter a password. Keep asking until they enter the correct password.  
"""pss=input("enter your password")
while True:
    check=input("enter your password")
    if pss == check:
        print("correct")
    break
"""
#12. Write a program using a while loop to generate the first n terms of the Fibonacci sequence.
"""num=int(input("enter a number"))
a=0
b=1
print(a,b)
i=1
while i<=num:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i=i+1

"""
#13. Build a program that checks if a given number is prime using a while loop.
"""num=int(input("enter a number"))
d=2
while d<=num//2:
    if num%d==0:
        print("not prime",num)
        
    d=d+1
else:
    print(num,"is prime")
    
"""
# nth prime number
"""n=int(input("enter the number"))
count=0
num=2
while count<n:
    d=2
    factor_count =0
    while d<=num//2:
        if num%d==0:
            factor_count=factor_count+1
            
        d=d+1
    if factor_count == 0:
        count=count+1
        if count==n:
            print(num)
    num=num+1
"""

#14. Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backwards)
#using a while loop.
"""num=input("enter a word")
i=0
j=len(num)-1
count=0
while i<j:
    if num[i]!=num[j]:
        count=count+1
    i=i+1
    j=j-1
if count==0:
     print("polidrom")
else:
     print("not polindrome")
"""
#5. Write a program to generate the first n rows of Pascal's Triangle using while loops.
  row=int(input("enter  the number:"))
row_no = 0
while row_no<row:
    col=0
    while col<=row:
        if col==0 or col==row:
            print(1,end=" ")
        else:
            pass
        col=col+1
    print()
    row=row+1



    
    


