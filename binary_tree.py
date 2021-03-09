from queue import queue
from stack import stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print(self, trav_type):
        if trav_type == 'preorder':
            print(self.preorder_traversal(self.root))
        elif trav_type == 'inorder':
            print(self.inorder_traversal(self.root))
        elif trav_type == 'postorder':
            print(self.postorder_traversal(self.root))
        elif trav_type == 'linear':
            print(self.level_traversal(self.root))
        elif trav_type == 'reverse list':
            print(self.reverse_trav_list(self.root))
        elif trav_type == 'reverse stack':
            print(self.reverse_trav_stack(self.root))


    def preorder_traversal(self, start, traversal=''):
        if start:
            traversal += (str(start.data)+ '_')
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal=''):
        if start:
            traversal = self.preorder_traversal(start.left, traversal)
            traversal += (str(start.data) + '_')
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal=''):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.data) + '_')
        return traversal

    def level_traversal(self, start, traversal ='', que = queue):
        if start == self.root:
            que.enq(start)
        if start:
            node = que.deq()
            traversal += (str(node.data) + '-')
            que.enq(node.left)
            que.enq(node.right)
            traversal = self.level_traversal(que.peek(), traversal, que)
        return traversal


    def reverse_trav_list(self, start, que = [], traversal = ''):
        if start == self.root:
            que.append(start)
            start = 0
        if start < len(que):
            if que[start].right:
                que.append(que[start].right)
            if que[start].left:
                que.append(que[start].left)
            start +=1
            traversal = self.reverse_trav_list(start, que)
        while len(que) >0:
            traversal += (str(que.pop().data) + '-')
        return traversal

    def reverse_trav_stack(self, start, traversal ='', que = queue, stack = stack):
        if start == self.root:
            queue.enq(start)
        if start:
            node = queue.deq()
            stack.push(node)
            if node.right:
                queue.enq(node.right)
            if node.left:
                queue.enq(node.left)
            traversal = self.reverse_trav_stack(queue.peek(), traversal, que, stack)
        while not stack.empty():
            traversal += (str(stack.pop().data) + '-')
        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_h = self.height(node.left)
        right_h = self.height(node.right)
        return 1 + max(left_h, right_h)

    def size(self, node, result = 0):
        if node is None:
            return 0
        result += 1 + self.size(node.left)
        result += 1 + self.size(node.right)
        return result - 1

        # even better:
        # return 1 + self.size(node.left) + self.size(node.right)

    def size_stack(self, start):
        if not start:
            return 0
        stack.push(start)
        count = 0

        while not stack.empty():
            node = stack.pop()
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
            count += 1
        return count

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.search_place(self.root, data)


    def search_place(self, node, item):
        if item < node.data:
            if node.left is None:
                node.left = Node(item)
            else:
                self.search_place(node.left, item)
        elif item> node.data:
            if node.right is None:
                node.right = Node(item)
            else:
                self.search_place(node.right, item)
        else:
            return


    def search_tree(self, data, node = None):
        if node is None:
            node = self.root
        if data == node.data:
            return node
        elif data < node.data and node.left:
            return self.search_tree(data, node.left)
        elif data > node.data and node.right:
            return self.search_tree(data, node.right)
        else:
            return None







