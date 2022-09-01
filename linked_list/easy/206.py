"""
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
 

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return "".join(["ListNode{val: ", str(self.val), ", next: ", str(self.next), "}"]) if self else "None"

class Solution:
    def reverseList(self, head):
        
        curr, prev = head, None
        # while curr:
        #     t = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = t

        while curr:            
            curr.next, prev, curr = prev, curr, curr.next            

        return prev

if __name__ == "__main__":
    tests = [
        [1, 2, 3, 4, 5],
        [1, 2],
        []
    ]

    for test in tests:
        h, p = None, None
        for v in test:
            n = ListNode(v, None)
            if not h:
                h = n
            if p:
                p.next = n
            p = n
        print(Solution().reverseList(h))
