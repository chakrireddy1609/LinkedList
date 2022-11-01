class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head is None:
            self.head = Node(data)

        else:
            newNode = Node(data)
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode

    def print(self):
        currNode = self.head
        while currNode:
            print(currNode.data)
            currNode = currNode.next


llist = LinkedList()
llist.append("Chakri")
llist.append("Anusha")
llist.print()

