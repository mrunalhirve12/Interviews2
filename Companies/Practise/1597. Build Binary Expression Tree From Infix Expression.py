"""
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with 2 children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression that it represents is (A o B), where A is the expression the left subtree represents and B is the expression the right subtree represents.

You are given a string s, an infix expression containing operands, the operators described above, and parentheses '(' and ')'.

Return any valid binary expression tree, which its in-order traversal reproduces s after omitting the parenthesis from it (see examples below).

Please note that order of operations applies in s. That is, expressions in parentheses are evaluated first, and multiplication and division happen before addition and subtraction.

Operands must also appear in the same order in both s and the in-order traversal of the tree.



Example 1:


Input: s = "3*4-2*5"
Output: [-,*,*,3,4,2,5]
Explanation: The tree above is the only valid tree whose inorder traversal produces s.
Example 2:


Input: s = "2-3/(5*2)+1"
Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
Explanation: The inorder traversal of the tree above is 2-3/5*2+1 which is the same as s without the parenthesis. The tree also produces the correct result and its operands are in the same order as they appear in s.
The tree below is also a valid binary expression tree with the same inorder traversal as s, but it not a valid answer because it does not evaluate to the same value.

The third tree below is also not valid. Although it produces the same result and is equivalent to the above trees, its inorder traversal does not produce s and its operands are not in the same order as s.

Example 3:

Input: s = "1+2+3+4+5"
Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]
Explanation: The tree [+,+,5,+,+,null,null,1,2,3,4] is also one of many other valid trees.


Constraints:

1 <= s.length <= 1000
s consists of digits and the characters '+', '-', '*', and '/'.
Operands in s are exactly 1 digit.
It is guaranteed that s is a valid expression.

"""

"""
Idea

We do 3 passes following the order of operations. :

Pass 1, ( and ): We iterate through s, convert each character to its corresponding node, and evaluate the expression inside parentheses using recursion.
Pass 2, * and /: We iterate through arr (array of nodes created in the previous pass) and convert all * and / sub-parts into trees.
Pass 3, + and -: We iterate through arr (array of nodes created in the previous pass) and convert the whole arr into a tree.
Credit to votrubac.


Complexity

Time complexity: O(N)
Space complexity: O(N)


"""
class Node(object):
     def __init__(self, val=" ", left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def expTree(self, s):
        return self.exp_tree_recu(s, 0, len(s) - 1)

    def exp_tree_recu(self, s, l, r):
        # convert s to arr of Nodes
        i, arr = l, []
        while i <= r:
            if s[i] == '(':
                j = i + 1
                bal = 1
                while bal > 0:
                    if s[j] == ')':
                        bal -= 1
                    elif s[j] == '(':
                        bal += 1
                    j += 1
                arr.append(self.exp_tree_recu(s, i + 1, j - 2))
                i = j
            else:
                arr.append(Node(s[i]))
                i += 1

        # evaluate arr only using ops (+- or */)
        def evaluate(ops):
            i, ans = 0, []
            while i < len(arr):
                node = arr[i]
                if not node.left and node.val in ops:
                    node.left = ans.pop()
                    node.right = arr[i + 1]
                    i += 1
                ans.append(node)
                i += 1
            return ans

        arr = evaluate('*/')
        return evaluate('+-')[0]

s = Solution()
s.expTree("1+2+3+4+5")