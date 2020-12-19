class Stack():
    """
    Stack Class.

    ATTRIBUTES
    ==========

    arr: list
        the stack array. this stack array implementation 
        assumes that there are no None type as element.

    top: int
        the top element index


    METHODS
    =======

    create(arr):
        arr: list
            initializes the list as stack array.

    push(Data):
        Data: any type
            adds Data to the top of the stack array.
    pop():
        no param
            returns the top most element.
    """

    def __init__(self, arr=None):
        self.arr = arr

    def create(self, arr):
        """
        initializes the stack array.
        
        PARAMETERS
        ==========
        
        arr: list
            an empty list or a list containing data

        RETURNS
        =======

        None
        """
        self.arr = arr
        self.top = len(self.arr) - 1
    
    def push(self, Data):
        """
        pushes data.

        PARAMETERS
        ==========

        Data: any type
            data to be pushed

        RETURNS
        =======
        None
        """
        self.arr.append(Data)
    
    def pop(self):
        """
        pops the last element.

        PARAMETERS
        ==========

        None

        RETURNS
        =======

        val: any type
            the top data element in the stack array.
        """
        if len(self.arr) > 0:
            val = self.arr[-1]
            del self.arr[-1]
            return val
        
        else: return None 