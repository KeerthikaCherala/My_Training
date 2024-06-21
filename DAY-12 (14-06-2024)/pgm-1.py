'''l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
len(l1)=len(l2)
[7,6+5,6+3,6+6,9+9,2+7,2+5,2+3,2+9,4+7,4+5,4+3,4]=====   OUTPUT:[13,11,9,15,7,9,5,11,11,9,7,13]
OUTPUT:[(13+11+9+15),(7+5+11+9),(11+9+7+13)] ====  [48,32,40]'''
l1=list(map(int,input().split(",")))
l2=list(map(int,input().split(",")))
e=[]
o=[]
i,j=0,0
res=0
res1=[]
def fun(l1,l2,e,o,i):
    if(i<len(l1)):
        if l1[i]%2==0:
            e.append(l1[i])
        if(l2[i]%2!=0):
            o.append(l2[i])
        fun(l1,l2,e,o,i+1)
    return  (e,o)
def fun1(e,o,res,i,j,res1):
    if(i<len(e)):
        if(j<len(o)):
            res=res+e[i]+o[j]
            return fun1(e,o,res,i,j+1,res1)
        res1.append(res)
        return fun1(e,o,0,i+1,0,res1)
    return res1
e,o=fun(l1,l2,e,o,i)
a=fun1(e,o,res,i,j,res1)
print(a)