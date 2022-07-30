"""
Medium
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
"""
class Solution:
    def exist(self, board, word):
        
        m, n = len(board), len(board[0])
        visited = set()
        
        def dfs(i, j, k):

            if board[i][j] == word[k]:
                
                if k == len(word)-1:
                    return True            
                
                visited.add((i, j))
                
                for r, c in [(i+1,j), (i,j+1), (i,j-1), (i-1,j)]:
                    
                    if (r >= 0 and r < m and
                        c >= 0 and c < n and
                        (r, c) not in visited and
                        dfs(r, c, k+1)):

                            return True

                visited.remove((i, j))
            
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False

if __name__ == "__main__":
    tests = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"),        
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"),
        ([["a", "b"],["c","d"]], "cdba"),
        ([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")        
        ]

    for test in tests:
        print(Solution().exist(test[0], test[1]))