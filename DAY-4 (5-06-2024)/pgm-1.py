class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            #sum=sum+t.data
            print(t.data,end="->")
            t=t.next
        print()
    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def addeven (self):       #sum of all values at even positions
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.next
        print(s)
    def addbeg(self,x):
        if self.head==None:
            t=node(x)
            self.node=t
        else:
            t=node(x)
            t.next=self.head
            self.head=t
    def lsearch(self,x):
        t=self.head
        while(t!=None):
            if(t.data==x):
                return "YES"
            t=t.next
        return "NO"
    def mid(self):
        t=self.head
        fast=t
        slow=t
        while(fast!=None and fast.next!=None):
                slow=slow.next
                fast=fast.next.next
        print(slow.data)
    def leo(self):         #To know the length of list is even or odd
        t=self.head
        fast=t
        while(fast!=None and fast.next!=None):
                fast=fast.next.next
        if(fast==None):
            print("Even")
        else:
            print("Odd")
    def subs(self):           #to know the length of longest substring
        t=self.head
        c1,c2=1,1
        while(t.next!=None):
            if ((t.next.data)-(t.data)==1):
                c1=c1+1
            else:
                c2=max(c1,c2)
                c1=1
            t=t.next
        print(max(c1,c2))
    def pairs(self):
        t=self.head
        while(t.next!=None):
            t1=t.next
            while(t1!=None):
                print(t.data,t1.data,end="")
                t1=t1.next
            t=t.next
            print()
    def llen(self):
        s=self.head
        c=1
        while(s!=None and s.next!=None):
            c=c+1
            s=s.next
        #print(c)
        return c
    def bubsort(self):
        t1=self.head
        p=None
        while(t1.next!=None):
            flag=0
            t=self.head
            while(t.next!=None):
                if(t.data >t.next.data):
                    flag=1
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
            if(flag==0):
                break
            p=t
            t1=t1.next
    '''def rev(self):
        t=self.head
        a=t
        b=a.next
        while(t.next!=None):
            a.next=None
            b=self.head
            c=b.next'''
    def rev(self):
       t = self.head 
       a = None       
       b = t.next         
       while (t!=None):
           t.next=a      
           a = t
           t = b
           if b:
               b = b.next
       #initializing head
       self.head = a
        
l1=sll()
l1.head=node(10)
l1.addback(1)
l1.addbeg(945)
l1.addback(78)
l1.addback(4)
l1.display()
l1.addeven()
l1.rev()
l1.display()
#n=l1.llen()
#l1.bubsort()
#l1.display()
#l1.pairs()
#print(l1.lsearch(3))
#l1.mid()
#l1.leo()
#l1.subs()