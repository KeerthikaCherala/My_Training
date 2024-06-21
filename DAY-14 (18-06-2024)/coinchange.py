'''
ip:[4,3,5]
    17
op:4-->minimum no.of coins required to get 17 rupees
'''
def fun(n):        #  0  1  2  3  4  5  6  7
    l1=[-1]*(n+1)  #[-1,-1,-1,-1,-1,-1,-1,-1]
    l1[0]=0        #[0,-1,-1,-1,-1,-1,-1,-1]
    for i in l:
        for j in range(1,n+1):
            if(j>=i):
                if(l1[j-i]!=-1):
                    if(l1[j]!=-1):
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1)
    print(l1[-1])#---->it print the total no:of coins requried to make the given amount
                
                    

l=list(map(int,input().split()))
n=int(input())
fun(n)


'''m=[]

a=[-1]*(n+1)
a[0]=0
m.append(a)


for i in range(1,len(l)):
    k=[0]*(n+1)
    m.append(k)
    


for i in range(len(l)):
    print(m[i])
    
print()

for i in range(len(l)):
    for j in range(len(m[i])):
        if l[i]==1:
            m[i][j]=j
        else:
            if j<l[i]:
                if m[i-1][j]<j:
                    m[i][j]=m[i-1][j]
                else:
                    m[i][j]=j
            elif j==l[i]:
                m[i][j]=1
            else:
                t=j-l[i]
                te=m[i][t]
                if te==-1:
                    m[i][j]=m[i-1][j]
                else:   
                    te=te+1
                    if m[i-1][j]<te:
                        m[i][j]=m[i-1][j]
                    else:
                        m[i][j]=te
                                                   
                    
for i in range(len(l)):
    print(m[i])'''