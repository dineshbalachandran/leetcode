"""
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""



class Solution:
    def longestConsecutive(self, nums) -> int:
       
        lcs = {}        
        for num in nums:
            if num in lcs:
                continue
            lcs[num] = None
            if num+1 in lcs:
                lcs[num] = num+1
            if num-1 in lcs:
                lcs[num-1] = num
                
        visited = set()
        def visit(num):
            if num in visited:
                return lcs[num]
            
            if lcs[num] == None:                
                lcs[num] = 1
            else:    
                lcs[num] = 1 + visit(lcs[num])
            
            visited.add(num)
            return lcs[num]
        
        maxlcslength = 0
        for num in lcs:
            length = visit(num)        
            maxlcslength = max(maxlcslength, length)
            
        return maxlcslength

    def compactLongestConsecutive(self, nums) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

if __name__ == "__main__":

    tests = [
        [100,4,200,1,3,2],
        [0,3,7,2,5,8,4,6,0,1]
    ]

    for test in tests:
        print(Solution().longestConsecutive(test))