"""
130. Surrounded Regions

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.

"""

from typing import List

class Solution:
  def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    m, n = len(board), len(board[0])
    visited, visiting = set(), set()

    def isFlippable(i, j):

      visiting.add((i, j))

      neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
      
      for r, c in neighbours:
        if (r, c) in visiting:
          continue

        if r < 0 or r >= m or c < 0 or c >= n:
          continue
        
        if board[r][c] == 'O' and ((r, c) in visited or not isFlippable(r, c)):          
          return False
      
      return True

    for i in range(m):
      for j in range(n):
        if i in [0, m-1] or j in [0, n-1] and board[i][j] == 'O':
          visited.add((i, j))

    for i in range(m):
      for j in range(n):
        
        if board[i][j] == 'O' and (i, j) not in visited:              
          flip = isFlippable(i, j)
          for r, c in visiting:
            if flip:
              board[r][c] = 'X'
            visited.add((r, c))              
          
          visiting.clear()

    return

  def solveAlternate(self, board: List[List[str]]) -> None:
    ROWS, COLS = len(board), len(board[0])

    def capture(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
            return
        board[r][c] = "T"
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)

    # 1. (DFS) Capture unsurrounded regions (O -> T)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                capture(r, c)

    # 2. Capture surrounded regions (O -> X)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"

    # 3. Uncapture unsurrounded regions (T -> O)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "T":
                board[r][c] = "O"

if __name__ == "__main__":

  tests = [
    [["X","X","X","X"],
     ["X","O","O","X"],
     ["X","X","O","X"],
     ["X","O","X","X"]],
    
    [["X"]]
  ]

  for test in tests:
    Solution().solve(test)
    print(test)