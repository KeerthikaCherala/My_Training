'''
    input:
        5 3 2 7 8 4
        M T W T F S
    -price of the pen
    -Buy it once and sell it once
    -Buy it and sell it in the same week
    -What is the maximum profit you can make?
    
    output:
        6   (Maximum profit)
'''
'''a=list(map(int,input().split()))
m2=min(a)
m=a.index(min(a))
if m==len(a)-1:
    m1=min(a[:m])
    m=a.index(m1)
n=max(a[m:])
profit=n-m2
print(profit)'''

a=list(map(int,input().split()))
profit=0
bp=a[0]
for i in a:
    if i<bp:
        bp=i
    elif (i-bp)>profit:
        profit=i-bp
print(profit)