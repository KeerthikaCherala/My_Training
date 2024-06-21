''' Using recursion take the below input and give the output
INPUT:
    a=[3,8,5,4,3]
    b=[5,0,9,3,2]
OUTPUT:
    result=(12,17)'''
a=list(map(int,input().split()))
b=list(map(int,input().split()))
def fun(i,s1,s2):
    if(i==len(a)):
        return s1,s2
    if(a[i]%2==0):
        s1=s1+a[i]
    if(b[i]%2!=0):
        s2=s2+b[i]
    return fun(i+1,s1,s2)
x,y=fun(0,0,0)
print(x,y)