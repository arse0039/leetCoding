# LeetCode - - Count Paths - Medium
"""
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be 
taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.

Can the grid be 1x1 and, if so, is that considered to be a path (from itself to itself)? Yes. and YES
Can the grid be empty? NOPE
Dynamic Programming -> Bottom-up ->
We KNOW that at the last position, there is only one path. Knowing this, we start at the final grid position
and move backwards through the grid. The number of paths any position can have is equal to the number of paths
available if it moved down or to the right. Since we already calculated these numbers, we can determine the number
of paths at any position by adding the number of paths from the bottom to the number of paths to the right. If the 
number is 0, we can just default to setting the grid space to 1 since we know at LEAST one will always be what belongs
x 1 1
1 5 2
1 2 1
TC - O(m*n) 
"""

#in -> m:int n:int -> RETURN # of possible unique paths
class Solution:
    def uniquePaths(self, m:int, n:int) -> int:
        # create an M x N grid to house th
        grid = [[0 for _ in range(n)] for _ in range(m)]
        colLen = n
        rowLen = m

        # starting in the last row, we can iterate backwards, seeding the number of paths
        # by adding down + right + 1. If it is outside of the bounds, it would return a 0
        for row in range(rowLen-1, -1, -1):
            for col in range(colLen -1, -1, -1):
                right = grid[row][col + 1] if col + 1 < colLen else 0
                down = grid[row + 1][col] if row + 1 < rowLen else 0
                grid[row][col] = right + down if right + down > 0 else 1

        return grid[0][0]    


test = Solution()
m = 3
n = 3
print(test.uniquePaths(m, n))