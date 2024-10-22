"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

nums = [1, 20, 13, 2, 5, 2, 1, 3, 4] -> 4

Can nums be empty? Yes
Can nums contain negative integers? Yes
Can there be duplicate numbers? Yes -> 

So, in linear time, we can loop through our input array. When we land on a number, we can add it to a hash map.
From there, we need to check to see if the previous number exists in the hashMap. If it does, we set it's count
value to the previous values count, +1. Otherwise, we just set it's count to 1 since it is the first value in the sequence.
We can update our max as we go, or loop through our counts and return the max at the end. Either way works.

"""

class Solution: 
    def longestConsecutive(self, nums:list[int]) -> int:
        visitedNumbers = {}
        maxVal = 0

        if len(nums) <= 1:
            return len(nums)
        
        for num in nums:
            visitedNumbers[num] = 1

        visited = set

        for i in range(len(nums)):
            numVal = nums[i]
            if numVal not in visited:
                prevVal =  numVal - 1

                while prevVal in visitedNumbers:
                    visitedNumbers[numVal] += 1
                    prevVal -= 1

                maxVal = max(maxVal, visitedNumbers[numVal])
        
        return maxVal
    


