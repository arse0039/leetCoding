# LeetCode 39- Combination Target Sum - Medium
# For this problem we must write a function that receives an array of ints
# and a target value (int). The goal is to return ALL combination of numbers 
# that sum to the target value using the values found within the nums array.
# We can use values an unlimited number of times! 
# Because we want to 
# This means that for each value, we can either subtract it from the target value or not
# We can then pass this new target value and repeat the process. With each subtracting, we also build
# an array of values as these are the values that potentially add up to give us our answer.
# If the target value is 0, we know we found a good sum and we can add it. If it is < 0, we went to far!
# The approach is to use a recursive function to build all possible outcomes! 
# Let's get to coding!!
# The time complexity for this is pretty awful. It's O(n * n-1 * n-2 * n-3) based on the target value. So O(n^t) OOF!

class Solution:
    def combinationSum(self, nums: list, target: int) -> list[list[int]]:
        result = []

        def backtrack(target, index, sumArray):
            # basecase 1 - it works!
            if target == 0:
                result.append(sumArray.copy())
                return
            if target < 0 or index > len(nums)-1:
                return
            
            currentVal = nums[index]
            sumArray.append(currentVal)
            backtrack(target-currentVal, index, sumArray)
            sumArray.pop()
            backtrack(target, index+1, sumArray)
        
        backtrack(target, 0, [])
        return result

test = Solution()
s1 = [2, 5, 6, 9]
s2 = [3, 4, 5]
s3 = [3]
target = 5
print(test.combinationSum(s3, target))