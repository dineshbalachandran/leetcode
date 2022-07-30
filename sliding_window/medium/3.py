"""
Medium

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxlength = 0
        store = {}
        
        for i in range(len(s)):
            if s[i] in store:
                newstart = store[s[i]] + 1
                for j in range(start, newstart):
                    store.pop(s[j])
                start = newstart
            
            store[s[i]] = i            
            maxlength = max(maxlength, i - start + 1)
        
        return maxlength

    def compactlengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

if __name__ == "__main__":
    tests = [
        "abcabcbb",
        "bbbbb",
        "pwwkew"
    ]

    for test in tests:
        print(Solution().lengthOfLongestSubstring(test))