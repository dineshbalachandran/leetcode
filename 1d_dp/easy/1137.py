"""
Easy
1137. N-th Tribonacci number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:
Input: n = 4
Output: 4

Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537

"""

class Solution:
    def tribonacci(self, n: int) -> int:

        t0, t1, t2 = 0, 1, 1

        if n == 0:
            return t0
        elif n == 1:
            return t1
        elif n == 2:
            return t2
        else:
            for i in range(3, n+1):
                t2, t1, t0 = t2+t1+t0, t2, t1
        
        return t2

if __name__ == "__main__":
  tests = [
    4,
    25
  ]

  for test in tests:
    print(Solution().tribonacci(test))