class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x):
        self.stack1.append(x)
        self.size += 1

    def pop(self):
        if self.stack2:
            x = self.stack2.pop()
        else:
            for _ in range(self.size-1):
                self.stack2.append(self.stack1.pop())
            x = self.stack1.pop()
        self.size -= 1
        return x

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        else:
            for _ in range(self.size-1):
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.size == 0

# Your MyQueue object will be instantiated and called as such:
obj = Queue()
obj.push(1)
obj.push(2)
y = obj.pop()
print(y)
print(obj.peek())
print(obj.empty())

