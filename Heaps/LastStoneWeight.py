# LeetCode 1046 - Last Stone Weight - Easy
# In this problem, we are given an array that reprsents the weights of stones. We take turns taking the
# heaviest two stones and smashing them together. Whatever value of stone that remains is then added
# to the stones array. This means that if stones have equal values, both are destroyed. When only one or no
# stones remain, we are done! Because we always want the largest value stones, we know that a Heap (also known as
# a priority queue) is needed. Specifically, we need a maxHeap! So, we just need to import the ole heapq library,
# make all thus numbers negative, and heapify the bad boy. From there, we can just pop off the two largest numbers,
# compare them, do maths, and add the stone if needed. Then we simply return the final stone value if it exists, 
# otherwise we can return a big ole goose egg.
# 

import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stonesHeap = [-stone for stone in stones]
        heapq.heapify(stonesHeap)
        
        while len(stonesHeap) > 1:
            stone1 = -heapq.heappop(stonesHeap)
            stone2 = -heapq.heappop(stonesHeap)

            if stone1 > stone2:
                result = stone1 - stone2
                heapq.heappush(stonesHeap, -result)
            if stone2 > stone1:
                result = stone2 - stone1 
                heapq.heappush(stonesHeap, -result)
            
        return -stonesHeap[0] if stonesHeap else 0

test = Solution()
stones = [1,2]
print(test.lastStoneWeight(stones))