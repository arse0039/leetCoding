"""
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Do the strings only contain english, lowercase letters? Correct
Can strings be empty? Yes
Can there duplicate strings? Yes 
Can the entire input be empty? If so, what should our return be? [[]]

The best approach is to iterate through each string in the strs array and sort it.
We can use a hash table to to store the sorted string as the key, with an array that
contains all of the words that are anagrams (their sorted string will match the key). So,
we can iterate through the strings, check if the sorted version is in the hashMap. If not, we 
will create new key:value pair for this sorted string with an array containing the word as the value,
otherwise, we can append the word to the existing array.
This will be a O(n log n) run time since we are sorting the strings at each iteration.
And a O(N) space complexity since we will create a hashTable for each word worst case.
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
        anagramHash = defaultdict(set)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            anagramHash[sortedWord].add(word)
        
        result = []
        for grams in anagramHash.values():
            result.append(list(grams))
        return result
    

strs = ["act","pots","tops","cat","stop","hat"]

test = Solution()
print(test.groupAnagrams(strs))
