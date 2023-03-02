"""
846. Hand of Straights

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size 
groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, 
return true if she can rearrange the cards, or false otherwise.

 

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.


Constraints:
1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length

"""

from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        count = {}
        for value in hand:
            count[value] = 1 + count.get(value, 0)
        
        h = list(count.items())
        heapq.heapify(h)

        while h:
            s = []
            v, c = heapq.heappop(h)
            if c-1 > 0:
                s.append((v, c-1))
            k = 1
            while k < groupSize:
                if not h:
                    return False                
                n, cn = heapq.heappop(h)
                if n-v > 1:
                    return False
                if cn-1 > 0:
                    s.append((n, cn-1))
                v = n 
                k += 1
            for v, c in s:
                heapq.heappush(h, (v, c))
        
        return True

    def isNStraightHandAlternate(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

if __name__ == "__main__":
  tests = [
    ([1,2,3,6,2,3,4,7,8], 3),
    ([1,2,3,4,5], 4)
  ]

  for test in tests:
    print(Solution().isNStraightHand(test[0], test[1]))

