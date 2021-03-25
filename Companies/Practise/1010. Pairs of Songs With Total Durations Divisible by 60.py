"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
"""
import collections
from typing import List

"""
Hint:

This one is similar to classical two-sum problem. where math objective function is x + y = target

The difference is that what we want this time is (x + y) % 60 = target = 0
"""
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # i % 60 = (60 - j%60)%60

        c = [0] * 60  # array for the remainder
        res = 0

        for j in time:
            # res += c[(60 - j%60)%60]
            res += c[-j % 60]
            c[j % 60] += 1

        return res

s = Solution()
s.numPairsDivisibleBy60([30,20,150,100,40])