"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.



Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1

"""
from typing import List

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return -1
        # instead of creating 2d array 'visited', we use the grid itself to represent visited status
        d = 1
        curr_level = [(0, 0)]
        grid[0][0] = 1
        while curr_level:
            next_level = []
            for i, j in curr_level:
                for di, dj in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    i1, j1 = i + di, j + dj
                    if 0 <= i1 < m and 0 <= j1 < n and grid[i1][j1] == 0:
                        if i1 == m - 1 and j1 == n - 1:
                            return d + 1
                        next_level.append((i1, j1))
                        grid[i1][j1] = 1
            curr_level = next_level
            d += 1
        return -1

"""
#ACCEPTED
q = collections.deque([(0,0,1)] if grid[0][0] == 0 else [])
        vis = set([(0,0)])
        while(q):
            i,j,d = q.popleft()
            if i == len(grid) -1 and j == len(grid[0]) - 1: return d
            for nei in [(i+1,j),(i+1,j+1),(i+1,j-1), (i,j+1),(i,j-1), (i-1,j+1),(i-1,j),(i-1,j-1)]:
                if 0 <= nei[0] < len(grid) and 0 <= nei[1] < len(grid[0]) and grid[nei[0]][nei[1]] == 0 and nei not in vis:
                    vis.add(nei)
                    q.append((nei[0],nei[1],d+1))
        return -1
"""

s = Solution()
s.shortestPathBinaryMatrix([[0,1],[1,0]])