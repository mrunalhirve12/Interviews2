"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        def dfs(node, dist):
            if not node:
                return

            cur_dist = dist
            if node.val in path:
                cur_dist = path[node.val]

            if cur_dist == K:
                res.append(node.val)

            dfs(node.left, cur_dist + 1)
            dfs(node.right, cur_dist + 1)
            return

        def find_path(node, path):
            if not node:
                return -1

            if node.val == target.val:
                path[node.val] = 0
                return 0

            left = find_path(node.left, path)
            if left >= 0:
                path[node.val] = left + 1
                return left + 1

            right = find_path(node.right, path)
            if right >= 0:
                path[node.val] = right + 1
                return right + 1

            return -1

        res = []
        path = {}
        find_path(root, path)
        dfs(root, path[root.val])
        return res

s = Solution()
print(s.distanceK([3,5,1,6,2,0,8,None,None,7,4], 5, 2))
