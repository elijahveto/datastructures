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
        current_node = self.head
        while current_node != after_node:
            current_node = current_node.next
        prev = current_node

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
        # if no nodes yet
        self.head = new_node

    def print(self):
        nodes = self.head
        while nodes.next:
            print(nodes.data)
            nodes = nodes.next
        print(nodes.data)

    def delete(self, del_node):
        current_node = self.head
        # if not empty and head node to be deleted
        if current_node and current_node.data == del_node:
            self.head = current_node.next
            current_node = None
            return
        # if not empty and list not finished yet
        elif current_node:
            while current_node.data != del_node and current_node:
                prev = current_node
                current_node = current_node.next
            # list finished and value not found
            if current_node is None:
                return
            prev.next = current_node.next
            current_node = None
            return

    def delete_at_index(self, position):
        # assuming linked list starts at 0
        current_node = self.head
        # if not empty and head node to be deleted
        if position == 0:
            self.head = current_node.next
            current_node = None
            return
        # if not empty and list not finished yet
        elif current_node:
            num = 1
            prev = None
            while num != position and current_node:
                prev = current_node
                current_node = current_node.next
                num += 1
            if current_node is None:
                return
            prev.next = current_node.next
            current_node = None

    def length(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def swap_data(self, node1, node2):
        size = self.length()
        if size >= 2:
            node_1, node_2 = None, None
            current_node = self.head
            loops = 0
            while loops <= size and node_1 == None or node_2 == None:
                # print(current_node.data)
                if current_node.data == node1:
                    node_1 = current_node
                elif current_node.data == node2:
                    node_2 = current_node
                current_node = current_node.next
                loops += 1
            if loops <= size:
                temp = node_1.data
                node_1.data = node_2.data
                node_2.data = temp
            return

    def swap_nodes(self, node1, node2):
        if node1 == node2:
            return

        prev_n1 = None
        node_1 = self.head
        while node_1 and node_1.data != node1:
            prev_n1 = node_1
            node_1 = node_1.next

        prev_n2 = None
        node_2 = self.head
        while node_2 and node_2.data != node2:
            prev_n2 = node_2
            node_2 = node_2.next

        if not node_2 or not node_1:
            return

        if prev_n1:
            prev_n1.next = node_2
        else:
            self.head = node_2

        if prev_n2:
            prev_n2.next = node_1
        else:
            self.head = node_1

        node_1.next, node_2.next = node_2.next, node_1.next

    def reverse(self):
        node = self.head
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        self.head = prev


    def merge(self, ll2):
        node1 = self.head
        node2 = ll2.head
        while node1:
            prev = node1
            node1 = node1.next
            while node2 and node2.data < node1.data:
                self.insert(node2.data, prev)
                prev = prev.next
                node2 = node2.next



