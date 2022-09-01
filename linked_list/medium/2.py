"""
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return "".join(["ListNode{val: ", str(self.val), ", next: ", str(self.next), "}"]) if self else "None"


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

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        c = 0
        dummy = ListNode()
        l3 = dummy
        while l1 and l2:
            s = l1.val + l2.val + c
            d, c = s % 10, s // 10            
            l3.next = ListNode(d)
            l1, l2, l3 = l1.next, l2.next, l3.next            
        
        r = l1 if l1 else l2
        while r:
            s = r.val + c
            d, c = s % 10, s // 10            
            l3.next = ListNode(d)
            l3 = l3.next
            r = r.next
        
        if c != 0:
            l3.next = ListNode(c)
        
        return dummy.next

if __name__ == "__main__":
    tests = [
        ([2,4,3], [5,6,4]),
        ([0],[0]),
        ([9,9,9,9,9,9,9], [9,9,9,9])
    ]

    for test in tests:
        h, n = test
        print(nodetoList(Solution().addTwoNumbers(listtoNode(h), listtoNode(n))))