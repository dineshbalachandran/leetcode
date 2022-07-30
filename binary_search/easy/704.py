"""
Easy
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

class Solution:
    def search(self, nums, target) -> int:
        
        def find(left: int, right: int) -> int:
            
            if left > right:
                return -1
            
            mid = left + (right-left) // 2
            
            if target > nums[mid]:
                return find(mid+1, right)
            elif target < nums[mid]:
                return find(left, mid-1)
            else:
                return mid
        
        return find(0, len(nums)-1)

if __name__ == "__main__":
    tests = [
        ([-1,0,3,5,9,12], 9),
        ([-1,0,3,5,9,12], 2)
    ]

    for test in tests:
        nums, target = test
        print(Solution().search(nums, target))

