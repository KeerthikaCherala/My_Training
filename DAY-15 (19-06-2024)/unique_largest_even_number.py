'''
    input:
        tu5g2k1h8
        g5g8gd6h3  ------> Extract the unique numbers from the given string. i.e, 521863 and give the largest possible even number as the output
    output:
        865312
'''
n1=input()
n2=input()
s1=set()
for i in n1:
    if i.isdigit():
        s1.add(int(i))
for i in n2:
    if i.isdigit():
        s1.add(int(i))
s1=list(s1)
s1.sort(reverse=True)
if (int(s1[-1])%2==0):
    print(''.join(s1))
else:
    for i in range(len(s1)-2,-1,-1):
        if (int(s1[i])%2==0):
            s1.append(s1.pop(i))
            print(''.join(s1))
            break
    else:
        print(-1)