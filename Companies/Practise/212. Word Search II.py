"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

    def startswith(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]

        return node


class Solution:
    def __init__(self):
        self.trie = Trie()
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def build_trie(self, words):
        for word in words:
            self.trie.add(word)

    def find(self, m, n, board, res, node, i, j, visited):
        if node.word:
            res.append(node.word)
            # too avoid duplicate. we can use set insted as well.
            node.word = None

        if i < 0 or j < 0 or i >= m or j >= n:
            return

        if board[i][j] not in node.children:
            return

        visited.add((i, j))
        for di, dj in self.directions:
            ni, nj = i+di, j+dj

            if (ni, nj) in visited:
                continue

            self.find(m, n, board, res,
                      node.children[board[i][j]], ni, nj, visited)

        visited.remove((i, j))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.build_trie(words)
        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                self.find(m, n, board, res, self.trie.root, i, j, set())

        return res

s = Solution()
s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])