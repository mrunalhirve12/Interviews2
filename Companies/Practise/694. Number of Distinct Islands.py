"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""


class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        allr = len(grid)
        allc = len(grid[0])

        def dfs(r, c, direction):
            if r < 0 or r >= allr or c < 0 or c >= allc or grid[r][c] == 'Visited' or grid[r][c] == 0:
                return direction
            grid[r][c] = 'Visited'
            up = dfs(r - 1, c, 'up')
            down = dfs(r + 1, c, 'down')
            right = dfs(r, c + 1, 'right')
            left = dfs(r, c - 1, 'left')
            return direction + up + down + right + left

        freq = set()
        ans = 0
        for row in range(allr):
            for column in range(allc):
                if grid[row][column] == 1:
                    res = dfs(row, column, '')
                    if res not in freq:
                        freq.add(res)
                        ans += 1
        return ans
s = Solution()
s.numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
