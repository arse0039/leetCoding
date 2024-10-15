# LeetCode - 133 - Clone Graph - Medium
## I/Os ##
"""
Input - node -> A node object that exists within our undirected graph
Output - A deep copy of the same node 
"""
## Design ## 
"""
We are given a Node object that has a DM of its neighbors. For the initial Node, we need to create a new Node. From there we need to iterate
through every child in the original array, recursively creating new copies of each node in the child list and creating deep copies. 
For our recursive function, we can stop when there are no more children left to move through. We 
"""

## Constraints ##
"""
Can we have cycles in our graph?
Can we receive no node? 
"""
## Example
""" 
    2
  1   3
"""

from typing import Optional
class Node:
    def __init__(self, val, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
class Solution:
    def cloneGraph(self, node:Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        storedNodes = {}
        
        copyRoot = Node(node.val)
        
        def copyNode(node:Node, copy:Node):
            if copy.val not in storedNodes:
                storedNodes[node] = copy
            for neighbor in node.neighbors:
                neighborCopy = storedNodes.get(neighbor, Node(neighbor.val))
                if neighborCopy in copy.neighbors:
                    return
                copy.neighbors.append(neighborCopy)
                copyNode(neighbor, neighborCopy)
            return
        
        copyNode(node, copyRoot)
        return copyRoot



        