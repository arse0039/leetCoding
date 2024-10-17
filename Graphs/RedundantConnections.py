# LeetCode - 684 - Redundant Connections - Medium
# IO
"""
 Input - Edges - a 2D array of INTs that represent edges that connect nodes
 Output - ARR -> An array of two integers representing an edge that can be removed
"""
# Design
"""
We are given an array of undirected edges and we want to find the cycle that exists.
This means that any node that contains only a single neighbor can not be a part of a cycle
so we don't need to worry about those. 
First, we can iterate through the array of edges and create a hashMap that represents nodes. We can
then seed adjacency list for each node.
For any node that has a neighbor, we can do a DFS, adding visited nodes as well as edges as we move through to their
own repsective arrays.
DFS will be recursively called on every neighbor node, making sure not to visit the previous node, since the graph is undirected.
Our recursive calls will stop once we reach a node with no neighbors, we visit a node we already visited, or we moved through every neighbor
successfully.
If we visit a node that has already been visited, we have found a cycle and can add all the edges to a set of edges.
Once we have done this for all nodes with neighbors, we can loop backwards through the edges array, returning the first match.
"""
# Constraints
"""
 Can there be multiple cycles in the graph? Maybe!
 Can edges be empty?  No
 Are there repeated edges? No
 Are all nodes unique? Yes
 Can edges contain anything other that integers? No
"""
# Example
edges = [[2, 1], [1, 3], [3, 4], [1, 4], [1, 5]]
result = [1, 4]

class Solution():
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        nodeHash = {}

        # create Nodes and adjacency list
        for edge in edges:
            e1, e2 = edge
            if e1 not in nodeHash:
                nodeHash[e1] = []
            if e2 not in nodeHash:
                nodeHash[e2] = []

            nodeHash[e1].append(e2)
            nodeHash[e2].append(e1)
        
        nodeHash = {key:neighbor for key, neighbor in nodeHash.items() if len(neighbor) > 1}
        
        visited = []
        cycleEdges = []
        
        def dfs(node:int, previous) -> None:
            # Base Cases - No Neighbors, Already Visited
            if len(nodeHash[node]) == 1 and nodeHash[node][0] in visited:
                return False
            if node in visited:
                #cycleEdges.append([node, previous])
                return True
            
            visited.append(node)
            for neighbor in nodeHash[node]:
                if neighbor in nodeHash and neighbor != previous:
                    cycleEdges.append([node, neighbor])
                    if not dfs(neighbor, node):
                        cycleEdges.pop()
                        return False
            return True
                
        # iterate through nodes that have neighbors to look for cycles

        dfs(list(nodeHash.keys())[0], -1)

        for i in range(len(edges) - 1, 0, -1):
            if edges[i] in cycleEdges or edges[i][::-1] in cycleEdges:
                return edges[i]
        
        
# edges=[[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
# test = Solution()
# print(test.findRedundantConnection(edges))


""" 
Turns out another approach is an algorithm called UnionFind
When we add an edge, we have two nodes. -> [1, 2]
We can track the number of connections each node has coming off of it, perhaps using a node class.
We can iterate through our edges, updating our previous nodes parents and children
the first val is the parent, the second is it's child, and vice versa.
So, if we add [1, 3] 
nodes =    [1, 2, 3]
children = [2, 1, 1] Because 1 now has 2 children and 2 and 3 now have one 
if we then try to add [2, 3]
nodes = [1, 2, 3]
child = [4, 2, 2] 
We need to update all the neighbors of the nodes from the edge and all of THOSE neighbors edges.   
This approach using a ranking system to deduce which node should be considered the parent node because it treats
this graph as a tree, where one node is considered to be the root node. The root node will have the mose number of
nodes beneath it! We start by creating an array for all nodes, with each node value at it's corresponding index.
When we get an edge, we look at the nodes provided in the edge in the parents array because we want to know what
that nodes parent is. If the value at that node's index is that nodes parent index. If we compare the node value to it's parent
index and they are the same, that means we reached the topmost parent. If they are not the same, that means that index has a parent
and we need to move up to that node. 
Once the value at an index parent[index] is the same as parent[parent[index]], we can return that node. We need to be updating the
top most parent as we move through the array as well. 
Once we do this for both nodes from the edge, we can update our rank. If the nodes have the same parent, it's an edge that created a 
cycle, so we can just return False.
Otherwise, we want to look at the ranking values at each parent node. The larger of the two needs to consume the smaller of the two
so that it remains the root. We can then update the parent's array so that the node with the smaller ranking is pointing to
its new topmost parent node. 
"""

class Solution2:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parents = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def findParent(node):
            currentParent = parents[node]
            # while the parent of the parent is not the same, we know we have not moved all the 
            # way up the tree! Once we reach the top of the tree, we can stop, because we found the
            # parent node, which we can return
            while parents[parents[node]] != parents[node]:
                parents[node] = parents[parents[node]]
            
            return parents[node]
        
        def union(node1, node2):
            parent1 = findParent(node1)
            parent2 = findParent(node2)

            # if the parents are the same, we have a cycle
            if parent1 == parent2:
                return False
            if rank[parent1] > rank[parent2]:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True

        for edge in edges:
            e1, e2 = edge
            if not union(e1, e2):
                return edge






edges=[[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
test = Solution2()
print(test.findRedundantConnection(edges))