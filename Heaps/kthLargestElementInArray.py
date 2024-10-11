# Leetcode -Kth Largest Element in an Array
# For this question, we are given an array of integers and an integer value 'k'. We are asked to return
# the k largest values that exist within the array. Nums is guaranteed to have at least one element
# and k will never be larger than the number of elements in the received array.
# When we see "k largest" we should immediately be thinking "maxHeap". By using a maxHeap we will have O(n) TC
# due to heapify being O(n) but it sure is easy!
# In order to create a maxHeap, all the values have to be negative, so we will need to create a new array with negative
# values. 

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        result = 0
        for _ in range(k):
            result = -heapq.heappop(maxHeap)

        return result