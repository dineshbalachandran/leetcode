"""
Given a deck of N cards numbered from 1 to N. A card should be removed in sequence starting from 1 and the card 
should be at the top of the deck for it to be removed. 
The card can be brought to the top of the deck by either moving all cards while maintaining relative order 
before it to the bottom of the deck or by bringing cards from the bottom of the deck to the top again maintaining order
The cost is calculated as the value of all the cards that are moved. If no cards require to be moved, i.e. the card is 
already at the top then the cost of removal of that card is zero.

The goal is to remove all cards from the deck in order such that the cost is it minimum.

For e.g. for the deck [3, 5, 1, 4, 2]

To remove 1: move cards 4, 2 and 1 to the top and remove 1, the cost for this is 7 (4+2+1). The cards are now in 
the order [4, 2, 3, 5]
To remove 2: move 4 to the bottom, the cost for this is 4, with the order now [3, 5, 4]
To remove 3: the cost is 0, as it is already at the top, with the order now [5, 4]
To remove 4: move 4 to the top, the cost is 4, with the order now [5]
To remove 5, the cost is 0, the total cost thus becomes 7 + 4 + 0 + 4 + 0 i.e. 15. This is the minimum cost
"""

from typing import List
from collections import deque

class Solution:
  def minCost(self, deck: List[int]) -> int:
    N = len(deck)
    
    bottom, top = deque([]), deque([])

    for i in range(N):
      bottom.appendleft(deck[i])
      top.append(deck[i])

    cost = 0
    for n in range(1, N):
      bcost, tcost = 0, 0
      while True:
        b = bottom.popleft()
        bcost += b
        if b == n:
          break
        bottom.append(b)
      while True:
        t = top.popleft()
        if t == n:
          break
        tcost += t
        top.append(t)
      cost += min(tcost, bcost)        
  
    return cost


if __name__ == "__main__":
  tests = [
    [3, 5, 1, 4, 2],
    [2, 3, 5, 1, 4],
    [1, 2, 3, 4],
    [4, 1, 2, 3]
  ]

  for test in tests:
    print(Solution().minCost(test))
