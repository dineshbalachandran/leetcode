"""
Easy

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        
        def invert(node):            
            if not node:
                return None
            
            node.left, node.right = invert(node.right), invert(node.left)
            
            return node
       
        return invert(root)

def listtoTree(l):
    def toTree(k):
        if k > len(l) - 1:
            return None

        node = TreeNode(l[k])
  
        node.left, node.right = toTree(2*k+1), toTree(2*k+2)

        return node
    
    return toTree(0)

def treetoList(root):

    if not root:
        return []

    q = deque()
    q.append(root)
    res = []

    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return res


if __name__ == "__main__":
    tests = [
        [4,2,7,1,3,6,9],
        [2, 1, 3],
        []
    ]

    for test in tests:
        l = listtoTree(test)
        print(treetoList(l))
        print(treetoList(Solution().invertTree(l)))
        print()