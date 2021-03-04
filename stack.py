class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.empty():
            return self.items[-1]

    def contains(self, data):
        if data in self.items:
            return True
        return False

    def empty(self):
        if len(self.items) == 0:
            return True
        return False

    def print_stack(self):
        print(self.items)


