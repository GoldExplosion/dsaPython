class BinaryTree():
    """
    Binary Tree class.

    ATTRIBUTES
    ==========

    data: int
        the key value

    left: BinaryTree
        the left child BT

    right: BinaryTree
        the right child BT

    METHODS
    =======

    insert(Data): 
        PARAMETERS
        ==========
        
        data: any type
            data to be added.

        RETURNS
        =======

        None

            initialization of binary tree.
    display(s): 
        PARAMETERS
        ==========

            to specify the order of printing.
            options: in , pre , post
        RETURNS
        =======

        None

            prints the tree in specified order
    
    find(n, count):
        PARAMETERS
        ==========

        n: int
            key value
        
        count: int
            positions value

        RETURNS
        =======

        count: int

            it returns the position value or else None.
            the position value goes like this...
                        0
                       /   \
                     1       2
                    /  \    /   \
                   3    4  5     6
                  / \  / \/ \   / \        

    search(key):
        PARAMETERS
        ==========

        key: int
            the to data to be searched

        RETURNS
        =======

        Node
            the Object address for the node. 
            if a node with the data value 
            equal to key doesn't exist, then
            it returns None.
    """

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, Data):
        if self.data is not None:
            if self.data >= Data:
                if self.left is None:
                    self.left= BinaryTree(Data)
                else:
                    self.left.insert(Data)
            else:
                if self.right is None:
                    self.right = BinaryTree(Data) 
                else:
                    self.right.insert(Data)
        else:
            self.data = Data 
    
    def display(self, s="in"):
        if s == "in":
            if self.left:
                self.left.display()
            print(self.data, end=" ")
            if self.right:
                self.right.display()
        elif s == "pre":
            print(self.data, end=" ")
            if self.left:
                self.left.display(s="pre")
            if self.right:
                self.right.display(s="pre")
        elif s=="post":
            if self.left:
                self.left.display(s="pre")
            if self.right:
                self.right.display(s="pre")
            print(self.data, end=" ")
        else:
            print("ERROR: Invalid Order Type")
    
    def find(self, n, count=0):
        if self.data == n:
            return count 
        
        if self.data < n:
            if self.right is None:
                return self.right
            return self.right.find(n, count=2*count+2)
        
        if self.left is None:
            return self.left 
        return self.left.find(n, count=2*count+1)
    
    def search(self, key):
        if self.data == key:
            return self
        
        if self.data < key:
            if self.right is None:
                return self.right 
            return self.right.search(key)
        
        if self.left is None:
            return self.left
        return self.left.search(key)
    
