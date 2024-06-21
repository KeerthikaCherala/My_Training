a=input()
s=[]
c=0
for i in a:
    if(i in '{[('):
        s.append(i)
    elif(not s):
        if(i=='}' and s[-1]=='{' or i=='(' and s[-1]==')' or i=='[' and s[-1]==']'):
            s.pop()
        else:
            print(c)
            break
if len(s)==0:
    print(-1)
        