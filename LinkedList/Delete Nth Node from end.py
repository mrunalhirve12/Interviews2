class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def deleteNode(self, n):
        first = self.head
        second = self.head
        for i in range(n):
            if (second.next == None):
                if (i == n-1):
                    self.head = self.head.next
                return self.head
        second = second.next

        while(second.next != None):
            second = second.next
            first = first.next

        first.next = first.next.next

if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.deleteNode(2)