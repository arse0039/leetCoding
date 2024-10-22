"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Inputs - nums -> array of integers
            k -> integer representing the number of most frequent elements we wish to return
Return - list[int] for the values that appear the most often, relative to k. 

Can nums be empty? If k >0 and nums is empty, should we return 0?
Can k be 0? If so, should the return be 0?

nums = [1, 2, 5, 1, 2, 2, 3] k =2

We can create a hash table to hold the counts (use use Counter from defaultdict). Once we have all the counts,
we can iterate through the items, adding the (count, value) to a heap. Once we are done, we can iterate
a number of times == k, popping from the heap to an array, and return the array.
The TC would be O(n) since we only ever iterate through the array once.  

"""
from collections import Counter
import heapq

class Solution():
    def topKFrequent(self, nums:list[int], k:int) -> list[int]:
        numsCount = Counter(nums)

        maxHeap = []
        for val, count in numsCount.items():
            heapq.heappush(maxHeap, (-count, val) ) #log n

        result = []
        for _ in range(k):
            count, val = heapq.heappop(maxHeap)
            result.append(val)
        
        return result