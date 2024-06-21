# A program to print all the possible three-three combinations of numbers in list.
l=list(map(int,input().split()))
k=3
def combo(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
combo(l,k)        