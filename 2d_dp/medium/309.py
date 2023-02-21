"""
Medium

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell 
one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000

"""

from typing import List

# Dynamic programming solution with constant space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #dp = [[0]*3 for _ in range(len(prices))]
        #dp[0][1] = -prices[0]
        
        c, b, s = 0, -prices[0], 0 #cooldown, buy, sell initial values
        
        for i in range(1, len(prices)):
            
            c, b, s = max(c, s), max(c-prices[i], b), max(b+prices[i], s)
            
            # dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            # dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
            # dp[i][2] = max(prices[i]+dp[i-1][1], dp[i-1][2])
            
        #return dp[len(prices)-1][2]
        
        return s

if __name__ == "__main__":

  tests = [
    [1,2,3,0,2],
    [1]
  ]

  for test in tests:
    print(Solution().maxProfit(test))

