"""
You are given an array non-negative integers heights which represent an elevation map. 
Each value heights[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
Input: height = [0,2,0,3,1,0,1,2,2,1]
                 0 0 2 0 1 2 1 0 0 0

This will be an O(n) approach where we do two passes. One from the left and one from the right
First, we will create an array of len(heights) and fill it with infinities (since we are looking for min vals).
Then, will move forward for our array, setting our max value to the first number. If the number is smaller than our current
max we calculate the volume by subtracting the number at that index from the max and store it in the trappedWater array. We
will choose th
Otherwise, we set the value to 0. 
We do the same thing moving backwards through the array but this time updating the values using the minimum between the existing values
and our calculated value. 

Once done, we will have an array of values, which we can take the total sum of and return said sum

Can heights be empty? If it is empty or contains less then 3 elements, the result will always be zero.
"""

class Solution:
    def trap(self, heights:list[int]) -> int:
        if len(heights) < 3:
            return 0

        trappedWater = [0] * len(heights)

        # move to the left
        maxHt = heights[0]
        for i in range(len(heights)):
            if heights[i] < maxHt:
                trappedWater[i] = maxHt - heights[i]
            else:
                maxHt = heights[i]

        # move back from the right
        maxHt = heights[-1]
        for i in range(len(heights)-1, -1, -1):
            if heights[i] < maxHt:
                trappedWater[i] = min(trappedWater[i], maxHt - heights[i])
            else:
                trappedWater[i] = 0
                maxHt = heights[i]
        
        return sum(trappedWater)
test = Solution()
height=[0,2,0,3,1,0,1,3,2,1]
print(test.trap(height))

    # Optimized:
class Solution2:
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2: 
            return 0
        
        result = 0
        
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]

        return result