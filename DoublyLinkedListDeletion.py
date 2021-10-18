class node:
    def __init__(self,data):
        self.data=data
        self.nlink=None
        self.plink=None
class doubly_linkedlist:
    def __init__(self):
        self.head=None

    def print_dll(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.nlink
            print()

    def print_dll_rev(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            n=self.head
            while n.nlink is not None:
                n=n.nlink 
            while n is not None:
                print("<--",n.data,end=" ")
                n=n.plink

    def add(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nlink is not None:
                n=n.nlink
            new_node.plink=n
            n.nlink=new_node

    def del_begin(self):
        if self.head is None:
            print("sorry u cant delete because linked list is already empty")
        elif self.head.nlink is None:
            self.head=self.head.nlink
        else:
            self.head=self.head.nlink
            self.head.plink=None
            

    def del_end(self):
        if self.head is None:
            print("sorry u cant delete bec it is already empty")
        elif self.head.nlink is None:
            self.head=self.head.nlink
        else:
            n=self.head
            while n.nlink.nlink is not None:
                n=n.nlink
            n.nlink.plink=None
            n.nlink=None

    def del_enter_node(self,x):
        if self.head is None:
            print("sorry linked list is already empty ")
        elif self.head.nlink is None:
            if self.head.data is x:
                self.head=self.head.nlink
            else:
                print("x is not present in the list")
        else:
            if self.head.data==x:
                self.head=self.head.nlink
                self.head.plink=None
            else:
                n=self.head
                while n is not None:
                    if n.data is x:
                        break
                    n=n.nlink
                if n is None:
                    print("node is not present in the list")    
                else:
                    if n.nlink is None:
                        if n.data is x:
                            n=n.plink
                            n.nlink = None 
                    else:
                        n.plink.nlink=n.nlink
                        n.nlink.plink=n.plink
                            




    




dll=doubly_linkedlist()
dll.add(10)
dll.add(20)
dll.add(30)
#dll.del_begin()
#dll.del_begin()
#dll.del_end()
#dll.del_end()
dll.del_enter_node(10)
dll.print_dll()



