if __name__ == "__main__":  
  t = [7, 7, 9]
  N = len(t)
  T = 8

  dp = [[0]*(N+1) for _ in range(T)]

  for s in range(1, T):
    for i in range(1, N+1):
      if t[i-1] <= s:
        dp[s][i] = 1 + dp[s-1][i-1]
      elif t[i-1] > s and s-t[i-1] >= 0:
        dp[s][i] = max(dp[s][i-1], 1 + dp[s-t[i-1]][i-1])
      else:
        dp[s][i] = dp[s][i-1]
  
  print(dp[-1][-1])