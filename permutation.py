def permutation(s, prefix=""):
  if len(s) == 0:
    print(prefix)
  else:
    for i in range(len(s)):
      rem = s[:i] + s[i+1:]
      print(rem, s[i])
      permutation(rem, prefix+s[i])

if __name__ ==  "__main__":
  permutation("abc")
