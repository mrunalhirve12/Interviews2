"""
Given a linked list, remove the n-th node from the end of list and return its head.
Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Follow up:
Could you do this in one pass?
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # if not node and n
        if not head or not n:
            return

        # initialize node to point ll; slowptr and headptr to operate
        dummy = ListNode(-1)
        dummy.next = head

        start_ptr = head
        end_ptr = head
        k = n

        while k > 0 and end_ptr:
            end_ptr = end_ptr.next
            k = k-1

        if not end_ptr:  ##why is this condition
            return head

        while end_ptr and end_ptr.next:
            start_ptr = start_ptr.next
            end_ptr = end_ptr.next

        if start_ptr.next:
            start_ptr.next = start_ptr.next.next

        return dummy.next


l1 = ListNode(1)

s = Solution()
s.removeNthFromEnd(l1, 1)

"""
Test Cases #1
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
s.removeNthFromEnd(l1, 2)
Test Cases #2
l1 = ListNode(1)
s = removeNthFromEnd(l1 1)
"""