class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, after_node):
        new_node = Node(data)

        # find node location
        temp = self.head
        while temp.data != after_node:
            temp = temp.next
        prev = temp

        new_node.next = prev.next
        prev.next = new_node

    def prepend(self, data):
        # if list not empty
        if self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        # if list empty
        self.append(data)

    def append(self, data):
        new_node = Node(data)
        # if there are nodes already
        if self.head:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            return
        #if no nodes yet
        self.head = new_node

    def print(self):
        nodes = self.head
        while nodes.next:
            print(nodes.data)
            nodes = nodes.next
        print(nodes.data)







