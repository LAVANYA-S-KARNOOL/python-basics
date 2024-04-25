class node:
    def __init__(self,data)->None:
        self.data=data
        self.next=None 
        self.prev=None
class dll:
    def __init__(self)->None:
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def insertatend(self,data):
            if self.head==None:
                self.head=node(data)
                self.tail=self.head
            else:
                new=node(data)
                self.tail.next=new
                new.prev=self.tail
                self.tail=new
    def printing(self):
            i=self.head
            while i:
                print(i.data)
                i=i.next
o=dll()
for i in range(1,6):
    o.insertatend(i)
    # o.insertatbeg(i)
o.printing()
