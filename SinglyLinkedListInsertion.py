class node:
    def __init__(self,data):
        self.data=data
        self.link=None
class linkedlist:
    def __init__(self):
        self.head=None

    def print_ll(self):
        if self.head is None:
            print("linked list is empty!")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.link
    def add_begin(self,data):
        new_node=node(data)
        new_node.link=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.link is not None:
                n=n.link
            n.link=new_node

    def add_after(self,data,x):
        new_node=node(data)
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.link
        if n is None:
            print("node is not present in ll")
        else:
            new_node.link=n.link
            n.link=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.data==x:
            new_node=node(data)
            new_node.link=self.head
            self.head=new_node
            return
        n=self.head
        while n.link is not None:
            if n.link.data==x:
                break
            n=n.link
        if n.link is None:
            print("node is not found")
        else:
            new_node=node(data)
            new_node.link=n.link
            n.link=new_node
            
    def insert_empty(self,data):
        if self.head is None:
            new_node=node(data)
            self.head=new_node
        else:
            print("linked list is not empty")




ll1=linkedlist()
#ll1.add_begin(10)
#ll1.add_begin(20)
#ll1.add_begin(30)
#ll1.add_end(40)
#ll1.add_after(100,20)
#ll1.add_mid(200,100)
#ll1.add_before(300,20)
#ll1.add_before(300,20)
ll1.insert_empty(10)
#ll1.insert_empty(10)
ll1.print_ll()

    
