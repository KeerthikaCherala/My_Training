'''
    input1:
        3
        xyz
        pqr
        abc
        "ypcxpaxrb"
    output:
        yes
    input2:
        4
        abcd
        xyze
        pqrw
        stuv
        "cyptdzsayq"
    output:
        no
    '''
n=int(input())
m=[]
for i in range(n):
    m.append(list(input()))
#matrix = [input() for _ in range(n)]
s=input()
flag=0
for i in range(len(s)):
    if(s[i] in m[i%n]):
        m[i%n].remove(s[i])
        continue
    else:
        flag=1
        break
if flag==1:
    print("NO")
else:
    print("YES")