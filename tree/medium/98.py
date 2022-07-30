"""
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isValidBST(self, root) -> bool:
        
        def isValid(node, left, right):
            
            if not node:
                return True
            
            if not (node.val > left and node.val < right):
                return False
            
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)
        
        return isValid(root, float("-inf"), float("inf"))

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
        [2,1,3],
        [5,1,4,None,None,3,6]
    ]

    for test in tests:
        l = listtoTree(test)
        print(Solution().isValidBST(l))