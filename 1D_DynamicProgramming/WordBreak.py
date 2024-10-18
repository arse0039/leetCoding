# LeetCode - 139 - Word Break - Medium
# Design 
"""
can s be an empty string? NO. At least one 
can wordDict be empty? No. At least 1 word
words contain english alph chars only? 
are all chars lower/upper case? LowerCase English only

We only care if a word in wordDict is in string. This means we can start at the beginning of the
string and check to see if it contains any of the words in word dict. If it does, we know we only need
to check the remaining substring moving forward. We need to check all paths of because if we have a word
like apple and dict contains app and apple, we could go two different ways. If we get to a point where none of
the words can fit or the length of the dict word is > length of the substring, we can stop. 

My first thought is to use recursion to test all paths. We know we found a valid path when the starting index
is the same as the ending index or length of the string. 
So, we can use a dfs approach, passing indexes to dfs to find substrings and then checking to see if we are at the last index, 
if so, we can return True. Otherwise, we iterate through wordsDict, using the word's length relative to the current
index to create a subString. We can compare the word to the subString and, if they are the same, we can continue into another
recursive call using the length of the found word plus the index. If the recursive chain ever returns True, we can return True. If we make 
it through the wordDict without ever finding a matched word, we can return False. 
To optimize, we can create a memo from specific indexes. If that index returns False, we can return add it to our memo meaning. That means
that if we ever get to that index in the future, we already know the result, so no need to redo the work!
"""

class Solution:
    def wordBreak(self, s:str, wordDict:list[str]) -> bool:
        memo = {}
        def dfs(index):
            if index == len(s):
                return True
            if index in memo:
                return memo[index]
            for word in wordDict:
                wordLen = len(word) 
                strSlice = s[index:wordLen+index]
                if word == strSlice:
                    if dfs(wordLen + index):
                        return True
            memo[index] = False

            return False
           
        return dfs(0)



s = "applepenapple"
wordDict = ["app", "pen", "apple"]

test = Solution()
print(test.wordBreak(s, wordDict))