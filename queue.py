class Queue:
    def __init__(self):
        self.que = []

    def enq(self, data):
        self.que.append(data)

    def deq(self):
        return self.que.pop(0)

    def peek(self):
        return self.que[0]

queue = Queue()


