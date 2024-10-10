#  LeetCode 1448 - Medium - Count Good Nodes in Binary Tree
# Another straight-forward question! We are tasked with finding "good" nodes in binary tree.
# "Good" means that the node has no values larger than itself on its path up to the root.
# this means we are examining linear paths from the leaf nodes back up to the root. If we know what the maximum
# value is of the nodes that preceed it, we can easily check if the current node's value is equal to or larger
# than it's ascendant. This means calculating the max as we go and passing it into future recursive calls
# and adding up the number of good nodes as we traverse the tree!

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            left = dfs(node.left, max(maxVal, node.val))
            right = dfs(node.right, max(maxVal, node.val))

            if node.val >= maxVal:
                return left + right + 1
            else:
                return left + right
        
        return dfs(root, root.val)


test = Solution()
n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(1)
n4 = TreeNode(3)
n5 = TreeNode(1)
n6 = TreeNode(5)

n1.left, n1.right = n2, n3
n2.left  = n4
n3.left, n3.right = n5, n6

print(test.goodNodes(n1))