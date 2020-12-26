from dsapy.BinaryTree import BinaryTree

#n1 = Node(23)

#n2 = Node(4)

#n3 = Node(23)

#n4 = Node(345)

a = BinaryTree(2)

a.insert(1)
a.insert(4)
a.insert(3)
a.insert(12)
a.insert(77)
a.insert(7)
a.insert(-22)



a.display()

print()

temp = a.search(-22)

print(temp)

if temp is not None:
    print(temp.data)

print(a.find(12))