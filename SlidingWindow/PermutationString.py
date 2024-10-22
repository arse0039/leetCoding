"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Input: s1 = "abc", s2 = "lecabee"
"aaabc"
 aabc

Can s1 or s2 be empty? Yes

A substring is a continuous string of characters within another string. The permutations of all
versions of a string are all the versions of that string that can be built from the characters in that string
So, n!  Because we only care if a version exists or not, we can work with one easy permutation, which is
the string in sorted order. If we sort both s1 and s2, finding the version of the string will be much easier.
Starting wth s2, we can compare the characters at s1[0] and s2[0].If they match, we can increase the window of the 
s2 and increment our pointer in s2 to look at the next character. If the pointer on s1 becomes >= len(s1), we know we found
a match. If we get to a point that doesn't match, we need to move our left pointer forward until it matches s1[0] or
until it == right. Then we can start the process over again
If our window never matches, the loop will break, and we can return False. 

"""

class Solution:
    def checkInclusion(self, s1:str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))
        
        for i in range(len(s2)):
            substr = s2[i:i+len(s1)]
            sortedSub = ''.join(sorted(substr))
            if sortedSub == s1:
                return True
            
        return False

test = Solution()
s1 = "abc"
s2 = "lecabee"

test.checkInclusion(s1, s2)

