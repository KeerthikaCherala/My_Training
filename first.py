x=int(input("Enter a number: "))
def dig_sum(x):
    sum=0
    temp=x
    while(x!=0):
        rem=x%10
        x=x//10
        sum=sum+rem
    if (sum%10==0):
        return sum
    else:
        return dig_sum(sum)
def prime(sum):
    n=sum
    if (n in [2,3,5,7]):
        return n
    else:
        n=n+1
        return dig_sum(n)
sum=dig_sum(x)  
prime(sum)  