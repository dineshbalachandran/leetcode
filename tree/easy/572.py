"""
Easy

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root
 with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's 
descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtreeX(self, root, subRoot) -> bool:        
        def subTree(node, subnode):
            
            if (not subnode and node) or (not node and subnode):
                return False
            
            if not node and subnode:
                return False
        
            if not node and not subnode:
                return True
            
            return ((node.val == subnode.val and 
                     subTree(node.left, subnode.left) and 
                     subTree(node.right, subnode.right)) or                     
                    (subTree(node.left, subRoot) or 
                     subTree(node.right, subRoot)))
        
        return subTree(root, subRoot)
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: return True
        if not s: return False
        
        if self.sameTree(s, t):
            return True
        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))
    
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        return False

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
        ([3,4,5,1,2],[4,1,2]),
        ([3,4,5,1,2,None,None,None,None,0], [4,1,2])
    ]

    for test in tests:
        p, q = listtoTree(test[0]), listtoTree(test[1])
        print(Solution().isSubtree(p, q)) # isSubtreeX is equivalent however does not work for a large tree for some subtle reason