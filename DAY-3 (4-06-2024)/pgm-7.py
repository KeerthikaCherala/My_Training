'''
    input:
        4
    output:
        _ _ _ _ a _ _ _ _
        _ _ _ a b a _ _ _
        _ _ a b c b a_ _
        _ a b c d c b a_
'''
n=int(input())
k=97
'''for i in range(0,n):
    for j in range(0,(2*n+1)):
        if i==0:
            if j==n:
                print(chr(97),end=" ")
            else:
                print("_",end=" ")
        else:
            print("_",end=" ")'''
for i in range(n,0,-1):
    for j in range(i):
        print("_",end="")
    if i==n:
        print(chr(k),end="")
    else:
        a=97
        for b in range(n-i):
            print(chr(a),end="")
            a=a+1
        print(chr(a),end="")
        for b in range(n-i):
            print(chr(a-1),end="")
            a=a-1
    for m in range(i):
        print("_",end="")
    print()