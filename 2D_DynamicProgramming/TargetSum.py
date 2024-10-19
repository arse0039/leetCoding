"""
You are given an array of integers nums and an integer target.
For each number in the array, you can choose to either add or subtract it to a total sum.
For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".
Return the number of different ways that you can build the expression such that the total sum equals target.

 target -> [1, 2, 3] -> 4        
                    5     3
                 7   3   5  1
               10    0  8    -2

DFS through each binary decision. When I hit the target value, I return 1. For each node I return the sum
of the left and right decisions. 

can target be negative? yes
can nums be empty?  No! 
"""



class Solution:
    def findTargetSumWays(self, nums:list[int], target:int) -> int:


        def dfs(index, currentSum):
            #bc currentSum == 0 ret 1
            if index == len(nums) and currentSum == target:
                return 1
            if index == len(nums) and currentSum != target:
                return 0

            #left dfs -> ADDED value
            left = dfs(index + 1, currentSum + nums[index])

            # right dfs -> Subtracted value
            right = dfs(index + 1, currentSum - nums[index])
 
            #return left + right
            return left + right

        # return dfs(0, target)
        return dfs(0, 0)
    
nums = [2, 2, 2]
target = 4

test = Solution()
print(test.findTargetSumWays(nums, target))