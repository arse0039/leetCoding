# LeetCode 78 - Subsets - Medium
# In this problem we are given an array of integer values and we need to return a list
# of EVERY possible subset of the array. When we see every possible, we should immediately
# start thinking of backtracking and dynamic programming. The best way to think of this is to
# construct a descision tree. For every possible value in the array, we can choose to add it 
# to the subtree we are building, or not add it. From there, we can run the same operations on the 
# next value in the array. We can choose to add it to the existing array or not. This means we can
# use a recursive function to add it and once that function call finishes, we can remove the value from
# subArray and call the function again. The biggest trick with this approach is that our subArray references
# a value in memory, so when we append it to the result and pop/append to it later, it will impact the final
# result array. To overcome this, we need to use the .copy() method to create a copy of the subArray that gets
# placed in the result and voila!


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(nums, index, subArray):
            if index > len(nums)-1:
                result.append(subArray.copy())
                return

            # we add the value and continue
            subArray.append(nums[index])
            dfs(nums, index + 1, subArray)
            # we don't add the value and continue
            subArray.pop()
            dfs(nums, index + 1, subArray)

        dfs(nums, 0, [])
        return result
    
test = Solution()

s1 = [1, 2, 3]
print(test.subsets(s1))