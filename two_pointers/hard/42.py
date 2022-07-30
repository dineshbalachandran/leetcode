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


if __name__ == "__main__":
    tests = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5],
    ]

    for test in tests:
        print(Solution().trap(test))