# LeetCode -  - Longest Palindrome Substring - Medium

# Design
"""
Given a string s, return the longest substring of s that is a palindrome.
A palindrome means that both characters on each side are the same.
This means that if we start in the middle of a string, we can calculate the longest palindrome value
for that index. If we hit a point where the letters don't match, we can update that index with the largest
value and store it so we don't redo it. Then we can do the same thing on the right and left indices.
So, we move our left and right pointers until they don't match, then the difference in the indices is the length
of the longest palindrome.
"""
# Constraints
"""
Can s be an empty string? NOPE! At least 1 
Can s contain any characters? NOPE! Just English letters
Can the characters be upper or lower case? Sure can! So Adjust for case!
"""
# Example


class Solution:
    def longestPalindrome(self, s:str) -> str:
        if len(s) == 1:
            return s
        
        maxPal = s[0]
        
        for i in range(len(s)):
            left = i
            right = i
            while left >= 0  and right < len(s) and s[left] == s[right]:
                palLength = right - left + 1
                if palLength > len(maxPal):
                    maxPal = s[left:right+1]
                left -= 1
                right += 1

            
            left = i
            right = i + 1
            while left >=0 and right < len(s) and s[left] == s[right]:
                palLength = right - left + 1
                if palLength > len(maxPal):
                    maxPal = s[left:right+1]
                left -= 1
                right += 1

            
            palLength = right - left + 1
            if palLength > len(maxPal):
                maxPal = s[left+1:right]

        return maxPal
            
s = "ababc"
s2 = "abbc"
s3 = "abb"
s4 = "ac"

test = Solution()
print(test.longestPalindrome(s4))