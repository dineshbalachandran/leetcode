"""
Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

"""

import random

class Solution:
    def findKthLargest(self, nums, k: int) -> int:     
        
        def quickSelect(start, end):
            
            def partition(start, end):

              p = random.randint(start, end)            
              nums[p], nums[end] = nums[end], nums[p]

              p = start
              for i in range(start, end):
                  if nums[i] > nums[end]:
                      nums[p], nums[i] = nums[i], nums[p]
                      p += 1
              nums[end], nums[p] = nums[p], nums[end]

              return p

            p = partition(start, end)
            if p < k-1:
                return quickSelect(p+1, end)
            elif p > k-1:
                return quickSelect(start, p-1)
            else:
                return nums[p]
        
        res = quickSelect(0, len(nums)-1)
        print(nums)
        return res

if __name__ == "__main__":
    tests = [
        ([3,2,1,5,6,4], 2),
        ([3,2,3,1,2,4,5,5,6], 4)
    ]

    for test in tests:
        print(Solution().findKthLargest(test[0], test[1]))