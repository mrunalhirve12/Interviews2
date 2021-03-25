# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge(l1, l2):

            newnode = ListNode(0)

            trace = newnode

            while (l1 and l2):

                if l1.val < l2.val:
                    newnode.next = ListNode(l1.val)
                    newnode = newnode.next
                    l1 = l1.next
                else:
                    newnode.next = ListNode(l2.val)
                    newnode = newnode.next
                    l2 = l2.next

            if l1:
                newnode.next = l1
            else:
                newnode.next = l2

            return trace.next

        def mergesort(cur):

            if cur.next == None:
                return cur

            slow = cur
            fast = cur.next

            while (fast and fast.next):
                slow = slow.next
                fast = fast.next.next

            l1 = cur
            l2 = slow.next

            slow.next = None

            l1 = mergesort(l1)
            l2 = mergesort(l2)

            return merge(l1, l2)

        if head == None or head.next == None:
            return head
        return mergesort(head)