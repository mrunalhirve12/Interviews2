#To do
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def solver(self,root,k):
        # -------------- Internal Solver --------------
        #     Space Complexity: O(1)
        #     Time  Complexity: O( L + k )
        #
        # 1) Calculate Linked-List Length
        def getL(n):
            L = 0
            while n:
                L += 1
                n = n.next
            return L
        L = getL(root)
        #
        # 2) Generate K-snippets:
        n  = root
        for i in range(k):
            head = n
            T    = int( math.ceil( L/float(k-i) ) )
            for _ in range(T-1):
                if not n:
                    break
                n = n.next
                L -= 1
            if n:
                n.next, n = None, n.next
                L        -= 1
            yield head
    def splitListToParts(self, root, k): # -> List[ListNode]:
        return [n for n in self.solver(root,k)]


