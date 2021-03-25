"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""
class ListNode():
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution():
    def move(self, l, diff):
        temp = l
        for i in range(diff):
            temp = temp.next
        return temp

    def calculate(self, l):
        cnt = 0
        while l:
            l = l.next
            cnt = cnt + 1
        return cnt

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # if not headA and not headB return None
        if not headA or not headB:
            return None

        m1 = self.calculate(headA)
        m2 = self.calculate(headB)

        diff = abs(m1-m2)

        if m1>m2:
            headA = self.move(headA, diff)
        else:
            headB = self.move(headB, diff)

        while True:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next







l1 = ListNode(0)
l1.next = ListNode(9)
l1.next.next = ListNode(1)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(4)

l2 = ListNode(3)
l2.next = ListNode(2)
l2.next.next = ListNode(4)


s = Solution()
s.getIntersectionNode(l1, l2)