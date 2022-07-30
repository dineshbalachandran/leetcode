"""
Medium

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return "".join(["ListNode{val: ", str(self.val), ", next: ", str(self.next), "}"]) if self else "None"



class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        curr = head
        nodelist = []
        while curr:
            nodelist.append(curr)
            curr = curr.next
        
        for i in range((len(nodelist) // 2)):
            h, t = nodelist[i], nodelist[len(nodelist)-1-i]
            p = h.next
            h.next = t
            t.next = p
            
        nodelist[len(nodelist)//2].next = None

    def reorderListTwoPointer(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

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
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5]
    ]

    for test in tests:
        n = listtoNode(test)   
        Solution().reorderList(n)     
        print(nodetoList(n))