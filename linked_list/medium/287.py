"""
Medium

287. Find the duplicate number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

The INSIGHT to this question is to recognise that this is similar to the linked list cycle detection problem. The presence of duplicates in the list, results in a cycle if 
the list values are treated as pointers to the list index.

"""

class Solution:
    def findDuplicate(self, nums) -> int:
        
        fast, slow = 0, 0
        
        #detect the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        #find the start of the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

if __name__ == "__main__":
    tests = [
        [1,3,4,2,2],
        [3,1,3,4,2]
    ]

    for test in tests:
        print(Solution().findDuplicate(test))