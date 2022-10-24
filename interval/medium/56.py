"""
Medium

56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        out = [intervals[0]]
        
        for start, end in intervals[1:]:            
            
            lastEnd = out[-1][1]
            
            if (start <= lastEnd):                
                out[-1][1] = max(lastEnd, end)
            else:
                out.append([start, end])
        
        
        return out

if __name__ == "__main__":
  tests = [
    [[1,3],[2,6],[8,10],[15,18]],
    [[1,4],[4,5]]
  ]

  for test in tests:
    print(Solution().merge(test))