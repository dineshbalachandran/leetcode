"""
Medium
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is 
sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals 
(merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def findInterval(val, start, end):
            
            l, r = start, end
            
            while l <= r:
                m = l + (r-l) // 2
                
                if val >= intervals[m][0] and val <= intervals[m][1]:
                    return [m, m]
                elif val < intervals[m][0]:
                    r = m-1
                elif val > intervals[m][1]:
                    l = m+1
            
            return [r, l]
        
        left = findInterval(newInterval[0], 0, len(intervals)-1)
        right = findInterval(newInterval[1], left[1], len(intervals)-1)
        
        
        l = min(intervals[left[1]][0], newInterval[0]) if left[1] >= 0 and left[1] < len(intervals) else newInterval[0]
        r = max(intervals[right[0]][1], newInterval[1]) if right[0] >= 0 and right[0] < len(intervals) else newInterval[1]
        
        del intervals[left[1]:right[0]+1]
        intervals.insert(left[1], [l,r])
        
        return intervals

    def insertalternate(
            self, intervals: List[List[int]], newInterval: List[int]
        ) -> List[List[int]]:
            res = []

            for i in range(len(intervals)):
                if newInterval[1] < intervals[i][0]:
                    res.append(newInterval)
                    return res + intervals[i:]
                elif newInterval[0] > intervals[i][1]:
                    res.append(intervals[i])
                else:
                    newInterval = [
                        min(newInterval[0], intervals[i][0]),
                        max(newInterval[1], intervals[i][1]),
                    ]
            res.append(newInterval)
            return res

if __name__ == "__main__":
    tests = [
        ([[1,3],[6,9]], [2,5]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
    ]

    for test in tests:
        print(Solution().insert(test[0], test[1]))