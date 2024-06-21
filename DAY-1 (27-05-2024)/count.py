'''ip:
     3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
     
  op:
  3-4
  5-1
  4-2
  6-2
  7-2
  1-1
  2-1
  8-2'''

a=list(map(int,input().split()))
b=[]
for i in a:
    if(i not in b):
        b.append(i)
for i in b:
    print(i,"-",a.count(i))
