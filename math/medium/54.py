"""
Medium

54. Rotate matrix spiral

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix):
        
        m = len(matrix)
        n = len(matrix[0])
        t, b = 0, m-1
        l, r = 0, n-1
        
        res = []
        
        while t <= b and l <= r:
            
            for j in range(l, r+1):
                res.append(matrix[t][j])
            
            for i in range(t+1, b+1):
                res.append(matrix[i][r])
          
            if len(res) == m*n:
                break
            
            for j in range(r-1, l-1, -1):
                res.append(matrix[b][j])
                      
            for i in range(b-1, t, -1):
                res.append(matrix[i][l])

            t += 1
            b -= 1
            l += 1
            r -= 1
            
        return res

if __name__ == "__main__":

  tests = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  ]

  for test in tests:
    print(Solution().spiralOrder(test))