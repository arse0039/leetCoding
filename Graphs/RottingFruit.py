# LeetCode - 994 - Rotting Fruit - Medium
## I/O's 
"""
Input - grid - a 2D Matrix of integers - either 0, 1, or 2
Output - INT - The minimum number of minutes it takes for all the fruit to turn rotten or -1 if there are
no rotten fruits or no ways to rot other fruits
"""
## Design
"""
For this problem, we care about the rotten fruit. This means that our first step is identify the 
rotten fruit (2) and store their coordinates in a deque. Using a deque is important because we want
to want rot fruit from the same points 'at the same time' using BFS. This means checking the upper,
lower, right, and left tiles of the grid for fresh fruit (1). If we find a piece of fresh fruit, we
can update its value to 2 and add it to the deque. 
We need to be sure that we push not only coordinates but the time the fruit rotted onto our deque.
When we pop the last piece of fruit from the stack, we can use it's time + 1 to deduce our minimum time. 
TC = O(m*n) due to have to loop through every element(m) in each row(n):
"""
## Constraints
"""
Can grid be empty? No 
"""
## Examples
 # 0 = Empty
 # 1 = Good Fruit
 # 2 = Rotten
grid = [
    [0, 0, 2],
    [1, 0, 0],
    [1, 1, 1]
]  # return 2

from collections import deque

class Solution():
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        time = 0
        # [row, col, time]
        rottenFruits = deque([]) #[ 2, 2]

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 2:
                    rottenFruits.append([i, j, time])

        def rotThemFruits(row:int, col:int, time:int) -> None:
            if ( row < 0 or row >= rowLen or
                 col < 0 or col >= colLen or
                 grid[row][col] != 1 
               ):
                return
            grid[row][col] = 2
            rottenFruits.append([row, col, time + 1])
        
        while rottenFruits:
            row, col, time = rottenFruits.popleft()
            rotThemFruits(row - 1, col, time) # upper
            rotThemFruits(row + 1, col, time) # lower
            rotThemFruits(row, col - 1, time) # left
            rotThemFruits(row, col + 1, time) # right

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    return -1
        return time    
        

test = Solution()
grid2 = [[2,1,1],[0,1,1],[1,0,1]]
print(test.orangesRotting(grid2))