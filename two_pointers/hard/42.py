"""
Hard
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Ex 1
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by 
array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
are being trapped.

Ex2
Input: height = [4,2,0,3,2,5]
Output: 9

"""
from typing import List

class Solution:
    def trap(self, height) -> int:
        
        if not height: return 0
        
        units = 0
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        
        while l < r:
            
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                units += leftmax - height[l]     
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                units += rightmax - height[r]
            
        return units
    
    # alternate solution using a monotonic stack approach
    def trap2(self, height: List[int]) -> int:

      monostack = [height[0]]
      units = 0

      for i in range(1, len(height)):
        if height[i] > monostack[-1]:
          if height[i] > monostack[0]:
            while monostack:
              units += monostack[0] - monostack.pop()
          else:
            j = len(monostack)-1
            while monostack[j] < height[i]:
              units += height[i] - monostack[j]
              monostack[j] = height[i]
              j -= 1
        monostack.append(height[i])

      return units 


if __name__ == "__main__":
    tests = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5],
    ]

    for test in tests:
        print(Solution().trap(test))