# LeetCode 102 - Medium
# This problem is all about using breadth-first search algorithm to add the values at each level.
# To use BFS, we need to use a deque DS to store the visited nodes. 
# We can

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        # Initialize the deque with the root node
        dq = deque([root])
        result = []

        # as long as there is something in the deque, we know we are still traversing the 
        # tree. 
        while dq:
            dqLen = len(dq)
            currentRow = []
            # Since we will be adding to the deck, we need to limit our loop here to the number of items 
            # we started with in the deque. This is the number of nodes in that row!
            for _ in range(dqLen):
                # pop the leftmost item from the deque, which is the leftmost node from the queue.
                current = dq.popleft()
                currentRow.append(current.val)
                # every node we pop, we need to add it's left and right child if they exist. This is how we create
                # the next "row" in the graph in order from left to right, making sure to skip Null values. 
                if current.left:
                    dq.append(current.left)
                if current.right:
                    dq.append(current.right)
            result.append(currentRow)

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

print(test.levelOrder(n1))