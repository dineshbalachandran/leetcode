"""
Medium
Given an array of strings strs, group the anagrams together. You can return the answer in 
any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

from collections import defaultdict
import collections

class Solution:
    def groupAnagrams(self, strs):
        
        def isAnagram(counts, t):
            
            tcounts = counts.copy()

            for c in t:
                if c in tcounts:                
                    tcounts[c] -= 1
                    if tcounts[c] == 0:
                        tcounts.pop(c)                
                else:
                    return False

            return True
        
        def generatedict(s):
            
            counts = defaultdict(int)            
            for c in s:
                counts[c] += 1
            
            return counts 
        
        groups = defaultdict(dict)
        
        for string in strs:
            anagrams = groups[len(string)]            
            
            found = False
            for anagram in anagrams:
                anagramlist, counts = anagrams[anagram]
                if isAnagram(counts, string):
                    anagramlist.append(string)
                    found = True
                    break
            if not found:
                anagrams[len(anagrams)+1] = ([string], generatedict(string))

        res = []
        for length in groups:
            anagrams = groups[length]
            for anagram in anagrams:
                res.append(anagrams[anagram][0])
        
        return res

    def alternateGroupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

if __name__ == "__main__":

    tests = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],
        ["", "b"]
    ]

    for test in tests:
        print(Solution().groupAnagrams(test))