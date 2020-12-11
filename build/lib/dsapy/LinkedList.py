class Node:
    """
    Node Class

    ATTRIBUTES
    ==========

    data: any type or object (defaut none)
            value of the node

    next: Node (default none)
            the next node

    prev: Node (default none)
            the previout node

    METHODS
    =======
    
    None
            

    """
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList():
    """
    Singly Linked List Class 

    ATTRIBUTES
    ==========

    head: Node (default none)
            the starting node.
    
    end: Node (default none)
            the ending node.
    
    count: Node (default 0)
            the number of nodes in
            the linked list.

    curr: Node (default None)
            used for iteration of 
            through the linked list.

    METHODS
    =======

    create(N):
        N: Node
            setting the head = N.

    insert(N, I):
        N: Node
        I: int (index to be inserted)
            inserting a node in the linked list.

    remove(N):
        N: Node
            remove a node from the linked list.

    delete():
        no param
            delete the linked list.

    add(N):
        N: Node
            adds N to the end of the linked list.

    addH(N):
        N:Node
            adds N to the head of the linked list.

    display():
        no param
            displays the linked list.
    """
    def __init__(self,curr=None,head=None, end=None, count=0):
        self.head = head
        self.end = end
        self.count = count
        self.curr = curr

    def create(self,X):
        self.head = X
        self.curr = X
        self.end = X
        self.count+=1

    def insert(self, N, I):
        # checks if the index is out of bound
        if I < 0:
            print("Error: Index is out of bound\n")
            return
        # edge case: to add the node to the begining  
        if I == 0:
            addH(N)
            return 
        # checks if the index is out of bound
        if I > count-1: 
            print("Error: Index is out of bound\n")
            return
        
        # edge case: to add the node to the end
        if I == count-1:
            add(N)
            return 

        # insertion in the middle of the linked list

        # iterates to the index position
        for i in range(I-1):
            self.curr = self.curr.next
        
        # insert operation
        N.next = self.curr.next
        self.curr.next = N
        # reset curr
        self.curr = self.head
        #incrementing count
        self.count += 1

    def remove(self,I):
        # checks if the index is out of bound
        if I < 0:
            print("Error: Index is out of bound\n")
            return
        # edge case: to add the node to the begining  
        if I == 0:
            if self.count == 1:
                delete()
            else:
                self.head = self.head.next
                self.count -= 1
            return 
        # checks if the index is out of bound
        if I > self.count-1: 
            print("Error: Index is out of bound\n")
            return
        
        # edge case: to add the node to the end
        if I == self.count-1:
            for i in range(I-1):
                self.curr = self.curr.next
            self.end = curr
            self.count -= 1
            return 

        for i in range(I-1):
            self.curr.next()
        
        # removing for singly linked list
        self.curr.next = self.curr.next.next
        self.curr = self.head
        self.count -= 1

    def delete(self):
        self.head = None
        self.end = None
        self.count = 0
        self.curr = None

    def add(self,N):
        self.end.next = N
        self.end = N
        self.count += 1
    
    def addH(self,N):
        N.next = self.head
        self.head = N
        self.count += 1

    def display(self):
        for i in range(count-2):
            print(curr.data + "->")
            curr = curr.next
        print(curr.data+"\n")
        self.curr = self.head

