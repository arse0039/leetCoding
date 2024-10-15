# LeetCode - 208 - Implement Prefix Tree - Medium
# For this problem, we want to create a prefix tree, also known as a trie, class.
# A Prefix Trie, or Trie, is a tree data structure that is used for word searches. Each letter is represented
# by a node. And each Node has a list of child nodes that attach to it. When we want to search, we can iterate 
# through the tree, comparing the characters of the word we want to search for to the children of the nodes in the
# trie tree. When a word is added, we can set a boolean flag to alert that it is the end of the word, meaning the search
# function will know that the word was added, and is not just a part of another word.
# This 

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.isEnd = False
        self.children = {}


class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode(char)
            current = current.children[char]
        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        if current.isEnd:
            return True
        else:
            return False
        
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return True

test = PrefixTree()

test.insert('app')
print(test.search('app'))
print(test.search('ap'))
print(test.insert('apple'))
print(test.startsWith('ap'))