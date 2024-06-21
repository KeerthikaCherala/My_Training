'''
    input-1:
        [1,2,3,4,1,2,3,1,2]
    output:
        [[1 2 3 4],[1 2 3],[1 2]]
    input-2:
        [2,3,1,3,4,3,2]
    output:
        [[2 3 1 4],[3 2],[3]]
    input-3:
        [4,5,2,1]
    output:
        [[4,5,2,1]]
'''
l=list(map(int,input().split(",")))
l1=[]
c=0
while(c!=len(l)):
    r=[]
    for i in range(len(l)):
        if(not str(l[i]).isalpha()):
            if(l[i] not in r):
                c=c+1
                r.append(l[i])
                l[i]='l'
    l1.append(r)
print(l1)
    
'''# Dictionary


'''        