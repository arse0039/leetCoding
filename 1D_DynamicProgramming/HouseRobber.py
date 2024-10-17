# LeetCode - 198 - House Robber - Medium
# IO
"""
Inputs - nums -> ARR(INT) -> Each integer represents the amount of money that house has.
Out -> INT -> The maximum amount of money we can earn by robbing houses
"""
# Design
"""
We are given an array of houses and can rob them to steal their money. We want to rob AS MANY houses as possible
to make the most money, so skipping more than one house does not make sense.
This means that we can either start at the first house and rob houses, or we can start at second house and rob them first.
The constraint is that we can not rob any house that is adjacent to a house we want to rob. The means that we have a LOT of different combinations 
we can take from any house moving forward.
If we start from the last house, we know that it can only be robbed for it's amount. Same for the second to last house.
So, we can look at a house. It's max value is the max value of all houses starting from index + 2. If we are outside of the bounds,
we return 0. We add the max returned value to that houses value and continue to work backwards to fill the entire array with values. From 
there, we just need to return the max value from that array's 0th or 1st index.
DP Problem! 
TC - O(n) since we iterate thtough every value in nums. We only ever need to look at two houses ahead to get the max. 
"""
# Constraints
"""
Can we go back and rob houses behind us? NO
Can the houses array be empty? No -> At least 
Can a house have negative money? No
"""
# Example
nums = [2,9,8,3,6] # 4
nums2 = [3, 2, 4, 8, 3] # 11

class Solution:
    def rob(self, nums:list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums) - 1, -1, -1):
            maxVal = 0
            maxOption1 = nums[i + 2] if i + 2 < len(nums) else 0
            maxOption2 = nums[i + 3] if i + 3 < len(nums) else 0
            maxVal = max(maxVal, maxOption1, maxOption2)
            nums[i] = nums[i] + maxVal
        return max(nums[0], nums[1])

test = Solution()
print(test.rob(nums))


                    
        