# LeetCode - - Max Area of Island - Medium
## I/Os ##
"""
Input - grid -> a 2D array that contains strings. Either '0' or '1'
Output - integer -> The maximum area of the islands found within the grid
"""
## Design ##
"""
We are given a 2D array that contains eithre 0 or 1s. 1s means that there is land present, 0 means there is water.
An island is a series of connected pieces of land. To find the max area of of island, we need to first find islands. We need
to ITERATE through the ROWS and COLS until we FIND A 1. When we do and it is NOT a coordinate we have VISITED already, we can
start to do a depth first search of the adjacent areas above, below, left, and right. If they are outside of our bounds, they
have been visited already (we will store visited coordinates) or the value is "0", we can stop. Otherwise, it will be another piece
of land, and we can increment our area count and continue recursively. Once we have finished our recursive calls, we can return the 
values up the chain and update our max value and continue forth until we finish the iteration and can return our max result
"""
## Constraints ##
"""
Can grid be empty? No. It will contain AT LEAST 1 
Are all columns in the grid the same length? Yes
Our 2D array will only contain "1" or "0"?  Correct!
"""
## Examples ##
grid = [
 ["0", "1", "1", "0"],
 ["1", "0", "1", "1"],
 ["1", "0",  "1", "0"]
]
result = 5


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxArea = 0
        rowLen = len(grid)
        colLen = len(grid[0])
        visited = []

        def dfs(row, col):
            if (row < 0 or col < 0 or
                row >= rowLen or col >= colLen or
                grid[row][col] == 0 or (row, col) in visited
                ):
                return 0
            
            visited.append((row, col))
            upper = dfs(row -1, col)
            lower = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)

            return 1 + upper + lower + left + right

        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea = max(maxArea, dfs(row, col))
        
        return maxArea

grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

test = Solution()
print(test.maxAreaOfIsland(grid))