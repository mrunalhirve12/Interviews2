"""
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.



Example 1:



Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:



Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9


Constraints:

2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
It is guaranteed that all elements in horizontalCuts are distinct.
It is guaranteed that all elements in verticalCuts are distinct.
"""


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: [int], verticalCuts: [int]) -> int:
        # appending the borders 0 and final horizontal line h height
        # appending horizontal cuts in sequence order
        hCuts = [0] + sorted(horizontalCuts) + [h]

        # appending the borders 0 and final vertical line w width
        # appending horizontal cuts in sequence order
        vCuts = [0] + sorted(verticalCuts) + [w]

        # print(hCuts,vCuts)

        # find the distance between each cut and its previous cut both horizontally and vertically

        for i in range(0, len(hCuts) - 1):
            hCuts[i] = hCuts[i + 1] - hCuts[i]
        for i in range(0, len(vCuts) - 1):
            vCuts[i] = vCuts[i + 1] - vCuts[i]

        # eliminate the last borders
        hCuts = hCuts[:-1]
        vCuts = vCuts[:-1]

        # Area between the max horizontal cut and max vertical cut is the one of maximum area
        # return after taking module 10^9+7
        return (max(hCuts) * max(vCuts)) % (10 ** 9 + 7)

s = Solution()
s.maxArea(5, 4, [1,2,4], [1,3])