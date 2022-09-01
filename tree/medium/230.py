"""
Medium

Given the root of a binary search tree, and an integer k, return the kth smallest value 
(1-indexed) of all the values of the nodes in the tree.
 
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    res = None
    count = 0
    
    def kthSmallest(self, root, k: int) -> int:
        
        def find(node):            
            if not node or self.res:
                return
            
            find(node.left)                        
            
            self.count += 1
            if self.count == k:
                self.res = node.val
                return
            
            find(node.right)            
            
            return

        find(root)
        
        return self.res

    def kthSmallestAlternate(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

def listtoTree(l):
    def toTree(k):
        if k > len(l) - 1:
            return None

        node = TreeNode(l[k]) if l[k] else None
  
        if node:
            node.left, node.right = toTree(2*k+1), toTree(2*k+2)

        return node
    
    return toTree(0)

if __name__ == "__main__":
    tests = [
        ([3,1,4,None,2], 1),
        ([5,3,6,2,4,None,None,1], 3)
    ]

    for test in tests:
        l, k = listtoTree(test[0]), test[1]
        print(Solution().kthSmallest(l, k))