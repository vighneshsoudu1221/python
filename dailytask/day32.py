#1 Write a Python function to rearrange a string so that each word is placed immediately after its reversed form.
#Preserve the original word order.
#Input: hello world python
#Output: hello olleh world dlrow python nohtyp
"""x="hello world python"
out=[]
res=x.split()
for i in res:
    out.append(i)
    out.append(i[::-1])
c=" ".join(out)
print(c)"""
#2 Write a Python function to find the longest word in a sentence that contains all unique characters.
#Input: apple dream house coding
#Output: dream
"""x="apple dream house coding"
def unique(x):
    length=0
    res=x.split()
    out=""
    for i in res:
        if len(i)==len(set(i)) and len(i)>length:
            length=len(i)
            out=i
    return out
re=unique(x)
print(re)  """   
#3 Write a Python function to find the word whose characters have the highest total ASCII value.
#If multiple words have the same value, return the first one.
#Input: cat dog apple
#Output: apple
"""x="cat dog apple"
def vowel(x):
    sum=0
    ress=" "
    res=x.split()
    for i in res:
        s=0
        for j in i:
            s=s+ord(j)
        if s>sum:
            sum=s
            ress=i
    return ress
res=vowel(x)
print(res)"""

#4 Write a Python function to decode a string where each alphabetic character is followed by a number indicating
#how many times it should be repeated.
#Input: a3b2c4
#Output: aaabbcccc
x="a3b2c4"
def repeated(x):
    d=" "
    for i in range(0,len(x)-1,2):
        d=d+x[i]*int(x[i+1])
    return d
        
y=repeated(x)
print(y)
            


            
            
        
