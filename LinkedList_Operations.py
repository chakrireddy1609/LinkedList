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

    def prepend(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def append_after_node(self,prevNode,data):
        if not prevNode:
            return "Node does not exist in Linked List"
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def delete(self,key):
        currNode = self.head
        if currNode and currNode.data == key:
            self.head = currNode.next
            currNode is None
            return

        prevNode = None
        while currNode and currNode.data != key:
            prevNode = currNode
            currNode = currNode.next
            if currNode is None:
                return
        prevNode.next = currNode.next
        currNode is None

    def delete_postion(self,pos):
        currNode = self.head
        if pos == 0:
            self.head = currNode.next
            currNode is None

        count = 0
        prevNode = None

        while currNode and count != pos:
            prevNode = currNode
            currNode = currNode.next
            count += 1

        if currNode is None:
            return
        prevNode.next = currNode.next
        currNode is None

    def len_iterative(self):
        currNode = self.head
        count = 0
        while currNode:
            count += 1
            currNode = currNode.next
        return count

    def len_recursive(self,node):
        if node is None:
            return 0
        return 1+self.len_recursive(node.next)


llist = LinkedList()
llist.append("Chakri")
llist.append("Anusha")
llist.prepend("Aadriti")
llist.print()
llist.append_after_node(llist.head.next,"Reddy")
llist.print()
llist.delete("Reddy")
llist.print()
print(llist.len_iterative())
print(llist.len_recursive(llist.head))





