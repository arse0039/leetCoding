# Leetcode - 152 - Maximum Product Subarry - Medium
# Design 
"""
We are given an array of int and we need to find the MAX product from subarrays within
this array. 
Brute force would be to iterate through each integer.
And from that integer, loop through every integer from index until the end, calculating subarray products
at each step and updating the max. This would be an O(n^2) TC approach. 

nums -> Can contain negative integers? YES 
nums -> Can it be empty? No! At LEAST one value
"""

class Solution:
    def maxProduct(self, nums:list[int]) -> int:
        result = float('-inf')

        for i in range(len(nums)):
            result = max(result, nums[i])
            runningMax = nums[i]
            for j in range(i+1, len(nums)):
                runningMax *= nums[j]
                result = max(result, runningMax)
            
        return result

"""
Another option would be to use a DP approach. This is because, for a value at any index, the product is the product of it's preceeding
index. So, instead of having to loop through the ENTIRE array twice, we can loop through it once, keeping track of the previous product up
until that point.
The issue is that negative numbers can inverse things. This means that an index may have a negative product value and a positive product.
For each index we need to store both it's negative value and it's positive value. What this really means is that we are going to store the 
index's original value as well as it's product if the product is the opposite signage. Another way to think about it is that we need to
store the smallest value and the largest value for that index. The max value can either be itself, the value of the pos*pos or the value of neg*neg.
The min value can be itself, neg*neg or pos*pos. 
We can then move to the next index, multplying that value by the positive value and the negative value, updating as we go and storing the MAX value
we find as we go (which will be the positive value since it will always hold the largest value. SHEW!! DP IS TOUGH!!!!
"""

class Solution2:
    def maxProduct(self, nums:list[int])-> int:
        if len(nums) == 1:
            return nums[0]
    
        result = float('-inf')
        prevPos = nums[0]
        prevNeg = nums[0]

        for i in range(1, len(nums)):
            curPos = prevPos * nums[i]
            curNeg = prevNeg * nums[i]
            prevPos = max(curPos, nums[i], curNeg)
            prevNeg = min(curNeg, nums[i], curPos)
            result = max(result, prevPos)

        return result


t1 = [1, 2, -3, 4]
t2 = [-1, -3, -4]
t3=[2,3,-2,4]
test2 = Solution2()
print(test2.maxProduct(t3))

        