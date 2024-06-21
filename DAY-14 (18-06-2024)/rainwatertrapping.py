'''
ip:-[2,5,2,3,6,7,1,0,5]-->heights of the buliding
op:-14

ip:-[2,5,2,3,6,7,1,0,5,7]-->heights of the buliding
op:-20

ip:-4 3 4 5 6 1 0 6 7
op:-12
'''

h=list(map(int,input().split()))

l=[0]*len(h)
r=[0]*len(h)
m=0

for i in range(len(h)):
    if h[i]>m:
        m=h[i]
    l[i]=m
        
m=0
for i in range(len(h)-1,-1,-1):
    if h[i]>m:
        m=h[i]
    r[i]=m

print(l,r)

s=0
for i in range(len(h)):
    #t=min(l[i],r[i])
    #s=s+(t-h[i])
    s=s+abs(min(l[i],r[i])-h[i])
print(s)
    


        
