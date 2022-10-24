"""
Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        
        if not root:
            return []
        
        res = []
        l = [root]
        while l:            
            l, nodes = [], l
            
            rl = []
            for node in nodes:
                rl.append(node.val)
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            res.append(rl)
        
        return res

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
        [3,9,20,None,None,15,7],
        [1],
        []
    ]

    for test in tests:
        l = listtoTree(test)
        print(Solution().levelOrder(l))