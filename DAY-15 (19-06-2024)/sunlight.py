l=list(map(int,input().split()))
mc,ec=1,1
m=l[0]
n=len(l)
for i in range(n):
    if(m<l[i]):
        mc=mc+1
        m=l[i]
    else:
        m=m
m=l[-1]
for i in range(n-1,0,-1):
    if(m<l[i]):
        ec=ec+1
        m=l[i]
    else:
        m=m
print(mc,ec)