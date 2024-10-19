# LeetCode - 518 - Coin Change 2 - Medium
"""
You are given an integer array coins representing coins of different denominations 
(e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.
Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.
You may assume that you have an unlimited number of each coin and that each value in coins is unique.
Unbound Knapsack Problem

Can coins array be empty? No. At least one coin
Can it contain negative values?  No
Can target amount be 0 or negative? >= 0

We can use a bottom-up approach to solve this problem. 
First, we Can create a 2D array where the column is of length target in descending order down to 0. So, target + 1
The rows will be of length(coins). The final value in each column should be 1 since there is only one way to make
a value of 0, which is no coins.
iterating through each coin (row) and working backwards through the amounts (col), we can 
"""


class Solution:
    def change(self, coins:list[int], target:int) -> int:
        # create an array len target + 1 and seed them with inf values
        grid = [[0 for i in range(target + 1)] for _ in range(len(coins) + 1)]
        for i in range(len(coins)):
            grid[i][-1] = 1

        for row in range(len(coins)-1, -1, -1):
            for col in range(target -1, -1, -1):
                targ = coins[row] - col
                if targ >= 0:
                    right = grid[row][targ]
                    below = grid[row+1][col]
                    grid[row][col] = right + below

        return grid[0][0]


coins = [1,2,3]
target = 4

test = Solution()
test.change(coins, target)


