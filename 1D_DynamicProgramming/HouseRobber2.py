# LeetCode - 213 - House Robber 2 - Medium
# IO
"""
Input - nums - ARR(INT)
output - INT -> Max value we can rob from non-adjacent houses. 
"""
# Design
"""
This problem is tricky! With our array of houses, we have a cycle that is formed. This cycle occurs because of TWO
houses that are connected. These houses are the the very first house and the very last house. If we omit the last house,
we can figure out what the max amount we can rob is from the first subSet of houses. If we omit the first house, we can 
figure out what the max amount we can rob is from that subSet.
What's important to note is that the cycle creates a block of two houses that can not be visited. The first node and it's neighbor 
on the left. This means that if we start from the first node, we can NEVER land on the last. And if we start inside of the array
we can NEVER land on the first. Aka, we can never actually cycle back. So, we can just run House Robber on the a subArray that 
does NOT include the first val -> [1:] and again on the subArr that does not include the final value -> [:-1]. 
Doing so gives us two max values we can use. We just need to return the max value from each of these.
On each subArray, we can work backwards from the end of the array if the array has 3 or more elements. Any less than that we can 
just return the max value from the first two elements or less elements.
Otherwise,  can look at the max values at index + 2 and index + 3 and update the value at the given index to be the max of those
two plus itself. This way we have updated the subArrs in place with max values and can return the max value between the value at index0
and the max value at index 1!

"""
# Constraints
"""
Can nums have less than 2 values?  Yes. It can have one value.
Are values in nums >= 0? Can they be negative?  Only positive integers
"""
# Example
nums = [1, 3, 2, 4, 8] # 18
nums2 = [4, 3, 1] # 4

class Solution:
    def rob(self, nums:list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def subRob(subArr: list[int]) -> int:
            if len(subArr) <= 2:
                return max(subArr)
            for i in range(len(subArr) - 3, -1, -1):
                oneMax = subArr[i+2] if i+2 < len(subArr) else 0
                twoMax = subArr[i+3] if i+3 < len(subArr) else 0
                indexMax = max(oneMax, twoMax) + subArr[i]
                subArr[i] = indexMax
            return max(subArr[0], subArr[1])
        
        removeFirst = subRob(nums[1:])
        removeLast = subRob(nums[:-1])

        return max(removeFirst, removeLast)

test = Solution()
print(test.rob(nums))
