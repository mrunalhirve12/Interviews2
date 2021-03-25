"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, x):
        if len(self.minstack) == 0:
            self.minstack.append(x)
        else:
            if x <= self.min_stack[-1]:
                self.min_stack.append(x)
        self.stack.append(x)

    def getMin(self):
        if self.minstack:
            return self.minstack[-1]

    def top(self):
        return self.stack[-1]


    def pop(self):
        tmp = self.stack.pop()
        if tmp == self.minstack[-1]:
            self.minstack.pop()

obj = MinStack()
obj.push()
obj.push()
obj.push()
obj.top()
obj.push(4)
obj.pop()
obj.push(4)


