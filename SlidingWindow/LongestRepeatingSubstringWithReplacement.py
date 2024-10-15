# LeetCode - 424 - Longest Repeating Substring with Replacement - Medium 
## I/Os ##
# Input - s - a STRING containing ONLY UPPERCASE ENGLISH LETTERS
# Input - k - an INT representing the number of replacements allowed. 
# Output - INT - The length of the longest substring which contains only ONE distinct character, accounting for k
## Design ##
# "AAABBB" -> k = 2 should return 5
# This problem is asking us to return a substring, which means we probably want to use a sliding window
# approach. We want to INITIALIZE TWO POINTERS, both at the start of the string (0). As long as the RIGHT POINTER
# IS SMALLER THAN THE LENGTH OF S, we want to build our substring. We build it by checking to see if our current value
# at the RIGHT POINTER IS THE SAME AS THE LEFT POINTER. If this is the case, we increase our length count, and update
# our max. If the values are NOT the same, we need to check our count. If the count is smaller than K, then we know we can still
# add the value to the count, move our right pointer, and decrease the count. 
# If the count is equal to K, we know the values don't match and we need to decrement count by 1, and increment our right pointer. 
# Continue on until the loop finishes, and then return our maxLength.
## Constraints##
# Can s be an empty string? No! It will be at least of length 1

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k:int) -> int:
        maxLen = 0
        left, right = 0, 0
        counts = defaultdict(int)
        for char in s:
            counts[char] = 0

        while right < len(s):
            counts[s[right]] += 1
            mostFreqChar = max(counts.values())
            while (right - left + 1) - mostFreqChar > k:
                counts[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right-left + 1)
            right += 1
                
        return maxLen
    

k= 1
test1 = "AAABABB"
test2 = "ABABAAB" # 6
test3= "ABCBCA" # 4

test = Solution()
print(test.characterReplacement(test1, k))