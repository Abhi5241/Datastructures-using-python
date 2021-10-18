class bst:
    def __init__(self,key):
        self.key=key
        self.rtree=None
        self.ltree=None

    def insert(self,data):
        if self.key is None:
            self.key=data
        elif self.key==data:
            pass

            
        elif self.key > data:
            if self.ltree:
                self.ltree.insert(data)
            else:
                self.ltree=bst(data)
        else:
            if self.rtree:
                self.rtree.insert(data)
            else:
                self.rtree=bst(data)

    def search(self,data):
        if self.key is None:
            print(f"{data} is not present in the tree.")
        elif self.key==data:
            print(f"{data} is present in the tree")
        elif self.key>data:
            if self.ltree:
                self.ltree.search(data)
            else:
                print(f"{data} is not present in the tree")
        else:
            if self.rtree:
                self.rtree.search(data)
            else:
                print(f"{data} is not present in the tree")


    def preorder(self):
        print(self.key,end=" ")
        if self.ltree:
            self.ltree.preorder()
        if self.rtree:
            self.rtree.preorder()
        

    def inorder(self):
        if self.ltree:
            self.ltree.inorder()
        print(self.key,end=" ")
        if self.rtree:
            self.rtree.inorder()

    def postorder(self):
        if self.ltree:
            self.ltree.postorder()
        if self.rtree:
            self.rtree.postorder()
        print(self.key,end=" ")


    def deletion(self,data,curr):
        if self.key is None:
            print("tree is empty you cant delete")
            return
        if data < self.key:
            if self.ltree:
                self.ltree=self.ltree.deletion(data,curr)
            else:
                print(f"{data} is not present in the tree")
        elif data > self.key:
            if self.rtree:
                self.rtree=self.rtree.deletion(data,curr)
            else:
                print(f"{data} is not present in the tree")
        else:
            if self.ltree is None:
                temp=self.rtree
                if data==curr:
                    self.key=temp.key
                    self.rtree=temp.rtree
                    self.ltree=temp.ltree
                    temp=None
                    return
                self=None
                return temp
            if self.rtree is None:
                temp=self.ltree
                if data==curr:
                    self.key=temp.key
                    self.rtree=temp.rtree
                    self.ltree=temp.ltree
                    temp=None
                    return
                self=None
                return temp

            n=self.rtree
            while n.ltree:
                n=n.ltree
            self.key=n.key
            self.rtree=self.rtree.deletion(n.key,curr)
        return self

    def minmax(self):
        if self.key is None:
            print("tree is empty")
        elif self.ltree is None:
            min=self.key
            temp=self.rtree
            while temp.rtree:
                temp=temp.rtree
            max=temp.key
            print(f"min={min} and max={max}")
            
        elif self.rtree is None:
            max=self.key
            temp=self.ltree
            while temp.ltree:
                temp=temp.ltree
            min=temp.key
            print(f"min={min} and max={max}")
            
        else:
            temp=self.ltree
            temp1=self.rtree
            while temp.ltree:
                temp=temp.ltree
            min=temp.key
            
            while temp1.rtree:
                temp1=temp1.rtree
            max=temp1.key
            print(f"min={min} and max={max}")






def count(node):
    if node is None:
        return 0
    return 1+count(node.ltree)+count(node.rtree)
    


root=bst(None)
root.insert(200)
list1=[100,20,30,40,50,10,300,400,50,1,1000]
for i in list1:
    root.insert(i)

root.minmax()





"""   
#root.search(10)
print("This is preorder :",end=" ")
root.preorder()
print("\nThis is inorder  :",end=" ")
root.inorder()
print("\nThis is postorder:",end=" ")
root.postorder()
print()
print("after deleting:")
root.preorder()
print()"""

