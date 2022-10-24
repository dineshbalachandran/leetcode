"""
Medium
Given an integer array arr and a target value target, return the integer value such that when 
we change all the integers larger than value in the given array to be equal to value, the sum of 
the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

 

Example 1:
Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

Example 2:
Input: arr = [2,3,5], target = 10
Output: 5

Example 3:
Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i], target <= 105
"""

import bisect

class Solution:
    def findBestValue(self, arr, target: int) -> int:
        
        arr.sort()
        cum = [0] * (len(arr)+1)
        
        for i in range(len(arr)):
            cum[i+1] = arr[i] + cum[i]

        
        def f(n):
            i = findIndex(n)
            #i = bisect.bisect_left(arr, n)
            
            return (cum[i] + (len(arr)-i)*n)
        
        def findIndex(n):
            #print(n)
            l, r = 0, len(arr)-1
            
            while l < r:
                m = l + (r-l) // 2
                if arr[m] < n:
                    l = m+1
                elif arr[m] > n:
                    r = m-1
                else:
                    return m
                #print(l,r)
            
            return (l)
            
        
        l, r = 0, arr[-1]
        while l < r-1:
            #print(l, r)
            m = (r+l) // 2
            
            sm = f(m)
            
            if sm < target:
              l = m
            elif sm > target:
              r = m
            else:
              return m

        return r if abs(target-f(r)) < abs(target-f(l)) else l

if __name__ == "__main__":
    tests = [
        ([4,9,3], 10),
        ([2,3,5], 10),
        ([60864,25176,27249,21296,20204], 56803),
        ([2,3,5], 11),
        ([15,1,1,1,1,1,1,1,1,1,1,1], 50)
    ]

    for test in tests:
        print(Solution().findBestValue(test[0], test[1]))