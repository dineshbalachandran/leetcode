"""
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        counts = dict()
        for c in s:
            counts[c] = counts.setdefault(c, 0) + 1
        for c in t:
            if c in counts:                
                counts[c] -= 1
                if counts[c] == 0:
                    counts.pop(c)                
            else:
                return False
        
        return True

    def compactIsAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True

    def morecompactIsAnagram(self, s: str, t: str) -> bool:
        countS = [0] * 26
        countT = [0] * 26

        for c in s:
            countS[ord(c) - ord('a')] += 1
        for c in t:
            countT[ord(c) - ord('a')] += 1
        
        return True if tuple(countS) == tuple(countT) else False
            
if __name__ == "__main__":

    tests = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("ab", "a")
    ]

    for test in tests:
        s, t = test
        print(Solution().morecompactIsAnagram(s, t))