# LeetCode - - Course Schedule - Medium
## I/Os
"""
Input - prerequisites - a 2D array of integer values -> [[0, 1], [1, 2]]. 
      - numberOfClasses - INT - the number of classes required to take 
Output - Boolean - True if it is possible to to take the course. False if it is not
"""
## Design
"""
For every array within the prereq array, the second value is a pre-requisite for the first. The pre-reqs create
a graph structure. For pre-reqs to make sense, the graph needs to be linear in nature. If we have a cycle, we know that 
the pre-req list does not work. This is because we need to take a later class to take an earlier class, which is impossible
since the earlier class is needed to take the later! 
We need to iterate through each pre-req list, adding pre-reqs for each course. Courses start at 0. We then need to do a dfs starting
at the first course, 0, and move through every node in the neighbors array, keeping track of nodes we already visited. If we re-visit a node,
we need to return False. If we get to a node that contains no neighbors, we made it to a leaf node, so we can stop and return True. 
The number of classes tells us how many course we need to create, which we can store in a hashMap. We can iterate through the prereqs to add neighbors
and then iterate through every course in our hashMap to do the dfs search.
"""
## Constraints
"""
Will numberOfClasses be equal to the number of unique course found in the prereqs array? Unclear
Will the course numbers all be unique?  YES
Will the course numbers start at 0 and increment by 1? Yes
"""

## Example
prereq = [
    [0, 1],
    [1, 2],
    [2, 0]
]

class Node:
    def __init__(self):
        self.neighbors = []

class Solution:
    def canFinish(self, numCourse: int, prereqs: list[list[int]]) -> bool:
        classMap = {}

        for i in range(numCourse):
            classMap[i] = Node()

        for reqs in prereqs:
            course, prereq = reqs
            classMap[course].neighbors.append(classMap[prereq])
        
        visited = []

        def dfs(node:Node) -> bool:
            if not node.neighbors:
                return True
            if node in visited:
                return False
            
            visited.append(node)
            for neighbor in node.neighbors:
                if not dfs(neighbor):
                    return False
            visited.pop()
            
            return True

        for id in classMap.keys():
            if not dfs(classMap[id]):
                return False
        return True
        
prerequisites=[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
test = Solution()
print(test.canFinish(20, prerequisites))