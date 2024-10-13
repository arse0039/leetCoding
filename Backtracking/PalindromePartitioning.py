# LeetCode - 131 - Palindrone Partitioning - Medium
# For this problem, we are given an array of strings, 's', and we are tasked with
# creating a function that returns a list of every substring that can be made from the
# string that is also a palindrome. 
# To solve this problem, we must first find all possible substrings. Once we do that, we can iterate
# through each substring to determine if it is a palindrome or not. 
# Because we need to find every substring to start, we know we need to use a backtracking approach
# So, we recursively move through each letter, building substrings, and placing them into a substring 
# array. To build a substring, we can either add a letter to the substring, or not, meaning that for each letter
#, we have two possible actions - add or not!
# Because we are using recursing, this approach allows us to build all possible substrings!

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        partition = []

        def findSubstrings(index):
            if index >= len(s):
                result.append(partition.copy())
                return
            
            for i in range(index, len(s)):
                if self.isPalindrome(s, index, i):
                    partition.append(s[index:i+1])
                    findSubstrings(i + 1)
                    partition.pop()
            
        findSubstrings(0)
        return result


    def isPalindrome(self, string, left, right):
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True         

        
test = Solution()
s1 = "aab"

print(test.partition(s1))