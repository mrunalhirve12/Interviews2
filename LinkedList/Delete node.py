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

    def deleteNode(self, key):
        temp = self.head

        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.data ==key:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return

        prev.next = temp.next #?

        temp = None



if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

