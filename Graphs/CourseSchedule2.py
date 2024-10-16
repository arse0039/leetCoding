# LeetCode - 210 - Course Schedule 2 - Medium
## I/Os
"""
 Input - prereqs - 2D array of INTS. 
 Input - numCourses - INT
 Output - array of INTS
"""
## Design
"""
We need to determine if we can take all the courses listed based on the prereqs array we receive. For every course, we 
can create a graph with neighbors being courses that are pre-reqs for that course. We know that a course can not be 
taken if there is a cycle within that graph. The order in which a courses can be taken is determined by doing a DFS 
on the neighbors of every course until we get to a point where we don't have any more neighbors. 
When we find a node with no neighbors, we add its value to the result. We then move back up the recursive chain. When a node has
iterated through all of it's neighbors, it's time for us to add that node's value to our results if it has not already
been added. 
If we find a cycle,
that is we visit a node we have already visited, we know that we can not complete the course, meaning it is impossible to 
complete all courses. If we can't complete a course, we can denote that in some way and use that denotation to clue is
in to the fact that we need to return an empty array. 
For any courses without prereqs, we can simply add them in wherever we want, or at the end of the result since they can be taken
at any time.
TC - O(n * m) where n is numCourses and m is the largest path of pre-reqs. 
"""
## Constraints
"""
Can numCourses be 0 or a negative value? NOPE 1 or more
can preReqs be empty?  Sure Can!
"""
## Example
prereqs = [[0,1], [1, 4], [1, 5], [2, 6]]
output = [5, 4, 1, 0, 6, 2, 3]

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Solution:
    def findOrder(self, numCourses: int, prereqs:list[list[int]],) -> list:
        classMap = {}
        canComplete = True
        result = []

        for i in range(numCourses):
            classMap[i] = Node(i)
        
        # get all the prereqs listed as neighbors
        for prereq in prereqs:
            course, pre = prereq
            classMap[course].neighbors.append(classMap[pre])
        
        visited = []
        def dfs(node: Node):
            nonlocal canComplete
            if not node.neighbors:
                result.append(node.val) if node.val not in result else None
                return
            if node in visited:
                canComplete = False
                return
            
            visited.append(node)
            for n in node.neighbors:
                dfs(n)
            visitedNode = visited.pop()
            result.append(visitedNode.val) if visitedNode.val not in result else None
            return
   
        for node1 in classMap.values():
            dfs(node1)
        
        return result if canComplete else []
        

test = Solution()
numCourses = 3
prerequisites = [[0,1],[1,2],[2,0]]
print(test.findOrder(prerequisites, numCourses))