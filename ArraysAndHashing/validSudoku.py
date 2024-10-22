"""
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Assume the board contains only integers, 1-9 or empty spaces?
So, we need to check each column to see if it contains a duplicate value. 
We Then need to check each row to see if it contains a duplicate.
Finally, we need to check each 3x3 grid -> Thinking out loud. When we go to do this, we will have already checked these 
When checking the row and column. We can create a hashMap for the 3x3 grids using // 3 for the row and col. If the 
val is already in that grid, we can return False
x 1 2  x x 4  x x 9
4 x x  9 2 1  x x 3
1 x 5  6 x x  7 x x

"""

class Solution:
    def isValidSudoku(self, grid:list[list[int]]) -> bool:
        gridMap = {}
        rowMap = {}
        colMap = {}
        rowLen = len(grid)
        colLen = (len(grid[0]))
         
        for row in range(rowLen):
            rowMap[row] = {}
            for col in range(colLen):
                if col not in colMap:
                    colMap[col] = {}
                if (row//3, col//3) not in gridMap:
                    gridMap[(row//3, col//3)] = {}

                if grid[row][col] != ".":
                    if grid[row][col] in rowMap[row]:
                        return False
                    rowMap[row].update({grid[row][col]: False})
                
                    if colMap[col].get(grid[row][col], 0):
                        return False
                    colMap[col].update({grid[row][col]: True})

                    if grid[row][col] in gridMap[(row//3, col//3)]:
                        return False
                    gridMap[(row//3, col//3)].update( {grid[row][col]: True} )
            
        return True 
                

                
        