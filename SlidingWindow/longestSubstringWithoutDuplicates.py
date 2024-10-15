# LeetCode - 3 - Longest Substring Without Duplicates - Medium
# For this problem, we must write a function that tells the user the longest
# substring contained within a string while accounting for duplicate characters
## Inputs and Outputs ##
# This function accepts one parameter:
# s - A string of characters - any possible printable ascii characters
# And it returns an integer -> The maximum length of a possible substring with no dupes
##  Design ##
# Looking for the longest substring, which means that we want to use a sliding window approach to
# build the substring. This means using two pointers, which both start at the begining of the string
# with the right pointer moving as long as it is pointing at a char that we have not yet seen.
# To track seen characters, we can store them in an array of seen chars. 
# While growing the subString, we should be calculating a new max value each time and storing it
# If we get to a visited character, that means we have reached the max length for that subString and 
# we need to remove a character, which means moving our left pointer. 
# Once the right pointer has reached the length of the received string, we can stop and return our max value!
# Constraints:
# Can s be an empty string: Yes
# Examples - "ssss"
# 

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0

        right = 0
        left = 0
        visited = deque([])

        while right < len(s):
            if s[right] not in visited:
                visited.append(s[right])
                maxLen = max(maxLen, len(visited))
                right += 1
            else:
                visited.popleft()
                left += 1
        
        return maxLen

test1 = "222" 
test2 = "abcbcga"

test = Solution()

print(test.lengthOfLongestSubstring(test2))