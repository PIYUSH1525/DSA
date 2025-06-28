class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

a = Node(20)
b = Node(10)
c = Node(50)
a.next = b
b.next =c
print(id(b))
print(a.next)