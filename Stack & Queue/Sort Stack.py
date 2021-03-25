def sortStack(stack):
    tmpstack = createstack()
    while isEmpty(stack) == False:
        tmp = top(stack)
        pop(stack)
        while (isEmpty(tmpstack) == False and int(top(tmpstack)) > int(tmp)):
            push(stack, top(tmpstack))
            pop(tmpstack)
        push(tmpstack, tmp)
    return tmpstack

def createstack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack, val):
    stack.append(val)

def top(stack):
    p = len(stack)
    return stack[p-1]

def pop(stack):
    if isEmpty(stack):
        print("Stack Underflow ")
        exit(1)
    return stack.pop()


# Driver Code
stack = createStack()
push(stack, str(34))
push(stack, str(3))
push(stack, str(31))
push(stack, str(98))
push(stack, str(92))
push(stack, str(23))

print("Sorted numbers are: ")
sortedst = sortStack(stack)
prints(sortedst)