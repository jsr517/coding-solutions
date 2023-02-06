class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_nodes(head):
    count = 1
    current = head
    while current.next is not None:
        current = current.next
        count += 1
    return count


nodeA = Node(2)
nodeB = Node(25)
nodeC = Node(43)
nodeD = Node(2123)
nodeE = Node(43)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

print("length is: ")
print(count_nodes(nodeA))
