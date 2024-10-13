# LeetCode -79 - SearchForWord - Medium
# For this problem, we are tasked with writing a function that receives two parameters:
# board - A 2D array of english letter characters which can be lowercase OR uppercase.
# word - A string the represents the word we are trying to search for. 
# Our goal is to determine whether or not the word argument can be found in the grid via horizontal
# and vertical neighbors. What this means is that we need to explore every letter in the board until
# we find an initial match. If so, we need to check all neighbors for a match for the next letter. If a neighbor
# is a match, we continue.... 
# We can return True if the word is found at any point, otherwise we return false.
# In order to do this, we need need to iterate through the matrix to find the first letter of the word. Once we find the 
# first letter, we can start exploring adjacent letters recursively to see if there is a match. If we get to a point
# where we found all the letters, we can return true back up the recursive chain and voila! 

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rowLen = len(board)
        colLen = len(board[0])
        
        def exploreNeighbors(coord, index, visited):
            row, col = coord
            if index == len(word):
                return True
            if row < 0 or row >= rowLen or col < 0 or col >= colLen:
                return False
            if board[row][col].upper() != word[index].upper():
                return False
            if coord in visited:
                return False
            
            if board[row][col].upper() == word[index].upper():
                visited.append(coord)
                upper = (row - 1, col)
                lower = (row + 1, col)
                left = (row, col - 1)
                right = (row, col + 1) 
                
                res = (exploreNeighbors(upper, index + 1, visited) or
                        exploreNeighbors(lower, index + 1, visited) or
                        exploreNeighbors(left, index + 1, visited) or
                        exploreNeighbors(right, index + 1, visited) )
            
            visited.pop()
            return res

        for i in range(rowLen):
            for j in range(colLen):
                if board[i][j] == word[0]:
                    if exploreNeighbors((i, j), 0, []):
                        return True
        return False
        

test = Solution()

board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAM"

print(test.exist(board, word))



