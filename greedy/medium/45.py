"""
Medium

45. Jump Game II


You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

1 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000

"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        #dp O(n2)
        dp = [float("inf")] * len(nums)
        dp[-1] = 0
        
        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, min(len(nums), i+nums[i]+1)):
                
                dp[i] = min(dp[i], 1+dp[j]) 
        
        return dp[0]
        
        
        #greedy O(n)
        # l, r = 0, 0
        # res = 0
        # while r < (len(nums) - 1):
        #     maxJump = 0
        #     for i in range(l, r + 1):
        #         maxJump = max(maxJump, i + nums[i])
        #     l = r + 1
        #     r = maxJump
        #     res += 1
        # return res

if __name__ == "__main__":
    tests = [
        [2,3,1,1,4],
        [2,3,0,1,4]
    ]

    for test in tests:
        print(Solution().jump(test))