# LeetCode - 323 - Count Connected Components - Medium
# IO
"""
Input - n -> INT -> The number of nodes present in the graph
Input - edges > A 2D array of INTs that represents undirected connections
Output - INT -> The number of Connected components that exist 
"""
# Design
"""
We first need to create a hashMap of Graph Nodes and their values based on n
We can then create an adjacency list for all the adjacent neighbors based on the received edge list by iterating through
edges and adding the values to both since it is undirected.
Once we have done this, we can run DFS from every node in our hashMap ONLY if it has not been visited already.
DFS will check to see if the node is a leaf node. If so, it will add it to the visited list and return.
If not, and we already visited it, we will return
We will then cycle through all the neighbors, assuming it wasnt the node we JUST visited (previous) and continue to dfs.
For each node from our map we iterate over, we will increment our count since nodes we already visited are part of their own
connected component. If we haven't visited a node, it is part of a new component. 
We can return our count once we have done all of our iterating. The end!
"""
# Constraints
"""
Can n be 0? No. At least 1 
Can there be duplicate edge values or will they be unique? Unique
"""
# Example
n = 3
edges = [[0, 1], [2, 0]] # 1
n = 6
edges [[0,1], [1,2], [2, 3], [4, 5]] # 2


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        nodeHash = {}
        visited = []
        components = 0

        for i in range(n):
            nodeHash[i] = Node(i)
        
        # create adjacency list
        for edge in edges:
            n1, n2 = edge
            nodeHash[n1].neighbors.append(nodeHash[n2])
            nodeHash[n2].neighbors.append(nodeHash[n1])
        
        def dfs(node:Node, previous:Node) -> None:
            if not node.neighbors:
                visited.append(node)
                return
            if node in visited:
                return
            
            visited.append(node)
            for neighbor in node.neighbors:
                dfs(neighbor, node)
            
            return
        
        for n in nodeHash.values():
            if n not in visited:
                components += 1
                dfs(n, None)
        
        return components