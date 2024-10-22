"""
Given an integer array nums, return an array output where output[i] is the product of all 
the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O (n)
O(n) time without using the division operation?

Example - [2, 4, 1, 5]
    left  [1  2  ]
    right  [20  5  5  1]      
          [20  10 40 8] 
Naive Approach -> Use two loops to loop through the array twice, ignoring when the index counter
is the same, adding the final product to the same index to a results array. This would be O(n^2)

O(n) approach -> We know that the product at a given index including itself is the product of all
the values on the right of the given index multiplied by the product of all the values on the left.
What if we created two arrays, one that help the left products for each index, and another that held
the right products. We could then loop through these arrays once, multiplying the values of the left
and right to fill the final array. The space complexity is O(3n) but the TC would be O(n)
"""

class Solution:
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        #create right product, left product, and result arrays
        rightProd = [1] * len(nums)
        leftProd = [1] * len(nums)
        result = []

        if len(nums) == 1:
            return [0]
        
        # seed our rightPrd array
        for i in range(len(nums)-2, -1, -1):
            rightProd[i] = nums[i + 1] * rightProd[i+1]

        for j in range(1, len(nums)):
            leftProd[j] = nums[j - 1] * leftProd[j-1]

        for k in range(len(nums)):
            result.append(rightProd[k] * leftProd[k])
        
        return result

