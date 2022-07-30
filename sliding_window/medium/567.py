"""
Medium
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false 
otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        source, target = [0]*26, [0]*26
        
        for i in range(len(s1)):
            target[ord(s1[i])-ord('a')] += 1
            source[ord(s2[i])-ord('a')] += 1
        
        tgt = tuple(target)
        
        if tuple(source) == tgt:
            return True
        
        for i in range(len(s1), len(s2)):
            source[ord(s2[i-len(s1)])-ord('a')] -= 1
            source[ord(s2[i])-ord('a')] += 1
            
            if tuple(source) == tgt:
                return True
        
        return False

if __name__ == "__main__":
    tests = [
        ("ab", "eidbaooo"),
        ("ab", "eidboaoo")
    ]

    for test in tests:
        s1, s2 = test
        print(Solution().checkInclusion(s1, s2))