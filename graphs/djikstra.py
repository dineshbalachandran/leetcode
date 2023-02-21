"""
Given a weighted, undirected and connected graph of V vertices and an adjacency list adj where adj[i] is a list of 
lists containing two integers where the first integer of each list j denotes there is edge between i and j , 
second integers corresponds to the weight of that  edge . You are given the source vertex S and 
You to Find the shortest distance of all the vertex's from the source vertex S. You have to return a list of i
ntegers denoting shortest distance between each node and Source vertex S.
 

Note: The Graph doesn't contain any negative weight cycle.

Example 1:

Input:
V = 2
adj [] = {{{1, 9}}, {{0, 9}}}
S = 0
Output:
0 9
Explanation:

The source vertex is 0. Hence, the shortest 
distance of node 0 is 0 and the shortest 
distance from node 1 is 9.
 

Example 2:
Input:
V = 3, E = 3
adj = {{{1, 1}, {2, 6}}, {{2, 3}, {0, 1}}, {{1, 3}, {0, 6}}}
S = 2
Output:
4 3 0

Explanation:
For nodes 2 to 0, we can follow the path-
2-1-0. This has a distance of 1+3 = 4,
whereas the path 2-0 has a distance of 6. So,
the Shortest path from 2 to 0 is 4.
The shortest distance from 0 to 1 is 1 .

"""

from typing import List

import heapq

class Solution:
  def djikstra(self, V: int, adj: List[List[(int, int)]], S: int) -> List[int]:
    dist = [float('inf')]*V
    dist[S] = 0
    
    h = []
    heapq.heappush(h, (0, S))

    visited = set()
    
    while h:
      _, u = heapq.heappop(h)
      visited.add(u)
      for v, d in adj[u]:
        if v not in visited:
          if dist[u] + d < dist[v]:
            dist[v] = dist[u] + d
            heapq.heappush(h, (dist[v], v))
    
    return dist


if __name__ == "__main__":
  tests = [
    (2, [[(1, 9)], [(0, 9)]], 0),
    (3, [[(1,1), (2,6)], [(2,3), (0,1)], [(1,3), (0,6)]], 2)
  ]

for V, adj, S in tests:
  #print(V, adj, S)
  print(Solution().djikstra(V, adj, S))



