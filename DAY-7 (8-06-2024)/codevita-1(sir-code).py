a=input()
n=int(input())
str=''
for i in range(n):
    b=input()
    if(b[0]=='L'):
        str=str+a[int(b[2])]
    else:
        str=str+a[-int(b[2])]
print(str)
b=[]
for i in range(len(a)-n+1):
    t=list(a[i:n+i])
    t.sort()
    b.append(t)
print(b)
str=list(str)
str.sort()
print(str)
for i in b:
    if(i==str):
        print("YES")
        break
else:
    print("NO")