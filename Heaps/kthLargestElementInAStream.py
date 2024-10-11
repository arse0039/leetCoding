# LeetCode 703 - Kth Largest Element in a Stream
# This problem is easy, which is true if you used the built-in heap data structure. If you build it 
# yourself, it is a medium question, imo. If we sort the received array of nums and remove values relative to 
# the length, we have ourselves a min heap. For add, we need to check the end values of the heap to know where 
# the new value goes. If its larger than the end value, we tack it on the end. If it is smaller than the right 
# value then we add it to the end. Otherwise, it goes in the middle, so we need to remove values until we find it's
# spot, add it in, then readd the values we took out. After we have done the adding operation, we need to pop values off
# based on the length of the heap relative to k. Then we can return the smallest value. 

import heapq
from collections import deque

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.heap = deque(sorted(nums) if nums else [])
        self.k = k
        while len(self.heap) > self.k:
            self.heap.popleft()

    def add(self, val: int) -> int:
        if val >= self.heap[-1]:
            self.heap.append(val)
        
        elif val < self.heap[-1] and val > self.heap[0]:
            removed = []
            while val > self.heap[0]:
                removed.append(self.heap.popleft())
            self.heap.appendleft(val)
            for _ in range(len(removed)):
                self.heap.appendleft(removed.pop())
        else:
            self.heap.appendleft(val)
        
        while len(self.heap) > self.k:
            self.heap.popleft()
        
        return self.heap[0]

# Using the heapq import. We can heapify the array and use heap methods to add items to the heap.
# This library will automatically update your minHeap. If we want to make it a maxHeap, we would want to insert
# negative values and return the negative version of the min val (which would be the max!)
# The methods are heapq.heapify(), heapq.heappop(), heapq.heappush(), heapq.heappushpop(), heapq.heapreplace()
class KthLargest2:
    def __init__(self, k: int, nums: list[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
    
    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

test = KthLargest2(3, [4, 5, 8, 2])
print(test.add(3))
print(test.add(5))
print(test.add(10))
print(test.add(9))
print(test.add(4))