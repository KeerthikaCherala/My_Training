def bfs(d,n):         #n = start node
    v=[]
    q=[n]
    while(len(q)!=0):
        for i in d[q[0]]:
            if i not in v and i not in q:
                q.append(i)
        v.append(q.pop(0))
    return v   
d={9:[1,3],1:[3,9],3:[5,1,9],5:[3,7],7:[6,5,4],6:[7,4],4:[6]}
print(bfs(d,9))