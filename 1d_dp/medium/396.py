"""
Medium

396. Rotate Function

You are given an integer array nums of length n.

Assume arrk to be an array obtained by rotating nums by k positions clock-wise. 
We define the rotation function F on nums as follow:

F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
Return the maximum value of F(0), F(1), ..., F(n-1).

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [4,3,2,6]
Output: 26
Explanation:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.

Example 2:
Input: nums = [100]
Output: 0
 
Example 3:
Input: nums = [4,3,2,6,9,-10]
Output: 85

Constraints:
n == nums.length
1 <= n <= 105
-100 <= nums[i] <= 100

"""

"""
The key insight is that taking the indexes to rotate in the anti-clockwise direction (equivalent to elements rotating
clockwise), each rotation increases the previous function value by the sum of all the elements whose current index is 
not zero. The element with current index zero reduces the previous sum by len(nums)-1*element value. Taking the two 
together the current function value = previous function value + sum of all non zero index values - len(nums)-1*value of
the element whose index is zero.

The sum of all elements whose current index is not zero can be pre-calculated by summing all values except itself and 
storing it in an array (cumsum).

"""

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        l, r = [0]*len(nums), [0]*len(nums)

        for i in range(1, len(nums)):
            l[i] = l[i-1] + nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            r[i] = r[i+1] + nums[i+1]
        
        cumsum = [l[i]+r[i] for i in range(len(nums))]

        #find the initial sum with the 0th index having the factor '0'
        X = 0
        for i in range(len(nums)):
            X += i*nums[i]
        
        S = X
        #find the remaining sums with the factor '0' starting with the last element 
        for k in range(len(nums)-1, 0, -1):
            X = X-(len(nums)-1)*nums[k]+cumsum[k]
            S = max(S, X)
        
        return S

if __name__ == "__main__":
  tests = [
    [4, 3, 2, 6],
    [100],
    [4, 3, 2, 6, 9, -10]
  ]

  for test in tests:
    print(Solution().maxRotateFunction(test))