# Longest substring without repeating characters
a=input()
i=0
d={}
s=''
m=len(s)
while (i<len(a)):
    while(i<len(a)):
        if(a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
        i=i+1
    i=d[a[i]]+1
print(m)