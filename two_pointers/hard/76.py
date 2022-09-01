"""
Hard

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the 
window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


"""

class Solution:

    #O(mn)
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ''
        
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        
        a = [i for i, c in enumerate(s) if c in count]

        i, j = 0, 0
        l, r = 0, len(s) - 1
        res = ''
        while j < len(a) or j-i >= len(t): 
            
            if all(v <= 0 for v in count.values()):                
                if a[j-1]-a[i] <= r-l:
                    l, r = a[i], a[j-1]
                    res = s[l:r+1]
            
                count[s[a[i]]] += 1
                i += 1
            else:
                if j < len(a):
                    count[s[a[j]]] -= 1
                    j += 1
                else:
                    count[s[a[i]]] += 1
                    i += 1
            
        return res
    
    #O(m+n)
    def minWindowAlternate(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
            


if __name__ == "__main__":
    tests = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
        ("aaaaaaaaaaaabbbbbcdd", "abcdd")        
    ]

    for test in tests:
        print(Solution().minWindow(test[0], test[1]))