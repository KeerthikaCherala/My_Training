'''
    input:
        2
        polikujmnhytgbvfredcxswqaz
        abcd---->string 1
        qwryupcsfoghjkldezxvbintma
        ativedoc---->string 2
    output:
        bdca ---->output1
        codevita ---->output2   
'''

'''n=int(input())             -----------------------------------------------MY CODE-----------------------------------------------------
for i in range(0,n):
    s=input()
    str=input()
    l=[]
    for i in str:
        l.append(s.index(i))
    print(l)
    l.sort()
    s1=''
    for i in l:
        s1=s1+s[i]
    print(s1)'''

# ------------------------------------------------------------SIR'S CODE------------------------------------------------------------------

n=int(input())
while(n):
    a=input()
    c=input()
    s=''
    for i in a:
        if(i in c):
            s=s+(i*c.count(i))
    print(s)
    n=n-1