# Leetcode - 309 - Buy and Sell Crypto with Cooldown - Medium

"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may buy and sell one NeetCoin multiple times with the following restrictions:

After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
You may only own at most one NeetCoin at a time.
You may complete as many transactions as you like.

Return the maximum profit you can achieve.

ex = [1, 7, 2, 5, 8] -> 9

Buy, Sell, Cooldown 
So, we have three options. Cooldown is ALWAYS an option. Buy/Sell is dependent one what we did prior. If our last
event was a buy, we can only sell. If our last event was cooldown, we can only buy. If our last even was sell, we can only cooldown
So, for each index, we can do a DFS from that point, moving forward in the array.
In our dfs, we have to know when to stop our recursion. When we make it to the end of the array, we are done
From here we just need to call dfs again passing in an updated index, which will be +1 for all, and an updated action, and 
an updated profit value.
This one is another tricky one. For all indexes, we know we can do a cooldown action, no matter. What the question then becomes,
can we buy or sell. It is a boolean choice, so we can designate with a boolean value. True means we have bought. False means
we have not. We can ONLY sell if the boolean is true. We can only buy if it is False. If we sell, the only option we have for the
next index is to cooldown it, so we can just skip it all together by moving to index + 2. 
At each index, we will have already calculated values for future operations. In order to avoid doing redundant work, we can store 
those values in a DP. For example, the last index in our example is 8. We really only have two options here. We can CD, which means
our profit is 0 or we can buy, which means our profit is -8. So, if we bought from that index, it is -8 if we have not bought, the max
profit is 0. We can save both values so we don't duplicate work
For the next value, 5, we can skip, but we would just return the values we just calculated, which would the next index without buying (0).
We can then choose to buy at 5. This means our only option at value 8 is to sell. And isBuying is False. So, we would sell, selling at 8 
would mean this index would have a max value of 8. Since 0 + 8 is 8. So now our memo has a max of 0 for isBuying is True and 8 for isBuying is False.


can prices be empty?  NO
can prices be negative? No 0 - 1000
"""

class Solution:
    def maxProfit(self, prices:list[int]) -> int:

        maxProf = 0
        memo = {}
        def dfs(index:int, haveBought: bool):
            nonlocal maxProf
            #BC -> Reach the end of the array index >= len(prices)
            # Already calculated profit for the index with either buying or selling
            if index >= len(prices):
                return 0
            if (index, haveBought) in memo:
                return memo[(index, haveBought)]

            # dfs for CD. index + 1
            # CD is a choice no matter what
            cd = dfs(index + 1, haveBought)

            # dfs for buy -> index + 1, profit - value
            # BUY only if haveBought false
            if not haveBought:
                buy = dfs(index + 1, True) - prices[index]
                memo[(index, haveBought)] = max(cd, buy)
            #dfs for sell -> index + 1, profit + value
            # Only if haveBought is TRUE
            if haveBought:
                sell = dfs(index + 2, False) + prices[index]
                memo[(index, haveBought)] = max(cd, sell)
            
            return memo[(index, haveBought)]
            
        return dfs(0, False)
    
prices = [1,3,4,0,4]
test = Solution()
print(test.maxProfit(prices))