n=int(input())
l=list(map(int,input().split()))
'''for i in range(n+1):
    if i not in l:
        print(i)'''
'''l=l.sort()
for i in range(n):
    if l[i]!=i:
        print(i)'''
add=((n*(n+1))//2)
s=0
s=sum(l)
print(add-s)