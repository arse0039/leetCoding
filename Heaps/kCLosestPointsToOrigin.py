# LeetCode 973 - k Closest Points To Origin - Medium
# In this problem, we are given an array of x and y coordinates. Our goal is to return the K number
# of points that are closest to the origin. We are given the formula to calculate distance to the origin
# and this tells us that what we really are looking for are the K smallest elements, since the smallest
# distances will be the ones closest to the origin. 
# Anytime we see "K smallest" or "K largest", we should immediately be thinking of a heap. Because heapifying
# something is an easy way to have access to the smallest or largest elements!
# For this problem, the tricky part is that we need to return the coordinates, not the distance. And we are minHeaping
# BASED on the distance. How do we account for this? Well, heapify can still work with tuples! It does NOT work with dicts.
# It will heapify based on the first tuple value. So, we just need to create that heap and then pull out the k smallest tuples, 
# slap the points in a results array, and voila!
# Time Complexity is O(n) because k could be equal to the number of points, meaning we would need to iterate through every 
# item in the minHeap to put into the results. Also, heapify is O(n). The other methods are O(log n)

import math, heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        minHeap = []
        for point in points:
            distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            minHeap.append((distance, point))
        
        heapq.heapify(minHeap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(minHeap)[1])
        
        return result

test = Solution()
points = [[0,2],[2,0],[2,2]]
k = 2
print(test.kClosest(points, k))