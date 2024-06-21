'''
ip:
2 5 7 9
1 3 6 7 10 13

op:
1 2 3 5 6 7 7 9 10 13'''

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=l1+l2
l.sort()
print(l)





