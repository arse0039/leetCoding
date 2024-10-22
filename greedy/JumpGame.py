
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        jumps = [False] * len(nums)
        jumps[-1] = True

        for index in range(len(nums) - 2, -1, -1):
            jumpIndex = nums[index]
            if index + jumpIndex >= len(nums):
                jumps[index] = True
            jumps[index] = jumps[jumpIndex+index]
        
        return jumps[0]


nums=[1,2,1,0,1]

test = Solution()
test.canJump(nums)