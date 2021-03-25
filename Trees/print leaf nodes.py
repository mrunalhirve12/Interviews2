# Python3 program to print
# leaf nodes from left to right

# Binary tree node
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to print leaf
# nodes from left to right
def printLeafNodes(root: Node) -> None:
    # If node is null, return
    if (not root):
        return

    # If node is leaf node,
    # print its data
    if (not root.left and
            not root.right):
        print(root.data,
              end=" ")
        return

    # If left child exists,
    # check for leaf recursively
    if root.left:
        printLeafNodes(root.left)

    # If right child exists,
    # check for leaf recursively
    if root.right:
        printLeafNodes(root.right)


# Driver Code
if __name__ == "__main__":
    # Let us create binary tree shown in
    # above diagram
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)

    # print leaf nodes of the given tree
    printLeafNodes(root)

# This code is contributed by sanjeev2552