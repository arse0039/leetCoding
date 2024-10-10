# LeetCode 98 - Medium - Valid Binary Search Tree
# For this problem, we need to determine if a received Binary Tree meets the
# critera for being a Binary Search Tree. In order to be a valid BST, for each node, 
# the left child must be a smaller value and the right child must be a larger value
# This means for every node, we need to check it's child on each level before moving to the next.
# I believe a BFS algo will work best here but DSF might work as well? Not sure on that one! 

# The approach is to look at each node, starting with the root and check the children's values
# against it. If they meet the criteria of min < node < max, we move on. If it isn't we know it 
# is not a valid tree and we can return False. Otherwise, we continue. If we traverse the entire tree
# without returning false, we know the tree is valid and can return True! EASY! Let's get to coding!
# We are guaranteed to have a node!
# Turns out DFS gives us the easiest approach. We set our min to -infitinity and max to infinity to start.
# When we move to the left, we expect smaller values, so we need to update our maximum boundary to the value that preceeded it
# This works because we know that the BST up until that node is valid. 
# When we move to the right, we are expecting larger values. This means that our minimum boundary value needs to be updated.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:

        def dfs(node, minVal, maxVal):
            if not node:
                return True
            
            if not (minVal < node.val < maxVal):
                return False
            
            # left means update our maximum boundary
            left = dfs(node.left, minVal, node.val)
            # right means update out minimum boundary
            right = dfs(node.right, node.val, maxVal)

            return left and right


        return dfs(root, float("-inf"), float("inf"))

test = Solution()
n1 = TreeNode(3)
n2 = TreeNode(1)
n3 = TreeNode(5)
n4 = TreeNode(0)
n5 = TreeNode(2)
n6 = TreeNode(4)
n7 = TreeNode(6)

n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7 

print(test.isValidBST(n1))