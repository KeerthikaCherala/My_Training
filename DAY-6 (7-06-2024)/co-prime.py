a=int(input())
b=int(input())
'''def factors(n):
    c=[]
    for i in range(2,(n//2)+1):
        if(n%i==0):
            c.append(i)
    return c
a1=factors(a)
b1=factors(b)
if not any(i in a1 for i in b1):
    print("Yes")
else:
    print("No")'''
for i in range(2,(min(a,b)//2)+1):
    if (a%i==0) and (b%i==0):
        print("NO")
        break
else:
    print("YES")