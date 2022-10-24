"""
Medium

Given an array nums of n integers, return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

"""

class Solution:
    def fourSum(self, numbers, target: int):
        
        numbers.sort()
        res = []
        
        for i, a in enumerate(numbers):
            
            if i > 0 and a == numbers[i-1]:
                continue
            
            for j, b in enumerate(numbers[i+1:]):
                
                if j > 0 and b == numbers[i+j]:
                    continue
            
                l, r = i+j+2, len(numbers)-1

                while l < r:
                    fourSum = a + b + numbers[l] + numbers[r]

                    if fourSum > target:
                        r -= 1
                    elif fourSum < target:
                        l += 1
                    else:
                        res.append([a, b, numbers[l], numbers[r]])

                        l += 1
                        while numbers[l] == numbers[l-1] and l < r:
                            l += 1
        return res


if __name__ == "__main__":
    tests = [
        ([1,0,-1,0,-2,2], 0),
        ([2,2,2,2,2], 8)
    ]

    for test in tests:
        print(Solution().fourSum(test[0], test[1])) 