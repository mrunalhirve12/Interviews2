class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxstack = []

    def push(self, x):
        if len(self.maxstack) == 0:
            self.maxstack.append(x)
        else:
            if x >= self.max_stack[-1]:
                self.max_stack.append(x)
        self.stack.append(x)

    def getMin(self):
        if self.max_stack:
            return self.max_stack[-1]

    def top(self):
        return self.stack[-1]


    def pop(self):
        tmp = self.stack.pop()
        if tmp == self.max_stack[-1]:
            self.max_stack.pop()

obj = MaxStack()
obj.push()
obj.push()
obj.push()
obj.top()
obj.push(4)
obj.pop()
obj.push(4)