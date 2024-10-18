# LeetCode - - Longest Increasing Subsequence - Medium
# Design
"""
For this problem, we could use a BF approach to iterate through each index
and iterate again from index + 1, counting subsequences and updating a running max total. That is (On^2)
To optimize, we can use a DP approach.
Working backwards, we can determine the maxSubsequence for each index in the array.
We can seed at the final element, which we know will have a count of 1. Acually, ALL elements will have a count of 1 to start with.
Starting from the last index - 1, we can iterate through all indexes ahead of it and check to see if our current value is 
less than the values we are iterating through. If it is, we can update the count in our dpArray but ONLY if the update is larger
than what already exists, since we are lookingfor the MAX subsequence. We can continue this nested loop until we have filled
the entire dpArr array and then return the max value from that array. VOILA! 
TC - O(n * n-1)


can nums be empty? NO. At least 1 value
nums only contains integers? Can they be negative? Yes and Yes
"""

# BF
class Solution:
    def lengthOfLIS(self, nums:list[int]) -> int:
        if len(nums) == 1:
            return 1
        
        dpArr = [1] * len(nums)
        dpArr[len(nums)-1] = 1

        for i in range(len(nums)-2, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dpArr[i] = max(dpArr[i], dpArr[j] + 1)
                
        return max(dpArr)
            

nums = [6, 1, 4, 8, 2, 4, 7]  # 4   
nums2 = [9,1,4,2,3,3,7]
nums3 = [0,3,1,3,2,3]
nums4 = [1] # 1
nums5 = [1, 2] # 2

test = Solution()
print(test.lengthOfLIS(nums5))
