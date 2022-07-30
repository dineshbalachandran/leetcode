"""
Medium

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
binary tree and inorder is the inorder traversal of the same tree, construct and 
return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        
        if not preorder:
            return None
        
        node = TreeNode(preorder[0])
        k = inorder.index(preorder[0])
        
        node.left = self.buildTree(preorder[1:k+1], inorder[:k])
        node.right = self.buildTree(preorder[k+1:], inorder[k+1:])
        
        return node

def treetoList(root):

    if not root:
        return []

    q = deque()
    q.append(root)
    res = []

    while q:
        node = q.popleft()
        res.append(node.val if node else None)
        if node:
            q.append(node.left)
            q.append(node.right)

    return res

if __name__ == "__main__":
    tests = [
        ([3,9,20,15,7], [9,3,15,20,7]),
        ([-1], [-1])
    ]

    for test in tests:        
        print(treetoList(Solution().buildTree(test[0], test[1])))