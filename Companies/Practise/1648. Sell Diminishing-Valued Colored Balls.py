"""
You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 109 + 7.



Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
Example 3:

Input: inventory = [2,8,4,10,6], orders = 20
Output: 110
Example 4:

Input: inventory = [1000000000], orders = 1000000000
Output: 21
Explanation: Sell the 1st color 1000000000 times for a total value of 500000000500000000. 500000000500000000 modulo 109 + 7 = 21.


Constraints:

1 <= inventory.length <= 105
1 <= inventory[i] <= 109
1 <= orders <= min(sum(inventory[i]), 109)
"""
import collections

class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        counter = collections.Counter(inventory)
        # k: the number of balls, v: the count of such kinds of ball with number k
        # sort so that biggest k is at the tail of the list
        cntList = sorted(list(counter.items()))
        # to prevent list from becoming empty
        cntList = [(0, 0)] + cntList
        res = 0

        while orders:
            # k1, k2 is the top 2 biggest number of balls, v1, v2 is their count
            k1, v1 = cntList.pop()
            k2, v2 = cntList.pop()

            # use the formula of sum of arithmetic sequences
            if (k1 - k2) * v1 <= orders:
                # if there are enough balls when all k1 balls can be transformed to k2 balls
                # there will be (k1-k2)*v1 balls calculated into result
                res += (k1 + k2 + 1) * (k1 - k2) // 2 * v1
                orders -= (k1 - k2) * v1

                v2 += v1
                cntList.append((k2, v2))
            else:
                # if there are not enough balls
                # there will be orders balls calculated into result
                num = orders // v1
                res += (k1 - num + 1 + k1) * num // 2 * v1 + (k1 - num) * (orders % v1)
                orders = 0

        return res % (10 ** 9 + 7)

s = Solution()
s.maxProfit([2,5], 4)