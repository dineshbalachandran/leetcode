"""
Medium

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.


(KADANE's algorithm)

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""

class Solution:
    def maxSubArray(self, nums) -> int:
        
        curSum = 0
        maxSum = nums[0]
        
        for n in nums:
            curSum = max(curSum + n, n)
            maxSum = max(curSum, maxSum)
        
        return maxSum

if __name__ == "__main__":
    tests = [
        [-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [5,4,-1,7,8]
    ]

    for test in tests:
        print(Solution().maxSubArray(test))
        