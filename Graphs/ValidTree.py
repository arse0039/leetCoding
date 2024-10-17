# LeetCode - 261 - Valid Tree - Medium
## I/O
"""
Input - n INT - An integer representing the number of Nodes present
Input - edges - a 2D array if integers, representing edges that connect nodes
Output - boolean -> True if the edges can create a valid Tree (no cycles) False if that can not.
"""
## Design
"""
For this problem, we need to create a Node for each value from 0 to n. 
Once we do this, we can create an adjacency list for every node using the edges. 
A graph is considered valid if all nodes are connected to one another and there are no cycles
This means we can start at node 0 and we can run DFS on all the neighbors. We will update which nodes we visit.
If we visit a node we already visited, we know we found a cycle and can return False. In order to ensure we don't move 
backwards, we will pass the previous node into the dfs search, making sure to skip it as a neighbor. Once we reach a leaf
node, we can add it to our visited list and return True. 
Once we finish running DFS on every neighbor of node 0, we can compare our visited arrays length to n. Because we needed to visit
every node, they should be the same! If they aren't we know we had nodes that weren't connected in the graph and can return False. 
Otherwise, we passed both checks and can return True!
"""
## Constraints
"""
Can we have duplicated edges? No 
Are the edges undirected? Yes
"""
## Example
n = 5
edges = [[0,1], [1, 4], [0, 3], [0, 2]] # true

class Node:
    def __init__(self):
        self.neighbors = []

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        nodeMap = {}
        for i in range(n):
            nodeMap[i] = Node()

        for edge in edges:
            n1, n2 = edge
            nodeMap[n1].neighbors.append(nodeMap[n2])
            nodeMap[n2].neighbors.append(nodeMap[n1])
        
        visited = []
        def dfs(node, previous=None):
            if node in visited:
                return False
            if not node.neighbors:
                visited.append(node)
                return True
            
            visited.append(node)
            for neighbor in node.neighbors:
                if neighbor != previous:
                    if not dfs(neighbor, node):
                        return False

            return True

        if not dfs(nodeMap[0]):
            return False
        
        return True if len(visited) == n else False
 
test = Solution()
n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
print(test.validTree(n, edges))