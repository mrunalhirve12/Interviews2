class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList :
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

def insert(root, item):
    temp = Node(item)

    if (root == None):
        root = temp #?
    else:
        ptr = root
        while(ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
        return root

def display(root):
    while (root != None):
        print(root.data)
        root = root.next

def arrayToList(self, arr, n):
    root = None
    for i in range (0, n , 1):
        root = insert(root, arr[i])
    return root




if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    arr = [1,2,3,4]
    n = len(arr)
    root = arrayToList(arr, n)






