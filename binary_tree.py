from queue import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print(self, traversal):
        if traversal == 'preorder':
            print(self.preorder_traversal(self.root, ''))
        elif traversal == 'inorder':
            print(self.inorder_traversal(self.root, ''))
        elif traversal == 'postorder':
            print(self.postorder_traversal(self.root, ''))
        else:
            print(self.level_traversal(self.root, ''))

    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.data)+ '_')
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.preorder_traversal(start.left, traversal)
            traversal += (str(start.data) + '_')
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.data) + '_')
        return traversal

    def level_traversal(self, start, traversal, que = queue):
        if start == self.root:
            que.enq(start)
        if start:
            node = que.deq()
            traversal += (str(node.data) + '-')
            que.enq(node.left)
            que.enq(node.right)
            traversal = self.level_traversal(que.peek(), traversal, que)
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.level_traversal(tree.root, ''))
#tree.print('level')
