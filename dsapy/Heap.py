from dsapy.Queue import Queue
import math

def Node():
    def __init__(self, data = None, parent = None):
        self.data = data 
        self.left = None 
        self.right = None

def Heap():
    """
    Min Heap Class

    ATTRIBUTES
    ==========

    data: int

    left: Heap
        left child

    right: Heap
        right child

    METHODS
    =======

    push():
        PARAMETERS
        ==========takeuchi
        n: int
            data to be pushed into the heap.
        
        RETURNS
        =======

        None

    pop():
        PARAMETERS
        ==========

        None

        RETURNS
        =======

        int
            the data on 
    """

    def __init__(self):
        self.que = Queue()
        self.root = None
        self.count = 0
    
    def height():
        return math.ceil(math.log2(self.count+1)) - 1

    def push(n):
        if self.root is None:
            self.root = Node(n)
            count += 1
            return
        
        self.que.push(self.root)
        while(!self.que.isempty()):
            temp = self.que.pop()
            if temp is None:
                temp = Node(n)
                count+=1
                self.que = Queue()
                return
            self.que.push(temp.left)
            self.que.push(temp.right)
    
    def pop():
        pop_que = Queue()
        if self.root is None:
            return self.root 

        N = self.height()
        curr = self.root
        for i in range(N-1):
            curr = curr.left
        
        self.que.push(self.root)
        temp1 = self.root 
        while(!self.que.isempty()):
            temp = self.que.pop()
            if temp is None:
                