"""
Medium

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            j = 0
            while (i-j) >= 0 and (i+j) < len(s):
                if s[i-j] == s[i+j]:                    
                    if 2*j >= len(res):
                        res = s[i-j:i+j+1]
                    j += 1
                else:                    
                    break
            
        
        for i in range(len(s)):
            j = 0
            while (i-j) >= 0 and (i+j+1) < len(s):
                if s[i-j] == s[i+j+1]:
                    if 2*j+1 >= len(res):                
                        res = s[i-j:i+j+2]
                    j += 1                    
                else:
                    break             
        
        return res

if __name__ == "__main__":
    tests = [
        "babad",
        "cbbd"
    ]

    for test in tests:
        print(Solution().longestPalindrome(test))