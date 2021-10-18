class node:
    def __init__(self,data):
        self.data=data
        self.plink=None
        self.nlink=None
class doubly_linkedlist:
    def __init__(self):
        self.head=None
    def print_dll(self):
        if self.head is None:
            print("doubly linkedlist is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n=n.nlink
            print()
    def print_dll_rev(self):
        if self.head is None:
            print("doubly linkedlist is empty")
        else:
            n=self.head
            while n.nlink is not None:
                n=n.nlink
            while n is not None:
                print("<---",n.data,end=" ")
                n=n.plink 

    def add_firstnode(self,data):
        if self.head is None:
            new_node=node(data)
            self.head=new_node  
        else:
            print("linked list is not empty")        

    def add_begin(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node=node(data)
            new_node.nlink=self.head
            self.head.plink=new_node
            self.head=new_node

    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nlink is not None:
                n=n.nlink
            n.nlink=new_node
            new_node.plink=n

    def add_after(self,data,x):
        if self.head is None:
            print("linked list is empty")
        else:
            new_node=node(data)
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nlink
            if n is None:
                print("item is not present")
            else:
                new_node.nlink=n.nlink
                new_node.plink=n
                if n.nlink is not None:
                    n.nlink.plink=new_node
                n.nlink=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("linked list is empty")
        else:
            new_node=node(data)
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                n=n.nlink
            if n is None:
                print("item not found in linked list")
            else:
                new_node.nlink=n
                new_node.plink=n.plink
                if n.plink is not None:
                    n.plink.nlink=new_node
                else:
                    self.head=new_node
                n.plink=new_node

dll=doubly_linkedlist()
#dll.add_firstnode(10)
#dll.add_begin(20)
#dll.add_begin(30)
dll.add_end(40)
dll.add_end(50)
dll.add_after(30,40)
dll.add_after(60,50)
dll.add_before(100,40)
dll.add_before(200,60)
dll.print_dll()
dll.print_dll_rev()

