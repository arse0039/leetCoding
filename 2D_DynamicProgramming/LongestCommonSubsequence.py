# LeetCode - Longest Common Subsequence - Medium
"""
Given two strings text1 and text2, return the length of the longest common subsequence between the 
two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or 
no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
A common subsequence of two strings is a subsequence that exists in both strings.

Can either of the strings be empty? No. At least 1 char
Strings only contain english chars? Correct
Do we need to adjust for case at all? No

When looking for a subsequence, we are comparing two different subStrings. If we cycle through a character
in each subString, we know that we are essentially, shortening the substring that we are looking at.
We can think of this as creating a 2D Grid.  Each value in the grid represents the length of the substring
that can be created from that portion of one substring relative to the other. When we find a matching 
letter, we can take the diagnal value and add one to it. Who knows. Just memorize this one!
  c  a  t 
r 3  2  1   
c 3  2  1
a 2  2  1
t 1  1  1 
b 0  0  0

"""

class Solution:
    def longestlongestCommonSubsequence(self, text1:str, text2:str) -> int:
        rowLen = len(text1)
        colLen = len(text2)

        grid = [[0 for _ in range(colLen+1)] for _ in range(rowLen + 1)]

        maxRes = 0

        for row in range(rowLen -1, -1, -1):
            for col in range(colLen -1, -1, -1):
                down = grid[row+1][col] 
                right = grid[row][col+1]
                diag = grid[row+1][col + 1]
                if text1[row] == text2[col]:
                    grid[row][col] = 1 + diag
                    maxRes = max(maxRes, grid[row][col])
                else:
                    grid[row][col] = max(down, right)
                    
        
        return grid[0][0]


text1 = "crab"
text2 = "cratcarab"

test = Solution()
print(test.longestlongestCommonSubsequence(text1, text2))