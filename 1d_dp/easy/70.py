"""
Medium
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Input: n = 8
Output: 34
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        n1, n2 = 2, 1
        
        for i in range(3, n):
            n2, n1 = n1, n1+n2
        
        return n1+n2

if __name__ == "__main__":
    tests = [
        2,
        3,
        8
    ]

    for test in tests:
        print(Solution().climbStairs(test))
        # flatMap Monad[List] range(3, n) tests
        # flatMap