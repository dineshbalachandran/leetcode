"""
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four 
edges of the grid are all surrounded by water.

 

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

import collections


class Solution:
    def numIslands(self, grid) -> int:
        
        if len(grid) == 0:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        visited = set()
        count = 0
        
        def bfs(row, col):
            
            q = collections.deque()
            visited.add((row, col))
            q.append((row, col))
            
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
            while q:
                r, c = q.popleft() 
                
                for dr, dc in directions:
                    rw = r + dr
                    cl = c + dc
                    if (rw in range(rows) and
                        cl in range(cols) and
                        grid[rw][cl] == '1' and
                        (rw, cl) not in visited):
                            q.append((rw, cl))
                            visited.add((rw, cl))
                
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
                    
        return count

if __name__ == "__main__":

    tests = [
        [["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]],
        [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]
    ]

    for test in tests:
        print(Solution().numIslands(test))
