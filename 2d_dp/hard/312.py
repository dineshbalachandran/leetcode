"""
Hard

312. Balloon Burst

THE PATTERN IS SIMILAR TO THE MATRIX CHAIN MULTIPLICATION PROBLEM and the SOLUTION is exactly the same

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an 
array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out 
of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100

"""

from functools import cache


class Solution:
  def maxCoins(self, dims):

    self.dims = [1] + dims + [1]
    

    @cache
    def a(i, j):

      return max((a(i,k) + self.dims[i]*self.dims[k]*self.dims[j] + a(k, j) for k in range(i+1, j)), default=0)

       
    return a(0, len(self.dims)-1)


if __name__ == "__main__":
  tests = [
    [3, 1, 5, 8],
    [1,5]
  ]

for test in tests:
  print(Solution().maxCoins(test))