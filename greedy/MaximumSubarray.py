# LeetCode - 53 - Maximum Subarray - Medium

# O(n2) Solution
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxRes = float('-inf')

        for i in range(len(nums)):
            runningSum = nums[i]
            maxRes = max(maxRes, runningSum)
            for j in range(i+1,len(nums)):
                runningSum += nums[j]
                maxRes = max(maxRes, runningSum)
        
        return maxRes
    
# Greedy
"""
To optimize this solution, we can use a linear time approach.
To do this, need to use two pointers to assess the array because we know that values that shrink
our total are the opposite of what we want to do. We are wanting to GROW our value. So, if we move a pointer
and it shrinks our number, we can move our pointers

1 -3 4 2 -7 4 2 3 1 -8
1 -2 4 6 -1 4 7 10 11 3

if prevSum + currentVal < currentVal 
"""

class Solution2:
    def maxSubArray(self, nums: list[int]) -> int:
        maxRes = nums[0]
        
        runningSum = nums[0]
        for i in range(1, len(nums)):
            if runningSum + nums[i] < nums[i]:
                runningSum = nums[i]
            else:
                runningSum += nums[i]
            
            maxRes = max(maxRes, runningSum)
      
        return maxRes
    

nums = [-200, -5, -15]
test2 = Solution2()
print(test2.maxSubArray(nums))