"""
Medium

A linked list of length n is given such that each node contains an additional random pointer, which 
could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where 
each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes 
should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. 
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the 
corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented 
as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or 
null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        
        nodemap = {None:None}
        
        dummy = Node(0)
        src, tgt = head, dummy
        
        while src:            
            n = nodemap.setdefault(src, Node(src.val))
            
            n.random = nodemap.setdefault(src.random, Node(src.random.val)) if src.random else None
            
            tgt.next = n
                        
            src, tgt = src.next, tgt.next
            
        return dummy.next

def listtoNode(l):
    nodes = { i: Node(l[i][0]) for i in range(len(l)) }
    nodes[None] = None 

    for i in range(len(l)):
        nodes[i].next = nodes[i+1] if i < len(l)-1 else None
        nodes[i].random = nodes[l[i][1]]

    return nodes[0]

def nodetoList(h):
    res = []
    n = h
    itoNode = []
    nodetoI = {None: None}
    
    i = 0
    while n:
        itoNode.append(n)
        nodetoI[n] = i
        n = n.next
        i += 1
    
    for i in range(len(itoNode)):
        res.append([itoNode[i].val, nodetoI[itoNode[i].random]])
    
    return res

if __name__ == "__main__":
    tests = [
        [[7,None],[13,0],[11,4],[10,2],[1,0]],
        [[1,1],[2,1]],
        [[3,None],[3,0],[3,None]]
    ]

    for test in tests:
        print(test)
        print(nodetoList(Solution().copyRandomList(listtoNode(test))))
        print()