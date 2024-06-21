'''
    input-1:
        "(([{}]))"
    output:
        -1
    input-2:
        "[{()]]"
    output:
        5
    input-3:
        "[()]()"
    output:
        -1
    input-4:
        "[(){}{()}]"
    output:
        -1
'''
class node:
    def __init__(self,x):
        self.data=x
        self.next= None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            '''self.tail.next=node(x)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next'''
            t=node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=self.tail.next
    def addbeg(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.head.prev=t
            t.next=self.head
            self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="-->")
            t=t.next
        print()
    def par(self):
        t=self.head
        s=[]
        pos=0
        flag=1
        while(t!=None):
            if(t.data in '{[('):
                s.append(t.data)
            elif(not s):
                if(t.data=='}' and s[-1]=='{' or t.data==']' and s[-1]=='[' or t.data=='(' and s[-1]==')'):
                        s.pop()
                else:
                    print(pos)
                    flag=1
                    break
            else:
                print(pos)
                flag=1
                #break
                pos=pos+1
        return -1
    '''def evsd(self):
        esum=0
        osum=0
        t=self.head
        def sol(t,osum,esum):
            if(t!=None):
                if(t.data%2==0):
                    esum=esum+t.data
                    t=t.next
                else:
                    osum=osum+t.data
                    t=t.next
                return sol(t,osum,esum)
            else:
                diff=(max(esum,osum)-min(esum,osum))
                return diff
        ans=sol(t,osum,esum)
        return ans'''
    def evsd(self,t,esum,osum):
        if t==None:
            return abs(esum-osum)  
        if(t.data%2==0):
            esum=esum+t.data  
        else:
            osum=osum+t.data
        return self.evsd(t.next,esum,osum)
    def primecount(self,t,c):
        if t==None:
            return c
        def prime(s,n):
            if(s>=(n//2)+1):
                return 1
            if(n%s==0):
                return 0
            return prime(s+1,n)
        if prime(2,t.data)==1:
            c=c+1
        return self.primecount(t.next,c)
    
l1=dll()
l1.addbeg("111")
l1.addback("2")
l1.addback("3")
l1.addback("4")
l1.addback("5")
l1.addback("6")
l1.display()
#----------------------print(l1.evsd(l1.head,0,0))
print(l1.primecount(l1.head,0))
#l1.par()