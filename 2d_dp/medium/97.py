"""
Medium

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
 
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}
        
        def dfs(i, j):            
            
            if (i == len(s1) and
                j == len(s2)):
                return True
            
            if (i, j) in memo:
                return memo[(i,j)]
            
            
            if i < len(s1) and j < len(s2) and s1[i] == s2[j] == s3[i+j]:
                memo[(i, j)] = dfs(i+1, j) or dfs(i, j+1)
            elif i < len(s1) and s1[i] == s3[i+j]:
                memo[(i, j)] = dfs(i+1, j)
            elif j < len(s2) and s2[j] == s3[i+j]:
                memo[(i, j)] = dfs(i, j+1)
            else:
                memo[(i, j)] = False
                
            
            return memo[(i,j)]
        
        return dfs(0, 0)

if __name__ == "__main__":
    tests = [
        ("aabcc", "dbbca", "aadbbcbcac"),
        ("aabcc", "dbbca", "aadbbbaccc"),
        ("", "", "")
    ]

    for test in tests:
        print(Solution().isInterleave(test[0], test[1], test[2]))