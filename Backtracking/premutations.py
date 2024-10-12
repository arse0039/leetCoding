# LeetCode - Permutations - Medium
# For this problem we are given an array of values and we are asked to return an 
# array that contains all possible permutations of the array. Because we are asked to
# find ALL possible outcomes, we know that this is a backtracking or DP. Because there is 
# not overlapping work being done, we know that backtracking is the way to go.
# For each value in the array, we can either add it to our permutation array or not.
# if not, we then cycle through every other value once again, adding values to the subarray, only
# if they aren't already in the subarray. All values in the array are guaranteed to be unique! 
# This is another monster time complexity where the number of iterations is based on the length of the array
# The time complexity is something like O(n^n), which is super gross. Ick! Backtracking, amirite?! 

class Solution:
    def permute(self, nums:list) -> list[list[int]]:
        result = []

        def backtrack(nums, index, permArr):
            # basecase - we know we can stop when the subArray has the same len as the nums array
            if len(permArr) == len(nums):
                if set(permArr) == set(nums):
                    result.append(permArr.copy())
                    return
                return
            if index > len(nums) -1:
                return
            
            current = nums[index]
            permArr.append(current)
            
            backtrack(nums, 0, permArr)

            permArr.pop()
            backtrack(nums, index + 1, permArr)
        
        backtrack(nums, 0, [])
        return result


test = Solution()
s1 = [1, 2, 3]
print(test.permute(s1))