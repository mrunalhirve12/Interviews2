"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.



Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1


Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""
from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def constructGraph(self, edges):
        for edge in edges:
            start, end = edge
            self.graph[start].append(end)
            self.graph[end].append(start)

    def dfs(self, node, visited):
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                self.dfs(neighbor, visited)

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if not edges:
            return n

        connectedComponents = 0
        self.constructGraph(edges)
        visited = [False] * n

        for node in range(n):
            if not visited[node]:
                connectedComponents += 1
                visited[node] = True
                self.dfs(node, visited)

        return connectedComponents

s = Solution()
s.dfs(5, [[0,1],[1,2],[3,4]])