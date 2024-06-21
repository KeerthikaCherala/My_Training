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
    def lsearch(self,x):
        t=self.head
        s=self.tail
        while(t!=s and t!=s.next):
            if(t.data==x or s.data==x):
                return "Found"
            t=t.next
            s=s.prev
        if(t.data==x):
            return "Found"
        return "Not Found"
    def leo(self):
        t=self.head
        s=self.tail
        while(t!=None):
            if(t==s.next or s==t.prev):
                return "Even"
            elif (t==s):
                return "Odd"
            t=t.next
            s=s.prev
    def pal(self):
        t=self.head
        s=self.tail
        while(t!=s and t!=s.next):
            if(t.data!=s.data):
                return "No"
            t=t.next
            s=s.prev
        return "Yes"
    def manipulate(self):
        f=self.head
        s=self.head
        while(f!=None):
            f=f.next.next
            s=s.next
        self.tail.next=self.head
        self.head.prev=self.tail
        t1=s.prev
        t1.next=None
        s.prev=None
        self.head=s
        self.tail=t1
    def swapel(self):
        t=self.head
        t1=t.next
        t3=None
        while(t!=None):
            t.next=t1.next
            t1.next=t
            t1.prev=t3
            t.prev=t1
            t3=t1.prev
            t,t1=t1,t
            t3=t1

l1=dll()
l1.addbeg(1)
l1.addback(2)
l1.addback(3)
l1.addback(4)
#l1.addback(1)
l1.display()
#l1.manipulate()
l1.swapel()
l1.display()
#l1.display()
#print(l1.lsearch(78))
#print(l1.leo())
#print(l1.pal())