"""
Medium

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and 
then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the 
expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

"""

class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
      
        memo = {}
        
        def dfs(i, t):
            
            if i == len(nums):
                if t == target:
                    return 1
                else:
                    return 0
            
            if (i, t) in memo:
                return memo[(i,t)]
            
            memo[(i,t)] = dfs(i+1, t - nums[i]) + dfs (i+1, t + nums[i])
            
            return memo[(i, t)]
        
        return dfs(0, 0)

if __name__ == "__main__":
    tests = [
        ([1,1,1,1,1], 3),
        ([1], 1)
    ]

    for test in tests:
        print(Solution().findTargetSumWays(test[0], test[1]))

