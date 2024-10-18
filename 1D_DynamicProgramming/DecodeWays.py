# LeetCode - - Decode Ways - Medium

# Design
"""
The max value a letter can have is 26, meaning two digits. This means we look at two characters at a time
if the two character block ends in a zero, we know it only has one possibility. If it starts with 0, it has 0,
otherwise it has 2 unless the value is greater than 26, then it is just 1 as well
The thing to consider is when we get to the end of the array, when we might only have one single digit left but we can create
logic for if the slice is only of length 1!

Min length of s?  at least one
Can s contain anything other than numeric chars? NO
"""


class Solution:
    def numDecodings(self, s:str) -> int:
    
        memo = {len(s) : 1}

        def dfs(index:int) -> int:
            if index in memo:
                return memo[index]
            if s[index] == '0':
                return 0
            
            res1 = dfs(index + 1)
            res2 = 0

            if index + 1 < len(s) and int(s[index:index+2]) <= 26:
                res2 = dfs(index + 2)
            
            result = res1 + res2
            memo[index] = result
            return result
        
        return dfs(0)
    
test = Solution()
s1 = "12" # 2
s2 = "1228" #
s3 = "101"
test.numDecodings(s1)

        

       





