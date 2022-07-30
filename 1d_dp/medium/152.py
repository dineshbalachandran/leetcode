"""
Medium

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
class Solution:
    def maxProduct(self, nums) -> int:
        
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n) 
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
            
        return res

if __name__ == "__main__":
    tests = [
        [2,3,-2,4],
        [-2,0,-1]
    ]

    for test in tests:
        print(Solution().maxProduct(test))    