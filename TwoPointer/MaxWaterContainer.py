# LeetCode - 11 - Max Water Container - Medium
# For this question we need to create a function that calculates the maximum amount
# of water we can trap based on different dimensions of water containers. 
# This function accepts one parameter:
# heights: An array of intergers that represent the height of one side of the container.
# This function will return a single integer value, which represents the maximum amount of water
# we can hold. 
## Design ##
# Example - [1, 7, 9, 5, 8, 8, 6]
# For this problem, we want to use either two-pointer approach 
# to find the max container size. The volume of water a container can hold is equal to the 
# minimum value of the two "sides" multiplied by the length of the container. The length 
# can be calculated by taking the difference in indexes between the right pointer and the left pointer
# We can iterate through the array, moving the pointers. We move the pointers by comparing values at both
# the left and right indices. We want to move whichever of the two indices is smaller. If they are the same, 
# we can move whichever! Time Complexity will be O(n) since we are always moving a pointer, which means we 
# move through every element of the array.
## Constraints ##
# Can the array contain negative values? No. Values from 0 - 1000 inclusive.
# Can the array be empty? - No. It always contain at least two values



class Solution:
    def maxArea(self, heights: list[int]) -> int:
        maxWater = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            leftHt = heights[left]
            rightHt = heights[right]
            minHt = min(leftHt, rightHt)
            difference = right - left
            maxWater = max(maxWater, (minHt * difference))

            if leftHt <= rightHt:
                left += 1
            else:
                right -= 1
        
        return maxWater

test = [1, 7, 9, 5, 8, 8, 6] 
test2 = [2, 2, 2, 2]

maxArea = Solution()

print(maxArea.maxArea(test2))
