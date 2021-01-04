class Queue():
    """
    Queue Class.

    ATTRIBUTES
    ==========

    que: list
        the queue

    METHODS
    =======

    push(D):
        
        parameters
        ==========
        D: any type
        
        returns
        =======

            pushes the data
    pop():
        
        parameters
        ==========
        None
        
        returns
        =======
        first data element
        
            pops the first data element
    isempty():
        parameters
        ==========
        None

        returns
        =======
        Boolean

            returns true if empty else false.
    """
    def __init__(self, que=[]):
        self.que = que
    
    def push(self, D):
        self.que.append(D)
    
    def pop(self):
        val = self.que[0]
        del self.que[0]
        return val
    
    def isempty():
        if len(self.que) == 0:
            return True
        else: return False 
        