"""
Easy

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the 
BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a 
node to be a descendant of itself).”

 

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according 
to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lcs(node, l, r):
            
            if l.val <= node.val and node.val <= r.val:
                return node
            
            if l.val > node.val and r.val > node.val:
                return lcs(node.right, l, r)
            else:
                return lcs(node.left, l, r)
            
        
        if q.val > p.val:
            return lcs(root, p, q)
        else:
            return lcs(root, q, p)

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
        ([6,2,8,0,4,7,9,None,None,3,5], 2, 8),
        ([6,2,8,0,4,7,9,None,None,3,5], 2, 4),
        ([2,1], 2, 1)
    ]

    for test in tests:
        l = listtoTree(test[0])
        p = TreeNode(test[1])
        q = TreeNode(test[2])        
        print(Solution().lowestCommonAncestor(l, p, q).val)