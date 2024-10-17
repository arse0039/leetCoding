# LeetCode - 127 - Word Ladder - HARD
# IO
"""
Input - beginWord - a string that denotes the word we are starting with
Input - endWord - a STR that denotes the word the want to end with
Input - wordList - an ARR of STRS. A list of words that we can use to transition to
Output - INT - The number of transitions it took to create the endWord
"""
# Design
"""
For this to work we need to create hashMap for all versions of each word. 
If a word has 3 chars then it has 3 different versions - ex cat -> *at, c*t, ca*
We need to iterate through EVERY word and create maps of these versions, with an array of words that match
those words. 
Once we do this, starting with beginWord, we could BFS to get our result. Using a deque, we add the beginWord
to the deque and continue for as long as there is something in the deque. For each version of the current word, we 
check to see if it is in the hashMap. If it is, we can add all the words in that array to the queue as long as 
we have no already visited that word. We can also pass along a count along with that word. We continue doing this, 
popping words off of our deque until we find a word that matches the endWord. Once that happens, we can return the count
value associated with that word. If we iterate through every word, our deque will eventually be empty. If this is the case,
we can return 0.  
"""
# Constraints
"""
Are all words guaranteed to be of the same length? YES
Are all the words in the wordList unique?  YES
Is the endWord guaranteed to be in the wordList? NO
"""
# Example
beginWord = "cat"
endWord = "sag"
wordList = ["bat","bag","sag","dag","dot"]
Output: 4

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord:str, wordList: list[str]) -> int:
        
        wordLen = len(beginWord)
        hashMap = {}

        if endWord not in wordList:
            return 0

        for word in wordList:
            for i in range(wordLen):
                wordCopy = list(word)
                wordCopy[i] = '*'
                wordCopy = ''.join(wordCopy)
                if wordCopy not in hashMap:
                    hashMap[wordCopy] = [word]
                else:
                    hashMap[wordCopy].append(word)

        visited = set()
        dq = deque([(beginWord, 1)])

        while dq:
            currentWord, count = dq.popleft()
            visited.add(currentWord)

            if currentWord == endWord:
                return count

            for i in range(wordLen):
                wordCopy = list(currentWord)
                wordCopy[i] = '*'
                wordCopy = ''.join(wordCopy)
                if wordCopy in hashMap:
                    for changeWord in hashMap[wordCopy]:
                        if changeWord not in visited:
                            dq.append((changeWord, count + 1))
                
        return 0
    
beginWord="a"
endWord="c"
wordList=["a","b","c"]
test = Solution()
print(test.ladderLength(beginWord, endWord, wordList))