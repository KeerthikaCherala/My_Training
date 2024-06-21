'''
    input:
        5
    output:
        * * * * *
        * 1 2 3 *
        * 4 5 6 *
        * 7 8 9 *
        * * * * *
'''
n=int(input())
k=1
for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(k,end=" ")
            k=k+1
    print()