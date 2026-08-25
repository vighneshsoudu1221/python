#1 write a python program to find the element that occurs most frequently in a neste list
#input:x=[[10,20,30][20,40,20][60,10,20]]
#output: Element: 20
       # frequency: 4
"""x=[[10,20,30],[20,40,20],[60,10,20]]
out={}

for i in x:
    for j in i:
        out[j]=out.get(j,0)+1
max_frequency=0
elment=0
for i in out:
    if out[i]>max_frequency:
        max_frequency=out[i]
        element=i
print("element:",element)
print("frequency:",max_frequency)"""

# 2. write a python program to sort a dictionary based on its values in descending order
# input: d={"A":45,"B":80,"C":25,"D":60,"E":90}
#output:{"E":90,"B":80,"D":60,"A":45,"c":25}
"""d={"A":45,"B":80,"C":25,"D":60,"E":90}
y=list(d.items())
for j in range(0,len(y)-1):
    for i in range(0,len(y)-j-1):
        if y[i][1]<y[i+1][1]:
            y[i],y[i+1]=y[i+1],y[i]
output={k:v for k,v in y}
print(output)"""

#3. write a function that takes a list as input and returns the first element  that occurs than once
#input: x=[10,25,30,15,25,40,30]
#output:frist repeating  element:25
"""
x=[10,25,30,15,25,40,30]
def count(x):
    out=[]
    count=1
    for i in x:
        if i in out:
            count=count+1
        else:
            out.append(i)
        if count>1:
            print("First repeating element:",i)
            break
count(x)
"""
#4.write a funtion that takes a string and return a new string after removing all vowel
#input:S="hello Wolrd"
#output:Hll Wrld
s="Hello Wolrd"
def vowel(s):
    out=""
    for i in s:
        if i not in "aeiouAEIOU":
            print(i,end="")
   
vowel(s)
            
        
        
    
