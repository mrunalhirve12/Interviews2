"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.


Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""

#ToDO

from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        cons = defaultdict(set)
        for a, b in connections:
            cons[a].add(b)
            cons[b].add(a)

        low = {}
        results = []

        def visit(node, from_node=None):
            if node in low:
                return low[node]
            cur_id = low[node] = len(low)

            for neigh in cons[node]:
                if neigh == from_node:
                    continue
                low[node] = min(low[node], visit(neigh, node))

            if cur_id == low[node] and from_node is not None:
                results.append([from_node, node])
            return low[node]

        visit(0)
        return results

s = Solution()
s.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])