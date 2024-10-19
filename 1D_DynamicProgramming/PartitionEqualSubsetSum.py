# LeetCode - 416 - Partition Equal Subset Sum - Medium
# Design 
"""
Equal subsets means that we if we add all the values and divide by two, we will have an integer. Both halves need
to be equal. So FIRST thing, if we sum and divide by two and the value is not even, we know the result is False already!

Otherwise, we need to move through our pairs. We can use dfs to create different combinations. If the combination equals
the half value, we can add it to our result. We can also use a memo to store combinations we have already looked at in order
to reduce redundant calculations. 
So, starting at index 0, we can call DFS. For all nodes ahead of that we can either choose to add them to the running sum
or not. We will also be tracking our indices to create our memo. 
We will add values. If the value is == to our half target, we can add them to a set. 
We can continue doing this until we have created all possible combinations. If our final set has two elements, we know that
we can do the thing! Otherwise, we can't! 

TC - O(2^n)
nums can only contain ints. Can they be negative? NO. Only positive integers
can nums be empty?  No. At least 1 number
"""

class Solution:
    def canPartition(self, nums:list[int]) -> bool:
    
        if sum(nums) % 2 != 0:
            return False
        
        halfSum  = sum(nums) / 2
        goodSums = set()

        indexPath = []
        indexSums = []
        def dfs(index:int) -> None:
            if sum(indexSums) == halfSum:
                goodSums.add(tuple(indexPath))
                return
            if ( sum(indexSums) > halfSum or 
                index >= len(nums) or 
                len(indexPath) == len(nums)
                ):

                return
            
            # we the number
            indexPath.append(index)
            indexSums.append(nums[index])
            dfs(index + 1)

            # we don't include the value
            indexPath.pop()
            indexSums.pop()
            dfs(index + 1)

            return

        dfs(0)
        if len(goodSums) >= 2:
            return True
        return False


# class Solution2:
#     def canPartition(self, nums):
#         if sum(nums) % 2 != 0:
#             return False

#         sumVals = [0]
#         halfSum = sum(nums) / 2
#         for i in range(len(nums)-2, -1, -1):
#             for val in sumVals:
#                 newSum = nums[i] + val
#                 if 
#                 if newSum not in sumVals:
#                     sumVals.append(newSum)         
#         return False

nums = [1, 2, 3, 4] # 10 -> 5

test = Solution()
print(test.canPartition(nums))