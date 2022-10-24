"""
Easy

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive 
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.

"""

class NumArray:

    def __init__(self, nums):
        
        self.tree = {}
        self.nums = nums
        
        def build(node, start, end):
            if start == end:                
                self.tree[node] = nums[start]
                return
            
            mid = (start+end) // 2
            
            build(2*node, start, mid)
            build(2*node+1, mid+1, end)
            
            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
            
        build(1, 0, len(self.nums)-1)
        

    def sumRange(self, left: int, right: int) -> int:
        
        def s(node, start, end):
            if start > right or end < left:
                return 0
            
            if left <= start and end <= right:
                return self.tree[node]
            
            mid = (start+end) // 2
            
            return s(2*node, start, mid) + s(2*node+1, mid+1, end)
        
        return s(1, 0, len(self.nums)-1)
        

if __name__ == "__main__":
  n = NumArray([-2, 0, 3, -5, 2, -1])
  for l,r in [(0,2), (2,5), (0,5)]:
    print(n.sumRange(l,r))