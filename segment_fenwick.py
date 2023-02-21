"""
Segment and Fenwick (BIT) tree implementation
"""

class Segment:
  def __init__(self, _A, _f = lambda x, y: x + y, _id = 0):
    self.A = _A
    self.tree = [0]*(4*len(self.A))
    self.f, self.id = _f, _id

    def build(i, start, end):
      if start == end:        
        self.tree[i] = self.A[start]
        return
      
      mid = (start + end) // 2
      build(2*i, start, mid)
      build(2*i+1, mid+1, end)
      self.tree[i] = self.f(self.tree[2*i], self.tree[2*i+1])
    
    build(1, 0, len(self.A)-1)
    
  def query(self, l, r):
    def calc(i, start, end):
      if r < start or end < l:
        return self.id
      
      if l <= start and end <= r:
        return self.tree[i]
      
      mid = (start + end) // 2
      return self.f(calc(2*i, start, mid), calc(2*i+1, mid+1, end))

    return calc(1, 0, len(self.A)-1)

  def update(self, idx, delta):
    def rebuild(i, start, end):
      if start == end:
        self.A[idx] += delta
        self.tree[i] = self.f(self.tree[i], delta)
        return
      
      mid = (start + end) // 2
      if start <= idx and idx <= mid:
        rebuild(2*i, start, mid)
      else:
        rebuild(2*i+1, mid+1, end)

      self.tree[i] = self.f(self.tree[2*i], self.tree[2*i+1])

    rebuild(1, 0, len(self.A)-1)    

class Fenwick:
  def __init__(self, _A, _f = lambda x, y: x + y):

    self.tree = [0]*(len(_A)+1)
    self.f = _f

    for i in range(len(_A)):
      self.update(i, _A[i])

  def update(self, i, delta):    
    i += 1
    while i < len(self.tree):
      self.tree[i] += delta
      i += (i & -i)

  def query(self, i):
    i += 1
    s = 0
    while i > 0:
      s = self.f(s, self.tree[i])
      i -= (i & -i)
    
    return s

if __name__ == "__main__":
  segtests = [
    ([1,3,5,7,9,11], (0, 2), (0, 3), (3, 8))
  ]

print("Segment")
for test in segtests:
  s = Segment(test[0])
  print(s.A)
  print(test[1][0], test[1][1],  s.query(test[1][0], test[1][1]))
  print(test[2][0], test[2][1],  s.query(test[2][0], test[2][1]))
  s.update(test[3][0], test[3][1])
  print(s.A)
  print(test[1][0], test[1][1],  s.query(test[1][0], test[1][1]))
  print(test[2][0], test[2][1],  s.query(test[2][0], test[2][1]))


fentests = [
    ([1,3,5,7,9,11], (0, 2), (0, 3), (3, 8))
  ]

print("Fenwick")
for test in fentests:
  s = Fenwick(test[0])
  print(s.tree)
  print(test[1][0], test[1][1],  s.query(test[1][1])-s.query(test[1][0]-1))
  print(test[2][0], test[2][1],  s.query(test[2][1])-s.query(test[2][0]-1))
  s.update(test[3][0], test[3][1])
  print(s.tree)
  print(test[1][0], test[1][1],  s.query(test[1][1])-s.query(test[1][0]-1))
  print(test[2][0], test[2][1],  s.query(test[2][1])-s.query(test[2][0]-1))

  