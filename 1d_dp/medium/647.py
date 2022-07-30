"""
Medium
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        for i in range(len(s)):
            j = 0
            while (i-j) >= 0 and (i+j) < len(s):
                if s[i-j] == s[i+j]:
                    j += 1
                else:                    
                    break
            count += j
        
        for i in range(len(s)):
            j = 0
            while (i-j) >= 0 and (i+j+1) < len(s):
                if s[i-j] == s[i+j+1]:
                    j += 1
                else:                    
                    break
            count += j
        
        return count

if __name__ == "__main__":
    tests = [
        "abc",
        "aaa"
    ]

    for test in tests:
        print(Solution().countSubstrings(test))