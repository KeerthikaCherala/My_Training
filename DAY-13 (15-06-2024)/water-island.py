'''
    input:
        5
        0 1 0 0 1
        1 0 0 1 1                                         0--->Water
        0 0 0 0 0                                         1---> Island
        1 0 0 0 0
        1 0 0 0 1
        
    output:
        2
'''
def fun(i,j,n,c):
    if (i<0 or j<o or i>=n or j>=n or a[i][j]!=1):
        return
    a[i][j]=2
    c1=fun(i,j-1,n,c)
    c1=fun(i,j+1,n,c)
    c1=fun(i-1,j,n,c)
    c1=fun(i+1,j,n,c)
    return c1
a=[]
n=int(input())
a = [[] for _ in range(n)] 
c1=0
m=0
for i in range(n):
    for j in range(n):
        if(a[i][j]==1):
            k=fun(i,j,n,0)
            if (k>m):
                m=k
            c1=c1+1
print(c1,m)