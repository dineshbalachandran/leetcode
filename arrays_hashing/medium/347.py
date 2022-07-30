"""
Medium
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

import collections
import heapq

class Solution:
    def topKFrequent(self, nums, k: int):
        # n log n

        counts = collections.defaultdict(int)
        for n in nums:
            counts[n] -= 1
        
        h = [(item[1], item[0]) for item in counts.items()]
        heapq.heapify(h)
        
        res = []
        for i in range(k):
            item = heapq.heappop(h)
            res.append(item[1])
        
        return res

    def oNtopKFrequent(self, nums, k):
    # O(n)
    # bucket sort
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

if __name__ == "__main__":

    tests = [   
        ([1,1,1,2,2,3], 2),
        ([1], 1),
        ([5,2,5,3,5,3,1,1,3], 2),
    ]

    for test in tests:
        nums, k = test
        print(Solution().topKFrequent(nums, k))