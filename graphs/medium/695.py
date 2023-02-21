"""
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

"""

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

      visited = set()
      m = len(grid)
      n = len(grid[0])

      maxarea = 0

      def visitNeighbours(i, j):

        neighbours = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]

        area = 0
        for r, c in neighbours:
          if (r, c) in visited:
            continue

          if r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == 1:
            visited.add((r, c))
            area += (1 + visitNeighbours(r, c))
        
        return area

      for i in range(m):
        for j in range(n):
          if (i, j) not in visited and grid[i][j] == 1:
            visited.add((i,j))
            maxarea = max(maxarea, 1 + visitNeighbours(i, j))
      
      return maxarea

if __name__ == "__main__":

  tests = [
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]],
    
    [[0,0,0,0,0,0,0,0]]
  ]

  for test in tests:
    print(Solution().maxAreaOfIsland(test))