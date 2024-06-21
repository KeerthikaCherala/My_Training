# Print the length of longest substring
s=input()
c1,c2=1,1
for i in range(len(s)):
    if (i+1)<len(s):
        if ord(s[i])-ord(s[i])==1:
            c1=c1+1
        else:
            c1=max(c1,c2)
            c1=1
print(c2)            