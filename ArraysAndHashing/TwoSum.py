"""
Given an array of integers nums and an integer target, return the indices 
i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

inputs = nums -> array of ints
target = a target value we need to add two values to equal

Are we allowed to sort the array?  Yes
Can the numbers and target be negative? Yes
Can the target be zero or the array be empty or contain only one value? 
Are all numbers unique or can they repeat? 

Example - [1, 5, 7, 2, 9] Target - 8
Naive Approach -> For each integer, we can iterate through the array, searching for the compliment, making sure
to skip itself. This would be a O(n ^ 2) since we are iterating through the array once, and once more for each pass.
Another approach would be to store each value and its index. We can loop through the array once, adding the numbers
as keys and the index as a value. We can loop again through each index to see if the compliment is in the dict.
If so, it check to see if it is not the same index and, if so, return the indices in the correct order. This 
approach would be O(n) with a spaced complexity of O(n). 

Finally, we can use a two-pointer approach. This only works if the array is sorted, however. Sorting the array gives us a 
O(n log n) time complexity, so it isn't as efficient as the hash map approach, though the space complexity is better at 
O(1).
"""

class Solution: 
    def twoSum(self, nums: list[int], target:int) -> list[int]:
        nums.sort()
        
        left, right = 0, len(nums) - 1

        while left < right:
            sumVal = nums[left] + nums[right]
            if sumVal == target:
                return [left, right]
            elif sumVal > target:
                right -= 1
            else:
                left += 1
        
        return [-1, -1]
    

test = Solution()
nums = [1, 5, 7, 2, 9] 
target = 8
print(test.twoSum(nums, target))

