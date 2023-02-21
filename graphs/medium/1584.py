"""
Medium

1584: Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, 
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path 
between any two points.

 

Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.

"""

from collections import deque
from typing import List
import heapq

class Solution:
  # KRUSKAL MINIMUM SPANNING TREE ALGORITHM (good for sparse graphs) O(E log E)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                
                edges.append((abs(xi-xj) + abs(yi-yj), i, j))
        
        heapq.heapify(edges)
        
        roots = [i for i in range(len(points))]
        self.uniqueroots = len(points)        
        
        def find(i):
            root = i
            while root != roots[root]:
                root = roots[root]
                
            while (i != root): # optimising step to speed up the next find call, amortized O(1)
                i, roots[i] = roots[i], root

            return root
        
        def union(i, j):            
            root1 = find(i)
            root2 = find(j)
            
            if root1 == root2:
                return
            
            roots[root1] = roots[root2]
            
        
        cost = 0
        while edges and self.uniqueroots > 1:
            edgecost, i, j = heapq.heappop(edges)
            
            if find(i) == find(j):
                continue
            
            cost += edgecost            
            union(i, j)
            
            self.uniqueroots -= 1
      
        return cost

    #PRIMS MINIMUM SPANNING TREE ALGORITHM (good for dense graphs) O(E log V)
    def minCostConnectPointsPrims(self, points: List[List[int]]) -> int:

      N = len(points)

      adj = {i: [] for i in range(N)}
      for i in range(N):
        xi, yi = points[i]
        for j in range(i+1, N):
          xj, yj = points[j]
          d = abs(xi-xj) + abs(yi-yj)

          adj[i].append([d, j])
          adj[j].append([d, i])

      visited = set()
      res = 0
      h = [[0, 0]]

      
      while len(visited) < N:
        cost, i = heapq.heappop(h)
        if i in visited:
          continue
        res += cost
        visited.add(i)
        for nCost, ni in adj[i]:
          if ni not in visited:
            heapq.heappush(h, [nCost, ni])
      
      return res


if __name__ == "__main__":
  tests = [
    [[0,0],[2,2],[3,10],[5,2],[7,0]],
    [[3,12],[-2,5],[-4,1]]
  ]

  for test in tests:
    print(Solution().minCostConnectPointsPrims(test))
    