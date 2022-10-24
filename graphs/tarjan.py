"""

Tarjan's algorithm to find strongly connected components (where every vertex in a cycle is reachable from every other vertex in the cycle and once such
a cycle is left, there is no way back into the SCC)

"""
class Solution:
  def tarjans(self, V, adj):
          # code here
          
          ids = {}
          low_link_ids = {}
          
          stack = []
          seen = set()
          
          self.id = -1
          
          res = {}
          
          def dfs(u):
              
              self.id += 1
              ids[u] = self.id
              low_link_ids[u] = self.id
              
              seen.add(u)
              stack.append(u)              
              
              for v in adj[u]:
                  if v not in ids:
                      dfs(v)
                  if v in seen:                      
                      low_link_ids[u] = min(low_link_ids[u], low_link_ids[v])
              
              if low_link_ids[u] == ids[u]:
                  while stack:
                      v = stack.pop()
                      seen.remove(v)                      
                      low_link_ids[v] = ids[u]
                      res.setdefault(low_link_ids[u], []).append(v)
                      if v == u:
                        break
          
          for u in range(V):
            if u not in ids:
              dfs(u)
          
          return list(res.values())

if __name__ == "__main__":
  adj = {}  
  adj[1] = [0]
  adj[0] = [2, 3]
  adj[2] = [1]
  adj[3] = [4]
  adj[4] = []
  print(Solution().tarjans(5, adj))