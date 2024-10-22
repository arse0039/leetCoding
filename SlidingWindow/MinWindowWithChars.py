"""
Given two strings s and t, return the shortest substring of s such that every 
character in t, including duplicates, is present in the substring. If such a substring 
does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
"""

class Solution:
    def minWindow(self, s:str, t:str) -> int:
        needMap = {}
        haveMap = {}
        haveCount = 0
        needCount = len(t)
        res = 0

        for i in range(len(t)):
            haveMap[t[i]] = 0
            if t[i] not in needMap:
                needMap[t[i]] = 1
            else:
                needMap[t[i]] += 1
        
        left = 0 
        right = 0

        while right < len(s):
            
            while haveCount < needCount:
                if s[right] not in needMap:
                    right += 1
                elif s[right] in needMap:
                    haveMap[s[right]] += 1
                    if haveMap[s[right]] == needMap[s[right]]:
                        haveCount += 1
            
            res = max(res, right - left)

            while haveCount == needCount:
                targ = s[left]
                haveMap[targ] -= 1
                if haveMap[targ] < needMap[targ]:
                    haveCount -= 1
                else:
                    left += 1
                    res = max(res, right - left)
            
        return res
            