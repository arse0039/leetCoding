"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Does the string contain all english, lower-case letters? No. Can be upper or lower can contain spaces. Can contain any ascii char.
can s be empty? If so, is an empty string considered a palindrome? Yes and yes

So, we know that palindrome has to have matching characters. This means they match starting
from the middle and working out, but that means we have to account for even/odd length strings
OR they are the same from the ends working in. Because we ONLY care if a single string is a palindrome,
the easiest approach is to start at the ends and work our way inward. This means we need to use a two-pointer
approach, which will give us an O(n) TC and an O(1) space complexity

ex - racecar T
ex - "" T
ex - "a" True 
ex "ab" False
ex - "racecir"
ex - "race car" TRUE
ex -  "race#car" 
"""

class Solution:
    def isPalindrome(self, s:str) -> bool:
        left = 0
        right = len(s) - 1

        while right > left:
            if s[right] == " " or not s[right].isalnum():
                right -= 1
            elif s[left] == " " or not s[left].isalnum():
                left += 1
            elif s[right].lower() != s[left].lower():
                return False
            else:
                right -= 1
                left += 1
        
        return True

s="tab a cat"
test = Solution()
test.isPalindrome(s)