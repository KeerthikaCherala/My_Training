a=[1,5,8,9]
b=[2,7,9,10,14]
i,j=0,0
c=[]

while (i<len(a) and j<len(b)):
    if a[i]<b[j]:
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1

'''using slice operator 
if(j<len(b)):
       c.extend(b[j:])
   if(i<len(a)):
       c.extend(a[i:])
'''
while(j<len(b)):
    c.append(b[j])
    j=j+1

while(i<len(a)):
    c.append(a[i])
    i=i+1
    
    
print(c)
        