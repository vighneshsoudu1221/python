
#A company's system records daily sales. Find the maximum number of consecutive days where the sales keep increasing.
#If the next day's sales are equal to orlower than the previous day, the streak starts again.
#Input: 100 120 150 140 160 180 200 190 210 O
"""x=[100,120,150,140,160,180,200,190,210]
pre=[]
y=[]
for i in range(0,len(x)-1):
    if x[i]<x[i+1]:
         y.append(x[i])
    else:
       if x[i]<x[i+1]:"""
           
"""            
2. A company receives a large customer log string and needs to identify the smallest continuous portion that contains all required characters.
Given two strings S and T, find the minimum-length substring of S that contains every character of T with the required frequency.
If no such substring exists, print -1.
Input:
S = "ADOBECODEBANC"
T = "ABC"
Output:
BANC
Example 2:
S = "AAABBC"
T = "AABC"
Output:
AABBC"""
