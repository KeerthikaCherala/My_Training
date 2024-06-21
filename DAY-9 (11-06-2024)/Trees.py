class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
    def create(self,root,x):
        if(root==None):
            return node(x)
        elif(root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
    
    def nodesum(self,root):
        if root==None:
            return 0
        return root.data+self.nodesum(root.left)+self.nodesum(root.right)
    
    def evensum(self,root):
        if root==None:
            return 0
        if root.data%2==0:
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        else:
            return self.evensum(root.left)+self.evensum(root.right)
        
    def oddsum(self,root):
        if root==None:
            return 0
        else:
            if root.data%2!=0:
                return root.data+self.oddsum(root.left)+self.oddsum(root.right)
            else:
                return self.oddsum(root.left)+self.oddsum(root.right)
            
    def diffofeveodd(self,root): 
        if root==None:
            return 0
        if root.data%2==0:
            return self.diffofeveodd(root.left)+self.diffofeveodd(root.right)+root.data
        return self.diffofeveodd(root.left)+self.diffofeveodd(root.right)-root.data
                            
    def Inorder(self,root):
        if root is not None:
            self.Inorder(root.left)
            print(root.data)
            self.Inorder(root.right)
            
    def Preorder(self,root):
        if root is not None:
            print(root.data)
            self.Preorder(root.left)
            self.Preorder(root.right)
        
    def Postorder(self,root):
        if root is not None:
            self.Postorder(root.left)
            self.Postorder(root.right)
            print(root.data)
            
    def height(self,root,h):
        if root==None:
            return -1
        return h+max(self.height(root.left,h),self.height(root.right,h))
    
    def baltree(self,root):
        return abs(self.height(root.left,0)-self.height(root.right,0)) <= 1
    
    def leafnodes(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        return self.leafnodes(root.left)+self.leafnodes(root.right)
        
    def leafnodesum(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data
        return self.leafnodesum(root.left)+self.leafnodesum(root.right)
        
    def search(self,root,n):
        if root==None:
            return 0
        if root.data==n:
            return 1
        if root.data>n:
            return self.search(root.left,n)
        else:
            return self.search(root.right,n)
    
    def depth(self,root,n,c):
        if root==None:
            return -1
        if (root.data==n):
            return c
        if root.data>n:
            return self.depth(root.left,n,c+1)
        else:
            return self.depth(root.right,n,c+1)
   
    def leftview(self,root,c,c1):
        if root==None:
            return 
        else:
            if c not in c1:
                c1.append(c)
                print(root.data)
        self.leftview(root.left,c+1,c1)
        self.leftview(root.right,c+1,c1)

    def rightview(self,root,c,c1):
        if root==None:
            return 
        else:
            if c not in c1:
                c1.append(c)
                print(root.data)
        self.rightview(root.right,c+1,c1)
        self.rightview(root.left,c+1,c1)
            
    def topview(self,root):
        if root==None:
            return
        d={}
        q=[(root,0)]
        while(len(q)!=0):
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            if(q[0][1] not in d):
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i])
    
    def bottomview(self,root):
        if root==None:
            return
        d={}
        q=[(root,0)]
        while(len(q)!=0):
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i])
            
                   
c1=[]
t1=tree()
t1.root=t1.create(t1.root,10)
t1.create(t1.root,5)
t1.create(t1.root,2)
t1.create(t1.root,7)
t1.create(t1.root,4)
t1.create(t1.root,3)
t1.create(t1.root,15)
t1.create(t1.root,11)
t1.create(t1.root,20)
print("----INORDER TRAVERSAL----")
t1.Inorder(t1.root)
print("----PREORDER TRAVERSAL----")
t1.Preorder(t1.root)
print("----POSTORDER TRAVERSAL----")
t1.Postorder(t1.root)
print("----SUM OF ALL NODES----")
print(t1.nodesum(t1.root))
print("----ABSOLUTE DIFFERENCE BETWEEN LEFT SUBTREE AND RIGHT SUBTREE----")
print(abs(t1.nodesum(t1.root.left)-t1.nodesum(t1.root.right)))
print("----EVEN SUM----")
print(t1.evensum(t1.root))
print("----ODD SUM----")
print(t1.oddsum(t1.root))
print("----ABSOLUTE DIFFERENCE BETWEEN EVEN SUM AND ODD SUM----")
print(abs(t1.diffofeveodd(t1.root)))
print("----HEIGHT----")
print(t1.height(t1.root,1))
print("----BALANCED TREE----")
if t1.baltree(t1.root):
    print("Balanced")
else:
    print("Not Balanced")
print("----LEAF NODES----")
print(t1.leafnodes(t1.root))
print("----LEAF NODE SUM----")
print(t1.leafnodesum (t1.root))
print("----SEARCHING----")
if t1.search(t1.root,9):
    print("Found")
else:
    print("Not Found")
print("----DEPTH OF THE NODE----")
print(t1.depth(t1.root,9,0))
l=[]
print("----TOP VIEW OF TREE----")
t1.topview(t1.root)
print()
print("----BOTTOM VIEW OF TREE----")
t1.bottomview(t1.root)
print()
print("----LEFT VIEW OF TREE----")
t1.leftview(t1.root,0,[])
print("----RIGHT VIEW OF TREE----")
t1.rightview(t1.root,0,[])