"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""
import collections

"""
It is easy to observe that the minimum number of conference rooms needed is equal to the size of the maximum set of pairwise overlapping intervals. This can be calculated as follows: We first sort the intervals in ascending start time to obtain intervals_sorted. Then we iterate over intervals_sorted, and for each intervals_sorted[i], we calculate the number of intervals intervals_sorted[j] (j < i) that has nontrivial overlap with intervals_sorted[i]. Denote the number by N_i. The minimum number of conference rooms needed is then given by the maximum of (N_i+1) over i.

To calculate N_i for each i, we first initialize a queue end_points of end time of each interval sorted in ascending order. We also use a counter pop_count to record the number of elements that has been dequeued from end_points. Then for each intervals_sorted[i], we dequeue from end_points, and update pop_count, until end_points[0] > intervals_sorted[i].start. It is easy to see that pop_count is precisely the number of intervals intervals_sorted[j] that has intervals_sorted[j].end <= intervals_sorted[i].start, which is the number of intervals intervals_sorted[j] (j < i) that has trivial overlap with intervals_sorted[i]. Therefore, the number N_i is given by i-pop_count.

Time complexity: O(n log n), space complexity: O(n).
"""

"""
class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x: x.start)
        heap = []
        heapq.heapify(heap)
        res = 1
        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
            else:
                if heap[0] <= interval.start:
                    heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
            res = max(res, len(heap))
        return res
"""

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if intervals ==[]:
            return 0
        intervals.sort()
        totalend=[0]
        for start,end in intervals:
            minend=min(totalend)
            if start<minend:
                totalend.append(end)
                #print(totalend)
            else:
                index=totalend.index(minend)
                totalend[index]=end
        #print(totalend)
        return len(totalend)

s = Solution()
s.minMeetingRooms([[0,30],[5,10],[15,20]])