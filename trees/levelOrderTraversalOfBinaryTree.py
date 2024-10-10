# LeetCode 102 - Medium

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
        
        dq = deque([root])
        result = []

        while dq:
            dqLen = len(dq)
            currentRow = []
            for _ in range(dqLen):
                current = dq.popleft()
                currentRow.append(current.val)
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