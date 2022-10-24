"""
Medium

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive 
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
"""

class NumArray:
    def __init__(self, A):
        self.tree = {}
        self.A = A

        def build(node, start, end):            
            if start == end:
                self.tree[node] = self.A[start]
                return
            
            mid = (start+end) // 2

            build(2*node, start, mid)
            build(2*node+1, mid+1, end)

            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
        
        build(1, 0, len(self.A)-1)

    
    def update(self, idx, val):

        def upd(node, start, end):
            if start == end:
                self.A[idx] = val
                self.tree[node] = val
                return
            
            mid = (start+end) // 2
            if start <= idx and idx <= mid:
                upd(2*node, start, mid)
            else:
                upd(2*node+1, mid+1, end)

            self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
        
        upd(1, 0, len(self.A)-1)

    def sumRange(self, left, right):

        def s(node, start, end):
            if start > right or end < left:
                return 0
            
            if left <= start and end <= right:
                return self.tree[node]
            
            mid = (start+end) // 2

            return s(2*node, start, mid) + s(2*node+1, mid+1, end)
        
        return s(1, 0, len(self.A)-1)


if __name__ == "__main__":
    n = NumArray([1, 3, 5])
    for q, l,r in [('q',0,2), ('u',1,2), ('q',0,2)]:
        if q == 'q':
            print(n.sumRange(l,r))
        else:
            n.update(l,r)