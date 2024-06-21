s=input()
l=[]
for i in s:
    if i=='*':
        l.pop()
    else:
        l.append(i)
print("".join(l))