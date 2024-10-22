"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

1 2, -3, 4, -6, -5 -> [0, 1, 2], [1, 3, 4], [0, 3, 5]

Can nums be empty?  Yes
Can nums contain 0s? -> Yes, of course


a + b + c = 0
b + c = -a
- 1 = 

Let's sort the array. To start. Then, for each value in the array (which will be our a value), we can iterate through the array
from that point forward, using a two-pointer approach to find the target (-a). By moving forward the array, we ensure that we 
will not have duplicate index values! 
When we get a match, we add that to our results array and finally return that result. 

"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[int]:
        nums.sort()
        result = []

        calculatedAs = set()
        for i in range(len(nums)):
            if nums[i] not in calculatedAs:
                calculatedAs.add(nums[i])
                left = i + 1
                right = len(nums) - 1

                while left < right:
                    summation = nums[i] + nums[left] + nums[right]
                    if summation == 0:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif summation < 0:
                        left += 1
                    else:
                        right -= 1
        
        return result
