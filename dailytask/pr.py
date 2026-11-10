lit=[1,0,2,3,0,4,0,53,]
first=[]
for i in range(0,len(lit)-1):
    if i==0:
        first.append(lit[i])
        lit.pop(lit[i])
print(lit+first)


