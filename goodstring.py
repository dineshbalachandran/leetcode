if __name__ == "__main__":  
  N, K = 4, 1
  S = 'abcd'

  cache = {}

  def dfs(i, k):

    if k == 0 or k > (N-i) or i >= N:
      return 0
    
    if (i, k) in cache:
      return cache[(i, k)]
    print(i, k)
    
    # v1 = ord(S[i]) - ord('a') 
    # v2 = dfs(i+1, k-1)
    # v3 = dfs(i+1, k)
    # print(v1, v2, v3)
    # cache[(i, k)] = v1*v2 + v3

    cache[(i, k)] = ord(S[i]) - ord('a') * dfs(i+1, k-1) + dfs(i+1, k)

    return cache[(i, k)]
  
  res = dfs(0, K)
  print(cache)
  print(res % (10**9+7))