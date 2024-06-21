'''
    Input: 12
    Output: YES
    ----> 12 can be represented as the sum of two primes - 5 & 7 <------
    consider 1 as a prime.
'''

def isprime(a):
    if(a==1):
        return 1
    if(a==2):
        return 2
    for i in range(2,(a//2)+1):
        if(a%i==0):
            return 0
    return 1
a=int(input())
for i in range(1,(a//2)+1):
    if (isprime(i) and isprime(a-i)):
        print("YES")
        break
else:
    print("NO")