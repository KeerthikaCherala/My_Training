'''
    input:
        [4,8,14,22,36,68]
        ----> All the elements in the list are non-prime numbers in the increasing order.
        the output should be the sum of all the highest prime numbers in between each pair of consecutive numbers in the list.
'''
'''def prime(a,b):
    l1=[]
    for i in range(a+1,b):
        for j in range(2,(i//2)+1):
            if(i%j==0):
                l1=l1.append(j)
            else:
                l1.append(0)
    r=max(l1)
    return r
l=list(map(int,input().split()))
s=[]
for i in range(len(l)-1):
    c=prime(i,i+1)
    s.append(c)
print(s)'''


def isprime(n):
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return 0
    return 1

def lprime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0

s=0
a=list(map(int,input().split()))
for i in range(len(a)-1):
    lprime(a[i],a[i+1])
    s=s+lprime(a[i],a[i+1])
print(s)    