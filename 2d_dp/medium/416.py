"""
Medium
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into 
two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        s //= 2
        dp = [[False]*(s+1) for _ in range(len(nums)+1)]
        
        for i in range(len(dp)):
            dp[i][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(1, s+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        #print(dp)
        return dp[-1][-1]

    def canPartitionAlternate(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False

if __name__ == "__main__":
  tests = [
    [1,5,11,5],
    [1,2,3,5]
  ]

  for test in tests:
    print(Solution().canPartition(test))