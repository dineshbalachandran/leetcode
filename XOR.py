if __name__ == "__main__":
  #A = [16, 15, 14, 2, 1]
  A = [18, 8, 2]
  N = len(A)

  res = []
  for i in range(N):
    for j in range(i+1, N):
      print(i, j, A[i], A[j], A[i] ^ A[j])
  
