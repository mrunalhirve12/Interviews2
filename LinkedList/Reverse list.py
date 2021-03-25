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

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #let curr point to start of the the LL
        curr = head
        #initialize prev and next to None
        prev = None
        next = None
        # while curr is not None(i.e end)
        while curr is not None:
            #store next first,
            # store prev in curr.next,
            # update prev and next
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev



if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.middle()