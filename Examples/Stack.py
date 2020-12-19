from dsapy.Stack import Stack

S = Stack()

l = [1,"boy",2,'k',5]

S.create(l)

print(S.pop())

print(S.arr)

S.push("dragon")

S.push(3)

print(S.arr)

print(S.pop())

print(S.arr)

print(S.pop())