n=int(input())
def rev(n,revn):
    revn=revn*10+(n%10)
    n=n//10
    if(n>0):
        return rev(n,revn)
    elif n==0:
        return revn
ans=rev(n,0)
if(n==ans):
    print("Palindrome")
else:
    print("Not Palindrome")