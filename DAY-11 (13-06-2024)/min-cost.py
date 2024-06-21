def cost(d,x,e,c,m,l1):           #x = starting node , e = ending node
    l.append(x)
    if (x==e):
        if(c<m):
            m=c
            l1=l.copy()
        l.pop()
        return m,l1
    for i in d[x]:
        if i[0] not in l:
            m,l1=cost(d,i[0],e,c+i[1],m,l1)
    l.pop()
    return m,l1
    
d={5:[(7,2),(3,4)],7:[(5,2),(4,2),(3,2)],4:[(7,2),(8,3),(2,5)],8:[(4,3),(3,2),(2,4)],3:[(5,4),(7,2),(8,2)],2:[(4,5),(8,4)]}
l=[]
c=[]
print(cost(d,5,2,0,999999,[]))