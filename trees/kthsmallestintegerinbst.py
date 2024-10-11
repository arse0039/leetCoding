# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        
        queue = []
        count = 0
        current = root
        while current:
            queue.append(current)
            current = current.left

        while queue:
            current = queue.pop()
            count += 1
            
            if count == k:
                return current.val

            if current.right:
                current = current.right
                queue.append(current)
                while current.left:
                    queue.append(current.left)
                    current = current.left
            
            


test = Solution()
n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(3)
n4 = TreeNode(1)
n5 = TreeNode(4)
n6 = TreeNode(7)
n7 = TreeNode(9)
n8 = TreeNode(2)

n1.left, n1.right = n2, n3
# n2.left, n2.right = n4, n5
# n3.left, n3.right = n6, n7
# n4.right = n8

print(test.kthSmallest(n1, 2))