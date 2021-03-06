"""
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # RECURSIVE SOLUTION
        # if not t1 or t2 (iterate all nodes)
        if t1 or t2:
            # add sum of nodes or t1 or t2
            root = t1 or t2 if not (t1 and t2) else TreeNode(t1.val + t2.val)
            # iterate recursively
            root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
            root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
            return root
        return None


l1 = TreeNode(1)
l1.right = TreeNode(2)
l1.left = TreeNode(3)
l1.left.left = TreeNode(5)

l2 = TreeNode(2)
l2.left = TreeNode(1)
l2.left.right = TreeNode(4)
l2.right = TreeNode(3)
l2.right.right = TreeNode(3)

s = Solution()
print(s.mergeTrees(l1,l2))