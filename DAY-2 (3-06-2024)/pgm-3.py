'''INPUT:
        10
   OUTPUT:
       sum of all even numbers from 1 to 10'''

def res(x):
    if(x==0):
        return 0
    return x+res(x-2)
n=int(input())
if(n%2==0):             #When the number is even.
    print(res(n))
else:                   #When the number is odd.
    print(res(n-1))
    
    
'''def add(n,i,s):
    if(i==n):
        return s
    if(i%2==0):
        s=s+i
        return add(n,i+1,s)
n=int(input())
print(add(n,0,0))'''