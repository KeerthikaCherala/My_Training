n=int(input())
k=int(input())
if k==1:
    print(n)
for i in range(2,(n//2)+1):
    if(i%n==0):
        