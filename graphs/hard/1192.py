"""
Hard

Critical Connections in a Network (TARJAN's algorithm for strongly connected components)

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network 
where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers 
directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.


Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.


"""

from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        self.id = -1
        
        ids = {}
        low = {}
        
        stack = []
        seen = set()
        
        adj = {}
        
        for u, v in connections:
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)
      
        res = []
        
        def dfs(u, p):
            
            self.id += 1
            
            ids[u] = self.id
            low[u] = self.id
            
            stack.append(u)
            seen.add(u)
            
            for v in adj[u]:
                if v == p:
                    continue
                if v not in ids:
                    dfs(v, u)
                if v in seen:
                    low[u] = min(low[u], low[v])
                else:
                    res.append([u, v])
                
            if low[u] == ids[u]:
                while stack:
                    v = stack.pop()
                    seen.remove(v)
                    low[v] = ids[u]
                    if v == u:
                        break
        
        for u in range(n):
            if u not in ids:                
                dfs(u, -1)
        
        return res

if __name__ == "__main__":

  tests = [
    (4, [[0,1],[1,2],[2,0],[1,3]]),
    (2, [[0,1]])
  ]

  for n, connections in tests:
    print(Solution().criticalConnections(n, connections))
