# LeetCode - 212 - Word Search 2 - Hard
## Inputs ##
# board - 2D ARRAY of english letter character strings
# words - ARRAY of STRINGS
## Outputs ##
# ARRAY of strings 
## Design ##
# To do a word search, we need to do a backtracking search through the 2D array for each word we 
# want to search for. We could also implement a Trie Datastructure for words that have similar starting sequences. 
# For every word in our words array, we need to do our backtracking function. We will start with the first character
# and iterate through the 2D array until we find a match. Then we can start searching the horizontal and vertical
# values from there, incrementing our index value for the character we are looking for. If the index == the length
# of the word we are searching for, we know we found the word and can return True. If we return true, we can add the word
# to our final result array.
# Searching for the horizontal means looking to the left and right indexes : example[][-1] and example[][+1]
# Searching for the vertical means looking to the upper and lower indixes: example[+1][] and example[-1][]
# so len(boards) will gives us us the number of rows. and len(boards[0]) will give us the number of columns. 
## Constraints ##
# Can the board be empty?  No
# Do we need to account for case? No
# Can words contain empty strings? No. At least a single character


class Solution:
    def findWords(self, board:list[list[str]], words:list[str]) -> list[str]:
        result = set()
        colLen = len(board[0])
        rowLen = len(board)
        visited = []

        def searchNeighbors(word, row, col, index, visited):
            if index == len(word):
                return True
            if row < 0 or row >= rowLen:
                return False
            if col < 0 or col >= colLen:
                return False
            if word[index] != board[row][col] or (row, col) in visited:
                return False
            
            visited.append((row, col))
            res = (searchNeighbors(word, row + 1, col, index + 1, visited) or # Lower
                    searchNeighbors(word, row - 1, col, index + 1, visited) or # Upper
                    searchNeighbors(word, row, col + 1, index + 1, visited) or # Right
                    searchNeighbors(word, row, col - 1, index + 1, visited))   # Left
            visited.pop()
            return res
        
        for word in words:
            for i in range(rowLen):
                for j in range(colLen):
                    if word[0] == board[i][j]:
                        visited.append((i, j))
                        if (searchNeighbors(word, i + 1, j, 1, visited) or # Lower
                            searchNeighbors(word, i - 1, j, 1, visited) or # Upper
                            searchNeighbors(word, i, j + 1, 1, visited) or # Right
                            searchNeighbors(word, i, j - 1, 1, visited)): # Left
                            result.add(word)
                        visited.pop()

        return list(result)

test = Solution()

board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]

words = ["bat", "cat","back", "backend"]

# print(test.findWords(board, words))


## This implementation is testing for using an approach with a Trie DS. It doesn't work. I'll have to come back
# and play around with it!
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}

class Solution2:
    def findWords(self, board:list[list[str]], words:list[str]) -> list[str]:
        root = TrieNode(None)
        result = []
        rowLen = len(board)
        colLen = len(board[0])

        for x in range(rowLen):
            for y in range(colLen):
                if board[x][y] not in root.children:
                    root.children[board[x][y]] = TrieNode(board[x][y])
                current = root.children[board[x][y]]
                self.buildTrie(board, current, x-1, y) # upper
                self.buildTrie(board, current, x+1, y) # lower
                self.buildTrie(board, current, x, y + 1) # right
                self.buildTrie(board, current, x, y - 1) # left

        def dfs(node:TrieNode, word: str, index: int) -> None:
            if index == len(word):
                result.append(word)
                return
            
            if word[index] in node.children:
                current = node.children[word[index]]
                dfs(current, word, index + 1)

            return
            
            
        for word in words:
            dfs(root, word, 0)
        
        return result


    def buildTrie(self, board, current:TrieNode, row:int, col:int):
        rowLen = len(board)
        colLen = len(board[0])

        if row < 0 or col < 0 or row >= rowLen or col >= colLen:
            return
        current.children[board[row][col]] = TrieNode(board[row][col])
        

test = Solution2()

test.findWords(board, words)