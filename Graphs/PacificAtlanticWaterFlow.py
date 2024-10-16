# LeetCode - 417 - Pacific Atlantic Waterflow - Medium
## I/Os
"""
Input - heights - A 2D array that contains integers which represent sea level heights.
Output - A 2D array of coordinates representing coords that can flow into both the ATL and Pacific
"""
## Design
"""
    Pacific = rows < 0 or col 0
    Atlantic = row >= len(row) OR col >= len(col)
For each value we need to look at the four surrouding values. UPPER and LEFT will move towrds the Pacific.
LOWER and RIGHT will move to the Atlantic. We should have two separate functions to assess these. 
The initial point we are moving from should be the max value. Every height needs to be smaller than that for
water to drain towards the ocean. We can continue searching using BFS if the adjacent values are smaller and 
return true if we end out of bounds. We will do this for both the pacifc and atlantic movements. If both return 
True up the recursive stack, we know that coordinate passes the test and should be added to our results array.
This approach did not work because because some points work for some and not for others.
The updates approach works from the ocean moving backwards. If a value is larger than the value that preceeds it and
that value could reach the ocean, we can work across the rows and columns that are adjacent to the oceans to start. This
is because all of those values will be equal to themselves and equal values can still run off water.
This means we run two loops. One where the column values increment. This means that we can iterate through the TOP row, since
incrementing column values will all connect to the pacific ocean (0, col, PACIFIC, heights[0][col]) as well as the LAST row.
The LAST row borders the Atlantic ocean, (rowLen - 1, col, ATLANTIC, heights[rowLen -1][col]). 
We can run another loop that increments the base on the length of the ROW. 
This means calculating access to oceans using the leftMost column, which borders the pacific : (row, 0, PACIFIC, heights[row][0])
And the furthest column, which borders on the ATLANTIC: (row, colLen - 1, ATLANTIC, heights[row][colLen-1]).
For every point, we can see if it is greater than the previous height it came from, if so, that means it leads to whatever ocean we
are moving to. If it is not, it is outside of the bounds OR we already visited it, we can just stop our recursive loop. 
"""
## Constraints
"""
Are heights positive values? No - Positive only
Can the grid be empty?  No - At least one value
"""
## Examples
"""
grid = [
[2, 4, 7, 6],
[3, 2, 4, 9],
[1, 5, 2, 2]
]
"""

class Solution():
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rowLen = len(heights)
        colLen = len(heights[0])
        canAtl = set()
        canPac = set()
        result = []

        # larger than the length - lower and right
        def dfs(row:int, col:int, ocean:set, height:int) -> bool:
            if ( row < 0 or col < 0 or 
                 row >= rowLen or col >= colLen or
                 (row, col) in ocean or 
                 heights[row][col] < height
                ):
                return
            
            ocean.add((row, col))
            dfs(row + 1, col, ocean, heights[row][col])
            dfs(row - 1, col, ocean, heights[row][col])
            dfs(row, col + 1, ocean, heights[row][col])
            dfs(row, col - 1, ocean, heights[row][col])
            
        # columns change
        for col in range(colLen):
            dfs(0, col, canPac, heights[0][col])
            dfs(rowLen - 1, col, canAtl, heights[rowLen - 1][col])
        
        # rows change
        for row in range(rowLen):
            dfs(row, 0, canPac, heights[row][0])
            dfs(row, colLen - 1, canAtl, heights[row][colLen - 1])

        for point in canAtl:
            if point in canPac:
                row, col = point
                result.append([row, col])

        return result
    

heights=[[1,2,3],[8,9,4],[7,6,5]]


test = Solution()

print(test.pacificAtlantic(heights))
# [1,0],[2,1]]