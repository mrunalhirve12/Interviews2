"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return -1

        freshCount, rotten = self.getFreshCountAndRottenPosition(grid)
        if freshCount == 0:
            return 0

        timeUsed = 0
        row = len(grid)
        col = len(grid[0])

        while rotten:
            size = len(rotten)
            if freshCount == 0:
                return timeUsed
            timeUsed += 1
            for _ in range(size):
                x, y = rotten.pop()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in directions:
                    newX = x + dx
                    newY = y + dy
                    if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 1:
                        rotten.insert(0, (newX, newY))
                        grid[newX][newY] = 2
                        freshCount -= 1

        return -1

    def getFreshCountAndRottenPosition(self, grid):
        row = len(grid)
        col = len(grid[0])
        freshCount = 0
        rotten = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    rotten.append((i, j))
        return freshCount, rotten

s = Solution()
s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])