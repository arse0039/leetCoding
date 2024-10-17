# LeetCode - 70 - Climbing Stairs - Easy
# IO
"""
Input - n INT -> Total number of stairs we can climb
Out - INT -> The number of distinct ways to climb the stairs
"""
# Design
"""
We can work backwards from n because we know we climbed every stair when we get to 0. 
From each stair, we can either take two steps or one step. However, when we draw out the decision
tree, we see that we have duplicated paths. We do NOT want to count those twice. That's what makes this a DP
question. We need to store our visited values in a memo. I liked to use a dict since it is O(1) lookup!
We can use recursion to take both paths, both -1 and -2 steps. If we have visited that step before, that means we already
calculated the number of steps from that point. We can return the value stored in our memo.
Otherwise, we keep going until we hit a 0. That counts as a path, so we can return 1. We pass up all valid paths, adding
them as we go until the recursive tree is done. Then that's the total number of paths!
"""
# Constraints
"""
Can n be a negative number? NO
Can n be 0? Yes
"""
# Examples
n = 4 # Output = 4

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        visited = []
        def helper(n):
            if n in memo:
                return memo[n]
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            visited.append(n)
            left = helper(n-1)
            right = helper(n-2)

            solved = visited.pop()
            memo[solved] = left + right

            return left + right
        
        return helper(n)
        
test = Solution()
print(test.climbStairs(4))


