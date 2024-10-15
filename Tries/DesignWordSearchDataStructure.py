# LeetCode - 211 - Design Word Search Data Structure - Medium
# For this problem, we are tasked with creating a data structure for managing a word search dictionary.
# This Data Structure needs to support users adding words to the dictionary and search for words
## Inputs & Methods ##
# Inputs - None
# addWord() - This method allows users to add words to our data structure. 
# It accepts a single parameter, 'word', which is a STRING. 
# It has no return value
# searc() - This method allows the user to search the data structure for a word or parts of a word. It 
#  accepts a single paramater, 'word, which is a STRING. 
# It returns a BOOLEAN. True if the search is a match, False if there is no match. 
## Design ##
# We need to use a OOP approach. Our WordDictionary class with use a Trie Data Structure to handle storage of
# letters. We will need our WordDictionary class to have a ROOT NODE that is the starting point for all searches.
# TrieNodes will be there own separate class. Every Trie will have a character, a dict for child nodes, and a boolean
# to denote if a letter represents the end of a word or not.
# This biggest challenge here is that users can use '.'s to denote any letter. This means that we will need to do a DFS from every node
# until we have found a match, and return True up the recursive call stack. 
## Example ##
# add Dog Add Hog Search Dog Search .og search ho.
## Constraints ##
# Will the added words and searched words always contain a letter? Yes at least 1

class TrieNode:
    def __init__ (self, char):
        self._char = char
        self._isEnd = False
        self._children = {}


class WordDictionary:
    def __init__ (self):
        self._root = TrieNode(None)
    
    def addWord(self, word:str) -> None:
        current = self._root
        for char in word:
            if char not in current._children:
                current._children[char] = TrieNode(char.lower())
            current = current._children[char]
        current._isEnd = True

    def search(self, word:str) -> bool:
        current = self._root
        return self.dfs(current, word, 0)
            
    
    def dfs(self, current:TrieNode, word: str, index: int) -> bool:
        for i in range(index, len(word)):
            currChar = word[i]
            if currChar == ".":
                for node in current._children.values():
                    if self.dfs(node, word, i + 1):
                        return True
                return False
            elif currChar in current._children:
                current = current._children[currChar]
            else:
                return False
        return current._isEnd
            

wordSearch = WordDictionary()
wordSearch.addWord('application')
wordSearch.addWord("appreciation")
print(wordSearch.search("app........n"))
 