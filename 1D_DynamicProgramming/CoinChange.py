# LeetCode - 322 - Coin Change - Medium
# Design
"""
For this problem, we need to use a 1-D Dynamic Programming approach. Specifcally, a bottom-up
approach. This is because we need to calculate the fewest number of coins needed for the smallest amounts first, 
which we can store in an array of size 0 - amount + 1.
So, let's create a 1D array first. This array will be seeded with values one larger than the amount we are given. This ensures
that we will be able to return -1 by checking to see if dpArr[amount] is larger than amount. This means there were NO minimum values
available to make change for it. We can also set dpArr[0] to zero since we know that no coins are needed to add up to 0.
We can then loop through our DP Array of amounts, starting at index 1 (since we are calculating the number of coins needed to create 
change for 1 cent). Using the index, we can then loop through our coin values. We can subtract the coin value from the index. If it is >= 0,
then we know we already have calculated the number of coins needed since we are working from the bottom up! We can then update the value
at that index to be the minumum if itself OR the value at the remaining value index + 1, since we would be adding the minimum number of coins
needed for the remaining value and simply add one more coin to it. We continue doing this for each coin, so that index will end up
with the FEWEST number of coins needed to make change for it. We do this for EVERY index up to the amount. Once we build this DP array, we can
return the value at dpArr[amount]. If it is larger than amount we return -1 instead!
find the MINIMUM number of coins needed. 

coins contains only positive values? CORRECT
can amount be zero? YES

TC - O(n * m) where n is amount and m is len(coins!)
"""


class Solution:
    def coinChange(self, coins:list[int], amount:int) -> int:
        if amount == 0:
            return 0
        
        dpArr = [amount + 1 for _ in range(amount + 1)]
        dpArr[0] = 0

        for i in range(1, len(dpArr)):
            for j in range(len(coins)):
                remaining = i - coins[j]
                if remaining >= 0:
                    dpArr[i] = min(dpArr[i], dpArr[remaining] + 1)
                
        return dpArr[amount] if dpArr[amount] <= amount else -1
                
        
            




s1 = [1, 5, 10]
s2 = [20]
s3 = [2, 3]
amount = 11
test = Solution()
print(test.coinChange(s2, amount))