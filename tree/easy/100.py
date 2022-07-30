"""
Easy

Given the roots of two binary trees p and q, write a function to check if they are the same or 
not.

Two binary trees are considered the same if they are structurally identical, and the nodes have 
the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        
        if (not p and q) or (not q and p):
            return False
        
        if not p and not q:
            return True
        
        return (p.val == q.val and 
                self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))

def listtoTree(l):
    def toTree(k):
        if k > len(l) - 1:
            return None

        node = TreeNode(l[k])
  
        if node:
            node.left, node.right = toTree(2*k+1), toTree(2*k+2)

        return node
    
    return toTree(0)

if __name__ == "__main__":
    tests = [
        ([1,2,3],[1,2,3]),
        ([1, 2], [1,None,2]),
        ([1,2,1], [1,1,2])
    ]

    for test in tests:
        p, q = listtoTree(test[0]), listtoTree(test[1])
        print(Solution().isSameTree(p, q))