# LeetCode - - Min Cost Climbing Stairs - Easy
#IO
"""
Input - cost ARR(INT) -> Each INT corresponds to the cost it takes to land on that step.
Output - the MIN cost needed to traverse the stairs:
"""
# Design
"""
We can start at either index 0 or index 1. 
From the start positions, we can either move ahead by 1 index or ahead by 2 indexes. We need to keep moving this way
until we move past the final step, aka we are outside the bounds of our array, cost.
In order to avoid duplicating work, we need to track the minimum cost for each node, using DFS to move back up the recursive
tree, updating our memo as we go for each index. 
We will recursively call our function using n-2 or n-1 since starting at the top of the stairs is the best approach!
"""
# Constraints
"""
Can costs be negative?  NO
Can the number of steps be 0 or 1? No. At least two steps
"""
# Example
cost = [1, 2, 1, 4, 5]

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        memo = [None] * len(cost)
        

        def helper(index):
            if index >= len(cost):
                return 0
            if memo[index]: 
                return memo[index]
        
            left = helper(index + 1)
            right = helper(index + 2)
            
            memo[index] = min(left, right) + cost[index]
            return memo[index]
        
        helper(0)
        return min(memo[0], memo[1])


class Solution2:
    def minCostClimbingStairs(self, cost):
        for i in range(len(cost)-1, -1, -1):
            oneJump = cost[i] + cost[i + 1] if i + 1 < len(cost) else cost[i]
            twoJump = cost[i] + cost[i + 2] if i + 2 < len(cost) else cost[i]
            cost[i] = min(oneJump, twoJump)
        
        return min(cost[0], cost[1])


test = Solution()
test2 = Solution2()

print(test2.minCostClimbingStairs(cost))
            


