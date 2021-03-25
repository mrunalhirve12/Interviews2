"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
class Solution(object):


    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # ITERATIVE SOLUTION
        if len(grid) == 0:
            return 0
        # count to store clusters
        count = 0
        # a set to maintain visited
        visit = set()
        # calculate height and width of the grid
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1' and (i, j) not in visit:
                    count += 1
                    stack = [(i, j)]
                    while stack:
                        u = stack.pop()
                        visit.add(u)
                        h, w = u[0], u[1]
                        # if h > 0 check row above having val as 1 and not visited
                        if h > 0 and grid[h - 1][w] == '1' and (h - 1, w) not in visit:
                            stack.append((h - 1, w))
                        # if i < ht (all cases) check below above having val as 1 and not visited
                        if h < height - 1 and grid[h + 1][w] == '1' and (h + 1, w) not in visit:
                            stack.append((h + 1, w))
                        # if j > 0 check  previous col in same row having val as 1 and not visited
                        if w > 0 and grid[h][w - 1] == '1' and (h, w - 1) not in visit:
                            stack.append((h, w-1))
                        # if j < width check  previous col in same row having val as 1 and not visited
                        if w < width - 1 and grid[h][w + 1] == '1' and (h, w + 1) not in visit:
                            stack.append((h, w + 1))
        return count

s = Solution()
s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])