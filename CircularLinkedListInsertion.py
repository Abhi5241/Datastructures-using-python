class node:
    def __init__(self,data):
        self.data=data
        self.link=None
class circular_linkedlist:
    def __init__(self):
        self.head=None
    def print_cll(self):
        if self.head is None:
            print("circular linked list is empty")
        else:
            n=self.head
            while n :
                print(n.data,"-->",end=" ")
                n=n.link
                if n == self.head:
                    break

    def add_begin(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            self.head.link=self.head
        else:
            n=self.head
            while n.link is not self.head:
                n=n.link
            new_node.link=self.head
            n.link=new_node
            self.head=new_node

    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head==new_node
            self.head.link=self.head
        else:
            n=self.head
            while n.link is not self.head:
                n=n.link
            new_node.link=self.head
            n.link=new_node

    def add_after(self,data,x):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            new_node.link=self.head

        else:
            n=self.head
            while n is not self.head.data:
                if n.data == x:
                    break
                n=n.link
            if n==self.head.data:
                print("item not found")
                
            elif n.data == x:
                new_node.link=n.link
                n.link=new_node
                
    

            

            

                    
            



cll=circular_linkedlist()
cll.add_begin(10)
"""cll.add_begin(20)
cll.add_begin(30)
cll.add_end(0)"""
cll.add_after(40,10)
cll.add_after(30,10)
cll.add_after(60,10)
cll.print_cll()
            

