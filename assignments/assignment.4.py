#1. Write a program to find the longest consecutive increasing subsequence in a list ofintegers.
#Input: [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#Output : [1,2,3,4,5]
"""
x=[1, 2, 3, 1, 2, 3, 4, 5,1, 2, 3, 4, 5]

def count(x):
    l=[]
    long=[]
    
    for i in range(0,len(x)-1):
        if x[i]<x[i+1]:
            if len(l)==0:
               l.append(x[i])
            l.append(x[i+1])
        else:
           if len(l)>len(long):
              long=l
           l=[]
    if len(l)>len(long):
        long=l
    
    return long
print(count(x))"""
                
            
#2. Write a Python program to decode a string where a number before brackets indicates
#how many times the characters inside the brackets should be repeated.
#Input: 3[a]2[bc]
#Output: aaabcbc
"""x = "3[a]2[bc]"

def fun(x):
    num = ""
    text = ""
    out = ""

    for i in x:
        if i.isdigit():
            num = num + i

        elif i == "[":
            text = ""

        elif i == "]":
            out = out + text * int(num)
            num = ""

        else:
            text = text + i

    print(out)

fun(x)
"""
#3. Write a program to group all the words that are anagrams of each other.
#Explaination: Two words are called anagrams if they contain the same characters with
#the same frequency, but the characters may appear in a different order.
#Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
#Output: [["eat", "tea", "ate"],["tan", "nat"],["bat"]]
x = ["eat", "tea", "tan", "ate", "nat", "bat"]

def anagram(x):
    d = {}

    for i in x:
        key = "".join(sorted(i))

        if key not in d:
            d[key] = []

        d[key].append(i)

    print(list(d.values()))

anagram(x)
#4. Write a program to count all substrings that are palindromes in a given string.
#A palindromic substring is a substring that reads the same forward and backward. For
#"aaa", the palindromic substrings are a, a, a, aa, aa, aaa, so the total count is 6.
#Input: ’aaa’
#Output: 6
"""x = "aaa"

def palindrome(x):
    count = 0

    for i in range(len(x)):
        for j in range(i + 1, len(x) + 1):
            sub = x[i:j]

            if sub == sub[::-1]:
                count = count + 1

    print(count)

palindrome(x)"""

        
