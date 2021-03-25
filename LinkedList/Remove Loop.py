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

    def detectLoopAndRemove(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                self.removeLoop(slow_p)
                return 1
        return 0

    def removeLoop(self, node):
        ptr1 = self.head
        while(1):
            ptr2 = node
            while(ptr2.next != node and ptr2.next != ptr1):
                ptr2 = ptr2.next

            if ptr2.next == ptr1:
                break

            ptr1 = ptr1.next

        ptr2.next = None





if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.detectLoop()