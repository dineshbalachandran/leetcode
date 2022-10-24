"""
Medium

19. Remove Nth Node from End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
 

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return "".join(["ListNode{val: ", str(self.val), ", next: ", str(self.next), "}"]) if self else "None"


class Solution:
    def removeNthFromEnd(self, head, n: int):        
        curr, prev = head, None
        
        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        
        curr = prev
        prev = None
    
        
        i = 1
        while curr:
            t = curr.next            
            curr.next = prev
            if i != n:
                prev = curr
            curr = t
            i += 1            
            
        return prev
    
    def removeNthFromEndAnother(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
            
        # delete
        left.next = left.next.next
        return dummy.next

def listtoNode(l):
    h, p = None, None
    for v in l:
        n = ListNode(v, None)
        if not h:
            h = n
        if p:
            p.next = n
        p = n

    return h

def nodetoList(h):
    res = []
    n = h
    while n:
        res.append(n.val)
        n = n.next
    
    return res

if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], 2),
        ([1], 1),
        ([1,2], 1)
    ]

    for test in tests:
        h, n = test
        print(nodetoList(Solution().removeNthFromEnd(listtoNode(h), n)))