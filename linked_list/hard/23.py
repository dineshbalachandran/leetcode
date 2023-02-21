"""
Hard

23. Merge K Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
import heapq

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return "".join(["ListNode{val: ", str(self.val), ", next: ", str(self.next), "}"]) if self else "None"
    # def __lt__(self, obj):
    #     return True if self.val < obj.val else False


class Solution:
    def mergeKListsNaive(self, lists):
        
        h = []
        
        for l in lists:            
            curr = l            
            while curr:
                heapq.heappush(h, curr.val)
                curr = curr.next                
        
        dummy = ListNode()
        curr = dummy
        while h:
            curr.next = ListNode(heapq.heappop(h))
            curr = curr.next
        
        return dummy.next
    
    # O(n*logK)
    def mergeKLists(self, lists):

        h = []
        i = 0
        for node in lists:
            if node:
                #the i is just a random value to facilitate heap comparison, in the event the 
                #node.val happen to have the same value and avoid having to implement a __lt__ in the ListNode
                heapq.heappush(h, (node.val, i, node)) 
                i += 1
        
        dummy = ListNode()
        curr = dummy
        while h:
            _, _, node = heapq.heappop(h)
            curr.next = ListNode(node.val)
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
            curr = curr.next
            i += 1
        
        return dummy.next

def listtoNode(l):   
    d = ListNode()
    c = d
    for v in l:
        c.next = ListNode(v)        
        c = c.next

    return d.next

def nodetoList(h):
    res = []
    n = h
    while n:
        res.append(n.val)
        n = n.next
    
    return res

if __name__ == "__main__":
    tests = [
        [[1,4,5],[1,3,4],[2,6]],
        [],
        [[]]
    ]

    for test in tests:
        ll = [listtoNode(l) for l in test]        
        print(nodetoList(Solution().mergeKLists(ll)))