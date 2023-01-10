"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very 
left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window 
moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

      q = deque([])
      res = []
      l = 0

      # a decreasing monotonic queue
      for r in range(len(nums)):

        while q and nums[r] > q[-1]:
            q.pop()

        q.append(nums[r])

        if r-l+1 == k:
          res.append(q[0])
          if nums[l] == q[0]:
            q.popleft()
          l += 1
  
      return res

if __name__ == "__main__":

  tests = [
    ([1,3,-1,-3,5,3,6,7], 3),
    ([1], 1)
  ]

  for nums, k in tests:
    print(Solution().maxSlidingWindow(nums, k))