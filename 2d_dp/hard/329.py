"""
Hard
329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1
 

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1


"""

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        memo = {}
        visiting = set()
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = 1
            visiting.add((i, j))
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if ni >= 0 and ni < len(matrix) and nj >= 0 and nj < len(matrix[0]):
                    if matrix[ni][nj] > matrix[i][j] and (ni, nj) not in visiting:
                        memo[(i, j)] = max(memo[(i, j)], 1 + dfs(ni, nj))
                    
            visiting.remove((i, j))
            return memo[(i, j)]

        
        res = float('-inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j))

        return res

if __name__ == "__main__":

  tests = [
    [[9,9,4],[6,6,8],[2,1,1]],
    [[3,4,5],[3,2,6],[2,2,1]],
    [[1]]
  ]

  for test in tests:
    print(Solution().longestIncreasingPath(test))

