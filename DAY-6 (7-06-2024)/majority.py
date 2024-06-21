l=list(map(int,input().split()))
'''n=len(l)//2
c=[]
for i in range(len(l)):
    c.append(l.count(l[i]))
    if c[i]>(n):
        print(l[i])
        break'''
c=1                              #count initialised as 1.
w=l[0]                           #winner variable started with first element of the list.
for i in range(1,len(l)):        
    if l[i]!=w:                  #Decrement the count value if the current element and winner elements are not same.
        c=c-1
        if c==0:     
            w=l[i]               #If the count is '0', winner is the current element and increment the count value.
            c=1
    elif l[i]==w:                #Increment the count value if the current element and winner elements are same.
        c=c+1
        w=l[i]                   #Winner is the current element.
print(w)