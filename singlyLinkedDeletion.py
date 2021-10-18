class node:
    def __init__(self,data):
        self.data=data
        self.link=None
class linkedList:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.link

    def add_begin(self,data):
        new_node=node(data)
        new_node.link=self.head
        self.head=new_node

    def del_begin(self):
        if self.head is None:
            print("sorry deletion wont happen due to linked list is already empty")
        else:
            self.head=self.head.link

    def del_end(self):
        if self.head is None:
            print("sorry deletion wont happen due to linked list is already empty")
        elif self.head.link is None:
            self.head=None
        
        else:
            n=self.head
            while n.link.link is not None:
                n=n.link
            n.link=None

    def del_mid(self,x):
        if self.head is None:
            print("sorry u can't delete bec it is already empty")
        elif self.head.data is x:
            self.head=self.head.link
        else:
            n=self.head
            while n.link is not None:
                if n.link.data==x:
                    break
                n=n.link
            if n.link is None:    
                print("sorry you can't delete because item is not present in the list")
            else:  
                n.link=n.link.link


ll1=linkedList()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
#ll1.del_begin()
#ll1.del_begin()
#ll1.del_end()
ll1.del_mid(10)
ll1.del_mid(200)
ll1.print_ll()


