'''ip:
     aaabbaaaaddd
   op:
     a3b2a4d3'''
'''
str=input()
c=1
i=0
j=1
l=[]
while(i<len(str) and j<len(str)):
    if(str[i]==str[j]):
        c=c+1
        i=i+1
        j=j+1
    else:
        l.append(str[i])
        l.append(c)
        c=1
        i=i+1
        j=j+1
l.append(str[i])
l.append(c)

print(' '.join(l))'''

a="aaabbaaaadddb"
c=1
b=''
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        c=c+1
    else:
        b=b+a[i]+str(c)
        c=1
b=b+a[-1]+str(c) #i+1 ,-1
print(b)
    
        