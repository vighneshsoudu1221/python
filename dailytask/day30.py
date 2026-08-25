#1.Write a Python program to compress a string.
#Input : aaabbc
#Output : a3b2c1
"""x="aaabbc"
count=1
st=""
for i in range(0,len(x)-1):
    if x[i]==x[i+1]:
        count=count+1
    else:
        st=st+x[i]+str(count)
        count=1
st=st+x[-1]+str(count)
        
print(st)"""

#2. Write a Python program to create a mirror string.
#Input : abc
#Output : abccba        
"""x="abc"
d=x[::-1]
print(x+d)
"""
#3. Write a Python program to find the longest palindromic substring.
#Input : babad
#Output : bab
"""x="babad"
s=" "
for i in range(len(x)):
    for j in range(len(x)-1,-1,-1):
        if x[i:j]==x[i:j][::-1]:
            if len(x[i:j])>len(s):
                s=x[i:j]
print(s)"""


#4.Write a Python function to remove all special characters from a string.
#Input : a@1#b
#Output : a1b
"""
x="a@1#b"
st=""
for i in x:
    if i.isalpha() or i.isdigit():
        st=st+i
print(st)
"""

#5.Write a Python function to reverse every alternate word in a sentence.
#Input : one two three four
#Output : one owt three ruof
x="one two three four"
st=""
for i in range(0,len(x)):
    if i%2!=0:
        st=st+x[i::-1]
    else:
        st=st+x[i]
print(st)

