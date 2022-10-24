"""
Easy

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:

        #method 1: dp
        # ans = [0] * (n+1)
        
        # start, end = 1, 2        
        # while True:            
        #     diff = (end-start)//2
            
        #     mid = min(start+diff, n+1)            
        #     for i in range(start, mid):
        #         ans[i] = ans[i-diff]
            
        #     end = min(end, n+1)
        #     for i in range(mid, end):
        #         ans[i] = ans[i-diff] + 1
            
            
        #     if end > n:
        #         break
            
        #     start *= 2
        #     end = 2*start
        
        #method 2: bit manipulation
        # ans = []
        # for i in range(n+1):
        #     n = i
        #     ans.append(0)
        #     while n > 0:
        #         n &= (n-1)
        #         ans[-1] += 1 
        
        #method 3: dp more compact
        ans = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            ans[i] = 1 + ans[i - offset]
        
        return ans

if __name__ == "__main__":
  tests = [
    2,
    5    
  ]

  for test in tests:
    print(Solution().countBits(test))
                