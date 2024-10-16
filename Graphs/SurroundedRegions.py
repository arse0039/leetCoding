# LeetCode - 130 - Surrounded Regions - Medium:
## I/Os 
"""
Inputs - board - 2D array that contains string chars. Either 'X' or 'O'
Outputs - NONE -> Updating board. 
"""
## Design
"""
First, we need to find our 'O' characters. We need to iterate through our matrix until we find a 'O'. Once we 
find a 'O' we need to figure out if it is surrounded. This means checking in all directions. For example, to check
above, we need to move up until we hit an 'X'. If we reach the outer bounds, we know we have not so we can return False 
down a recurive chain. If we hit an X, that means it IS surrounded above and we can return True. We need to do recursive
calls in all 6 directions. If they all return True, we know the node is surrounded and we can update it to be an 'X' and move to 
the next coordinate in our matrix. 
I misunderstood the problem. A group of 'O's is considered surrounded if EVERY O within that group is considered surrounded. Surrounded
means it has an X above, below, left and right. if a single O within a group is NOT surrounded, none of them will be. This means that we
can NOT use BFS from a 'O', we need to first identify nodes that we KNOW are NOT surrounded and mark them. From there, we can mark any adjacent
'O' as not surrounded and continue doing that, updating the board.
Once complete, we can iterate through the board changing all O's to X's, and all the nodes marked as unsurrounded as Os again!
"""
## Constraints
"""
Because we are modifying the board, there are no constraints to consider. 
"""
## Example
board=[
    ["O","X","X","O","X"],
    ["X","O","O","X","O"],
    ["X","O","X","O","X"],
    ["O","X","O","O","O"],
    ["X","X","O","X","O"]
    ]

class Solution:
    def solve(self, board:list[list[str]]) -> None:
        rowLen = len(board)
        colLen = len(board[0])

        def dfs(row: int, col:int) -> None:
            if ( row < 0 or col < 0 or 
                row >= rowLen or col >= colLen or 
                board[row][col] != 'O'
                ):
                return
            
            board[row][col] = "#"

            dfs(row + 1, col) # lower
            dfs(row - 1, col)  # upper
            dfs(row, col + 1)  # right
            dfs(row, col - 1)  # left

        # search outer rows for unsurrounded points
        for cols in range(colLen):
            if board[0][cols] == 'O':
                dfs(0, cols)
            if board[rowLen - 1][cols] == 'O':
                dfs(rowLen -1, cols)
        
        # search outer cols for unsurrounded pointers
        for row in range(rowLen):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][colLen-1] == 'O':
                dfs(row, colLen - 1)

        # iterate through the board now and update all O's to X's and # back to O's
        for row in range(rowLen):
            for col in range(colLen):
                if board[row][col] == "#":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"


        print(board)
test = Solution()
test.solve(board)