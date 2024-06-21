'''
ip:
  prime number 
  13   14
op:
  13   17
  
'''

'''n=int(input())
c=0
for i in range(2,(n//2)+1):
    if n%i==0:
        c=1
        break
if c==1:
    k=True
    while(k): 
        n=n+1
        co=0
        for i in range(2,(n//2)+1):
            if n%i==0:
                co=1
        if co==1:
            continue
        else:
            print(n)
            k=False
else:
    print(n)'''
#factors always available in first half of the numbers only
# 100 come in 1 to 50 but it will not come in 51 to 99
n=int(input())
while(1):
    c=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            c=c+1
            break 
    if(c==0):
        print(n)
        break
    else:
        n=n+1
    
