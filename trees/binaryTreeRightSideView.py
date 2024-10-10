# Leetcode 199 - Medium - Binary Tree Right Side View
# This problem asks us to she only nodes that visible from the right side of the tree.
# Essentially, this means the right-most node in every row. Because we need to analyze the nodes
# per row, we know this means using a BFS algorithm, which means using a handy-dandy deque!
# The only caveat here is that we only want to add the last node per row, so we just need to use a for loop 
# within the traversal to add values the final iteration. 
# Time Complexity is O(n * m) where n is the number of nodes in the BST and m is the max width. 

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root) -> list[int]:
        result = []
        if not root:
            return result
        
        dq = deque([root])

        while dq:
            dqLen = len(dq)
            for i in range(dqLen):
                currentNode = dq.popleft()
                if i == dqLen - 1:
                    result.append(currentNode.val)
                dq.append(currentNode.left) if currentNode.left else None
                dq.append(currentNode.right) if currentNode.right else None
            
        
        return result

test = Solution()
n1 = TreeNode(5)
n2 = TreeNode(3)
n3 = TreeNode(8)
n4 = TreeNode(1)
n5 = TreeNode(4)
n6 = TreeNode(7)
n7 = TreeNode(9)
n8 = TreeNode(2)

n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7
n4.right = n8

print(test.rightSideView(n1))