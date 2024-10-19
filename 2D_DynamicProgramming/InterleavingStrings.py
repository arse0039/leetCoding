# LeetCode - - Interleaving Strings - Medium
"""
You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met

|n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...

can either s1 or s2 be empty? at least 1 in each
is s3 guaranteed to be len s1 + s2? no
can s3 be empty? No. At least 1 character
are all characters the same case? yes. All lowercase English

s1 = ab
s2 = ab
s3 = abab

So, we can start with the s3 and run dfs on it, first letters from each string. If the letters
match, we will do a dfs, shrinking the one that matches. If they don't match, we can return False
If we get to a point where s3, s2, and s1 are all empty, we know we formed the s3 and can return True

"""

class Solution:
    def isInterleave(self, s1:str, s2:str, s3:str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        memo = {}

        def dfs(sub1, sub2, sub3):
            # bc if len sub3, sub2 and sub1 are all 0
            if len(sub3) == 0 and len(sub2) == 0 and len(sub3) == 0:
                memo[(sub1, sub2, sub3)] = True
                return True
            if (sub1, sub2, sub3) in memo:
                return memo[(sub1, sub2, sub3)]

            # if sub1[0] matches sub3, do dfs with sub1. Pass slices [1:] for both
            if sub1 and sub3[0] == sub1[0]:
                oneWay = dfs(sub1[1:], sub2, sub3[1:]) 
            else: 
                oneWay = False

            # if sub2[0] matches sub3, do dfs with sub2. Pass same slices
            if sub2 and sub3[0] == sub2[0]:
                secondWay = dfs(sub1, sub2[1:], sub3[1:])
            else:
                secondWay = False
            
            memo[(sub1, sub2, sub3)] = oneWay or secondWay
            return oneWay or secondWay

        return dfs(s1, s2, s3)

