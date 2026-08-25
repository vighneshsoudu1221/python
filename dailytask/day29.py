#1.Write a Python function to count the number of words that contain at least two vowels.
#Input:Python is easy to learn
#Output:2
#Explanation:Count the words that contain at least two vowels.
"""s="Python is easy to learn"
def vowel(st):
    count=0
    for i in range(0,len(st)):
        for j in "aeiouAEIOU":
           if st[i]==j:
               count=count+1
               if count==2:
                   print(count)
               
vowel(s)
"""
#2.Write a Python function to find the first character that appears more than once in a string.
#Input:abcaefbd
#Output:a
#Explanation:
#The character a is the first character that appears more than once.
"""s="abcaefbd"
def count(st):
    res=""
    for i in st:
        if st[0] in st:
            res=st[0]
    print(res)
                   
count(s)
"""
#3.Write a Python function to check whether a string contains all unique characters.
#Input:python
#Output:True
#Explanation:
#Return True if no character appears more than once; otherwise, return False.
"""x="python"
def unique(n):
    for i in n:
        if n.count(i)>1:
            return False
    return True
res=unique(x)
print(res)"""
#4.Write a Python function to create a new dictionary by assigning a rank to each key based on its value in descending order. The highest value should get rank 1.
#Input:{'A': 85, 'B': 92, 'C': 78, 'D': 88}
#Output:{'B': 1, 'D': 2, 'A': 3, 'C': 4}
#Explanation:
#Assign ranks based on the values in descending order. The key with the highest value gets rank 1, the next highest gets rank 2, and so on.
"""d={'A': 85, 'B': 92, 'C': 78, 'D': 88}
def ranks(st):
    sorted_marks=sorted(st.items(), key=lambda x: x[1],reverse=True)
    result={}
    
    for rank, (key, value) in enumerate(sorted_marks, 1):
        result[key] = rank

    return result
print(ranks(d))"""
#5.Write a Python function to check whether two lists are rotations of each other.
#Input:
#[1, 2, 3, 4, 5]
#[3, 4, 5, 1, 2]
#Output:
"""True
Explanation:
Return True if one list can be obtained by rotating the other; otherwise, return False."""




