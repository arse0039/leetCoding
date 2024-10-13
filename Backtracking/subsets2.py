# LeetCode 90 - Subsets 2 - Medium
# Similar to subsets we already solved, this problem tasks us with creating a function that 
# receives and array of integers that are non-unique, meaning there may be duplicates. Our job is return
# a 2D array that contains all possible subsets of the received array WITHOUT any duplication. 
# Similar to the subset problem, we want to use backtracking. How do we know to use backtracking? Because it wants
# ALL possible outcomes. 
# We need to recursively move through each value to build a subset array. The key with duplicates is just that we 
# don't want to add it to the results if it already exists. Otherwise, it is pretty much the same! 
# So, our two choices when building a sub-array are to either use the current value or not and build it moving forward.
# Let's get to work!

class Solution:
    def subsetsWithDup(self, nums:list) -> list[list[int]]:
        result = []
        memo = []

        def backtrack(index, subArray):
            #basecase - if we made to the end of the nums array, we created the subset!
            if index > len(nums)-1:
                srtSub = sorted(subArray)
                if srtSub not in memo:
                    result.append(subArray.copy())
                    memo.append(srtSub)
                return
                
            current = nums[index]
            subArray.append(current)
            backtrack(index + 1, subArray)

            subArray.pop()
            backtrack(index + 1, subArray)

        backtrack(0, [])
        return result


test =Solution()
s1 = [7, 7]
s2 = [1, 2, 1]

print(test.subsetsWithDup(s2))