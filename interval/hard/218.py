"""
Hard

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, 
return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. 
Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark 
the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; 
the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

 

Example 1:


Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
 

Constraints:

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings is sorted by lefti in non-decreasing order.

"""

import heapq

class Solution:
    def getSkyline(self, buildings):
        
        ends, points = {}, []
        for b in buildings:
          points += ((b[0], -1, -b[2]), (b[1], 1, -b[2]))
          ends[points[-2]] =  points[-1]

        points.sort()
        
        lookup = {c:i for i, c in enumerate(points)} #1 based index        
        
        BIT = [0] * (len(points)+1)

        #note the query and update functions are an scoped to the right instead of left as is usual for a Fenwick/BIT tree, this because MAX does not have an inverse function
        #this is the key insight
        def query(i): 
            res = 0
            while (i <= len(BIT)):                
                res = max(res, BIT[i])
                i += (i&-i)
            return res
        
        def update(i, h):            
            while i > 0:
                BIT[i] = max(BIT[i], h)
                i -= (i&-i)
            
        res = []
        for i, p in enumerate(points): #n            
            if p[1] == -1:
              end = ends[p]
              update(lookup[end], -p[-1])
            
            h = query(i+1)

            if not res or res[-1][1] != h:
              if res and res[-1][0] == p[0]:
                res[-1][1] = h
              else:
                res.append([p[0], h])
        
        return res

    
    #using a heap is much shorter, elegant and "understandable" solution

    """

    1.First, sort the critical points by its left endpoints. We treat R in (R,0,None) as left endpoint. Then scan across the critical points from left to right.

    2.We only push right end points onto the heap. Think of it as a proxy for the entire rectangle. The key is its negative height because heapq implements min-heap. 
    The heap keeps track of the current max height.

    3.In the for-loop, we pop the hp until all right endpoints smaller than the current left end point are gone. 
    Interestingly, we don't traverse through the heap and remove a rectangle every time an incoming left endpoint comes along. Because we only care about the max height, aka, heap[0][0].

    3.Finally, after updating the heap, we check whether the current max height (hp[0[0]) differs from the last max height (res[-1][1] ), if so, we append the hp[0][0] as the height .
    
    In short,
    a. if the height at current left point is the first in the heap (after we just updated it),then negH == -hp[0][0].
    b. if the height at current left point is not the first in the heap ,that means it is either completely overshadowed by the taller buildings or it will be used when the 
    taller building is popped from the heap. In the second case, don't forget that our lower building's right endpoint is still in the heap, when taller building is popped from the heap, 
    and the lower building's height becomes the max height.
    
    """

    def getSkylineHeap(self, buildings):
      
      edges = []
      for l, r, h in buildings:
        edges.append((l,-h,r))
        edges.append((r,0,0)) 

      edges.sort()

      res, heap = [[0,0]], [(0, float('inf'))]      

      for l, h, r in edges:

        while l >= heap[0][1]:
          heapq.heappop(heap)
        
        if h != 0:
          heapq.heappush(heap, (h, r))
        
        if res[-1][1] != -heap[0][0]:
          res.append([l, -heap[0][0]])

      return res[1:]


    



if __name__ == "__main__":
  print(Solution().getSkylineHeap([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))