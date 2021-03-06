"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.data = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        rtype = dummyhead = ListNode(0)

        while l1 and l2:
            if l1.data < l2.data:
                rtype.next = ListNode(l1.data)
                l1 = l1.next
            else:
                rtype.next = ListNode(l2.data)
                l2 = l2.next
            rtype = rtype.next

        if l1:
            rtype.next = l1

            # if l2 list still present
        if l2:
            rtype.next = l2

        return dummyhead.next






l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)

s =   Solution()
s.mergeTwoLists(l1, l2)
