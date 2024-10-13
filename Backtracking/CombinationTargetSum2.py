# LeetCode - 40 - Combination Target Sum 2 -  Medium
# For this problem we are tasked to create a function that receives an array of integers,
# which may contain duplicate values as we all as a target integer. We want to return an
# array of number combinations that sum to the target value. However, we have a contraint of not 
# being able to add duplicate values. 
# Much like the original combinationSum problem, we want to use backtracking to help us find ALL
# of the combinations. The trick is not including duplicates!
# In order to ensure there are no duplicates, we must first sort the array. We can then iterate through the 
# duplicate values to the final value to ensure that it does not get used twice. 

class Solution():
    def combinationSum2(self, nums:list, target:int) -> list[list[int]]:
        result = []
        nums = sorted(nums)

        def backtrack(nums, target, index, subArr):
            if target == 0:
                result.append(subArr.copy())
                return
            if target < 0 or index > len(nums) -1:
                return
            
            current = nums[index]
            subArr.append(current)      
            backtrack(nums, target-current, index+1, subArr)

            subArr.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(nums, target, index+1, subArr)

        backtrack(sorted(nums), target, 0, [])
        return result

test = Solution()
s1 = [1,2,3,4,5]
s2 = [1,2,2,4,5,6,9]
target = 8

print(test.combinationSum2(s2, target))
