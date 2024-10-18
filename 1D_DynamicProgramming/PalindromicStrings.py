# LeetCode - 647 - Palindromic Strings - Medium 

# Constraints
"""
What is the min length of s? 1
What kind of characters can s contain? lowercase English
Do we need to account for case? No
Can we use repeated palindromes? 
"""
# Design
"""
We receive a string, s. We need to find palindromes, which are srings that are the same forward as 
they are backwards. 
We need to iterate through each index, looking for substrings. The index we start at will be treated
as the middle point, and we will work left and right from there. With palindromes, we need to account for
palindromes of even lengths and palindromes of odd length because the middle index will be different in each case.
We will use a while loop from each index with two pointers. If the letters at the pointers match, we have a palindrome
and can continue looking at the next left and right indices, so we will update our left and right pointers by 1. 
Each time the while loop evaluates to true, we know we found a palindrome and we can append it to an array. Once the 
while loop finishes, we know we hit a non-palindrome and can move on to calculating the even version
"""

class Solution:
    def countSubstrings(self, s:int) -> int:
        if len(s) == 1:
            return 1
        
        subStr = set()

        for i in range(len(s)):

            # odd palindromes
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                subStr.add((s[left:right+1], left, right))
                left -= 1
                right += 1
            
            # even palindromes
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                subStr.add((s[left:right+1], left, right))
                left -= 1
                right += 1
            
        return len(subStr)


ex1 = "abbc" # 5
ex2 = "ababc" # 7
ex3 = "abb" # 4
ex4 = "ab" # 2

test = Solution()
print(test.countSubstrings(ex4))