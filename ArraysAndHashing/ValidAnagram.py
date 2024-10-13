# LeetCode - 249 - Valid Anagram - Easy
# For this problem, we need to write a function that checks to see if two strings are anagrams
# of one another. The function has two parameters:
# s - string
# t - string
# and returns a boolean: True if they ARE anagrams of one another and FALSE if they are not. 
# In order to be an anagram, the two strings must have the same characters as one another.
# There are multiple ways to approach this problem. For an O(n log n) approach, we can sort both strings
# and compare the strings. If they are the same, we return True. But let's do better and create an O(n)
# approach. To do this, we can create hashmaps for each string. We can iterate through each value in string1, 
# increasing the count of the hashMap value. We can do the same for string2. Finally, we can compare the
# two hashMaps to see if they are the same. 
# Of note: We do not need to account for case in this problem!


class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        sHash = {}
        tHash = {}

        for char in s:
            if char in sHash:
                sHash[char] += 1
            else:
                sHash[char] = 1
        
        for char in t:
            if char in tHash:
                tHash[char] += 1
            else:
                tHash[char] = 1
        
        if sHash == tHash:
            return True
        else:
            return False

test = Solution()
s1 = "racecar"
s2 = "caracew"

print(test.isAnagram(s1, s2))