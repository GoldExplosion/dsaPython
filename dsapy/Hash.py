class Hash():
    """
    Hash class
    
    PARAMETERS
    ==========
    hashTable: list

    METHODS
    =======
    display():

    hashing():

    insert():
    """
    def __init__(self):
        self.hashTable = [[] for _ in range(10)]

    def hashing(self, val):
        return val % len(self.hashTable)

    def insert(self, key, val):
        hashKey = self.hashing(key)
        self.hashTable[hashKey].append(val)

    def display(self):

        for i in range(len(self.hashTable)):
            print(i, end= " ")

            for j in self.hashTable[i]:
                print("-->", end = " ")
                print(j, end = " ")
            
            print()