"""
Given a binary tree, determine if it is height-balanced

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
 

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

      def dfs(node):
        
        if not node:
          return (True, 0)

        left, right = dfs(node.left), dfs(node.right)

        return ( (True if left[0] and right[0] and abs(left[1]-right[1]) <= 1 else False, 1+max(left[1], right[1])) )
      
      return dfs(root)[0]

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
        [3,9,20,None,None,15,7],
        [1,2,2,3,3,None,None,4,4],
        []
    ]

    for test in tests:
        l = listtoTree(test)
        print(Solution().isBalanced(l))


