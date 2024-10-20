# LeetCode - 329 - Longest Increasing Path in Matrix - HARD
"""
You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.
Return the length of the longest strictly increasing path within matrix.
From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.

5 3 5
2 6 8
9 0 9

# memo to stored max values for each [row][col]
# dfs

Can the grid be empty?  No. At least 1x1
"""

class Solution:
    def longestIncreasingPath(self, grid:list[list[int]]) -> int:
        # memo to store max values (row, col)
        memo = {}
        rowLen = len(grid)
        colLen = len(grid[0])

        # dfs
        # visited list for storing visited indices so we don't go back

        visited = []
        def dfs(row:int, col:int, prevVal) -> int:
            # base case  if current val at the index is smaller or equal to prevVal
            # or we are outside of the bounds return 1 or indices already visited ret 0
            if (row < 0 or col < 0 or 
                row >= rowLen or col >= colLen or
                grid[row][col] <= prevVal or (row, col) in visited
                ):
                return 0
            if (row, col) in memo:
                return memo[(row, col)]

            visited.append((row, col))
            currentVal = grid[row][col]
            #dfs up row -1 col
            up = dfs(row -1, col, currentVal)
            #dfs down row + 1 col
            down = dfs(row + 1, col, currentVal)
            #dfs left row, col -1
            left = dfs(row, col - 1, currentVal)
            # dfs right row, col + 1
            right = dfs(row, col + 1, currentVal)
            # store the maxVal of the 4 dfs + 1 in memo for that index
            maxPath = max(up, down, left, right)
            memo[(row, col)] = maxPath + 1
            visited.pop()
            return maxPath + 1
        
        for row in range(rowLen):
            for col in range(colLen):
                dfs(row, col, -1)
        return max(memo.values())

matrix=[
    [5,5,3],
    [2,3,6],
    [1,1,1]
    ]


test = Solution()
print(test.longestIncreasingPath(matrix))