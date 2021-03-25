class CreatingQueueWithTwoStacks():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.push(x)

    def dequeue(self):
        if not self.stack1:
            while self.stack1.size() > 0:
                self.stack2.push(self.stack1.pop())
            res = self.stack2.pop()
            while self.stack2.size() > 0:
                self.stack1.push(self.stack2.pop())
            return res


q = CreatingQueueWithTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
a = q.dequeue()
print(a)
b = q.dequeue()
print(b)
c = q.dequeue()
print(c)
d = q.dequeue()
print(d)
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
