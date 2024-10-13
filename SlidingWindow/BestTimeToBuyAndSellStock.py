# LeetCode - 121- Best Time to Buy and Sell Stock - Easy
# We are tasked with writing a function that returns the maximum amount of moola we can make
# from buying and selling stonks. The function has one input parameter:
# prices: an array of integers 
# and it returns an integer value that represents the max money we can make.
# Within the array is a window of time that represents when we can make the most money. Making
# money is done by buying low and selling high. The means that we want our window to start at 
# the lowest point, and end at the highest point. This sounds like a great job for our good pal
# sliding window man!
# To solve this, we need to create a sliding window. We create two pointers that are at the same point.
# We will iterate through the array, moving the right pointer if the value is greater than or equal to
# the left pointer value and updating our max value as we go. If the right pointer is SMALLER than our left 
# we need to adjust our window by moving the right pointer to the left and continuing the process.
# once the left pointer has reached the end of the array, we know we are done and we can return the value!
# This algo is O(n) time complexity since our right pointer is always moving and we iterate through each
# value only once. 
# Of note, prices will always contains AT LEAST one value

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0
        
        left = 0
        right = 0

        while right < len(prices):
            currentVal = prices[right] - prices[left]

            if prices[right] >= prices[left]:
                result = max(result, currentVal)
                right += 1
            else:
                left = right
                right += 1
        
        return result

test = Solution()
s1 = [10,1,5,6,7,1]

print(test.maxProfit(s1))

