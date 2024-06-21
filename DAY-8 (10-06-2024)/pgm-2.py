'''s=input()
s=set(s)
if len(s)==27:
    print("YES")
else:
    print("NO")'''    
s= input()
s=set(s)
c=0
for i in s:
    if i.islower():
        c=c+1
if c==26:
    print("YES")
else:
    print("NO")
    
'''
a=input()
for i in range(97,123):
    if(chr(i) not in a):
        print("NO")
else:
    print("YES")



a=input()
d=[0]*26
for i in a:
    if(i.islower()):
    d[ord(i)-97]=1
print(all(d))
'''