'''
    input:
        4
    output:
        1 1 1 1 1 1 1
        1 2 2 2 2 2 1
        1 2 3 3 3 2 1
        1 2 3 4 3 2 1
        1 2 3 3 3 2 1
        1 2 2 2 2 2 1
        1 1 1 1 1 1 1
'''
n=int(input())
k=1
for i in range(0,(2*n)-1):
    for j in range(0,(2*n)-1):
        if i==0 or i==2*n-2 or j==0 or j==2*n-2:
            print(k,end="")           
        else:
            print('2',end="")
    print()