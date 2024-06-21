'''
  ip:
    7854
  op:
    2(count of how many prime digits)
'''
n=int(input())
c=0
while(n):
    if(n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)
        
        