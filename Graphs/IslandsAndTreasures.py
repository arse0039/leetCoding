# LeetCode - 286 - Islands and Treasures - Medium
## I/Os
"""
Input - grid -> a 2D array of INTEGERS
Output - grid -> a 2D array of INTEGERS that has been transformed or None? 
"""
## Design
"""
For this task we need to look at each indivdual number. We only care if a number is 2147483647. If this is the case, we need
to use a bfs to look at all of the surrounding grids. If a surrounding value is not 2147483647 or -1, then we would update the current
locations value to be 1 + the adjacent value. If the value is -1, we return, since we are at a dead end. If the value is 2147483647, we do
bfs on that value to continue our search through the grid. We also need to track visited coordinates in case the grid is unsolvable. We don't
want to get stuck in a recursive loop!
"""
## Constraints
"""
Can grid be empty? 
Are the puzzles always solvable?
"""
## Example
# grid = [
# [x, -1, 0, x],
# [x, x, x, -1],
# [0, -1, x, x]
# ]

class Solution:
    def islandsAndTreasure(self, grid:list[list[int]]) -> None:
        rowLen = len(grid)
        colLen = len(grid[0])
        visited = []

        def bfs(row, col, count):
            if (row < 0 or col < 0 or
                 row >= rowLen or col >= colLen or
                 (row, col) in visited or
                 grid[row][col] == -1 or
                grid[row][col] <  count
                ):
                return 
            
            visited.append((row, col))
            grid[row][col] = min(grid[row][col], count)
            bfs(row - 1, col, count + 1) # upper
            bfs(row + 1, col, count + 1) # lower
            bfs(row, col - 1, count + 1) # left
            bfs(row, col + 1, count + 1) # right

            visited.pop()

        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == 0:
                    bfs(row, col, 0)

test = Solution()
grid = [
  [0,-1],
  [2147483647,2147483647]
]
test.islandsAndTreasure(grid)