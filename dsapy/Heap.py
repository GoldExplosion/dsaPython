class Heap():
    """
    Min. Heap Class.

    PARAMETERS
    ==========

    arr: list
        heap array

    METHODS
    =======

    parent(n):
        PARAMETERS
        ==========
        n: int
            index position of the child.
        
        RETURNS
        =======
        int
            parent index position.
        
        to find the parent index position.
    push(n):
        PARAMETERS
        ==========
        n: int 
            data to be pushed.

        RETURNS
        =======
        None
            to append a data point to the 
            heap list.

    pop():
        PARAMETERS
        ==========

        RETURNS
        =======

    heapify():

    swap():

    heap_append():

    climb():
    """

    def __init__(self, arr=[]):
        self.arr = arr

    def push(self,n):
        self.arr.append(n)
    
    def pop(self):
        var = self.arr[-1]
        del self.arr[-1]
        return var

    def parent(self,n):
        if n%2 !=0:
            return (n-1)/2
        else: return (n-2)/2
    
    def swap(self,a,b):
        temp = self.arr[b]
        self.arr[b] = self.arr[a]
        self.arr[a] = temp 

    def parent(self,n):
        if n%2 !=0:
            return (n-1)//2
        else: return (n-2)//2
    
    def climb(self, k):
        curr = self.arr[k]
        par = self.parent(k)
        if  par<0:
            return 
        if self.arr[par] > curr:
            self.swap(par, k)
            self.climb(par)
    
    def heap_append(self, n):
        self.push(n)
        last = len(self.arr) -1
        self.climb(last)
    
    def heapify(self):
        temp = Heap()
        while(not len(self.arr)==0):
            var = self.pop()
            temp.heap_append(var)
        self.arr = temp.arr 


