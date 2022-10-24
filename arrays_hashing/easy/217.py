"""
Easy

217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct

Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution:
    def containsDuplicate(self, nums) -> bool:
        bag = set()
        for num in nums:
            if num in bag:
                return True
            bag.add(num)
        
        return False

if __name__ == "__main__":

    tests = [
        [1,2,3,1],
        [1,2,3,4],
        [1,1,1,3,3,4,3,2,4,2]
    ]

    for test in tests:
        print(Solution().containsDuplicate(test))



