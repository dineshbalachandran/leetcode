"""
Easy
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node 
(0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        
        slow, fast = head, head
        
        while fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                continue
            fast = fast.next
            if slow == fast:
                return True
        
        return False

def listtoNodeWithLoop(l, pos):
    h, p = None, None
    posNode = None
    for i, v in enumerate(l):
        n = ListNode(v, None)
        if i == pos:
            posNode = n
        if not h:
            h = n
        if p:
            p.next = n
        p = n

    if p and posNode:
        p.next = posNode

    return h

if __name__ == "__main__":
    tests = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1)
    ]

    for test in tests:
        h = listtoNodeWithLoop(test[0], test[1])
        print(Solution().hasCycle(h))