#DAY-2 Program-1
def dig_sum(x,sum1):
    #sum1=0
    if(x<10):
        return prime(x)
    else:
        while(x!=0):
            rem=x%10
            x=x//10
            sum1=sum1+rem
        if (sum1>=10):
            return dig_sum(sum1,0)
        else:
            return sum1
def prime(sum2):
    n=sum2
    if (n in [2,3,5,7]):
        return n
    else:
        return dig_sum(temp+1,0)
x = int(input("Enter a number: "))
temp=x
sum1=0
sum2 = dig_sum(x,sum1)
# print(sum2)
print(prime(sum2))