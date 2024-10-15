# LeetCode - - Count Number of Islands - Medium
## I/Os ##
"""
Inputs: 
 grid - a 2D ARRAY that contains either a "0" or a "1".
Outputs:
 An INTEGER representing the total number of islands in our grid
"""
## Design ##
"""
We are given a 2D array that contains strings that are either "0" or a "1". A "0" represents water
and a "1" represents land. When 1s are next to one another, they represent a contiguous body of land, aka 
an island! We want to count the total number of islands and return that number. Starting at the first value in the
grid, we want to iterate through every value in every row. If it is a one, we know that we need to do a depth first search.
What that means is that we look at all adjacent values (upper, lower, left, right) to see if the are a 1 or not. Because we found
a 1, we can increase our island count. From here, we only care about marking adjacent 1s as being coordinates we can't visit again,
since they are a part of the same island. We can end our search whenever we reach a 0. From here, we continue our loop, checking
to see if the coordinate has been visited already. If so, that means we already counted it. If not, it's a new island! 
"""

## Examples ##
"""
[0, 1, 1, 0]
[1, 0, 0, 1]
[1, 1, 0, 1]
result = 3
"""

## Constraints ##
"""
Can our grid be empty?  No. It will always contain at least 1 row
The grid is guaranteed to only contain 0s and 1s?  Correct
All arrays within grid will be of the same length? Correct
"""

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        result = 0
        rowLen = len(grid)
        colLen = len(grid[0])

        visited = []
    
        def dfs(row:int, col:int) -> None:
            if ((row, col) in visited or 
            row < 0 or col < 0 or
            row >= rowLen or col >= colLen or
            grid[row][col] == "0"
            ):
                return

            visited.append((row, col))
            dfs(row + 1, col) # lower
            dfs(row - 1, col) # upper
            dfs(row, col + 1) # right
            dfs(row, col - 1) # left

        for row in range(rowLen):
            for col in range(colLen):
                if grid[row][col] == "1" and (row, col) not in visited:
                    result += 1
                    dfs(row, col)
        
        return result
    
grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
result = 3

test = Solution()
print(test.numIslands(grid))