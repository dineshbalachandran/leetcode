"""
Easy
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes 
of the first two lists.

Return the head of the merged linked list.

 

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return "".join(["ListNode{val: ", str(self.val), ", next: ", str(self.next), "}"]) if self else "None"


class Solution:
    def mergeTwoLists(self, list1, list2):
        
        if not list1:
            return list2
        elif not list2:
            return list1
        
        head = None
        while list1 and list2:
            if list1.val >= list2.val:
                if not head:
                    head = list2
                while list2 and list2.val <= list1.val:
                    p = list2
                    list2 = list2.next
                p.next = list1
            else:
                if not head:
                    head = list1
                while list2 and list1.val <= list2.val:
                    p = list1
                    list1 = list1.next
                p.next = list2
        
        return head

    def mergeLists(self, list1, list2):

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
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
        ([1, 2, 4], [1, 3, 4]),
        ([], []),
        ([], [0])
    ]

    for test in tests:
        l1, l2 = listtoNode(test[0]), listtoNode(test[1])
        print(nodetoList(Solution().mergeLists(l1, l2)))