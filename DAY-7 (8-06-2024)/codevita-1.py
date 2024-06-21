'''
    input:
        school
        3
        L 2      ---> hoolsc
        R 3      ---> oolsch
        L 1      ---> chools
    ---->hoc
    check whether hoc is an anagram of the sub-sequences of school.
'''
s1=input()
k=int(input())
q=[]
nums=[]
for i in range(k):
    q.append(input())
#print(q)
for item in q:
  nums.append(int(item[1:]))
#print(nums)
s2=''
for i in nums:
    s2=s2+s1[i]
#print(s2)
l=[]
for i in range(len(s1)-2):
    l.append(s1[i:i+k])
print(l)
l.sort()
#print(l)
s2=''.join(sorted(s2))
#print(s2)
if s2 in l:
    print("YES")
else:
    print("NO")