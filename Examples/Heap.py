from dsapy.Heap import Heap

a = [5,7,8,34,7,34, 2, 0]

l = Heap(a)

l.heapify()

print(l.arr)