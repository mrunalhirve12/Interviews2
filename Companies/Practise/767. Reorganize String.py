"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500]
"""

"""
To solve this problem, we can first count up the frequencies of each character in S, storing them in a dictionary. We then add all of the keys to a priority queue, where the priority is -frequency (as python uses a min-heap rather than a max-heap for their priority queue implementation).

Now, we want to ensure that two adjacent characters do not match, and we also want to use the highest frequency characters first, so we don't run out of room at the end. Simply popping from the priority queue would put all same characters next to eachother such as

aaabbc
What we want is to alternate between the two highest priority characters in the heap. A clever way to do this is to pop off the highest priority character, and not re-adding it to the priority queue until the second highest priority character has also been popped. This turns the above example into

ababac
Thus, we have:
"""
import heapq


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""

        # Get frequency of each letter
        freq = {}
        for c in S:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        # Add to heap (python is min heap)
        heap = []
        for c in freq:
            heapq.heappush(heap, (-freq[c], c))

        # Pop first element off, adding it to res
        res = ""
        prev = heapq.heappop(heap)
        res += prev[1]

        # To avoid chars being next to eachother, pop from heap,
        # and don't readd that char to the heap until the next iteration
        while heap:
            curr = heapq.heappop(heap)
            res += curr[1]
            # Readd prev if it still has frequency left
            if prev[0] < -1:
                heapq.heappush(heap, (prev[0] + 1, prev[1]))
            prev = curr

        if len(res) != len(S):
            return ""
        return res

s = Solution()
s.reorganizeString("aab")