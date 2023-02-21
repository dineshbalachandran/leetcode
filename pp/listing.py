"""


"""

if __name__ == "__main__":
  N = [5,6,7]
  M = [7]

  dp = [[0]*(len(N)+2) for _ in range(len(M)+2)]

  for j in range(2, len(N)+2):
    dp[1][j] = dp[1][j-2] + N[j-2]
  
  for i in range(2, len(M)+2):
    dp[i][1] = dp[i-2][1] + M[i-2]

  for i in range(2, len(M)+2):
    for j in range(2, len(N)+2):
      dp[i][j] = max(N[j-2]+dp[i][j-2], N[j-2]+dp[i-1][j-1], M[i-2]+dp[i-1][j-1], M[i-2]+dp[i-2][j])
  
  print(dp[-1][-1])